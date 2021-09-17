from bin import globals

def run(date_range):
    if date_range == "W":
        seconds = 7*24*3600
    elif date_range == "D":
        seconds = 24*3600
    elif date_range == "H":
        seconds = 3600
    return seconds

