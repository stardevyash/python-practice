from ifelse import main
from data import l

def save_data():
    name = main()

    if name:
        l.append(name.upper())