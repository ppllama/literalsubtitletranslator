import pysubs2, sys
from utils import get_colour
from config import SHIFT_TIME

def import_file(file_path, verbose=False):

    try:
        with open(file_path, "r") as source_file:
            content = source_file.read()
        with open("subtitles.srt", "w") as fp:
            fp.write(content)
        subs = pysubs2.load("subtitles.srt")
        if verbose:
            print(f"importing file:{file_path}")
        print("File imported successfully!, File_path:", file_path)
        return subs

    except Exception as e:
        print(e)
        sys.exit(1)

def buildSSA(event_list, file_path):
    subs = pysubs2.SSAFile()
    for i in range(len(event_list)):
        event_list[i][0]
        event_list[i][1]
        text_jap = ""
        text_eng = ""
        for j in range(0, len(event_list[i][0])):
            colour = r"\c" + str(get_colour())
            space = ""
            if j > 0:
                space = " "
            text_jap += f"{space}{{{colour}}}{event_list[i][0][j]}"
            text_eng += f"{space}{{{colour}}}{event_list[i][1][j]}"
            text = text_eng + r"\N" + text_jap
        subs.append(pysubs2.SSAEvent(start=event_list[i][2].start,
                                     end=event_list[i][2].end,
                                     text=text,))
        
    subs.shift(s=SHIFT_TIME)
    
    subs.save(file_path,format_="ass")