import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT


schema_translate_subtitle = types.FunctionDeclaration(
    name="translate_subtitle",
    description="Constructs subtitle from given list of translations.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "translated_dict_list": types.Schema(
                type=types.Type.STRING,
                description="Translations from Japanese to English word for word as a valid JSON list of dictionaries. Each item in the list is one subtitle line as its dictionary.",
            ),
        },
    ),
)


def ai_initiate(user_prompt, verbose):
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User Prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    return client, messages

def generate_content(client, messages, verbose):

    available_function = types.Tool(
        function_declarations=[
            schema_translate_subtitle
        ]
    )   


    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001',
        contents = messages,
        config=types.GenerateContentConfig(tools=[available_function],
            system_instruction=SYSTEM_PROMPT,
            tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode=types.FunctionCallingConfigMode.ANY))
    ))

        

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


    function_calls = response.function_calls
    if function_calls:
        for call in function_calls:
            return call.args

    else:
        print(f"Error: Text response generated: {response.text}")
        return


