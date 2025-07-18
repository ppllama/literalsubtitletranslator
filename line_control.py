from config import NUMBER_OF_LINES_PER_REQUEST
from fugashi_split import fugashi_split

class LineControl():
    
    def __init__(self, subs, verbose):
        self.subs = subs
        self.verbose = verbose


    def line_prompt(self, line_number):
        number_of_lines = len(self.subs)

        if self.verbose:
            print(f"Line Number (zero indexed): {line_number + 1}\n")

        if number_of_lines == 0 or not (0 <= line_number < number_of_lines):
            return f"end of document at {number_of_lines}"

        def get_text(index):
            return str(self.subs[index].text) if 0 <= index < number_of_lines else "None"

        contextminus2 = get_text(line_number - 2)
        contextminus1 = get_text(line_number - 1)
        contextplus1  = get_text(line_number + NUMBER_OF_LINES_PER_REQUEST)
        contextplus2  = get_text(line_number + NUMBER_OF_LINES_PER_REQUEST + 1)

        lines_to_translate = []
        for i in range(min(NUMBER_OF_LINES_PER_REQUEST, number_of_lines - line_number)):
            lines_to_translate.append(fugashi_split(self.subs, line_number + i))
        
        parts = []
        
        if line_number == 0 or line_number == 1:
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

        if line_number == number_of_lines - 1 or line_number == number_of_lines - 2:
            parts.append("### End of subtitle")

        return "\n".join(parts)