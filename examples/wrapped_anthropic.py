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

    # With system prompt and temperature
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        max_tokens=1024,
        system="You should end every response with ':)'",
        temperature=0.0,
    )

    # Without system prompt and temperature
    response = client.generate(
        messages=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        max_tokens=1024,
    )

    logger.info(response.text)
