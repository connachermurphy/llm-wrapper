import logging
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    api_key = os.environ.get("GOOGLE_API_KEY")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Please introduce yourself. Please end your response with ':)'",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                include_thoughts=True,
                thinking_level="low",
            )
        ),
    )

    # Report full response
    logger.info("Full response:")
    logger.info(response)

    # Initialize text and reasoning strings
    text = []
    reasoning = []

    # Extract text and reasoning
    for part in response.candidates[0].content.parts:
        if not part.text:
            continue
        if part.thought:
            reasoning.append(part.text)
        else:
            text.append(part.text)

    text = "\n".join(text).strip()
    reasoning = "\n".join(reasoning).strip()

    logger.info("Text:")
    logger.info(text)

    logger.info("Reasoning:")
    logger.info(reasoning)
