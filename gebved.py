while True:
    q = "qを入力したら終了です"
    print(q)
    a = input("入力よろ:")
    if a == "q":
        break
    elif a.isdigit() and 0 == int(a)%2:
        print("偶数あざす")
    elif a.isdigit() and 1 == int(a)%2:
        print("奇数あざす")
    else:
        print("数値入力して")
        
