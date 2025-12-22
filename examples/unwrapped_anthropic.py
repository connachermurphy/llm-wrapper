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
        max_tokens=1024,
        temperature=0.7,
        system="You should end every response with ':)'",
        messages=[{"role": "user", "content": "Hello, Claude"}],
    )

    logger.info(message.content[0].text)
