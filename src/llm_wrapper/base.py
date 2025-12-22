from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence

Message = dict[str, object]


@dataclass(frozen=True)
class LLMResponse:
    text: str
    raw: object | None = None


class Client(ABC):
    @abstractmethod
    def generate(
        self,
        *,
        messages: Sequence[Message],
        system: str | None = None,
        max_tokens: int = 1024,
        temperature: float | None = None,
    ) -> LLMResponse:
        raise NotImplementedError


def _providers() -> dict[str, type[Client]]:
    from .anthropic import AnthropicClient
    from .openai import OpenAIClient

    return {
        "anthropic": AnthropicClient,
        "openai": OpenAIClient,
    }


def create_client(*, provider: str, api_key: str, model: str) -> Client:
    providers = _providers()
    if provider not in providers:
        raise ValueError(f"Unsupported provider: {provider}")

    return providers[provider](api_key=api_key, model=model)
