import os

"""
This file is for handling the database logic. It is used to get and set the values of the database.
Which is a folder of txt files for state management.
"""

##################################################################################


def GetScore():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Score.txt"), "r") as f:
        return int(f.read())


def SetScore(score):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Score.txt"), "w") as f:
        f.write(str(score))


##################################################################################


def GetLevel():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "level.txt"), "r") as f:
        return int(f.read())


def SetLevel(level):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "level.txt"), "w") as f:
        f.write(str(level))


##################################################################################


def GetGamestate():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Gamestate.txt"), "r") as f:
        return f.read()


def SetGamestate(newGamestate):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Gamestate.txt"), "w") as f:
        f.write(str(newGamestate))


##################################################################################


def GetHighScore():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Highscore.txt"), "r") as f:
        return int(f.read())  # int(f.read())?


def SetHighScore(newHighScore):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    if newHighScore > int(GetHighScore()):
        with open(os.path.join(txt_folder_path, "Highscore.txt"), "w") as f:
            f.write(str(newHighScore))


def manualSetHighScore(newHighScore):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Highscore.txt"), "w") as f:
        f.write(str(newHighScore))


##################################################################################

# The code below is discontinued

##################################################################################


def Hat():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Hat.txt"), "r") as f:
        return f.read()  # More logic could be added here to check if the hat is valid.


def SetHat(newHat):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Hat.txt"), "w") as f:
        f.write(str(newHat))


##################################################################################


def SetChar(char):
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Char_selection.txt"), "w") as f:
        f.write(str(char))


def SelectedChar():
    txt_folder_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "txts")
    )
    with open(os.path.join(txt_folder_path, "Char_selection.txt"), "r") as f:
        return int(f.read())


##################################################################################
