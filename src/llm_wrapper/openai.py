from openai import OpenAI

from .base import Client, LLMResponse, Message


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

        message = self._client.responses.create(**request)
        text = message.output_text if message.output_text else ""
        return LLMResponse(text=text, raw=message)
