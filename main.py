import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
from ai_generator import ai_initiate, generate_content
from config import MAX_ITERS
from fugashi import Tagger
from import_file import import_file
from line_control import LineControl


def main():

    # load_dotenv()
    verbose = "--verbose" in sys.argv
    
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("LiteralTranslator App")
        print('Usage: python main.py "<path to file>" "start=<starting_line_number>"')
        sys.exit(1)

    # api_key = os.environ.get("GEMINI_API_KEY")
    # client = genai.Client(api_key=api_key)


    subs = import_file(args[0], verbose)
    for arg in sys.argv[1:]:
        if arg.startswith("start="):
            start = int(arg.split("=", 1)[1])

    control = LineControl(subs, verbose, global_state=start)
    user_prompt = control.line_prompt()

    # if verbose:
    #     print(f"User Prompt: {user_prompt}\n")

    # messages = [
    #     types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    # ]

    i = 0
    while True:
        i += 1
        if i > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        
        try:
            client, messages = ai_initiate(user_prompt, verbose)
            response_translations = generate_content(client, messages, control, verbose)
            if verbose:
                print(f"Calling function 'translate_subtitle' with args '{response_translations}'")
            control.translate_subtitle(**response_translations)
            

        except Exception as e:
            print(f"Error in generate_content: {e}")
    

        
    print(subs[0].text)


if __name__=="__main__":
    main()