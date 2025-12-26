import logging
import os

from dotenv import load_dotenv

from llm_wrapper import create_client

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("ANTHROPIC_API_KEY")

    client = create_client(
        provider="anthropic",
        api_key=api_key,
        model="claude-haiku-4-5-20251001",
    )

    # With system prompt
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Can you introduce yourself?",
            }
        ],
        max_tokens=2048,
        system="You should end every response with ':)'",
        reasoning={
            "type": "enabled",
            "budget_tokens": 1024,
        },
    )

    logger.info("Full response:")
    logger.info(response)

    logger.info("Text:")
    logger.info(response.text)

    logger.info("Reasoning:")
    logger.info(response.reasoning)

    # Without system prompt
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Can you introduce yourself?",
            }
        ],
        max_tokens=2048,
        reasoning={
            "type": "enabled",
            "budget_tokens": 1024,
        },
    )

    logger.info("Full response:")
    logger.info(response)

    logger.info("Text:")
    logger.info(response.text)

    logger.info("Reasoning:")
    logger.info(response.reasoning)
