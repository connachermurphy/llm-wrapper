import logging
import os

from dotenv import load_dotenv

from llm_wrapper import create_client

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("OPENAI_API_KEY")

    client = create_client(
        provider="openai",
        api_key=api_key,
        model="gpt-5-nano-2025-08-07",
    )

    # With system prompt and temperature
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Hello, GPT-5 Nano",
            }
        ],
        max_tokens=1024,
        system="You should end every response with ':)'",
        reasoning={
            "effort": "minimal",
        },
    )

    logger.info(response.text)

    # Without system prompt and temperature
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Hello, GPT-5 Nano",
            }
        ],
        max_tokens=1024,
        reasoning={
            "effort": "minimal",
        },
    )

    logger.info(response.text)
