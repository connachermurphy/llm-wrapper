from google import genai
from google.genai import types

from .base import Client, LLMResponse, Message


# TODO: type response
def _extract_text_and_reasoning(response) -> tuple[str, str]:
    text = []
    reasoning = []

    for part in response.candidates[0].content.parts:
        if not part.text:
            continue
        if part.thought:
            reasoning.append(part.text)
        else:
            text.append(part.text)

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    return text, reasoning


class GoogleClient(Client):
    def __init__(self, *, api_key: str, model: str) -> None:
        self._client = genai.Client(api_key=api_key)
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
        contents = system + "\n" if system is not None else ""

        contents += "Messages:\n"
        for message in messages:
            contents += f"{message['role']}: {message['content']}\n"

        request = {
            "model": self._model,
            "contents": contents,
        }

        if reasoning is not None:
            request["config"] = types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(**reasoning)
            )

        # TODO: max_tokens
        # TODO: build request object
        # TODO: configure temperature

        response = self._client.models.generate_content(**request)

        response_text, response_reasoning = _extract_text_and_reasoning(response)

        return LLMResponse(
            text=response_text, reasoning=response_reasoning, raw=response
        )
