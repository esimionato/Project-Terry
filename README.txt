README:

author: Nicholas Peterson
	npeterso@andrew.cmu.edu

Project-Terry is a Dragon Quest-esque role-playing experience coded in Python3 and features several elements from the original games by Square Enix. The game features battling, puzzles, leveling up, and somewhat of framework of dictionaries and keying guides for connecting more navigable maps at the directory level. Such “maps” must be pieced together in some sort of tiled map editors and saved as .tmx files. Others may also add more monsters and sprites to the bestiary, though the format for their stats is admittedly a bit more esoteric.


The author does not own any pictures and/or tilesets used for the graphics of this game. The .tmx tilemaps provided are original pieces created by the author, while being pieced together from palettes of media and art not owned by the author. Such pieces of media utilized in making these are property of their respective creator but are both used by the author in a “transformative” manner and in a manner that does not garner financial gain, as described under Title 17 of the United States Code, 17 U.S.C. § 107 and weighing for protected fair use.

Tilesets and game art were either ripped from existing Square Enix ROMs or were made available through applications such as RPG maker, or sites such as opengameart.org

Music pieces featured were composed by Koichi Sugiyama and can also be enjoyed in most Square Enix Dragon Quest titles.


How to Run:

	Install pygame and libraries (directions follow)

#############################################################################################

              Windows

Download the correct Pygame .whl file from:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

pygame-1.9.2a0-cpXX-none-win32.whl

With XX replaced with
    - "34" if using Python 3.4
    - "35" if using Python 3.5

Open a Command Prompt (Start Menu -> type "cmd" in search -> Enter)

Navigate to the Scripts folder of your Python installation using the "cd" command

For example, if Python is installed in C:\Python35, type

    cd Python35\Scripts

Use pip to install Pygame

    pip install C:\Users\Me\Downloads\pygame-1.9.2a0-cp35-none-win32.whl

#############################################################################################

	Mac OSX:

Open a Terminal window

Type the command

    brew -v

If you get an error (brew: not found), then install homebrew by using the command

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Install all the Pygame dependencies:

    brew install mercurial git
    brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi

Use pip to install Pygame from source:

    pip3 install hg+http://bitbucket.org/pygame/pygame

#############################################################################################

 Now, download & install the following dependencies in the easy-enough manner as described above  
 (again simply utilizing pip install or pip3 install in cmd or terminal window):
	
       download: https://github.com/bitcraft/pyscroll
	pip3 install pyscroll

       download: https://github.com/bitcraft/PyTMX
	pip3 install pytmx	    
	

#############################################################################################

Running the game:

open Main.py file in text editor of choosing and run

OR

open terminal or cmd prompt
cd path/to/folder/Demo
python3 Main.py

OR

open terminal
python3 (and drag with your mouse Main.py to the terminal)


controls 

	AWSD navigating character
	A - left
	W - up
	S - down
	D - right
	
	
	in battle:
	SPACE - attack
	R     - run
