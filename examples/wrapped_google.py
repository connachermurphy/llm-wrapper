import logging
import os

from dotenv import load_dotenv

from llm_wrapper import create_client

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("GOOGLE_API_KEY")

    client = create_client(
        provider="google",
        api_key=api_key,
        model="gemini-3-flash-preview",
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
            "effort": "medium",
            "summary": "auto",
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
            "effort": "medium",
            "summary": "auto",
        },
    )

    logger.info("Full response:")
    logger.info(response)

    logger.info("Text:")
    logger.info(response.text)

    logger.info("Reasoning:")
    logger.info(response.reasoning)
