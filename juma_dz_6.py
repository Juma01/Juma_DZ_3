def int_func():
    for word in input("Введите слова через пробел с маленькими англицскими буквами:").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} Это не английские буквы и слова ! ")


int_func()
