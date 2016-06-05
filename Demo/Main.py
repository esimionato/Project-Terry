# by Nicholas Peterson
# scrolling functionality and pygame wrapper from 
# Quest.py, tutorial of pyscroll module by bitcraft
# animated water tileset: http://opengameart.org/content/animated-water-tiles
# Music from Dragon Quest symphonic suite
# Tilesets from rpg maker, Dragon Quest games, pyscroll demo
# monster images and characters from Dragon Quest games
# Tilemaps by Nicholas Peterson

import os.path
import math
import random 

import pygame
from pygame.locals import *
from pytmx.util_pygame import load_pygame

import pyscroll
import pyscroll.data
from pyscroll.group import PyscrollGroup



################################################################################
RESOURCES_DIR = 'data'

HERO_MOVE_SPEED = 100  # pixels per second

# filename + portal# : new filename
InstDictIn = {
    "data/DragonQuest.tmxportal1": "town.tmx", 
    "data/DragonQuest.tmxportal2": "castleTown.tmx",
    "data/DragonQuest.tmxportal3": "towerEntrance.tmx",
    "data/DragonQuest.tmxportal4": "temple1.tmx", 

    "data/town.tmxportal1": "town1-house1.tmx",
    "data/town1.tmxportal1": "town1-house1.tmx",
    "data/town2.tmxportal1": "town1-house1.tmx",
    "data/town.tmxportal2": "town1-inn.tmx",
    "data/town1.tmxportal2": "town1-inn.tmx",
    "data/town2.tmxportal2": "town1-inn.tmx",


    "data/castleTown.tmxportal1": "castleTown-inn.tmx",

    "data/towerEntrance.tmxportal1": "Tower.tmx",
    "data/temple1.tmxportal1": "temple2.tmx",
    "data/town1-house1.tmxportal1": "house1Basement.tmx",
    "data/house1Basement.tmxportal1": "house1Basement2.tmx",
    # start of puzzle
    "data/house1Basement2.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2.tmxportal6": "house1Basement2-6.tmx",

    "data/house1Basement2-1.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-1.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-1.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-1.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-1.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-1.tmxportal6": "house1Basement2-6.tmx",

    "data/house1Basement2-2.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-2.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-2.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-2.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-2.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-2.tmxportal6": "house1Basement2-6.tmx",

    "data/house1Basement2-3.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-3.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-3.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-3.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-3.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-3.tmxportal6": "house1Basement2-6.tmx",

    "data/house1Basement2-4.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-4.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-4.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-4.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-4.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-4.tmxportal6": "house1Basement2-6.tmx",


    "data/house1Basement2-5.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-5.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-5.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-5.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-5.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-5.tmxportal6": "house1Basement2-6.tmx",

    "data/house1Basement2-6.tmxportal1": "house1Basement2-7.tmx",
    "data/house1Basement2-6.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-6.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-6.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-6.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-6.tmxportal6": "house1Basement2-3.tmx",

    "data/house1Basement2-7.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-7.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-7.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-7.tmxportal4": "house1Basement2-8.tmx",
    "data/house1Basement2-7.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-7.tmxportal6": "house1Basement2-3.tmx",

    "data/house1Basement2-8.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-8.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-8.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-8.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-8.tmxportal5": "house1Basement2-9.tmx",
    "data/house1Basement2-8.tmxportal6": "house1Basement2-3.tmx",

    "data/house1Basement2-9.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-9.tmxportal2": "house1Basement2-10.tmx",
    "data/house1Basement2-9.tmxportal3": "house1Basement2-3.tmx",
    "data/house1Basement2-9.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-9.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-9.tmxportal6": "house1Basement2-3.tmx",


    "data/house1Basement2-10.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-10.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-10.tmxportal3": "house1Basement2-11.tmx",
    "data/house1Basement2-10.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-10.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-10.tmxportal6": "house1Basement2-3.tmx",

    "data/house1Basement2-11.tmxportal1": "house1Basement2-1.tmx",
    "data/house1Basement2-11.tmxportal2": "house1Basement2.tmx",
    "data/house1Basement2-11.tmxportal3": "house1Basement2-11.tmx",
    "data/house1Basement2-11.tmxportal4": "house1Basement2-2.tmx",
    "data/house1Basement2-11.tmxportal5": "house1Basement2-5.tmx",
    "data/house1Basement2-11.tmxportal6": "house1Basement2-3.tmx",

    # end of puzzle
    "data/house1Basement2-11.tmxportal7": "house1Basement3.tmx",
    "data/house1Basement3.tmxportal1": "town1.tmx",
    "data/house1Basement3-1.tmxportal1": "town1.tmx",


    "data/town1.tmxportal10": "house1Basement3-1.tmx",
    "data/town2.tmxportal10": "house1Basement3-1.tmx",

            }
# current filename: instance portalO (portal out)
InstDictOut = {
    "data/town.tmx": "DragonQuest.tmx", 
    "data/town1-house1.tmx": "town.tmx", 
    "data/DragonQuest.tmx": "DragonQuest.tmx",
    "data/castleTown.tmx": "DragonQuest.tmx", 
    "data/towerEntrance.tmx": "DragonQuest.tmx",
    "data/town1-inn.tmx": "town.tmx", 
    "data/castleTown-inn.tmx": "castleTown.tmx",
    "data/temple1.tmx": "DragonQuest.tmx",
    "data/Tower.tmx": "towerEntrance.tmx",
    "data/TowerNoDragon.tmx": "towerEntrance.tmx",
    "data/data/TowerNoDragon.tmx": "towerEntrance.tmx",
    "data/temple2.tmx": "temple1.tmx",

    "data/house1Basement.tmx": "town1-house1.tmx",
    "data/house1Basement2.tmx": "house1Basement.tmx",
    "data/house1Basement2-1.tmx": "house1Basement.tmx",
    "data/house1Basement2-2.tmx": "house1Basement.tmx",
    "data/house1Basement2-3.tmx": "house1Basement.tmx",
    "data/house1Basement2-4.tmx": "house1Basement.tmx",
    "data/house1Basement2-5.tmx": "house1Basement.tmx",
    "data/house1Basement2-6.tmx": "house1Basement.tmx",
    "data/house1Basement2-7.tmx": "house1Basement.tmx",
    "data/house1Basement2-8.tmx": "house1Basement.tmx",
    "data/house1Basement2-9.tmx": "house1Basement.tmx",
    "data/house1Basement2-10.tmx": "house1Basement.tmx",
    "data/house1Basement2-11.tmx": "house1Basement.tmx",

    "data/house1Basement3.tmx": "house1Basement2-11.tmx",
    "data/town1.tmx": "DragonQuest.tmx",
    "data/town2.tmx": "DragonQuest.tmx",
    "data/house1Basement3-1.tmx": "house1Basement2-11.tmx"
            }

# current filename : song
MusicDict = {
    "data/town.tmx": "MelodyOfLove.wav", 
    "town.tmx": "MelodyOfLove.wav", 
    "town1-house1.tmx": "MelodyOfLove.wav",
    "data/town1-house1.tmx": "MelodyOfLove.wav",
    "data/DragonQuest.tmx": "ThroughTheFields.wav", 
    "DragonQuest.tmx": "ThroughTheFields.wav",
    "data/castleTown.tmx": "Strolling.wav",
    "castleTown.tmx": "Strolling.wav","data/towerEntrance.tmx": 
    "UnknownWorld.wav",
    "towerEntrance.tmx": "UnknownWorld.wav",
    "town1-inn.tmx": "MoonRiverPub.wav", 
    "data/town1-inn.tmx": "MoonRiverPub.wav",
    "data/castleTown-inn.tmx": "AncientTown.wav", 
    "castleTown-inn.tmx": "AncientTown.wav",
    "temple1.tmx": "Endless.wav", 
    "data/temple1.tmx": "Endless.wav",
    "Tower.tmx": "UnknownWorld.wav", 
    "data/Tower.tmx": "UnknownWorld.wav",
    "data/TowerNoDragon.tmx": "UnknownWorld.wav",
    "data/temple2.tmx": "Endless.wav",

    "data/house1Basement.tmx": "Psaro.wav",
    "data/house1Basement2.tmx": "Psaro.wav",
    "data/house1Basement2-1.tmx": "Psaro.wav",
    "data/house1Basement2-2.tmx": "Psaro.wav",
    "data/house1Basement2-3.tmx": "Psaro.wav",
    "data/house1Basement2-4.tmx": "Psaro.wav",
    "data/house1Basement2-5.tmx": "Psaro.wav",
    "data/house1Basement2-6.tmx": "Psaro.wav",
    "data/house1Basement2-7.tmx": "Psaro.wav",
    "data/house1Basement2-8.tmx": "Psaro.wav",
    "data/house1Basement2-9.tmx": "Psaro.wav",
    "data/house1Basement2-10.tmx": "Psaro.wav",
    "data/house1Basement2-11.tmx": "Psaro.wav",

    "data/house1Basement3.tmx": "AncientTown.wav",
    "data/house1Basement3-1.tmx": "AncientTown.wav",
    "data/town1.tmx": "MelodyOfLove.wav",
    "data/town2.tmx": "MelodyOfLove.wav",
            }

# key current filename: entrance location on old filename
OldEntranceDict = {
    "data/town.tmx": (1024, 750), 
    "data/town1-house1.tmx": (542, 630),
    "data/town1.tmx": (1024, 750),
    "data/town2.tmx": (1024, 750),
     "data/DragonQuest.tmx": (1000, 1000),
    "data/castleTown.tmx": (961, 250), 
    "data/towerEntrance.tmx": (767, 327.5),
    "data/town1-inn.tmx": (396.4, 124.2),
    "data/castleTown-inn.tmx": (813, 1010), 
    "data/temple1.tmx": (1402, 565.4),
    "data/Tower.tmx": (406, 625.5),
    "data/TowerNoDragon.tmx": (406, 625.5),
    "data/temple2.tmx": (289, 302),

    "data/house1Basement.tmx": (129.7, 145.3),

    "data/house1Basement2.tmx": (286.75, 43.9),
    "data/house1Basement2-1.tmx": (286.75, 43.9),
    "data/house1Basement2-2.tmx": (286.75, 43.9),
    "data/house1Basement2-3.tmx": (286.75, 43.9),
    "data/house1Basement2-4.tmx": (286.75, 43.9),
    "data/house1Basement2-5.tmx": (286.75, 43.9),
    "data/house1Basement2-6.tmx": (286.75, 43.9),
    "data/house1Basement2-7.tmx": (286.75, 43.9),
    "data/house1Basement2-8.tmx": (286.75, 43.9),
    "data/house1Basement2-9.tmx": (286.75, 43.9),
    "data/house1Basement2-10.tmx": (286.75, 43.9),
    "data/house1Basement2-11.tmx": (286.75, 43.9),
    
    "data/house1Basement3.tmx": (286.3, 792.0),
    "data/house1Basement3-1.tmx": (286.3, 792.0)

            }

# number roll: monster name
monsterDict = {
    0: "slime", 1: "slime", 
    2: "red slime",  3: "red slime", 
    4: "draky", 
    5: "mud man", 6: "draky", 7: "mud man", 8: "draky", 9: "slime",
    10: "mud man", 11: "dragon", 12: "ghost", 13: "draky", 14: "ghost",
    15: "draky"
            }
# number roll: monster name, second dictionary (harder monsters)
monsterDict2 = {
    0: "draky", 1: "mud man", 2: "rogue knight", 3: "skeleton",
    4: "rogue knight", 5: "rogue knight", 6: "skeleton", 7: "skeleton",
    8: "skeleton", 9: "skeleton", 10: "golem", 11: "golem", 12: "golem"
            }
# hold names of bosses to call and give special text appearance
bossDict = { 
    "Wight Knight",

            }


# monster name: (image.png, (resizeX, resizeY), Y adjustor up/down, +-adj)
                                            # (negative adj for left)
monsterImageDict = {
    "slime": ("slime.png", (90, 90), 40), 
    "mud man": ("mudMan.png", (180, 185), -10), 
    "draky": ("draky.png", (150, 100), 20),
    "red slime": ("redslime.png", (80, 80), 40),
    "dragon": ("dragon.png", (300, 250), -60, -120),
    "rogue knight": ("rogueknight.png", (150, 150), -10),
    "skeleton": ("skeleton.png", (120, 160), -10), 
    "ghost": ("ghost.png", (140, 160), -10),
    "golem": ("golem.png", (260, 300), -60),
    "axeman": ("knightErrant.png", (230, 250), -50, -120),
    "beserker": ("knightAberrant.png", (230, 250), -50, -120),
    "ent": ("ent.png", (270, 280), -80, -120),
    "Wight Knight": ("wightknight.png", (350, 370), -90, -190)
            }

# hp str def
monsterStatDict = {
    "slime":(("hitpoints. strength. defense."), (5, 3, 5)),
    "red slime": (("hp. str. def."), (6, 7, 4)),
    "draky": (("hp. str. def."), (10, 8, 4)),
    "mud man": (("hp. str. def."), (12, 10, 7)),
    "dragon": ((), (750, 100, 100), ""), "skeleton": ((), (20, 15, 20)),
    "rogue knight": ((), (20, 15, 28)), 
    "ghost": ((), (9, 8, 5)),
    "golem": ((),(90, 35, 40)),
    "axeman": ((), (120, 50, 50)),
    "beserker": ((),(150, 80, 30)),
    "ent": ((), (120, 40, 40)),
    "Wight Knight": ((), (890, 220, 150))
            }

# monster name: exp reward
expDict = {
    "slime": 5, "red slime": 10, "draky": 15, "mud man": 30,
    "dragon": 5500, "skeleton": 60, "rogue knight": 90, "ghost": 20, 
    "golem": 350, "axeman": 500, "berserker": 800, "ent": 525,
    "Wight Knight": 9000
            }

# tmx object.name: (row, cols, row, col)
villagerDict = {
    "oldMan2": (8, 12, 2, 4), "girl1": (8, 12, 1, 7),
    "man1": (8, 12, 2, 10), "merchant1": (8, 12, 6, 4),
    "oldMan1Back": (8, 12, 0, 1), "man2": (8, 12, 6, 1), "girl2": (8, 12, 2, 7),
    "noble1": (8, 12, 6, 10), "merchant2": (8, 12, 7, 4)
            }

# see villagerDict
villager2Dict = {
    "nun1": (8, 12, 6, 10), "fighter": (8, 12, 2, 1),
    "priest": (8, 12, 2, 10), "guard": (8, 12, 2, 4)
            }

# if changing values, make sure hitpoints <= maxHitpoints
heroStats = {
    "maxHitpoints": 27, "hitpoints": 27, "strength": 8, 
    "defense": 7, "agility": 10, "level": 1, "exp": 0
            }

# keyed to levels to distribute agility points (for battle dodge chance)
agilityDict = {2: 2, 3: 3, 4: 3, 6: 5, 9: 5, 12: 10, 15: 10, 19: 20
            }


# current level: exp threshold to level up to next
levelDict = {
    1: 30, 2: 90, 3: 240, 4: 480, 5: 900, 6: 1000, 7: 2000, 8: 3500, 
    9: 6000, 10: 9500, 11: 15000, 12: 22000, 13: 31000, 14: 50000,
    15: 69000, 16: 90000, 17: 120000, 18: 151000, 19: 200000
            }

# tilemap: "mode" of the map to enable different monsterDict
battleDict = {
    "data/temple1.tmx" :"Overworld",
    "data/towerEntrance.tmx": "Peaceful",
    "data/Tower.tmx": "Dungeon",
    "data/DragonQuest.tmx": "Overworld",
    "data/temple2.tmx": "Dungeon2",
    "data/house1Basement.tmx": "Dungeon3",
    "data/house1Basement2.tmx": "Peaceful"
            }

# key filename: image background for battle mode
backgroundDict = {
    "data/Tower.tmx": "Resources/towerInside.jpg", 
    "Tower.tmx": "Resources/towerInside.jpg", 
    "data/temple1.tmx": "Resources/desert.jpg", 
    "data/house1Basement.tmx": "Resources/cellar.jpg",
    "data/temple2.tmx": "Resources/desertDungeon.jpg",
    "data/temple1.tmx": "Resources/desert.png",
    "data/house1Basement2.tmx": "Resources/cellar.jpg"

             }


################################################################################
# functions from original pyscroll demo Quest.py by bitcraft
def init_screen(width, height):
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    return screen


# makes loading maps a little easier
def get_map(filename):
    return os.path.join(RESOURCES_DIR, filename)


# makes loading images a little easier
def load_image(filename):
    return pygame.image.load(os.path.join(RESOURCES_DIR, filename))

screen = init_screen(900, 700)

################################################################################

# use pygame time to add delay without pygame pause (x in milliseconds)
def timeDelay(x):
    clock1 = pygame.time.get_ticks()
    clock2 = pygame.time.get_ticks()

    while clock2 - clock1 < x:
        clock2 = pygame.time.get_ticks()

    return None

# loads and plays song, only .wav works for dev's computer
def playMusic(song):
    # does not crash if file misnamed/does not quite exist
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1, 0.0) # '-1' as first parameter
                                         # therefore loops
    except pygame.error: 
        print("music error:", song)

def playSound(sound, vol):
    # does not crash if file misnamed/does not exist
    try:               
        soundEffect = pygame.mixer.Sound(sound)
        soundEffect.set_volume(vol)
        pygame.mixer.Sound.play(soundEffect)
    except pygame.error: 
        print("sound effect error:", sound)


# object for multirow/column pallete of characters
class Pallete(pygame.sprite.Sprite):
    # initializes images with pallete of character sprites
    def __init__(self, filename, rows=1,cols=1, row=0, col=0):
        self.rows = rows
        self.cols = cols
        pygame.sprite.Sprite.__init__(self)
        image = load_image(filename).convert_alpha() 
        (width, height) = image.get_size()
        (self.width, self.height) = (width, height)
        (charWidth, charHeight) = (width / cols, height / rows)
        self.image= image.subsurface(
                    (col * charWidth, row * charHeight, charWidth, charHeight))
        self.image = pygame.transform.scale(self.image, (32, 40))

class Villager(pygame.sprite.Sprite):
    # to be called in case of tmx object type being "person"
    def __init__(self, filename,x, y, rows=1, cols=1, row=0, col=0):
        pygame.sprite.Sprite.__init__(self)
        image = load_image(filename).convert_alpha()
        (width, height) = image.get_size()
        (charWidth, charHeight) = (width / cols, height / rows)
        self.type = "villager"

        self.frames = list()
        for z in range(0,2):
            self.frames.append(image.subsurface(
                    ((z+col) * charWidth, row * charHeight, 
                        charWidth, charHeight)))
            self.frames[z]= pygame.transform.scale(self.frames[z], (32, 40))
        self.image = self.frames[0]
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8)
        self.velocity = [0, 0]
       
    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom


    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def move_back(self, dt):
        # moves sprite back after collision if called
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def idleAnimation(self, ticks):
        # adds idle animation for sprite character
        n = 0
        # adjusts to nearest 500 milliseconds
        ticks = ticks//500*500
        if ticks%500 == 0:
            n = 0
        if ticks%1000 == 0:
            n = 1

        self.image = self.frames[n]



      

# Controls Battle between Hero and randomly rolled monsters
class Battle(object):
    def __init__(self, game, hero, position, screen):
        self.hero = hero
        self.levelPlaceholder = hero.level
        self.leveled = False
        self.game = game
        self.screen = screen

        self.position = position
        # rolls based on hero's location on map
        # different numbers give different monsters
        if position[0] < 900 and position[1] < 500:
            self.diceRoll = random.randint(7, 10)
            image = "Resources/desert.png"

        elif position[1] < 150:
            self.diceRoll = random. randint(7, 8)
            image = "Resources/desert.png"
            
        elif position[0] < 900: 
            self.diceRoll = random.randint(4, 6)
            image = "Resources/plains.png"

        else: 
            self.diceRoll = random.randint(0, 3)
            image = "Resources/field.jpg"

        if game.filename == "data/Tower.tmx" or game.filename == "Tower.tmx":
            self.diceRoll = 11
        if game.mode2 == "Dungeon3":
            self.diceRoll = random.randint(12, 15)
  
        monsterName = monsterDict[self.diceRoll]

        # else second monster dictionary
        if game.filename == "data/temple2.tmx":
            self.diceRoll = random.randint(0,9)
            monsterName = monsterDict2[self.diceRoll]
   
            monsterName = monsterDict2[self.diceRoll]
        if game.mode2 != "Overworld":
            image = backgroundDict[game.filename]
        
        self.monsterName = monsterName
        self.monster = Monster(monsterName, self, screen)
        self.monsterDeadText = "The " + monsterName + " was defeated!" 

        # load battle backdrop
        self.background = pygame.image.load(image)

    # draws rectangular battle menu
    def drawRectMenu(self, surface, x, y):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(surface, BLACK, [x/5, y/2 + 70, x/2+100, y/5])
        pygame.draw.rect(surface, WHITE, [x/5, y/2 + 70, x/2+100, y/5], 5)


    def drawBattle(self, surface):
        # draws monster image and menus
        x = surface.get_width()
        y = surface.get_height()
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        pygame.draw.rect(surface, BLACK, [100, 100, x - 200, y-200])
        pygame.draw.rect(surface, WHITE, [100, 100, x - 200, y-200], 5)
        myFont = pygame.font.SysFont("monospace", 30)
        text = myFont.render(" Battle",1, WHITE)

        # draw battle background
        self.background = pygame.transform.scale(self.background,
         (x - 200, y-200))
        surface.blit(self.background, (100, 100))
        surface.blit(text, (100, 100))

        # render monster dead text if monster is at or below 0 HP
        
        if self.monster.hitpoints > 0:
            adj = -50
            name = self.monster.monsterName
            if len(monsterImageDict[name]) >= 4:
                adj = monsterImageDict[name][3]
            surface.blit(self.monster.image, (x/2+adj, 
                y/2-90+self.monster.reposition))
            control1 = myFont.render("Attack: [SPACE]", 1, WHITE)
            control2 = myFont.render("Run:    [R]", 1, WHITE)

        if self.monster.hitpoints <= 0:
            self.prompt = myFont.render(self.monsterDeadText, 1, WHITE)
            surface.blit(self.prompt, (x/5, 140))

        if self.monster.hitpoints <= 0:
            if self.levelPlaceholder < self.hero.level:
                self.leveled = True
            if self.leveled == True:
                placement = (x/5 + 10, y/2 + 70)
                levelText = self.hero.name + " leveled up!"
                levelText = myFont.render(levelText, 1, WHITE)
                surface.blit(levelText, placement)

            
            # pause battle music
            if self.game.mode2 == "Overworld":
                pygame.mixer.music.pause()
           
            # if self.leveled == False:
            #     self.monster.text = ("The " + self.monster.monsterName  
            #     + " was defeated!")
            if self.leveled:
                statGrowth = self.hero.statGrowth
                lvl = self.hero.level
                self.monster.text = ("HP += " 
                    + str(statGrowth[lvl][0])
                    + " STR += " + str(statGrowth[lvl][1])
                    + " DEF += " + str(statGrowth[lvl][2]))
                self.monster.text2 = None
            
           

        # monster appear prompt otherwise
        else:
            self.prompt = myFont.render("A " + self.monsterName + 
            " appeared" + "!", 1, WHITE)
            if self.monsterName in bossDict:
                self.prompt = myFont.render("The " + self.monsterName + 
            " appears" + "!", 1, WHITE)
            if self.monsterName == "Wight Knight":
                self.prompt = myFont.render("The " + self.monsterName + 
            " strides forth" + "!", 1, WHITE)
            if self.monsterName == "dragon":
                self.prompt = myFont.render("This " + self.monsterName + 
            " appears menacing" + "!",
            1, WHITE)

            if self.monster.monsterName not in bossDict:
                extraText = myFont.render("It wants to fight!", 1, WHITE)
                surface.blit(extraText, (x/5, 170))
            surface.blit(self.prompt, (x/5, 140))
            

        # draw menu
        self.drawRectMenu(surface, x, y)
        edge = (x/3 + x/15)

        length = len(self.monster.text)
        # wraps long text to next line
        if self.monster.text2 == None and length*50 > edge:
            place = len(self.monster.text)
            self.monster.text2 = " "
            while length * 21 > edge or self.monster.text2[-1] != " ":
                place -= 1
                self.monster.text2 += self.monster.text[place:]
                self.monster.text = self.monster.text[0:place]
                length = len(self.monster.text)
                # must reverse constructed text
            self.monster.text2 = self.monster.text2[::-1]
 
        monsterText = myFont.render(self.monster.text, 1, WHITE)
        if self.monster.text == "What will you do?":
            surface.blit(control1, (x/2, y/2 + 131))
            surface.blit(control2, (x/2, y/2 + 161))
        surface.blit(monsterText, (x/3 + x/11 + 10 , y/2 + 100))
        if self.monster.text2 != None:
            monsterText2 = myFont.render(self.monster.text2, 1, WHITE)
            surface.blit(monsterText2, (x/3 + x/11 + 10, y/2 + 131))

        # render level up text if necessary
        if self.levelPlaceholder < self.hero.level:
            self.leveled = True
            newLvl = self.hero.level
            statGrowth = self.hero.statGrowth
            placement = (x/5 + 10, y/2 + 70)

            
            timeDelay(500)

        # hero stats text
        hitpoints = ("HP " + str(self.hero.hitpoints) + "/" 
            +str(self.hero.maxHitpoints))
        strength = "STR  " + str(self.hero.strength)
        defense = "DEF  "    + str(self.hero.defense)
        (HPText, STRText, DEFText) = (myFont.render(hitpoints, 1, WHITE),
                        myFont.render(strength, 1, WHITE),
                        myFont.render(defense, 1, WHITE))
        name = self.hero.name + "  Lv: " + str(self.hero.level)
        name = myFont.render(name, 1, WHITE)
        # if not self.leveled:
        surface.blit(name, (x/5 + 10 , y/2 + 70))
        surface.blit(HPText, (x/5 + 20 , y/2 + 100))
        surface.blit(STRText, (x/5 + 20, y/2 + 131))
        surface.blit(DEFText, (x/5 + 20, y/2 + 161))
    
        pygame.display.flip()

    # atttempt to end battle
    def endBattle(self, game):
        if self.monster.hitpoints <= 0:
            game.battleInstance = False
            if self.monster.monsterName == "dragon":
                oldMap = InstDictOut["data/TowerNoDragon.tmx"]
                game.filename = "TowerNoDragon.tmx"
                self.hero.levelUp(self)
                timeDelay(1500)
                self.hero.dragonKilled = True
                timeDelay(1500)
                game.mode = "Peaceful"
               
            else:
                self.hero.levelUp(self)
                timeDelay(1500)
                game.mode = battleDict[self.game.filename]
        self.hero.position = self.position
        print("exp =", self.hero.exp)
        print("lvl =", self.hero.level)
        print("###########################")
        # when hero faints, sent back to startpoint of current instance for now
        if self.hero.hitpoints <= 0:
            game.battleInstance = False
            self.hero.hitpoints = self.hero.maxHitpoints
            self.hero.position = (game.startpoints[0][0],
                         game.startpoints[0][1])
            if game.filename in battleDict:
              
                game.mode = battleDict[game.filename]
                game.mode2 = battleDict[game.filename]


class Monster(object):

    def __init__(self, name, battle, surface):
        self.battle = battle
        self.screen = surface

        # pull monster sprite filename
        filename = monsterImageDict[name][0]
        image = load_image(filename).convert_alpha() 
        # give monster name
        self.monsterName = name
        self.screen = surface
        self.image = image
        # pull resize parameters
        (x, y) = monsterImageDict[name][1]
        self.image = pygame.transform.scale(self.image, (x, y))
        """hipoints. strength. defense."""
        stats = monsterStatDict[name][1]
        (self.hitpoints, self.strength, self.defense) = (stats[0], 
            stats[1], 
            stats[2])

        # reposition parameter
        self.reposition = monsterImageDict[name][2]
        self.text = "What will you do?"
        self.text2 = None

    # monster attacks hero
    def attack(self, other):
        # attack initiated
        screen = self.screen
        timeDelay(300)

        # dodge chance based on hero agility
        if other.agility <= 10:
            dodgeRoll = random.randint(1,8)

        elif other.agility > 10 and other.agility <= 20:
            dodgeRoll = random.randint(1, 10)

        elif other.agility > 20 and other.agility <= 45:
            dodgeRoll = random.randint(1, 12)

        elif other.agility > 45:
            dodgeRoll = random.randint(1, 16)

        # hero 1/8 chance to dodge
        if dodgeRoll >= 8:
            self.text =  "But " + other.name + " dodged the attack!"
            self.text2 = None

            # dodge sound initiated
            playSound("dodge.wav", .3)

            # battle text refreshed
            self.battle.drawBattle(screen)
            timeDelay(600)
            return None
            # player dodges, end turn

        # else player did not dodge, monster then attacks
       
        if self.strength - other.defense <= 0 :
             # player's defense was too high for monster, so -= 1
            other.hitpoints -= 1
            if other.hitpoints < 0: other.hitpoints = 0

            # hit sound
            playSound("enemyhit.wav", 1)
        
            self.text = other.name + " takes little damage."
            self.text2 = None

            # battle text refreshes
            self.battle.drawBattle(screen)
            timeDelay(600)

        # if monst. strength > defense, monster does more than one damage
        else:
            damage = math.ceil((self.strength - other.defense))
            # also extra damage to be rolled on with random
            extraDamage = math.ceil(damage/10)
            damage = damage + random.randint(0, extraDamage)
            
            other.hitpoints = other.hitpoints - damage
            if other.hitpoints < 0: other.hitpoints = 0
            
            # hit sound
            playSound("enemyhit.wav", 1)

            self.text = other.name + " took " + str(damage) + " damage!"
            self.text2 = None
            # battle text refreshes
            self.battle.drawBattle(screen)
            timeDelay(600)

        # hero faints if hp = 0
        if other.hitpoints == 0:
            self.text = str(other.name) + " has fainted!"
            self.text2 = None
           
            # battle text
            pygame.mixer.music.pause()
            self.battle.drawBattle(screen)
            timeDelay(1500)



# character sprite controlled by player
class Hero(Pallete):
    def __init__(self):
        # main objective of game (for now) bool initialized
        self.attacking = False
        self.dragonKilled = False
        # player names character
        self.name = input("Enter your name: ")
        self.name = str(self.name)
        Pallete.__init__(self, 'heroes.png', 8, 12, 6, 3)
        (rows, cols) = (self.rows, self.cols)
        image = load_image('heroes.png').convert_alpha() 
        (width, height) = (self.width, self.height)
        (charWidth, charHeight) = (width / cols, height / rows)
        self.type = "hero"

        # set up graphical "turning" for hero character's sprite
        # up, right, down, left; all different character sprites
        self.ups = list()
        self.rights = list()
        self.downs = list()
        self.lefts = list()

        # the image frames are in a grid, so below deals with the cells
        for col in range(0,2):
            self.ups.append(image.subsurface(
                        ((col+3) * charWidth, 6 * charHeight, 
                            charWidth, charHeight)))
            self.ups[col]= pygame.transform.scale(self.ups[col], (32, 40))
            self.rights.append(image.subsurface(
                        ((col+3) * charWidth, 5 * charHeight, 
                            charWidth, charHeight)))
            self.rights[col] = pygame.transform.scale(self.rights[col], 
                                                            (33, 41))
            self.downs.append(image.subsurface(
                        ((col+3) * charWidth, 4 * charHeight, 
                            charWidth, charHeight)))
            self.downs[col] = pygame.transform.scale(self.downs[col], (32, 40))
            self.lefts.append( image.subsurface(
                        ((col+3) * charWidth, 7 * charHeight, 
                            charWidth, charHeight)))
            self.lefts[col] = pygame.transform.scale(self.lefts[col], (33, 41))
        # begin game looking forward idle animation
        self.currImageList = self.ups

        # initialize hero stats
        self.exp = heroStats["exp"]
        self.level = heroStats["level"]
        self.hitpoints = heroStats["hitpoints"]
        self.maxHitpoints = heroStats["maxHitpoints"]
        self.strength = heroStats["strength"]
        self.defense = heroStats["defense"]
        self.agility = heroStats["agility"]

        # initialize hero velocity
        self.velocity = [0, 0]
        self._position = [0, 0]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 8)

        self.statGrowth = {2: [5, 2, 2], 3:[3, 2, 2], 4:[4, 2, 2], 
                    5: [5, 3, 2], 6:[7, 6, 3], 7:[7, 5, 2],
                    8: [8, 4, 1], 9:[5, 6, 5], 10:[4, 8, 2],
                    11: [8, 5, 3], 12:[12, 5, 4], 13:[5, 3, 2],
                    14: [9, 2, 3], 15:[20, 5, 4], 16:[5, 3, 3],
                    17: [9, 2, 3], 18:[3, 6, 4], 19:[12, 3, 3],
                    20: [9, 4, 3], 21:[3, 4, 4], 22:[20, 3, 3]}
        

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)

    def update(self, dt):
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        # moves sprite back after collision if called
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def walkAnimation(self, ticks):
        # adds animation for hero character
        n = 0
        if self.velocity[0] == 0 and self.velocity[1] == 0:
            ticks = ticks//500*500
            if ticks%500 == 0:
                n = 0
            if ticks%1000 == 0:
                n = 1
        else:
            ticks = ticks //350*350
            if ticks%350 == 0:
                n = 0
            if ticks%700 == 0:
                n = 1
        self.image = self.currImageList[n]

    # attacking for battles
    def attack(self, other):
        screen = other.screen
        # cannot attack if either are monster or hero are fainted
        if other.hitpoints <= 0 or self.hitpoints <= 0:
            return None   # end function
        if other.hitpoints > 0:
            # attack sound
            playSound("attack.wav", .3)
            
        # time delay between attack and hit, .6 sec
        delay = 600
        other.text = self.name + " readied an attack!"
        other.text2 = None

        # battle text refreshes
        other.battle.drawBattle(screen)
        timeDelay(delay)

        

        # hitsound
        playSound("hit.wav", .5)

        # default is always 1 damage if strength < monst. defense
        if self.strength - other.defense <= 0:
            other.text = "The " + other.monsterName + " took 1 damage."
            other.text2 = None
            # battle text
            other.battle.drawBattle(screen)

            other.hitpoints -= 1
            timeDelay(delay)

        else:
            damage = math.ceil((self.strength -  other.defense))
            
            # roll random extra damage from 10% of damage
            extraDamage = math.ceil(damage/10)
            damage = damage + random.randint(0, extraDamage)

            other.text = ("The " + other.monsterName + " took " + str(damage)
                     + " damage!")
            other.text2 = None
            # battle text
            other.battle.drawBattle(screen)
      
            other.hitpoints = other.hitpoints - damage

            timeDelay(delay)
     
        # monster attacks if monster is still alive (and hero)
        if other.hitpoints > 0 and self.hitpoints > 0: 
            timeDelay(450)
            other.text = "The " + other.monsterName + " lunges forth!"
            other.text2 = None

            # enemy is attacking sound plays
            playSound("enemyattack.wav", .3)
        
            # battle text refreshes
            other.battle.drawBattle(screen)
            timeDelay(300)

            # actual monster attack function called
            other.attack(self)
            heroStats["hitpoints"] = self.hitpoints
        
        # or else update experience on turn monster is fainted
        else: 
            experience = expDict[other.monsterName]
            self.exp += experience
            # update experience points
            heroStats["exp"] = self.exp
            other.text = (" " + self.name + " gained " + str(experience) + 
                    " exp. points!")
            other.text2 = None
            other.battle.drawBattle(screen)

            # victory sound
            playSound("winbattle.wav", .2)
            self.attacking = False
            timeDelay(2500)

     

    def levelUp(self, battle):
        # dictionary of stat growth at diff levels
        while self.exp >= levelDict[self.level]:
            self.level += 1
            # update leveled stats dictionary
            heroStats["level"] = self.level
            heroStats["hitpoints"] += self.statGrowth[self.level][0]
            heroStats["maxHitpoints"] += self.statGrowth[self.level][0]
            heroStats["strength"] += self.statGrowth[self.level][1]
            heroStats["defense"]  += self.statGrowth[self.level][2]
            if self.level in agilityDict:
                heroStats["agility"] += agilityDict[self.level]

            # update object stats
            self.hitpoints = heroStats["hitpoints"]
            self.maxHitpoints = heroStats["maxHitpoints"]
            self.strength = heroStats["strength"]
            self.defense = heroStats["defense"]
            self.agility = heroStats["agility"]

            # delay 2.5 seconds between level up sounds

            # level up sound
            playSound("levelUp.wav", .3)

            # refresh texts
            battle.drawBattle(screen)
            # delay
            delay = 2500
            timeDelay(delay)

################################################################################

class QuestGame(object):

    def __init__(self, filename, oldEntrance=None, oldmap = None, hero=None):
        self.portalName = ""

        # puzzle solved modifies town file used
        if filename == "house1Basement3.tmx":
            InstDictIn["data/DragonQuest.tmxportal1"] = "town2.tmx" 
            for tmx in InstDictOut:
                if InstDictOut[tmx] == "town.tmx":
                    InstDictOut[tmx] = "town2.tmx"

        self.moving = True
        self.oldfilename = None
        self.battle = 1
        self.filename = get_map(filename)
        if self.filename == "data/DragonQuest.tmx":
            self.mode = "Overworld"

        else:
            if self.filename in battleDict:
                self.mode = battleDict[self.filename]
            else:
                self.mode = "Peaceful"
        self.mode2 = self.mode
        self.oldMap = oldmap
        if self.oldMap == None:
            self.oldMap = filename

        # true while running
        self.running = False
        # load data from pytmx
        tmx_data = load_pygame(self.filename)
        # setup Tiled object metadata
        self.walls = list()
        for object in tmx_data.objects:
            # collision walls are represented by .tmx object layer metadata 
            if object.type != "startpoint" and object.type != "person":
                self.walls.append(pygame.Rect(
                    object.x, object.y,
                    object.width, object.height))

        self.portalsIn = list()
        self.portalsOut = list()
        self.villagers = list()
        
        self.oldEntrance = oldEntrance
        overworld = "DragonQuest.tmx"
        self.battleInstance = False

        self.portalNames = list()
        # add portals to separate collide lists
        for object in tmx_data.objects:
            if object.type == "portalIn":
                self.portalNames.append(object)
                self.portalsIn.append(pygame.Rect(
                    object.x, object.y,
                    object.width, object.height))
            elif object.type == "portalO":
                self.portalsOut.append(pygame.Rect(
                    object.x, object.y,
                    object.width, object.height))
            if object.type == "person":
                if object.name in villagerDict:
                    (rows, cols, row, col) = villagerDict[object.name]
                    pic = "villagers.png"
                else:
                    (rows, cols, row, col) = villager2Dict[object.name]
                    pic = "villagers2.png"
                (x, y) = (object.x, object.y)
                
                self.villagers.append(Villager(pic, x, y, rows, cols, row, col))



        self.startpoints = []
        for object in tmx_data.objects:
            if object.name == "startpoint":
                self.startpoints.append((object.x, object.y))

        # create new data source for pyscroll
        map_data = pyscroll.data.TiledMapData(tmx_data)
        # create new renderer (camera)
        self.map_layer = pyscroll.BufferedRenderer(map_data, screen.get_size(),
            alpha = False)
        self.map_layer.zoom = 2
        if MusicDict[self.filename] == "Psaro.wav":
            self.map_layer.zoom = 1.75

        # set default zoom when not in overworld
        if self.oldMap == overworld and self.filename != "data/" + overworld:
            self.map_layer.zoom = self.map_layer.zoom - .25
        TowerMap = "data/TowerNoDragon.tmx"
        if self.filename == "data/Tower.tmx" or self.filename == TowerMap :
            self.map_layer.zoom -= .75

        # initialize hero sprite layer within group;
        # layer made to 5 so treebrances/roofs overlap character etc.
        self.group = PyscrollGroup(map_layer=self.map_layer, default_layer=5)
        for villager in self.villagers:
            self.group.add(villager)
        
        if hero == None:
            self.hero = Hero()
        # retains hero object if exists as well as its attributes
        else: self.hero = hero 

        # render hero in desired placement on map
        self.hero.position = (self.startpoints[0][0], self.startpoints[0][1])
        self.oldPlace = self.hero.position
        self.group.add(self.hero)

        # initialize steps count for determining battle trigger
        self.steps = 0


    def drawMap(self, surface):
        # center the map/screen on our Hero
        self.group.center(self.hero.rect.center)

        # draw the map and all sprites
        self.group.draw(surface)


    # keeps track of where newest instance was entered
    # within the old map
    def nearestPortal(self, trigger=False):
        (x, y) = self.hero.position 

        for portal in self.portalsIn:
            if trigger == False:
                trigger = True
                self.oldEntrance = (portal.x, portal.y)
                (p, q) = self.oldEntrance
            distanceNew = (math.sqrt((x - portal.x)**2+(y-portal.y)**2))
            distanceOld = (math.sqrt((x - p)**2+(y-q)**2))
        
            if distanceNew < distanceOld:
                distanceOld = distanceNew
                self.oldEntrance = (portal.x, portal.y)
                (p, q) = (portal.x, portal.y)
        for portal in self.portalNames:
            if self.almostEquals((p,q), (portal.x, portal.y)):
                self.portalName = portal.name

    # handles keys pressed
    def handle_input(self):
        poll = pygame.event.poll
        
        if self.battle == None:
            self.battle = 1
            return

        event = poll()
        while event:
            
            if event.type == QUIT:
                self.running = False
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    break
                # controls pyscroll zoom
                m = self.mode2
                if event.key == K_EQUALS:

                    if self.mode != "Battle":
                        if m != "Dungeon3" and m != "Dungeon2":
                            self.map_layer.zoom += .25

                if event.key == K_MINUS:
                    value = self.map_layer.zoom - .25
                    if MusicDict[self.filename] == "Psaro.wav":
                        if value < 1.75: return
                    if self.mode != "Battle":
                        if m != "Dungeon3" and m != "Dungeon2":
                            if value > 1: self.map_layer.zoom = value


                # battle run away
                elif event.key == K_r:
                    if self.battle == None:
                        return
                    HPhero = self.hero.hitpoints
                    HPmon = self.battle.monster.hitpoints
                    if HPhero <= 0 or HPmon <= 0:
                        return
                    escapeRoll = random.randint(1, self.hero.agility)
                    if escapeRoll > 5:
                        self.battle.monster.text = (str(self.hero.name) +
                        " ran away!")
                        self.battle.monster.text2 = None

                        # refresh text
                        self.battle.drawBattle(screen)

                        # escaping sound
                        playSound("escape.wav", .4)

                        timeDelay(2200)
                        
                        # change music
                        if self.mode2 == "Overworld":
                            pygame.mixer.music.pause()
                            song = MusicDict[self.filename]
                            playMusic(song)
                       

                        if self.mode == "Battle":
                            self.mode = battleDict[self.filename]
                            self.steps = 0
                        if self.battleInstance == True:
                            self.battleInstance = False
                    else: 
                        # if player fails escape check, monster attacks
                        timeDelay(450)
                        self.battle.monster.text = ("The " + 
                                self.battle.monster.monsterName + 
                            " blocks the way!")
                        self.battle.monster.text2 = None

                        # refresh text
                        self.battle.drawBattle(screen)
                        # pause screen .45 sec
                        timeDelay(450)

                        # initiate monster attacking sound
                        playSound("enemyattack.wav", .3)
                        # attack function called
                        self.battle.monster.attack(self.hero)

                
                elif event.key == K_o and self.mode != "Battle":
                    # resets hero position because stuck
                    self.hero.position = self.startpoints[0]
                elif event.key == K_p:
                    #gives hero's postion on map in REPL (for dev)
                    print(self.hero.position)
                if self.mode == "Battle":
                    if event.key == K_SPACE:
                        if self.hero.attacking == True: 
                            self.hero.attacking = False
                            return None
                        if self.battle != 1:
                            if self.hero.attacking == False:
                                hp1 = self.hero.hitpoints
                                hp2 = self.battle.monster.hitpoints
                                if hp1 > 0 and hp2 > 0:
                                    self.hero.attacking = True
                                    self.hero.attack(self.battle.monster)

                if self.moving == False:
                 # boolean for player character being able to move after battle
                    position = self.hero.position
                    n = 100000
                    movementList = (K_w, K_a, K_d, K_s)
                    if event.key in movementList:
                        while n > 0:
                            n-=1
                        self.moving = True
                        self.hero.position = position
                    

            # this will be handled if the window is to be resized
            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                self.map_layer.set_size((event.w, event.h))

            event = poll()

        # AWSD for left, up, down, right controls
        pressed = pygame.key.get_pressed()
        # moves character along map, but only if not in battle mode
        if self.mode != "Battle" and self.moving != False:
            ticks = pygame.time.get_ticks()
            if pressed[K_w]: 
                self.hero.currImageList = self.hero.downs
                self.hero.walkAnimation(ticks)
                self.hero.velocity[1] = -HERO_MOVE_SPEED
                self.steps += 1
            elif pressed[K_s]:
                self.hero.currImageList = self.hero.ups
                self.hero.walkAnimation(ticks)
                self.hero.velocity[1] = HERO_MOVE_SPEED
                self.steps += 1
            else:
                self.hero.velocity[1] = 0
            if pressed[K_a]:
                self.hero.currImageList = self.hero.lefts
                self.hero.walkAnimation(ticks)
                self.hero.velocity[0] = -HERO_MOVE_SPEED
                self.steps += 1
            elif pressed[K_d]:
                self.hero.currImageList = self.hero.rights
                self.hero.walkAnimation(ticks)
                self.hero.velocity[0] = HERO_MOVE_SPEED
                self.steps += 1
            
            else:
                self.hero.velocity[0] = 0
            # sprint
            if pressed[K_SPACE]:
                self.hero.velocity[0] *= 1.5
                self.hero.velocity[1] *= 1.5
                # more likely to battle encounter if sprinting
                if self.hero.velocity[0] > 0 or self.hero.velocity[1] > 0:
                    self.steps += 2
                if self.hero.velocity[0] >= 1.5 * HERO_MOVE_SPEED:
                    pass
                if self.hero.velocity[1] >= 1.5 * HERO_MOVE_SPEED:
                    pass

        # stops character from moving when battlescreen is initiated
        if self.mode == "Battle":
            (self.hero.velocity[0], self.hero.velocity[1]) = (0, 0)

    # checks for pygame collisions within sprite groups
    def update(self, dt):
        
        self.group.update(dt)

        # check if the sprite's feet collide with tmx objects
        # uses "feet" of sprite so character can overlap somewhat with walls
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.portalsIn) > -1:
                if sprite.type == "hero":

                    self.nearestPortal()
                    filename = InstDictIn[self.filename+self.portalName]
                    if self.hero.dragonKilled == True:
                        if filename == "Tower.tmx":
                            filename = "TowerNoDragon.tmx"
                    self.filename = filename
               
                    self.hero.position = (self.startpoints[0][0],
                                     self.startpoints[0][1])

            elif sprite.feet.collidelist(self.portalsOut) > -1:
                if sprite.type == "hero":
                    filename = InstDictOut[self.filename]
                    self.filename = filename
                    self.hero.position = (self.startpoints[0][0],
                                        self.startpoints[0][1])

            elif sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)

    # plays music based on map file keyed to dictionary
    # also covers changing map sound effect
    def changeMusicAndInstance(self, surface, oldMusic=None):
        tmap = self.filename
        song = MusicDict[tmap]
        # instance change sound, from Zelda stairs sound
        playSound("Enter.wav", .15)

        if oldMusic == None:
            oldMusic = MusicDict[self.oldMap]
       
        if self.mode != "Overworld":
            if song == oldMusic: return None
       
        # loops music indefinitely for that map
        playMusic(song)
        


    # takes two coordinates and returns whether they're almost equal
    @staticmethod
    def almostEquals(position1, position2):
        (x1, y1) = position1
        (x2, y2) = position2
        epsilon = 60
        if abs(x1-x2) < epsilon:
            if abs(y1-y2) < epsilon:
                 return True
        return False

    # whenever character moves, attempts to initiate battle
    def encounterBattle (self):
        position = self.hero.position
        # prevents battle from happening right on town portal
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.portalsIn) > -1:
                return None
        if self.almostEquals(position, self.oldPlace): return None
        if self.mode == "Peaceful" or self.mode == "Battle": return None
        diceRoll = random.randint(0, 1000)
        #increased encounter rate when walking without encountering
        # a single battle for a certain number of steps
        threshold = 600
        if self.filename == "data/Tower.tmx":
            threshold = 50
        if self.mode == "Dungeon3":
            threshold = 1200
        if self.steps > threshold:
            if diceRoll < 500:
                self.mode = "Battle"
                self.steps = 0

        if self.steps > 200:
        # lower encounter rate when just beginning to walk
            if diceRoll < 200:
                self.mode = "Battle"
                self.steps = 0


        self.oldPlace = position

    # runs gameloop and draws based on self.mode
    def run(self):
        filename = self.filename
        clock = pygame.time.Clock()
        self.running = True
        try:
            while self.running:
                ticks = pygame.time.get_ticks()
                dt = clock.tick() / 1000.

                # hero idle animation
                self.hero.walkAnimation(ticks)

                #villager animation
                for villager in self.villagers:
                    villager.idleAnimation(ticks)

                # attempt to encounter battle in overworld/dungeons
                self.encounterBattle()
                if self.mode == "Battle":
                    if self.battleInstance == False:
                        if filename in battleDict:
                            self.mode2 == battleDict[self.filename]
                        
                        if self.mode2 == "Overworld":
                            battleMusic = "Battle.wav"
                            # play battle encounter music
                            playMusic(battleMusic)

                        self.battleInstance = True
                        # initiliaze battle
                        self.battle = Battle(self, self.hero, 
                            self.hero.position, screen)
                    self.battle.drawBattle(screen)

                if self.mode == "Battle":
                    # change music to old music when monster defeated
                    HP = self.hero.hitpoints
                    if self.battle.monster.hitpoints <= 0 or HP <= 0:
                        # hero's hp < 0
                        if HP <= 0:
                            pygame.mixer.music.pause()

                            # game over sound played
                            playSound("gameOver.wav", 1)
                            self.battle.monster.text = "GAME OVER"

                            self.moving = False
                            self.battle.monster.text2 = None

                            # refresh battle text displayed
                            self.battle.drawBattle(screen)
                            timeDelay(6000)

                        song = MusicDict[self.filename]
                        print("mode2 =", self.mode2)
                        if self.mode2 == "Overworld":
                            playMusic(song)
                       
                        self.moving = False
                        self.battle.endBattle(self)
                        self.battle = None
                        
                # changing map
                if self.filename != filename:
                    # going out of the map and towards overworld
                    if self.oldMap == "data/" + self.filename:
                        oldMap = (InstDictIn["data/" + 
                            self.filename+self.portalName])

                        self.__init__(self.filename, self.oldEntrance, 
                            oldMap,
                            self.hero)
                        oldMusic = MusicDict[self.filename]
                        self.changeMusicAndInstance(screen, oldMusic)
                    # going into the map, into town, houses, etc.
                    else:
                        oldMusic = MusicDict[filename]
                        oldMap = InstDictOut["data/" + self.filename]
                        self.__init__(self.filename, self.oldEntrance, 
                            oldMap,
                            self.hero)
                        self.changeMusicAndInstance(screen, oldMusic)
                    self.oldEntrance = OldEntranceDict[filename]

        
                    if  "data/" + InstDictOut[filename] == self.filename:
                        if self.oldEntrance != None:
                            position = (self.oldEntrance[0], 
                                self.oldEntrance[1])
                            self.hero.position = position
                            self.oldPlace = position
                    
                    
                    self.run()
                if self.mode != "Battle":
                    self.drawMap(screen)
                        
                
                self.handle_input()
                self.update(dt)

                pygame.display.flip()
        except KeyboardInterrupt:
            self.running = False


################################################################################



if __name__ == "__main__":
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.font.init()
    
    pygame.display.set_caption('RPG')

    try:
        state = QuestGame('DragonQuest.tmx')
        state.changeMusicAndInstance(screen)
        state.run()

    except:
        pygame.error
        pygame.quit()
        raise
