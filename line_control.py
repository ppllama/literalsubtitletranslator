from config import NUMBER_OF_LINES_PER_REQUEST
from fugashi_split import fugashi_split

class LineControl():
    
    def __init__(self, subs):
        self.subs = subs


    def line_prompt(self, line_number):
        number_of_lines = len(self.subs)
        # if number_of_lines <= 0 or line_number > number_of_lines:
        if number_of_lines == 0 or not (0 <= line_number < number_of_lines):
            return f"end of document at {number_of_lines}"
        
        # if line_number - 2 < 0:
        #     contextminus2 = "None"
        # else:
        #     contextminus2 = str(self.subs[line_number - 2].text)
        
        # if line_number - 1< 0:
        #     contextminus1 = "None"
        # else:
        #     contextminus1 = str(self.subs[line_number - 1].text)
        
        # if line_number + NUMBER_OF_LINES_PER_REQUEST > number_of_lines - 1:
        #     contextplus1 = "None"
        # else:
        #     contextplus1 = str(self.subs[line_number + NUMBER_OF_LINES_PER_REQUEST].text)

        # if line_number + NUMBER_OF_LINES_PER_REQUEST + 1 > number_of_lines - 1:
        #     contextplus2 = "None"
        # else:
        #     contextplus2 = str(self.subs[line_number + NUMBER_OF_LINES_PER_REQUEST + 1].text)

        def get_text(index):
            return str(self.subs[index].text) if 0 <= index < number_of_lines else "None"

        contextminus2 = get_text(line_number - 2)
        contextminus1 = get_text(line_number - 1)
        contextplus1  = get_text(line_number + NUMBER_OF_LINES_PER_REQUEST)
        contextplus2  = get_text(line_number + NUMBER_OF_LINES_PER_REQUEST + 1)

        lines_to_translate = []
        for i in range(min(NUMBER_OF_LINES_PER_REQUEST, number_of_lines - line_number)):
            lines_to_translate.append(fugashi_split(self.subs, line_number + i))
        
        output = []
        if line_number == 0:
            output.append("start of subtitle")
        output.append(contextminus2)
        output.append(contextminus1)
        output.extend(lines_to_translate)
        output.append(contextplus1)
        output.append(contextplus2)
        if line_number == number_of_lines - 1:
            output.append("end of subtitle")

        return output