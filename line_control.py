from config import NUMBER_OF_LINES_PER_REQUEST
from fugashi_split import fugashi_split
from ast import literal_eval
from google import genai
from google.genai import types
import math

class LineControl():
    
    def __init__(self, subs, verbose, global_state=0):
        self.subs = subs
        self.global_state = global_state #keeps track of which line was last called
        self.current_line = None
        self.verbose = verbose
        self.iters = math.ceil(len(subs)/NUMBER_OF_LINES_PER_REQUEST)


    def line_prompt(self):
        number_of_lines = len(self.subs)

        if self.verbose:
            print(f"Line Number: {self.global_state + 1}\n")

        if number_of_lines == 0 or not (0 <= self.global_state < number_of_lines):
            return f"end of document at {number_of_lines}"

        def get_text(index):
            return str(self.subs[index].text) if 0 <= index < number_of_lines else "None"

        contextminus2 = get_text(self.global_state - 2)
        contextminus1 = get_text(self.global_state - 1)
        contextplus1  = get_text(self.global_state + NUMBER_OF_LINES_PER_REQUEST)
        contextplus2  = get_text(self.global_state + NUMBER_OF_LINES_PER_REQUEST + 1)

        lines_to_translate = []
        for i in range(min(NUMBER_OF_LINES_PER_REQUEST, number_of_lines - self.global_state)):
            lines_to_translate.append(fugashi_split(self.subs, self.global_state + i))
            lines_to_translate.append(get_text(self.global_state + i))
        
        parts = []
        
        if self.global_state == 0 or self.global_state == 1:
            parts.append("### Start of subtitle")
            parts.append("")

        for label, text in [
            ("### Context -2", contextminus2),
            ("### Context -1", contextminus1)
        ]:
            if text != "None":
                parts.append(label)
                parts.append(text)
                parts.append("")

        parts.append("### Line:" if len(lines_to_translate) == 1 else "### Lines:")
        parts.extend(lines_to_translate)
        parts.append("")

        for label, text in [
            ("### Context +1", contextplus1),
            ("### Context +2", contextplus2)
        ]:
            if text != "None":
                parts.append(label)
                parts.append(text)
                parts.append("")

        if self.global_state + NUMBER_OF_LINES_PER_REQUEST >= number_of_lines - 1 or self.global_state + NUMBER_OF_LINES_PER_REQUEST >= number_of_lines - 2:
            parts.append("### End of subtitle")
        
        self.current_line = self.global_state
        self.global_state = self.global_state + NUMBER_OF_LINES_PER_REQUEST - 1

        return "\n".join(parts)
    

    def translate_subtitle(self, translated_dict_list):
        list_of_subtitle_events = []
        translated_dict_list = literal_eval(translated_dict_list)
        for line in translated_dict_list:
            subtitle_event = []
            jap_tokens = []
            eng_tokens = []
            for key, value in line.items():
                jap_tokens.append(key)
                eng_tokens.append(value)
            subtitle_event.append(jap_tokens)
            subtitle_event.append(eng_tokens)
            subtitle_event.append(self.subs[self.current_line])
            list_of_subtitle_events.append(subtitle_event)
        return list_of_subtitle_events

        




schema_translate_subtitle = types.FunctionDeclaration(
    name="translate_subtitle",
    description="Constructs subtitle from given list of translations.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "translated_dict_list": types.Schema(
                type=types.Type.STRING,
                description="Translations from Japanese to English word for word as a list of python dictionaries. Each item in the list is one subtitle line as its dictionary.",
            ),
        },
    ),
)