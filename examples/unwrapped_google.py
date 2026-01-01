import logging

from dotenv import load_dotenv
from google import genai
from google.genai import types

logging.basicConfig(level=logging.INFO)

# TODO: can we explicitly initialize the client with an API key?
# TODO: parse thought and content from response object
# TODO: switch to interactions API?

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    client = genai.Client()

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

    # Print text and thought (for now)
    for part in response.candidates[0].content.parts:
        if not part.text:
            continue
        if part.thought:
            print("Thought: ", part.text)
        else:
            print("Text: ", part.text)


# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Provide a list of 3 famous physicists and their key contributions",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=1024)
#         # Turn off thinking:
#         # thinking_config=types.ThinkingConfig(thinking_budget=0)
#         # Turn on dynamic thinking:
#         # thinking_config=types.ThinkingConfig(thinking_budget=-1)
#     ),
# )

# print(response.text)

# Example of client-side state management:
# from google import genai

# client = genai.Client()

# conversation_history = [
#     {"role": "user", "content": "What are the three largest cities in Spain?"}
# ]

# interaction1 = client.interactions.create(
#     model="gemini-3-flash-preview", input=conversation_history
# )

# print(f"Model: {interaction1.outputs[-1].text}")

# conversation_history.append({"role": "model", "content": interaction1.outputs})
# conversation_history.append(
#     {"role": "user", "content": "What is the most famous landmark in the second one?"}
# )

# interaction2 = client.interactions.create(
#     model="gemini-3-flash-preview", input=conversation_history
# )

# print(f"Model: {interaction2.outputs[-1].text}")
