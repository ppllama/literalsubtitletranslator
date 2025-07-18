from fugashi import Tagger

def fugashi_split(subs, line_number):
    tagger = Tagger()
    dict_keys = {}
    for word in tagger(subs[line_number].text):
        dict_keys[word] = None
    return str(dict_keys)

