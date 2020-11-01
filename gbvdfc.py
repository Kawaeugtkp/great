import re
text = """キリンは大昔から_複数名詞_の興味の対象でした。キリンは_複数名詞_の中で一番背が高いです
が、科学者たちはそのような長い_体の一部_をどうやって獲得したのか説明できません。キリンの身長は
_数値__単位_近くあり、その高さのほとんどは脚と_体の一部_によるものです。"""

def m(mls):
    a = re.findall("_.*?_", mls)
    if a is not None:
        for word in a:
            b = "{}を入力".format(word)
            new = input(b)
            mls = mls.replace(word, new)
        print(mls)
    else:
        print("引数mlsが無効です")

m(text)
