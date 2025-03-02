# Skybound
![Skybound Logo](imgs/IdleL2.png)
![Skybound Logo](imgs/sky2.png)
## A 2d platformer OOP game with:
- State management and different screens (Menu, start, game, pause, gameover...).
- Fluid animations Using a spritesheet with JSON metadata
- Different background music based on gamestates.
- NPC monster with simple AI
- Infinite, random level creation.
- A shop with coin systems and different characters
- A simple database for storing highscore, player selection, etc with homemade API functionality.
- 46 MB executable with pyinstaller instructions
- Documented according to PEP-8 (ish) and well structured.

## Works on Windows, Mac, Linux, Android

## Missing functionality:
- Parallaxing background + Background shaders
- Pause screen: Clickable buttons, pause music functionality

## I took the background images from here
[Background images](https://craftpix.net/freebies/free-sky-with-clouds-background-pixel-art-set/)


## You can run the game by running main.py if you have the dependecies
- Python 3
- Pygame

## Build instructions for pyinstaller to create exe file (only 46MB!):

1. Pip install Pyinstaller and Pygame

2. Modify the Pyinstaller script for your Path: "C:Path to game"

3. Run the script: 

pyinstaller --noconfirm --onefile --windowed --optimize "1" --icon "C:Path to game\Skybound\icon.ico" --name "Skybound4" --add-data "C:Path to game\Skybound\font;font/" --add-data "C:\Path to game\Skybound\txts;txts/" --add-data "C:Path to game\Skybound\imgs;imgs/" --add-data "C:Path to game\Skybound\sfxs;sfxs/"  "C:Path to game\Skybound\main.py"

4. Output will be in a dist folder, with build data in a build folder
