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
