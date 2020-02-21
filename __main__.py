import sys

from googletrans import Translator

t = Translator()

sentence = sys.argv[1]

print(sentence)

for _ in range(10):

    initial = sentence

    sentence = t.translate(text=sentence, src="pt", dest="en").text
    print(sentence)
    sentence = t.translate(text=sentence, src="en", dest="pt").text

    if sentence == initial:
        print("Fixed point!")
        break
    
    print(sentence)
