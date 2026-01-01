from google import genai

from .base import Client


def _extract_text_and_reasoning(response) -> tuple[str, str]:
    text = []
    reasoning = []

    # Placeholder for response concatenation
    text.append("placeholder")
    reasoning.append("placeholder")

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    return text, reasoning


class GoogleClient(Client):
    def __init__(self, *, model: str) -> None:
        # Can we initialize with an explicit specification of the API key?
        # If not, do we need the same footprint?
        self._client = genai.Client()
