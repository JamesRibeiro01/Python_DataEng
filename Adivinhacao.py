print("*************************************")
print("Bem vindo ao jogo de Advinhação")
print("*************************************")

#Definindo a variavel de numero secreto

numero_secreto = 42 

#comando usado para interação com o usuario no console.
#O valor digitado pelo usuario deve ser capturado por uma variavel, entao definimo o input como valor para a variavel chute
#todo valor digitado no console é considerado uma string, caso seja passado um "numero" deve ser feito a conversão.
#Usando a função int(), para realizar a "Conversão"
chute = int(input("Digite o seu número!\n"))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

print("Você digitou", chute)


#condiçao IF usado para comparação de dois ou mais valores, condicional.
#Para comparar dois valores no IF vc deve usar o == para comparação, somente "=" é usado para atribuição
# O codigo IF no final do bloco da condição deve ser iniciado com :
if (acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Seu chute foi maior do que o número secreto")
    elif(menor): #elif (else if) 
        print("Seu chute foi menor do que o número secreto")


print("Fim de Jogo")