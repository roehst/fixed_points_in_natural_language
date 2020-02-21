import sys

from googletrans import Translator

cycle = [
    "pt",
    "en",
    "de",
    "fr",
    "it",
    "zh-cn",
    "pt"
]

t = Translator()

sentence = sys.argv[1]

print(sentence)

j = 0

for i in range(10):

    initial = sentence

    for (a, b) in zip(cycle, cycle[1:]):
        sentence = t.translate(text=sentence, src=a, dest=b).text
        j+=1
        print(j, sentence)

        if sentence == initial:
            print("Fixed point!")
            sys.exit(0)
