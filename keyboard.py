from Global import *


class Key:
    def __init__(self, x, y, litters_, display_=display, size=1):
        self.x = x
        self.y = y
        self.size = size
        self.display = display_
        self.mists = 0
        self.litters = litters_[0]
        self.shift = litters_[1]
        self.wight = 75
        self.height = 75

        self.act_1 = 160
        self.act_2 = 200
        self.act_3 = 60

        self.inactive_colour = (self.act_1, self.act_2, self.act_3)
        self.active_colour = (self.act_1, self.act_2 - 20, self.act_3)

    def draw(self, condition=False):
        self.act_1 = 160 + self.mists * 5
        self.act_2 = 200 - self.mists * 15
        self.act_3 = 60
        self.inactive_colour = (self.act_1, self.act_2, self.act_3)
        self.active_colour = (255, 255, 0)
        if condition:
            pygame.draw.rect(self.display, self.active_colour, (self.x, self.y, self.wight * self.size, self.height))
        else:
            pygame.draw.rect(self.display, self.inactive_colour, (self.x, self.y, self.wight * self.size, self.height))
        pygame.draw.rect(self.display, (64, 128, 255), (self.x, self.y, self.wight * self.size, self.height), 4)  # рисует рамку
        counter = 0
        for i_ in self.litters:
            print_txt(i_, self.x + counter + 25, self.y - counter + 30, font_type='font_1.otf')
            counter += 20


litter_list_1 = [(['`', '~'], 'R'), (['1', '!'], 'R'), (['2', '@'], 'R'), (['3', '#'], 'R'), (['4', '$'], 'R'),
                 (['5', '%'], 'R'), (['6', '^'], 'R'), (['7', '&'], 'L'), (['8', '*'], 'L'), (['9', '('], 'L'),
                 (['0', ')'], 'L'), (['-', '_'], 'L'), (['=', '+'], 'L')]
litter_list_2 = [(['q', 'Q'], 'R'), (['w', 'W'], 'R'), (['e', 'E'], 'R'), (['r', 'R'], 'R'), (['t', 'T'], 'R'),
                 (['y', 'Y'], 'L'), (['u', 'U'], 'L'), (['i', 'I'], 'L'), (['o', 'O'], 'L'), (['p', 'P'], 'L'),
                 (['[', '{'], 'L'), ([']', '}'], 'L')]
litter_list_3 = [(['a', 'A'], 'R'), (['s', 'S'], 'R'), (['d', 'D'], 'R'), (['f', 'F'], 'R'), (['g', 'G'], 'R'),
                 (['h', 'H'], 'L'), (['j', 'J'], 'L'), (['k', 'K'], 'L'), (['l', 'L'], 'L'), ([';', ':'], 'L'),
                 (["'", '"'], 'L'), (['\\', '|'], 'L')]
litter_list_4 = [(['z', 'Z'], 'R'), (['x', 'X'], 'R'), (['c', 'C'], 'R'), (['v', 'V'], 'R'), (['b', 'B'], 'R'),
                 (['n', 'N'], 'L'), (['m', 'M'], 'L'), ([',', '<'], 'L'), (['.', '>'], 'L'), (['/', '?'], 'L')]
litter_list_5 = [([' ', ' '], 'L')]


list_1, list_2, list_3, list_4, list_5 = list(), list(), list(), list(), list()
x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5 = 100, 420, 150, 500, 200, 580, 250, 660, 300, 740
for i in litter_list_1:
    list_1.append(Key(x_1, y_1, i))
    x_1 += 100

for i in litter_list_2:
    list_2.append(Key(x_2, y_2, i))
    x_2 += 100

for i in litter_list_3:
    list_3.append(Key(x_3, y_3, i))
    x_3 += 100

left_shift = Key(x_4 - 170, y_4, (['Shift_L'], 'L'), size=2)
for i in litter_list_4:
    list_4.append(Key(x_4, y_4, i))
    x_4 += 100
right_shift = Key(x_4, y_4, (['Shift_R'], 'R'), size=2)

for i in litter_list_5:
    list_5.append(Key(x_5, y_5, i, size=10))
    x_5 += 100


key_dict = dict()

for litters, key_object in zip(litter_list_1, list_1):
    key_dict[litters[0][0]] = key_object
    key_dict[litters[0][1]] = key_object
for litters, key_object in zip(litter_list_2, list_2):
    key_dict[litters[0][0]] = key_object
    key_dict[litters[0][1]] = key_object
for litters, key_object in zip(litter_list_3, list_3):
    key_dict[litters[0][0]] = key_object
    key_dict[litters[0][1]] = key_object
for litters, key_object in zip(litter_list_4, list_4):
    key_dict[litters[0][0]] = key_object
    key_dict[litters[0][1]] = key_object
for litters, key_object in zip(litter_list_5, list_5):
    key_dict[litters[0][0]] = key_object
    key_dict[litters[0][1]] = key_object


def draw_keyboard():
    global list_1, list_2, list_3, list_4, list_5
    for i_ in list_1:
        i_.draw()
    for i_ in list_2:
        i_.draw()
    for i_ in list_3:
        i_.draw()
    left_shift.draw()
    for i_ in list_4:
        i_.draw()
    right_shift.draw()
    for i_ in list_5:
        i_.draw()
