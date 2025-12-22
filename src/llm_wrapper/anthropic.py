from anthropic import Anthropic

from .base import BaseClient, LLMResponse, Message


class AnthropicClient(BaseClient):
    def __init__(self, *, api_key: str, model: str) -> None:
        self._client = Anthropic(api_key=api_key)
        self._model = model

    def generate(
        self,
        *,
        messages: list[Message],
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float | None = None,
    ) -> LLMResponse:
        request = {
            "model": self._model,
            "max_tokens": max_tokens,
            "messages": messages,
        }
        if system is not None:
            request["system"] = system
        if temperature is not None:
            request["temperature"] = temperature

        message = self._client.messages.create(**request)
        text = message.content[0].text if message.content else ""
        return LLMResponse(text=text, raw=message)
