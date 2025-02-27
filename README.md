# Skybound
![Skybound Logo](imgs/char4.png)
## A 2d platformer OOP game with:
- State management, different screens.
- Animations, sfxs.
- NPC monster with simple AI and infinite, random level creation.
- A simple database for storing highscore, player selection, 
with homemade API functionality.
- Documented according to PEP-8 (ish).

## Missing functionality:
- Parallaxing background + Background shaders
- Main menu: Shop functionality, character selection functionality
- Pause screen: Clickable buttons, pause music functionality
- Animation spritesheet for better animation control
- Player class: different character selections

## I took some art from the internet


## Example Build instructions for pyinstaller script / autopytoexe:

pyinstaller --noconfirm --onefile --windowed --icon "C:Path to game\sprites\icon.ico" --name "Skybound4" --add-data "C:Path to game\font;font/" --add-data "C:\Path to game\txts;txts/" --add-data "C:Path to game\sprites;sprites/" --add-data "C:Path to game\sfxs;sounds/"  "C:Path to game\main.py"
