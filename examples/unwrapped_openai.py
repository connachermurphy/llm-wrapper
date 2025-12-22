import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key,
    )

    response = client.responses.create(
        model="gpt-5-nano-2025-08-07",
        instructions="You should end every response with ':)'",
        input=[
            {
                "role": "user",
                "content": "Hello, Claude",
            }
        ],
        max_output_tokens=1024,
        reasoning={
            "effort": "minimal",
        },
    )

    logger.info(response.output_text)
