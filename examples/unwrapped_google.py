import logging

from dotenv import load_dotenv
from google import genai

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    load_dotenv()

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Can you introduce yourself?",
    )

    print(response.text)
    print(response)

# api_key = os.environ.get("GEMINI_API_KEY")


# gemini-3-flash-preview

# from google import genai
# from google.genai import types

# client = genai.Client()
# prompt = "What is the sum of the first 50 prime numbers?"
# response = client.models.generate_content(
#     model="gemini-2.5-pro",
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(include_thoughts=True)
#     ),
# )

# for part in response.candidates[0].content.parts:
#     if not part.text:
#         continue
#     if part.thought:
#         print("Thought summary:")
#         print(part.text)
#         print()
#     else:
#         print("Answer:")
#         print(part.text)
#         print()

# from google import genai
# from google.genai import types

# client = genai.Client()

# prompt = """
# Alice, Bob, and Carol each live in a different house on the same street: red, green, and blue.
# The person who lives in the red house owns a cat.
# Bob does not live in the green house.
# Carol owns a dog.
# The green house is to the left of the red house.
# Alice does not own a cat.
# Who lives in each house, and what pet do they own?
# """

# thoughts = ""
# answer = ""

# for chunk in client.models.generate_content_stream(
#     model="gemini-2.5-pro",
#     contents=prompt,
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(include_thoughts=True)
#     ),
# ):
#     for part in chunk.candidates[0].content.parts:
#         if not part.text:
#             continue
#         elif part.thought:
#             if not thoughts:
#                 print("Thoughts summary:")
#             print(part.text)
#             thoughts += part.text
#         else:
#             if not answer:
#                 print("Answer:")
#             print(part.text)
#             answer += part.text

# from google import genai
# from google.genai import types

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="Provide a list of 3 famous physicists and their key contributions",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_level="low")
#     ),
# )

# print(response.text)

# Use dynamic thinking?


# from google import genai
# from google.genai import types

# client = genai.Client()

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
