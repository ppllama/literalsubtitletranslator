import pysubs2, sys

def import_file(file_path, verbose=False):

    try:
        with open(file_path, "r") as source_file:
            content = source_file.read()
        with open("subtitles.srt", "w") as fp:
            fp.write(content)
        subs = pysubs2.load("subtitles.srt")
        if verbose:
            print(f"importing file:{file_path}")
        return subs
    except Exception as e:
        print(e)
        sys.exit(1)