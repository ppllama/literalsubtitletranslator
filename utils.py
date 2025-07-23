from random import randrange

def make_get_colour():
    last_called = [None]
    def get_colour():
        very_distinct_ass_colors = [
        "&H0000FF&",  # Bright Red
        "&H00FF00&",  # Bright Green
        "&HFF0000&",  # Deep Blue
        "&H007FFF&",  # Orange
        "&H00D7FF&",  # Gold
        "&HFFB6C1&",  # Pink
        "&HCCCC00&",  # Aqua
        "&HFFFFFF&",  # White
]
        while True:
            color = very_distinct_ass_colors[randrange(0,8)]
            if color == last_called[0]:
                continue
            else:
                last_called[0] = color
                return color
    return get_colour

get_colour = make_get_colour()