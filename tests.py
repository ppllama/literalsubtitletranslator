from import_file import import_file
from line_control import LineControl

subs = import_file("content/Dororo S01E01.ja.srt", verbose=True)
control = LineControl(subs, verbose=True)
print(control.line_prompt(194))