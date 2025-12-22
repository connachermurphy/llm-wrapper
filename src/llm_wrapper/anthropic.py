from anthropic import Anthropic

from .base import Client, LLMResponse, Message


class AnthropicClient(Client):
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
        reasoning: dict | None = None,
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
        if reasoning is not None:
            request["thinking"] = reasoning

        message = self._client.messages.create(**request)
        text = next(block.text for block in message.content if block.type == "text")
        return LLMResponse(text=text, raw=message)
