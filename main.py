from Global import *
from keyboard import *

txt_list = add_txt('text1.txt')
txt_short_list = [txt_list[i] for i in range(5)]
string_txt = txt_short_list[0]

counter = 0
res_tt = 0
mist_count = 0
mist_count_str = 0
mists = 0
last_len = 0
total_len = 0
total_mists = 0
words_number = 0

t = time.time()
while process:
    counter += 1
    main_font = fonts[0] + '.otf'
    display.fill((255, 255, 255))
    for event in pygame.event.get():  # перебираем события
        if event.type == pygame.QUIT:
            process = False  # Если мы нажали на кнопочку закрыть, то мы выходим из приложения
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка: ", event.button)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_txt = input_txt[:-1]
            elif (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE) and len(string_txt) == len(input_txt):
                res_tt = int(60 * len(input_txt) / (time.time() - t))
                last_len = len(string_txt)
                mists = int(mist_count_str)
                total_mists += mists
                total_len += last_len
                words_number = len(string_txt.split())
                t = time.time()
                input_txt = ''
                if len(txt_list) > 1:
                    txt_list.pop(0)
                    txt_short_list = [txt_list[i] for i in range(5)] if len(txt_list) >= 5 else [i for i in txt_list]
                    string_txt = txt_short_list[0]
                else:
                    txt_short_list = ['']
                    string_txt = 'End!'
                mist_count_str = 0
            else:
                input_txt += event.unicode
                if string_txt[:len(input_txt)] != input_txt:
                    key_dict[string_txt[len(input_txt) - 1]].mists = min(13, key_dict[string_txt[len(input_txt) - 1]].mists + 1)
                    if string_txt[len(input_txt) - 1] == string_txt[len(input_txt) - 1].upper():
                        if key_dict[string_txt[len(input_txt) - 1]].shift == 'L':
                            left_shift.mists = min(13, left_shift.mists + 1)
                        else:
                            right_shift.mists = min(13, right_shift.mists + 1)
                    mist_sound()
                    mist_count += 1
                    mist_count_str += 1
                    input_txt = input_txt[:-1]
                elif len(input_txt):
                    key_dict[input_txt[-1]].mists = max(0, key_dict[input_txt[-1]].mists - 0.2)
                    if string_txt[len(input_txt) - 1] == string_txt[len(input_txt) - 1].upper():
                        if key_dict[string_txt[len(input_txt) - 1]].shift == 'L':
                            left_shift.mists = max(0, left_shift.mists - 0.2)
                        else:
                            right_shift.mists = max(0, right_shift.mists - 0.2)

    print_txt(string_txt, 50, 200, font_color=(200, 200, 200), font_type=main_font)
    print_txt(input_txt, 50, 200, condition=True, font_type=main_font) if counter // 25 % 2 == 0 else print_txt(input_txt, 50, 200, font_type=main_font)

    for i in range(94):
        display.blit(pygame.image.load('x.png'), (50 + 16 * i, 240))
    for i in range(len(txt_short_list)):
        print_txt(txt_short_list[i], 50, 266 + 30 * i, font_type=main_font)

    string = button.draw(240, 50, 'add text', add_txt)
    change_font_button.draw(100, 50, 'next font', change_font)
    # ТУТ ДОЛЖНА БЫТЬ КНОПКА ДЛЯ СТАТИСТИКИ

    if string is not None:
        txt_list = string
        txt_short_list = [txt_list[i] for i in range(5 if len(txt_list) >= 5 else len(txt_list))]
        string_txt = txt_short_list[0]
    draw_keyboard()
    if len(input_txt) < len(string_txt):
        key_dict[string_txt[len(input_txt)]].draw(condition=True)
        if string_txt[len(input_txt)] == string_txt[len(input_txt)].upper() and string_txt[len(input_txt)] != ' ':
            if key_dict[string_txt[len(input_txt)]].shift == 'L':
                left_shift.draw(condition=True)
            else:
                right_shift.draw(condition=True)
    statistics(mist_count, res_tt, mists, last_len, total_mists, total_len, words_number)
    pygame.display.update()
    counter %= 1000
