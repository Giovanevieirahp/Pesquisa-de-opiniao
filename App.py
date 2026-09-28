#classificações da entrevistas

excelentes = 0
boas = 0
ruins = 0

# Coletar as respostas dos entrevistados

for i in range(50):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    resposta = int(input("Digite 1 para excelente, 2 para boa ou 3 para ruim: "))
    if resposta == 1:
        excelentes += 1
    elif resposta == 2:
        boas += 1
    elif resposta == 3:
        ruins += 1


#resultados

print(f"Total de respostas excelentes (1): {excelentes}")
print(f"Total de respostas boas (2): {boas}")
print(f"Total de respostas ruins (3): {ruins}")