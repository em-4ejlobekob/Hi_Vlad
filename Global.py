import time
import pygame

# from Button import Button
pygame.init()
fonts = ['font_1', 'font_2', 'font_3', 'font_4', 'font_5']
main_font = fonts[0] + '.otf'
display = pygame.display.set_mode((1600, 900))
from functions import *
process = True
input_txt = ''
from Button import Button
button = Button(120, 50)
change_font_button = Button(120, 50)

