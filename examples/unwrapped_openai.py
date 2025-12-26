import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    # Client initialization
    load_dotenv()

    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(
        api_key=api_key,
    )

    # API call
    response = client.responses.create(
        model="gpt-5-nano-2025-08-07",
        instructions="You should end every response with ':)'",
        input=[
            {
                "role": "user",
                "content": "Can you introduce yourself?",
            }
        ],
        max_output_tokens=2048,
        reasoning={
            "effort": "medium",
            "summary": "auto",
        },
    )

    # Report full response
    logger.info("Full response:")
    logger.info(response)

    # Initialize text and reasoning strings
    text = []
    reasoning = []

    # Extract text and reasoning
    for item in response.output:
        if item.type == "message":
            for c in item.content or []:
                if getattr(c, "type", None) == "output_text":
                    text.append(c.text)
        elif item.type == "reasoning":
            for s in item.summary or []:
                if getattr(s, "type", None) == "summary_text":
                    reasoning.append(s.text)

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    logger.info("Text:")
    logger.info(text)

    logger.info("Reasoning:")
    logger.info(reasoning)
