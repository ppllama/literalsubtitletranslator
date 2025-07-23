import sys, os
from ai_generator import ai_initiate, generate_content
from config import STARTING_LINE
from fugashi import Tagger
from importexport import import_file, buildSSA
from line_control import LineControl


def main():

    verbose = "--verbose" in sys.argv
    
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("LiteralTranslator App")
        print('Usage: python main.py "<path to file>" "start=<starting_line_number>"')
        sys.exit(1)
    file_path = os.path.abspath(args[0])

    if not os.path.isfile(file_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
        

    subs = import_file(file_path, verbose)
    start = STARTING_LINE
    for arg in sys.argv[1:]:
        if arg.startswith("start="):
            start = int(arg.split("=", 1)[1])

    control = LineControl(subs, verbose, global_state=start)
    user_prompt = control.line_prompt()

    i = 0
    complete_list_of_subtitle_events = []
    while True:
        i += 1
        if i > control.iters:
            print(f"Maximum iterations ({control.iters}) reached.")
            break
        
        try:
            client, messages = ai_initiate(user_prompt, verbose)
            response_translations = generate_content(client, messages, verbose)
            print(response_translations)
            if verbose:
                print(f"Calling function 'translate_subtitle' with args '{response_translations}'")
            complete_list_of_subtitle_events.extend(control.translate_subtitle(**response_translations))

        except Exception as e:
            print(f"Error in generate_content: {e}")
        
    os.path.dirname(file_path)
    output_path = str(os.path.dirname(file_path)) + "/" + str(os.path.basename(file_path)) + "_translated.ass"
    buildSSA(complete_list_of_subtitle_events, output_path)

    return "translated successfully!"


if __name__=="__main__":
    main()