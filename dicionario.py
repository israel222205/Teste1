dict = {
    "cringe": "algo vergonhoso",
    "stalkear": "investigar alguem online",
    "vdd": "abreviação da palavra verdade",
    "vlw": "abreviação da palavra valeu",
    "hater": "pessoa que está constantemente criticando os outros"
}

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras minúsculas): ")

if word in dict.keys():
    print(dict[word])
else:
    print("a palavra não foi encontrada")
