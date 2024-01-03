secret_number = 100

chute = int(input("Digite seu chute\n"))


print("*********************************************")
print("Você escolheu o número: ", chute)


print("*********************************************")


if(secret_number == chute):
    print("Você acertou!")
else:
    print("Você errou!")