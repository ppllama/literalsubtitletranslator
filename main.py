import sys, os
from ai_generator import ai_initiate, generate_content
from config import STARTING_LINE, AI_FAIL_LIMIT
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
    start = STARTING_LINE - 1
    for arg in sys.argv[1:]:
        if arg.startswith("start="):
            start = int(arg.split("=", 1)[1]) - 1

    control = LineControl(subs, verbose, global_state=start)
    

    i = 0
    j = 0
    complete_list_of_subtitle_events = []
    proceed = True
    while True:
        i += 1
        if j > AI_FAIL_LIMIT:
            print("AI keeps failing. Mission Abort")
            sys.exit(1)
        elif proceed == False:
            i -= 1
        if i > control.iters:
            print(f"Maximum iterations ({control.iters}) reached.")
            break
        
        try:
            user_prompt = control.line_prompt(proceed)
            client, messages = ai_initiate(user_prompt, verbose)
            response_translations = generate_content(client, messages, verbose)
            if response_translations == None:
                raise Exception("Generate Content Failed. Retrying...")
            print(f"generate content success! {i}")
            if verbose:
                print(f"Calling function 'translate_subtitle' with args '{response_translations}'")
            current_subtitle_events = control.translate_subtitle(**response_translations)
            print(f"Subtitle events parsed {i}")
            if verbose:
                print(f"Subtitle events parsed! {i}", current_subtitle_events)
            complete_list_of_subtitle_events.extend(current_subtitle_events)
            if verbose:
                print("List of subtitle events so far:", complete_list_of_subtitle_events)
            proceed = True

        except Exception as e:
            proceed = False
            j += 1
            print(f"Error: {e!r} (type: {type(e)}). Retrying...")
        
    if verbose:
        print("The complete list of subtitle events:", complete_list_of_subtitle_events)

    output_path = str(os.path.dirname(file_path)) + "/" + str(os.path.basename(file_path)) + "_translated.ass"
    buildSSA(complete_list_of_subtitle_events, output_path)

    print(f"translated successfully. File saved to {output_path}")
    return


if __name__=="__main__":
    main()