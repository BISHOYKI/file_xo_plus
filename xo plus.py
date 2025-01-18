import random

while True:
    while True:
        try:
            # function
            def xo(user_game, pcgame):
                if user_game == 9:
                    The_playbook[0] = "x"
                elif user_game == 8:
                    The_playbook[1] = "x"
                elif user_game == 7:
                    The_playbook[2] = " x"
                elif user_game == 6:
                    The_playbook[3] = "x"
                elif user_game == 5:
                    The_playbook[4] = "x"
                elif user_game == 4:
                    The_playbook[5] = " x"
                elif user_game == 3:
                    The_playbook[6] = "x"
                elif user_game == 2:
                    The_playbook[7] = "x"
                elif user_game == 1:
                    The_playbook[8] = " x"

                if pcgame == 9:
                    The_playbook[0] = "o"
                elif pcgame == 8:
                    The_playbook[1] = "o"
                elif pcgame == 7:
                    The_playbook[2] = " o"
                elif pcgame == 6:
                    The_playbook[3] = "o"
                elif pcgame == 5:
                    The_playbook[4] = "o"
                elif pcgame == 4:
                    The_playbook[5] = " o"
                elif pcgame == 3:
                    The_playbook[6] = "o"
                elif pcgame == 2:
                    The_playbook[7] = "o"
                elif pcgame == 1:
                    The_playbook[8] = " o"

                a = The_playbook[0]
                b = The_playbook[1]
                c = The_playbook[2]
                d = The_playbook[3]
                f = The_playbook[4]
                g = The_playbook[5]
                h = The_playbook[6]
                p = The_playbook[7]
                o = The_playbook[8]

                print(c, "|", b, "|", a)
                print("---+---+---")
                print(g, "|", f, "|", d)
                print("---+---+---")
                print(o, "|", p, "|", h)


            def win_and_stone(The_playbook_test):
                win_and_lose = False
                win_for_o_or_x = 1
                if The_playbook_test[0] == "x" and The_playbook_test[1] == "x" and The_playbook_test[2] == " x" \
                or The_playbook_test[3] == "x" and The_playbook_test[4] == "x" and The_playbook_test[5] == " x" \
                or The_playbook_test[6] == "x" and The_playbook_test[7] == "x" and The_playbook_test[8] == " x" \
                or The_playbook_test[2] == " x" and The_playbook_test[5] == " x" and The_playbook_test[8] == " x" \
                or The_playbook_test[1] == "x" and The_playbook_test[4] == "x" and The_playbook_test[7] == "x" \
                or The_playbook_test[0] == "x" and The_playbook_test[3] == "x" and The_playbook_test[6] == "x" \
                or The_playbook_test[0] == "x" and The_playbook_test[4] == "x" and The_playbook_test[8] == " x" \
                or The_playbook_test[2] == " x" and The_playbook_test[4] == "x" and The_playbook_test[6] == "x":
                    win_and_lose = True
                    win_for_o_or_x = 2
                elif The_playbook_test[0] == "o" and The_playbook_test[1] == "o" and The_playbook_test[2] == " o" \
                or The_playbook_test[3] == "o" and The_playbook_test[4] == "o" and The_playbook_test[5] == " o" \
                or The_playbook_test[6] == "o" and The_playbook_test[7] == "o" and The_playbook_test[8] == " o" \
                or The_playbook_test[2] == " o" and The_playbook_test[5] == " o" and The_playbook_test[8] == " o" \
                or The_playbook_test[1] == "o" and The_playbook_test[4] == "o" and The_playbook_test[7] == "o" \
                or The_playbook_test[0] == "o" and The_playbook_test[3] == "o" and The_playbook_test[6] == "o" \
                or The_playbook_test[0] == "o" and The_playbook_test[4] == "o" and The_playbook_test[8] == " o" \
                or The_playbook_test[2] == " o" and The_playbook_test[4] == "o" and The_playbook_test[6] == "o":
                    win_and_lose = True
                    win_for_o_or_x = 3
                return win_and_lose, win_for_o_or_x


            def prevent_dtep_repeat_test(prevent_dtep_repeat, The_playbook_test5, option_3):
                while True:
                    user_game = int(input())
                    if user_game in prevent_dtep_repeat:
                        print("Enter another number")
                    elif user_game > 9 or user_game < 1:
                        print("Enter a number between 1 and 9")
                    else:
                        if option_3 == 1:
                            if user_game == 9:
                                The_playbook_test5[0] = "x"
                            elif user_game == 8:
                                The_playbook_test5[1] = "x"
                            elif user_game == 7:
                                The_playbook_test5[2] = " x"
                            elif user_game == 6:
                                The_playbook_test5[3] = "x"
                            elif user_game == 5:
                                The_playbook_test5[4] = "x"
                            elif user_game == 4:
                                The_playbook_test5[5] = " x"
                            elif user_game == 3:
                                The_playbook_test5[6] = "x"
                            elif user_game == 2:
                                The_playbook_test5[7] = "x"
                            elif user_game == 1:
                                The_playbook_test5[8] = " x"
                        elif option_3 == 2:
                            if user_game == 9:
                                The_playbook_test5[0] = "o"
                            elif user_game == 8:
                                The_playbook_test5[1] = "o"
                            elif user_game == 7:
                                The_playbook_test5[2] = " o"
                            elif user_game == 6:
                                The_playbook_test5[3] = "o"
                            elif user_game == 5:
                                The_playbook_test5[4] = "o"
                            elif user_game == 4:
                                The_playbook_test5[5] = " o"
                            elif user_game == 3:
                                The_playbook_test5[6] = "o"
                            elif user_game == 2:
                                The_playbook_test5[7] = "o"
                            elif user_game == 1:
                                The_playbook_test5[8] = " o"

                        stop1 = test_and_draw(The_playbook_test5)
                        stop2, win_for_o_or_x = win_and_stone(The_playbook_test5)
                        prevent_dtep_repeat.append(user_game)
                        break
                return user_game, stop1, stop2, win_for_o_or_x


            def test_and_draw(The_playbook_test_4):
                stop = False
                random_option = []
                if The_playbook_test_4[0] == "  ":
                    random_option.append(9)
                if The_playbook_test_4[1] == " ":
                    random_option.append(8)
                if The_playbook_test_4[2] == "  ":
                    random_option.append(7)
                if The_playbook_test_4[3] == "  ":
                    random_option.append(6)
                if The_playbook_test_4[4] == " ":
                    random_option.append(5)
                if The_playbook_test_4[5] == "  ":
                    random_option.append(4)
                if The_playbook_test_4[6] == "  ":
                    random_option.append(3)
                if The_playbook_test_4[7] == " ":
                    random_option.append(2)
                if The_playbook_test_4[8] == "  ":
                    random_option.append(1)

                if random_option == []:
                    stop = True
                return stop


            def option_game_the_pc(The_playbook_test6, user_game, option_2):
                if option_2 == 1:
                    if user_game == 9:
                        The_playbook_test6[0] = "x"
                    elif user_game == 8:
                        The_playbook_test6[1] = "x"
                    elif user_game == 7:
                        The_playbook_test6[2] = " x"
                    elif user_game == 6:
                        The_playbook_test6[3] = "x"
                    elif user_game == 5:
                        The_playbook_test6[4] = "x"
                    elif user_game == 4:
                        The_playbook_test6[5] = " x"
                    elif user_game == 3:
                        The_playbook_test6[6] = "x"
                    elif user_game == 2:
                        The_playbook_test6[7] = "x"
                    elif user_game == 1:
                        The_playbook_test6[8] = " x"
                elif option_2 == 2:
                    if user_game == 9:
                        The_playbook_test6[0] = "o"
                    elif user_game == 8:
                        The_playbook_test6[1] = "o"
                    elif user_game == 7:
                        The_playbook_test6[2] = " o"
                    elif user_game == 6:
                        The_playbook_test6[3] = "o"
                    elif user_game == 5:
                        The_playbook_test6[4] = "o"
                    elif user_game == 4:
                        The_playbook_test6[5] = " o"
                    elif user_game == 3:
                        The_playbook_test6[6] = "o"
                    elif user_game == 2:
                        The_playbook_test6[7] = "o"
                    elif user_game == 1:
                        The_playbook_test6[8] = " o"
                    print(The_playbook_test6)
                while True:
                    stop = False
                    pc_game = 10
                    if option_2 == 1:
                        stop, pc_game = test_win_for_o(The_playbook_test6)
                        if stop:
                            print("llllllllllll")
                            return pc_game
                            break
                        stop, pc_game = test_win_for_x(The_playbook_test6)
                        if stop:
                            print("hhhhhhhhh")
                            print(pc_game)
                            print(The_playbook_test6)
                            return pc_game
                            break

                    elif option_2 == 2:
                        stop, pc_game = test_win_for_x(The_playbook_test6)
                        if stop:
                            print("hhhhhhhhh")
                            print(pc_game)
                            print(The_playbook_test6)
                            return pc_game
                            break
                        stop, pc_game = test_win_for_o(The_playbook_test6)
                        if stop:
                            print("llllllllllll")
                            return pc_game
                            break

                    stop, pc_game = special_characters(The_playbook_test6, option_2)
                    if stop:
                        print("jjjjjjjjjjjjjjj")
                        print(option_2)
                        print(The_playbook_test6)
                        print(pc_game)
                        return pc_game
                        break
                    stop, pc_game = options(The_playbook_test6, option_2)
                    if stop:
                        print("ppppppppppppp")
                        print(option_2)
                        print(The_playbook_test6)
                        print(pc_game)
                        return pc_game
                        break
                    stop, pc_game = random_game(The_playbook_test6)
                    if stop:
                        print(option_2)
                        print("rrrrrrrrr")
                        return pc_game
                        break

                    return pc_game


            def test_win_for_o(The_playbook_test):
                pc_game = 10
                stop = False
                # win_for_o
                # العمود الاول
                if The_playbook_test[2] == " o" and The_playbook_test[5] == " o" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[5] == " o" and The_playbook_test[8] == " o" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[2] == " o" and The_playbook_test[8] == " o" and The_playbook_test[5] == "  ":
                    pc_game = 4
                    stop = True
                # العمود الثانى
                if The_playbook_test[1] == "o" and The_playbook_test[4] == "o" and The_playbook_test[7] == " ":
                    pc_game = 2
                    stop = True
                if The_playbook_test[4] == "o" and The_playbook_test[7] == "o" and The_playbook_test[1] == " ":
                    pc_game = 8
                    stop = True
                if The_playbook_test[1] == "o" and The_playbook_test[7] == "o" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # العمود الثالث
                if The_playbook_test[0] == "o" and The_playbook_test[3] == "o" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[3] == "o" and The_playbook_test[6] == "o" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "o" and The_playbook_test[6] == "o" and The_playbook_test[3] == "  ":
                    pc_game = 6
                    stop = True
                # الصف الاول
                if The_playbook_test[1] == "o" and The_playbook_test[2] == " o" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "o" and The_playbook_test[1] == "o" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[0] == "o" and The_playbook_test[2] == " o" and The_playbook_test[1] == " ":
                    pc_game = 8
                    stop = True
                # الصف الثانى
                if The_playbook_test[4] == "o" and The_playbook_test[5] == " o" and The_playbook_test[3] == "  ":
                    pc_game = 6
                    stop = True
                if The_playbook_test[3] == "o" and The_playbook_test[4] == "o" and The_playbook_test[5] == "  ":
                    pc_game = 4
                    stop = True
                if The_playbook_test[3] == "o" and The_playbook_test[5] == " o" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # الصف الثالث
                if The_playbook_test[7] == "o" and The_playbook_test[8] == " o" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[6] == "o" and The_playbook_test[7] == "o" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[6] == "o" and The_playbook_test[8] == " o" and The_playbook_test[7] == " ":
                    pc_game = 2
                    stop = True
                # الخط مائل الاول
                if The_playbook_test[0] == "o" and The_playbook_test[4] == "o" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[4] == "o" and The_playbook_test[8] == " o" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "o" and The_playbook_test[8] == " o" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # الخط مائل الثانى
                if The_playbook_test[2] == " o" and The_playbook_test[4] == "o" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[4] == "o" and The_playbook_test[6] == "o" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[2] == " o" and The_playbook_test[6] == "o" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True

                return stop, pc_game


            def test_win_for_x(The_playbook_test):
                pc_game = 10
                stop = False
                # win_for_x
                # العمود الاول
                if The_playbook_test[2] == " x" and The_playbook_test[5] == " x" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[5] == " x" and The_playbook_test[8] == " x" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[2] == " x" and The_playbook_test[8] == " x" and The_playbook_test[5] == "  ":
                    pc_game = 4
                    stop = True
                # العمود الثانى
                if The_playbook_test[1] == "x" and The_playbook_test[4] == "x" and The_playbook_test[7] == " ":
                    pc_game = 2
                    stop = True
                if The_playbook_test[4] == "x" and The_playbook_test[7] == "x" and The_playbook_test[1] == " ":
                    pc_game = 8
                    stop = True
                if The_playbook_test[1] == "x" and The_playbook_test[7] == "x" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # العمود الثالث
                if The_playbook_test[0] == "x" and The_playbook_test[3] == "x" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[3] == "x" and The_playbook_test[6] == "x" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "x" and The_playbook_test[6] == "x" and The_playbook_test[3] == "  ":
                    pc_game = 6
                    stop = True
                # الصف الاول
                if The_playbook_test[1] == "x" and The_playbook_test[2] == " x" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "x" and The_playbook_test[1] == "x" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[0] == "x" and The_playbook_test[2] == " x" and The_playbook_test[1] == " ":
                    pc_game = 8
                    stop = True
                # الصف الثانى
                if The_playbook_test[4] == "x" and The_playbook_test[5] == " x" and The_playbook_test[3] == "  ":
                    pc_game = 6
                    stop = True
                if The_playbook_test[3] == "x" and The_playbook_test[4] == "x" and The_playbook_test[5] == "  ":
                    pc_game = 4
                    stop = True
                if The_playbook_test[3] == "x" and The_playbook_test[5] == " x" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # الصف الثالث
                if The_playbook_test[7] == "x" and The_playbook_test[8] == " x" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[6] == "x" and The_playbook_test[7] == "x" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[6] == "x" and The_playbook_test[8] == " x" and The_playbook_test[7] == " ":
                    pc_game = 2
                    stop = True
                # الخط مائل الاول
                if The_playbook_test[0] == "x" and The_playbook_test[4] == "x" and The_playbook_test[8] == "  ":
                    pc_game = 1
                    stop = True
                if The_playbook_test[4] == "x" and The_playbook_test[8] == " x" and The_playbook_test[0] == "  ":
                    pc_game = 9
                    stop = True
                if The_playbook_test[0] == "x" and The_playbook_test[8] == " x" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True
                # الخط مائل الثانى
                if The_playbook_test[2] == " x" and The_playbook_test[4] == "x" and The_playbook_test[6] == "  ":
                    pc_game = 3
                    stop = True
                if The_playbook_test[4] == "x" and The_playbook_test[6] == "x" and The_playbook_test[2] == "  ":
                    pc_game = 7
                    stop = True
                if The_playbook_test[2] == " x" and The_playbook_test[6] == "x" and The_playbook_test[4] == " ":
                    pc_game = 5
                    stop = True

                return stop, pc_game


            def options(The_playbook_test_2, option_3):
                pc_game = 10
                option = []
                stop = False
                print(f"option {option_3}")
                if The_playbook_test_2[8] == "  ":
                    test = 1
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[7] == " ":
                    test = 2
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[6] == "  ":
                    test = 3
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[5] == "  ":
                    test = 4
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[4] == " ":
                    test = 5
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[3] == "  ":
                    test = 6
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[2] == "  ":
                    test = 7
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[1] == " ":
                    test = 8
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                if The_playbook_test_2[0] == "  ":
                    test = 9
                    if win_test(The_playbook_test_2, option, test,option_3):
                        stop = True

                print(f"option3 {option}")
                if not option == []:
                    pc_game = random.choice(option)
                return stop, pc_game


            def win_test(The_playbook_test_for_o, option, test, option_4):
                dale = 10
                yes_no = False
                pc_game = 10
                if   option_4 == 1:
                    if test == 9:
                        The_playbook_test_for_o[0] = "o"
                        dale = 0
                    elif test == 8:
                        The_playbook_test_for_o[1] = "o"
                        dale = 1
                    elif test == 7:
                        The_playbook_test_for_o[2] = " o"
                        dale = 2
                    elif test == 6:
                        The_playbook_test_for_o[3] = "o"
                        dale = 3
                    elif test == 5:
                        The_playbook_test_for_o[4] = "o"
                        dale = 4
                    elif test == 4:
                        The_playbook_test_for_o[5] = " o"
                        dale = 5
                    elif test == 3:
                        The_playbook_test_for_o[6] = "o"
                        dale = 6
                    elif test == 2:
                        The_playbook_test_for_o[7] = "o"
                        dale = 7
                    elif test == 1:
                        The_playbook_test_for_o[8] = " o"
                        dale = 8

                elif option_4 == 2:
                    if test == 9:
                        The_playbook_test_for_o[0] = "x"
                        dale = 0
                    elif test == 8:
                        The_playbook_test_for_o[1] = "x"
                        dale = 1
                    elif test == 7:
                        The_playbook_test_for_o[2] = " x"
                        dale = 2
                    elif test == 6:
                        The_playbook_test_for_o[3] = "x"
                        dale = 3
                    elif test == 5:
                        The_playbook_test_for_o[4] = "x"
                        dale = 4
                    elif test == 4:
                        The_playbook_test_for_o[5] = " x"
                        dale = 5
                    elif test == 3:
                        The_playbook_test_for_o[6] = "x"
                        dale = 6
                    elif test == 2:
                        The_playbook_test_for_o[7] = "x"
                        dale = 7
                    elif test == 1:
                        The_playbook_test_for_o[8] = " x"
                        dale = 8

                if option_4 == 1:
                    # win_for_x
                    # العمود الاول
                    if The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[5] == " o" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[5] == " o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[5] == "  ":
                        pc_game = 4
                        yes_no = True
                    # العمود الثانى
                    if The_playbook_test_for_o[1] == "o" and The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[7] == " ":
                        pc_game = 2
                        yes_no = True
                    if The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[7] == "o" and The_playbook_test_for_o[1] == " ":
                        pc_game = 8
                        yes_no = True
                    if The_playbook_test_for_o[1] == "o" and The_playbook_test_for_o[7] == "o" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # العمود الثالث
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[3] == "o" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[3] == "o" and The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[0] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 6
                        yes_no = True
                    # الصف الاول
                    if The_playbook_test_for_o[1] == "o" and The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[1] == "o" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[1] == " ":
                        pc_game = 8
                        yes_no = True
                    # الصف الثانى
                    if The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[5] == " o" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 6
                        yes_no = True
                    if The_playbook_test_for_o[3] == "o" and The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[5] == "  ":
                        pc_game = 4
                        yes_no = True
                    if The_playbook_test_for_o[3] == "o" and The_playbook_test_for_o[5] == " o" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # الصف الثالث
                    if The_playbook_test_for_o[7] == "o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[7] == "o" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[7] == " ":
                        pc_game = 2
                        yes_no = True
                    # الخط مائل الاول
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[0] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "o" and The_playbook_test_for_o[8] == " o" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # الخط مائل الثانى
                    if The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[4] == "o" and The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[2] == " o" and The_playbook_test_for_o[6] == "o" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True

                elif option_4 == 2:
                    # win_for_x
                    # العمود الاول
                    if The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[5] == " x" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[5] == " x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[ 5] == "  ":
                        pc_game = 4
                        yes_no = True
                    # العمود الثانى
                    if The_playbook_test_for_o[1] == "x" and The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[7] == " ":
                        pc_game = 2
                        yes_no = True
                    if The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[7] == "x" and The_playbook_test_for_o[1] == " ":
                        pc_game = 8
                        yes_no = True
                    if The_playbook_test_for_o[1] == "x" and The_playbook_test_for_o[7] == "x" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # العمود الثالث
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[3] == "x" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[3] == "x" and The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[0] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 6
                        yes_no = True
                    # الصف الاول
                    if The_playbook_test_for_o[1] == "x" and The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[1] == "x" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[1] == " ":
                        pc_game = 8
                        yes_no = True
                    # الصف الثانى
                    if The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[5] == " x" and The_playbook_test_for_o[3] == "  ":
                        pc_game = 6
                        yes_no = True
                    if The_playbook_test_for_o[3] == "x" and The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[5] == "  ":
                        pc_game = 4
                        yes_no = True
                    if The_playbook_test_for_o[3] == "x" and The_playbook_test_for_o[5] == " x" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # الصف الثالث
                    if The_playbook_test_for_o[7] == "x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[7] == "x" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[7] == " ":
                        pc_game = 2
                        yes_no = True
                    # الخط مائل الاول
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[8] == "  ":
                        pc_game = 1
                        yes_no = True
                    if The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[0] == "  ":
                        pc_game = 9
                        yes_no = True
                    if The_playbook_test_for_o[0] == "x" and The_playbook_test_for_o[8] == " x" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True
                    # الخط مائل الثان
                    if The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[6] == "  ":
                        pc_game = 3
                        yes_no = True
                    if The_playbook_test_for_o[4] == "x" and The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[2] == "  ":
                        pc_game = 7
                        yes_no = True
                    if The_playbook_test_for_o[2] == " x" and The_playbook_test_for_o[6] == "x" and The_playbook_test_for_o[4] == " ":
                        pc_game = 5
                        yes_no = True


                if dale == 0:
                    The_playbook_test_for_o[0] = "  "
                elif dale == 1:
                    The_playbook_test_for_o[1] = " "
                elif dale == 2:
                    The_playbook_test_for_o[2] = "  "
                elif dale == 3:
                    The_playbook_test_for_o[3] = "  "
                elif dale == 4:
                    The_playbook_test_for_o[4] = " "
                elif dale == 5:
                    The_playbook_test_for_o[5] = "  "
                elif dale == 6:
                    The_playbook_test_for_o[6] = "  "
                elif dale == 7:
                    The_playbook_test_for_o[7] = " "
                elif dale == 8:
                    The_playbook_test_for_o[8] = "  "
                if yes_no:
                    option.append(test)
                return yes_no


            def random_game(The_playbook):
                random_option = [10]
                stop = True
                if The_playbook[0] == "  ":
                    random_option.append(9)
                if The_playbook[1] == " ":
                    random_option.append(8)
                if The_playbook[2] == "  ":
                    random_option.append(7)
                if The_playbook[3] == "  ":
                    random_option.append(6)
                if The_playbook[4] == " ":
                    random_option.append(5)
                if The_playbook[5] == "  ":
                    random_option.append(4)
                if The_playbook[6] == "  ":
                    random_option.append(3)
                if The_playbook[7] == " ":
                    random_option.append(2)
                if The_playbook[8] == "  ":
                    random_option.append(1)

                random_option.remove(10)
                pc_game = random.choice(random_option)

                return stop, pc_game


            def special_characters(The_playbook, option):
                random_option = [10]
                stop = False
                if option == 1:
                    if The_playbook == ['  ', ' ', ' x', '  ', 'o', '  ', 'x', ' ', '  ']:
                        random_option = random.choice([2, 4, 6, 8])
                        stop = True
                pc_game = random_option
                print(pc_game)
                return stop , pc_game


            The_playbook = ["  ", " ", "  ", "  ", " ", "  ", "  ", " ", "  "]
            prevent_dtep_repeat = []
            user_input = []
            numbers = [1, 3, 7, 9]
            win_and_lose = False
            random_number = random.randint(1, 2)

            if random_number == 1:
                pc_input = 10
                user_input, stop1, stop2, win_for_o_or_x = prevent_dtep_repeat_test(prevent_dtep_repeat, The_playbook,1)
                if user_input == 9 or user_input == 7 or user_input == 3 or user_input == 1:
                    pc_input = 5
                elif user_input == 5:
                    pc_input = random.choice(numbers)
                elif user_input == 2 or user_input == 6 or user_input == 8 or user_input == 4:
                    pc_input = 5
                else:
                    print("Enter number")
                prevent_dtep_repeat.append(pc_input)
                xo(user_input, pc_input)

                for i in range(4):
                    user_input, stop1, stop2, win_for_o_or_x = prevent_dtep_repeat_test(prevent_dtep_repeat,The_playbook, 1)
                    if win_for_o_or_x == 2:
                        xo(user_input, 10)
                        print("win for x\n")
                        print("\n")
                        break
                    if win_for_o_or_x == 3:
                        xo(user_input, 10)
                        print("win for o\n")
                        print("\n")
                        break
                    if stop1:
                        xo(user_input, 10)
                        print("draw")
                        print("\n")
                        break

                    print(f"win_for_o_or_x  {win_for_o_or_x}")
                    pc_input = option_game_the_pc(The_playbook, user_input,1)
                    xo(user_input, pc_input)
                    win_and_lose, win_for_o_or_x = win_and_stone(The_playbook)
                    prevent_dtep_repeat.append(pc_input)
                    if win_and_lose:
                        print("\n")
                        break

            elif random_number == 2:
                print(" 7 | 8 | 9 ")
                print("---+---+---")
                print(" 4 | 5 | 6 ")
                print("---+---+---")
                print(" 1 | 2 | 3 ","\n")
                pc_input = random.randint(1, 9)
                xo(pc_input, 10)
                prevent_dtep_repeat.append(pc_input)

                for i in range(4):
                    user_input, stop1, stop2, win_for_o_or_x = prevent_dtep_repeat_test(prevent_dtep_repeat, The_playbook,2)
                    if stop1:
                        xo(pc_input, 10)
                        print("draw")
                        break
                    if win_for_o_or_x == 3:
                        xo(pc_input, 10)
                        print("win for x\n")
                        break
                    if win_for_o_or_x == 2:
                        xo(pc_input, 10)
                        print("win for o\n")
                        break
                    pc_input = option_game_the_pc(The_playbook, user_input,2)
                    stop = test_and_draw(The_playbook)
                    xo(pc_input, user_input)
                    win_and_lose, win_for_o_or_x = win_and_stone(The_playbook)
                    prevent_dtep_repeat.append(pc_input)
                    if win_for_o_or_x == 2:
                        print("win for x\n")
                        break
                    if win_for_o_or_x == 3:
                        print("win for o\n")
                        break
                    stop = test_and_draw(The_playbook)
                    if stop:
                        print("draw")
                        break

        except ValueError as ex:
            print("ERROR")
            print("Enter number:")