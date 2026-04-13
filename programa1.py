import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("Bem vindo ao gerador de senhas, quantas caracteres a senha teria?"))
senha = ""

for i in range(comprimento):
    senha += random.choice(caracteres)

print(senha)