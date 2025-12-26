from openai import OpenAI

from .base import Client, LLMResponse, Message


# TODO: type response
def _extract_text_and_reasoning(response) -> tuple[str, str]:
    text = []
    reasoning = []

    for item in response.output:
        if item.type == "message":
            for c in item.content or []:
                if getattr(c, "type", None) == "output_text":
                    text.append(c.text)
        elif item.type == "reasoning":
            for s in item.summary or []:
                if getattr(s, "type", None) == "summary_text":
                    reasoning.append(s.text)

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    return text, reasoning


class OpenAIClient(Client):
    def __init__(self, *, api_key: str, model: str) -> None:
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def generate(
        self,
        *,
        messages: list[Message],
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float | None = None,
        reasoning: dict | None = None,
    ) -> LLMResponse:
        request = {
            "model": self._model,
            "max_output_tokens": max_tokens,
            "input": messages,
        }
        if system is not None:
            request["instructions"] = system
        if temperature is not None:
            request["temperature"] = temperature
        if reasoning is not None:
            request["reasoning"] = reasoning

        response = self._client.responses.create(**request)

        response_text, response_reasoning = _extract_text_and_reasoning(response)

        return LLMResponse(
            text=response_text, reasoning=response_reasoning, raw=response
        )
