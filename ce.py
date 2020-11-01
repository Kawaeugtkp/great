import random
def hangman():
    wordlist = ["Java", "Python", "computer", "hacker", "painter"]
    random_list = random.randint(0,4)
    word = wordlist[random_list]
    wrong = 0
    stages = ["1", "2", "3", "4", "5", "6"]
    rletters = list(word)
    borard = ["__"]*len(word)
    win = False
    print("\n")
    while wrong < len(stages)-1:
        msg = input("文字を入力:")
        if msg in rletters:
            cindex = rletters.index(msg)
            borard[cindex] = msg
            rletters[cindex] = '$'
        else:
            wrong += 1
        e = wrong + 1
        print("".join(borard))
        print(stages[0:e])
        if '__' not in borard:
            print("貴方の勝ち")
            print(word)
            win = True
            break
    if win == False:
        print(stages[0:wrong+1])
        print("あなたの負け！正解は{}.".format(word))
