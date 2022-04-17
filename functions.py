import easygui
import pygame
from Global import display, main_font, fonts


def print_txt(message, x, y, font_color=(0, 0, 0), font_type=main_font, font_size=26, condition=False, dspl=display):
    font_type = pygame.font.Font(font_type, font_size)
    message = message + '|' if condition else message
    txt = font_type.render(message, True, font_color)
    dspl.blit(txt, (x, y))


def add_txt(txt=None):

    if txt is None:
        txt = easygui.fileopenbox()
    if txt is None:
        return None

    with open(txt, 'r') as f:
        a, s = list(), ''
        for i in [i for i in ' '.join(f.read().split('\n')).split(' ') if i != '']:
            if len(s) == 0:
                s = i
            elif len(s) + len(i) < 80:
                s = ' '.join([s, i])
            else:
                a.append(s)
                s = i
        a.append(s)
    return a


# record results function

def statistics(mist_count, res_tt, mists, last_len, total_mists, total_len, words_number, x=1200, y1=20, y2=50):
    print(last_len)
    print_txt('mistakes: ' + str(mist_count), x, y1, font_type='font_1.otf')  # ошибки
    print_txt('litters per minute: ' + str(res_tt), x, y2, font_type='font_1.otf')  # символы в минуту
    print_txt('words per minute: ' + str(words_number), x, y2 + 30, font_type='font_1.otf')  # слова в минуту
    if last_len > 0:
        print_txt('% of fails in string: ' + str(int(100 * mists / last_len)) + '%', x, y2 + 60, font_type='font_1.otf')
    else:
        print_txt('% of fails in string: 0%', x, y2 + 60, font_type='font_1.otf')
    if total_len > 0:
        print_txt('% of fails in string: ' + str(int(100 * total_mists / total_len)) + '%', x, y2 + 90, font_type='font_1.otf')
    else:
        print_txt('total % of fails: 0%', x, y2 + 90, font_type='font_1.otf')


def mist_sound():
    pygame.mixer.Sound.play(pygame.mixer.Sound('mist_click.mp3'))
    pygame.time.delay(10)


def change_font():
    from Global import fonts
    fonts.append(fonts[0])
    fonts.pop(0)
