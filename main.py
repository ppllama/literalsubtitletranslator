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
    

    i = 0
    complete_list_of_subtitle_events = []
    # proceed = True
    while True:
        i += 1
        if i > control.iters:
            print(f"Maximum iterations ({control.iters}) reached.")
            break
        
        try:
            user_prompt = control.line_prompt()
            client, messages = ai_initiate(user_prompt, verbose)
            response_translations = generate_content(client, messages, verbose)
            # if response_translations == None:
            #     continue
            print("generate content success!")
            if verbose:
                print(f"Calling function 'translate_subtitle' with args '{response_translations}'")
            current_subtitle_events = control.translate_subtitle(**response_translations)
            print("Subtitle_events_parsed")
            if verbose:
                print("Subtitle_events_parsed!", current_subtitle_events)
            complete_list_of_subtitle_events.extend(current_subtitle_events)
            if verbose:
                print("List of subtitle events so far:", complete_list_of_subtitle_events)
            # proceed = True

        except Exception as e:
            print(f"Error in generate_content: {e}")
            # proceed = False
            # i -= 1
        
    if verbose:
        print("The complete list of subtitle events:", complete_list_of_subtitle_events)

    output_path = str(os.path.dirname(file_path)) + "/" + str(os.path.basename(file_path)) + "_translated.ass"
    buildSSA(complete_list_of_subtitle_events, output_path)

    print(f"translated successfully. File saved to {output_path}")
    return


if __name__=="__main__":
    main()