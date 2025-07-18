
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT, MAX_ITERS, STARTING_LINE, NUMBER_OF_LINES_PER_REQUEST
from fugashi import Tagger
from import_file import import_file
from line_control import LineControl


def main():

    load_dotenv()
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("LiteralTranslator App")
        print('Usage: python main.py "<path to file>"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    subs = import_file(args[0], verbose)
    control = LineControl(subs, verbose)
    line_number = STARTING_LINE
    user_prompt = control.line_prompt(line_number)

    if verbose:
        print(f"User Prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    i = 0
    while True:
        i += 1
        if i > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        
        try:
            response_text = generate_content(client, messages, verbose)
            if response_text:
                print(f"Final response: {response_text}")
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    



    
        
    print(subs[0].text)


if __name__=="__main__":
    main()