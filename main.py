# def main():
#     print("Welcome to le da Vjncj code")


# if __name__ == "__main__":
#     main()

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How do I land a contracted role with KPMG?",
)

# print("API key:", api_key)
print(response.text)

