from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence


Message = dict[str, object]


@dataclass(frozen=True)
class LLMResponse:
    text: str
    raw: object | None = None


class BaseClient(ABC):
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


def _providers() -> dict[str, type[BaseClient]]:
    from .anthropic import AnthropicClient

    return {
        "anthropic": AnthropicClient,
    }


def create_client(*, provider: str, api_key: str, model: str) -> BaseClient:
    providers = _providers()
    if provider not in providers:
        raise ValueError(f"Unsupported provider: {provider}")

    return providers[provider](api_key=api_key, model=model)
