This is a very simple python script to find fixed points in translation networks.

You'll need to install the googletrans library.

# What is a fixed point in a translation network?

An example will make it clear.

Esta é uma ferramenta de tradução com ponto fixos.
1 This is a translation tool with fixed point.
2 Dies ist ein Übersetzungs-Tool mit festen Punkt.
3 Ceci est un outil de traduction avec le point fixe.
4 Questo è uno strumento di traduzione con il punto fisso.
5 这是与固定点翻译工具。
6 Este é um ponto fixo de ferramentas de tradução.
7 This is a fixed point of translation tools.
8 Dies ist ein Fixpunkt von Übersetzungstool.
9 Ceci est un point fixe de l’outil de traduction.
10 Questo è un punto fisso dello strumento di traduzione.
11 这是翻译工具的固定点。
12 Esta é uma ferramenta de tradução de ponto fixo. <<<<<<<<
13 This is a fixed-point translation tool.
14 Dies ist ein fester Punkt-Übersetzungs-Tool.
15 Ceci est un outil de traduction point fixe.
16 Questo è un punto fisso di strumento di traduzione.
17 这是翻译工具的固定点。
18 Esta é uma ferramenta de tradução de ponto fixo. <<<<<<<<<
Fixed point!

# How to change the languages the tool cycles over?

Look at line 5:

```
cycle = [
    "pt",
    "en",
    "de",
    "fr",
    "it",
    "zh-cn",
    "pt"
]
```

# How to use it?

`python __main__.py "Some sentence you want to play with!"`

# Can you find long cycles?

Eu adoro cerveja, mas nao gosto de batata
1 I love beer, but not potato taste
2 Ich liebe Bier, aber nicht Kartoffelgeschmack
3 bière I amour, mais pas la saveur de pommes de terre
4 Mi piace la birra, ma non il sapore della patata
5 我喜欢啤酒，但马铃薯的不是味道
6 Eu gosto de cerveja, mas não o sabor da batata
7 I like beer, but not the taste of the potato
8 Ich mag Bier, aber nicht den Geschmack der Kartoffel
9 J'aime la bière, mais pas le goût de la pomme de terre
10 Mi piace la birra, ma non il gusto della patata
11 我喜欢啤酒，但不是土豆的味道
12 Eu gosto de cerveja, mas não o gosto de batatas
13 I like beer, but not the taste of potatoes
14 Ich mag Bier, aber nicht den Geschmack von Kartoffeln
15 J'aime la bière, mais pas le goût de pommes de terre
16 Mi piace la birra, ma non il gusto di patate
17 我喜欢啤酒，但不是土豆味道
18 Eu gosto de cerveja, mas não batatas gosto
19 I like beer, but do not like potatoes
20 Ich mag Bier, aber nicht wie Kartoffeln
21 Je aime la bière, mais pas comme les pommes de terre
22 I birra amore, ma non come le patate
23 我爱啤酒，而不是像土豆
24 Eu amo a cerveja, ao invés de batatas
25 I love beer, instead of potatoes
26 Ich liebe Bier, statt Kartoffeln
27 J'aime la bière, au lieu de pommes de terre
28 Mi piace la birra, invece di patate
29 我喜欢啤酒，而不是土豆
30 Eu gosto de cerveja, mas não batatas
31 I like beer, but not potatoes
32 Kartoffeln I wie Bier, aber nicht
33 Les pommes de terre Je aime la bière, mais pas
34 Le patate I Love Beer, ma non
35 土豆我喜欢啤酒，但不
36 Batatas, eu gosto de cerveja, mas não
37 Potatoes, I like beer, but not
38 Kartoffeln, Ich mag Bier, aber nicht
39 Les pommes de terre, j'aime la bière, mais pas
40 Le patate, mi piace la birra, ma non
41 土豆，我喜欢啤酒，但不
42 Batatas, eu gosto de cerveja, mas não
Fixed point!
