

def converter():

    word = input("Type a word ")
    for char in word.upper():
        chars = [char]
        for cha in chars:
            asci = ord(cha)
            lis = bin(asci)
            print(lis.replace('b', ''))


converter()
