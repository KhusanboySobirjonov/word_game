"""
Sana : 19/11/2022
Sobirjonov Khusanboy
#26 - dars : So'z topish o'yini
Anvar Nazrullayev ustoz 1 - videosida mantiq tomonlama tushuntirgani uchun tashakkur
"""

from words_list import words
import random as r
 

def get_word():
    """So'zlarni random qilib beradigan funksiya"""
    word = r.choice(words)
    return word


def display(letters = None, word = None):
    """Harflarni so'z ichida bor yoki yo'qligini tekshirib qaytaruvchi funksiya""" 
    user_words = []
    for i in range(len(word)):
        user_words.append('-')
    if letters != None:
        for i in range(len(letters)):
            char = []
            for j in range(len(word)):
                if letters[i] == word[j]:
                    char.append(j)
            for k in char:
                if user_words[k] != letters[i]:
                    user_words[k] = letters[i]
                    break
    user_letters = ''
    for i in user_words:
        user_letters += i
    if letters == None:
        print(f"\nMen {len(word)} belgili so'z o'yladim. ( " ' " va " - " belgilari ham bo'lishi mumkin) Topa olasizmi ?\n{user_letters}")
    return user_letters


def play():
    """O'yin holati haqida ma'lumot beruvchi funksiya"""
    txt = get_word()
    text = display(word = txt)
    user_letters = ''
    while True:
        letter = input("Harf kiriting : ")
        user_letters += letter
        if text == display(user_letters, txt):
            print("Bunday harf yo'q.")
        else:
            print(f"{letter.upper()} harfi to'g'ri.")
        text = display(user_letters, txt)
        if text == txt:
            print(f"Tabriklayman! {txt.upper()} so'zini {len(user_letters)} ta urinishda topdingiz.")
            break
        print(f"{text.upper()} \nShu vaqtgacha kiritgan harflaringiz: {user_letters.upper()}")











