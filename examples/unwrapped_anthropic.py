import logging
import os

from anthropic import Anthropic
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("ANTHROPIC_API_KEY")

    client = Anthropic(
        api_key=api_key,
    )

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        messages=[
            {
                "role": "user",
                "content": "Can you introduce yourself?",
            }
        ],
        max_tokens=2048,
        system="You should end every response with ':)'",
        thinking={
            "type": "enabled",
            "budget_tokens": 1024,
        },
    )

    # Report full response
    logger.info("Full response:")
    logger.info(message)

    # Initialize text and reasoning strings
    text = []
    reasoning = []

    # Extract text and reasoning
    for block in message.content:
        if block.type == "text":
            text.append(block.text)
        elif block.type == "thinking":
            reasoning.append(block.thinking)

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    logger.info("Text:")
    logger.info(text)

    logger.info("Reasoning:")
    logger.info(reasoning)
