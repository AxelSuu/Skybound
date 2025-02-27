# Skybound
![Skybound Logo](imgs/char5.png)![Skybound Logo](imgs/char4_7.png)![Skybound Logo](imgs/char5_2.png)![Skybound Logo](imgs/jumping_r.png)![Skybound Logo](imgs/Mob3.png)
![Skybound Logo](imgs/sky2.png)
## A 2d platformer OOP game with:
- State management, different screens.
- Animations, sfxs.
- NPC monster with simple AI and infinite, random level creation.
- A simple database for storing highscore, player selection, 
with homemade API functionality.
- 43 MB executable with pyinstaller instructions
- Documented according to PEP-8 (ish).

## Missing functionality:
- Parallaxing background + Background shaders
- Main menu: Shop functionality, character selection functionality
- Pause screen: Clickable buttons, pause music functionality
- Animation spritesheet for better animation control
- Player class: different character selections

## I took some art from the internet


## Build instructions for pyinstaller (only 43MB!):

pyinstaller --noconfirm --onefile --windowed --icon "C:Path to game\imgs\icon.ico" --name "Skybound4" --add-data "C:Path to game\font;font/" --add-data "C:\Path to game\txts;txts/" --add-data "C:Path to game\imgs;imgs/" --add-data "C:Path to game\sfxs;sfxs/"  "C:Path to game\main.py"
