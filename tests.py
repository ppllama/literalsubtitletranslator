from importexport import import_file, buildSSA
from line_control import LineControl
from ai_generator import generate_content, ai_initiate
from utils import get_colour
import os

verbose = True
file_path = "/home/vishnu/workspace/github.com/ppllama/literalsubtitletranslator/content/Dororo S01E01.ja.srt"
subs = import_file("content/Dororo S01E01.ja.srt", verbose)
control = LineControl(subs,verbose, global_state=0)
prompt = control.line_prompt()
print(prompt)
# client, messages = ai_initiate(prompt, verbose)
# response_translations = generate_content(client, messages, verbose)
# print(response_translations)

# print(get_colour())

complete_list_of_subtitle_events = []
complete_list_of_subtitle_events.extend(control.translate_subtitle('[{"奥方様": "My lady", "もう少し": "just a little more", "に": "to", "ござりまする": "is", "ぞ": "!"}, {"奥方様": "My lady", "お気を確かに": "stay calm", "もう少し": "just a little more", "に": "to", "ござりまする": "is"}, {"醍醐様": "Lord Daigo", "か": "?"}, {"この": "This", "地獄堂": "Hell Hall", "へ": "to", "入られた": "entered", "ということは": "means that"}, {"神仏": "Gods and Buddhas", "を": "to", "捨て": "abandon", "この": "these", "鬼神": "demons", "たち": "to"}, {"もはや": "Now", "お": "to", "止め": "stop", "する": "doing", "こと": "that", "は": "is", "でき": "can", "ます": "do", "まい": "not", "な": "...", "..."}, {"もう": "One", "一度": "more time", "だけ": "just", "言う": "say", "て": "and", "おき": "keep", "ましょう": "let\'s..."}, {"醍醐様": "Lord Daigo", "...": "..."}, {"御仏": "Buddha", "の": "\'s", "道": "path", "を": "to", "外れる": "deviate", "は": "is", "外道": "heresy", "...": "..."}, {"外道": "Heretic", "に": "in", "ある": "being", "は": "is", "人": "human", "に": "is", "あら": "not", "ず": "...", "..."}, {"踏み出せ": "Step out", "ば": "if", "、": ",", "この": "this", "先": "ahead", "あなた様": "you", "を": "are", "待っ": "waiting", "て": "is", "いる": "there", "の": "is", "は": "is", "ただ": "only", "地獄": "hell", "...": "..."}, {"上人殿": "Venerable Shonin", "...": "...", "地獄": "Hell", "と": "is", "は": "is", "この世": "this world", "の": "\'s", "こと": "thing", "よ": "...", "..."}, {"そなた": "You", "ら": "all", "が": "that", "日がな": "all day long", "一": "one", "日": "day", "拝ん": "worshipping", "で": "with", "い": "being", "た": "past", "御仏": "Buddha", "の": "\'s", "道": "path", "など": "etc.", "、": ",", "どこ": "anywhere", "に": "to", "も": "even", "あり": "exist", "は": "is", "せ": "not", "ぬ": "...", "..."}, {"で": "Then", "は": "...", "...": "...", "どう": "how", "あっ": "be", "て": "...", "も": "also", "...": "..."}, {"知れ": "Known", "た": "thing", "こと": "..."}]'))
print(complete_list_of_subtitle_events)
# output_path = str(os.path.dirname(file_path)) + "/" + str(os.path.basename(file_path)) + "_translated.ass"
# buildSSA(complete_list_of_subtitle_events, output_path)