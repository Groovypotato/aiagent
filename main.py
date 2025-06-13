import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = ""
flag = ""

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

if len(sys.argv) > 1:
    user_prompt = sys.argv[1]

if len(sys.argv) > 2:
    flag = sys.argv[2]





if len(user_prompt) > 1:
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
    )
    if flag == "--verbose":
        print(f"User prompt: {sys.argv[1]}")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)
else:
    sys.exit(1)

