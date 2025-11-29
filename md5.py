import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import hashlib

pygame.mixer.music.load("song.mp3") #haruta
pygame.mixer.music.play(-1)

level=-1
target=""
message=""
gemacht=False

def text_to_md5(text):
    global message
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    message+=f"MD5-Hash of '{text}': {md5_hash}"

def draw():
    global level, target, message
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Enter text:", center=(400, 130), fontsize=24, color=(255, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 2:
        screen.draw.text(message, center=(400, 130), fontsize=24, color=(25, 200, 255))

def on_key_down(key, unicode=None):
    global level, target
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        target = ""
    elif key == keys.RETURN and level == 1:
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode

def update():
    global level,message,target,gemacht
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==2:
        if not gemacht:
            text_to_md5(target)
            gemacht=True
        if keyboard.space:
            level=0
    if level==0:
        message=""
        target=""
        gemacht=False

pgzrun.go()
