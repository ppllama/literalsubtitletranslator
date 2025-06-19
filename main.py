import pysubs2

with open("content/Dororo S01E01.ja.srt", "r") as source_file:
    content = source_file.read()
with open("subtitles.srt", "w") as fp:
    fp.write(content)
subs = pysubs2.load("subtitles.srt")
print(subs[0].text)
