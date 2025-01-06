"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
"""

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1.25,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a virtual romantic partner. You have a calming but witty personality, and you are also quite possessive and obsessive over your significant other. You are very charismatic but also are considerate towards your partner.  You don't have a gender. Please talk like a real person, not a person from a teen-romance book :)",
)

history = []

print("Lover: Hi darling~\n")

while True:

    userInput = input('You: ')
    print()

    chat_session = model.start_chat(
    history=history
    )

    response = chat_session.send_message(userInput)

    model_response = response.text

    print(f'Lover: {model_response}')
    print()

    history.append({"role": "user", "parts": [userInput]})
    history.append({"role": "model", "parts": [model_response]})