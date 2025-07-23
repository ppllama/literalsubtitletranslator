from importexport import import_file
from line_control import LineControl
from ai_generator import generate_content, ai_initiate
from utils import get_colour

verbose = True
subs = import_file("content/Dororo S01E01.ja.srt", verbose)
control = LineControl(subs,verbose, global_state=10)
prompt = control.line_prompt()
# print(prompt)
# client, messages = ai_initiate(prompt, verbose)
# response_translations = generate_content(client, messages, verbose)
# print(response_translations)

print(get_colour())


print(control.translate_subtitle([{"奥方様": "My Lady", "、": ",", "もう": "just", "少し": "a little", "に": "more to", "ござりまする": "is", "ぞ": "!"}, {"奥方様": "My Lady", "、": ",", "お": "please", "気": "mind", "を": "your", "確か": "steady", "に": "...", "もう": "just", "少し": "a little", "に": "more to", "ござりまする": "is"}, {"醍醐様": "Lord Daigo", "か": "?"}, {"この": "This", "地獄堂": "Hell Hall", "へ": "to", "入られた": "entered", "という": "that", "こと": "thing", "は": "is"}]))