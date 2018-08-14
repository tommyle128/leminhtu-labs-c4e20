from random import randint, choice

# from eval import calc
# from xyz import calc
# import eval 

phep_tinh = ['+', '-', '*', '/']
loi = [-1, 0, 1]

playing = True

while playing:
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(phep_tinh)
    error = choice(loi)

    res = eval.calc(x, y, op)

    display_res = res + error
    print('* ' * 10)
    print("{} {} {} = {}".format(x, op, y, display_res))
    print('* ' * 10)

    ans = input ("(Y/N)?").lower()

    if error == 0 and ans == "y":
        print("Yay")
    elif error == 0 and ans == "n":
        print("You are wrong")
    elif error != 0 and ans == "y":
        print("You are wrong")
    elif error != 0 and ans == "n":
        print("Yay")

    play = input("Continue (Y/N)?").lower()
    if play == "y":
        playing = True
        count += 1
    else:
        playing = False



