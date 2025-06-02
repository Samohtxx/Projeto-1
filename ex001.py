#Aqui as variáveis recebem uma função de perguntar nome, idade e altura
name = input ('Qual é o seu nome? ')
age = input ('Qual é a sua idade? ')
height = float(input ('Qual é a sua altura? '))

#Aqui as variáveis terão a função de receber dois números inteiros e entregar a soma deles
som1 = int(input('Qual o primeiro número que deseja somar? '))
som2 = int(input('Qual o segundo número que deseja somar? '))

#Aqui as váriaveis terão a função de receber dois números decimais e entregar a média 
med1 = float(input('Qual a sua primeira nota? '))
med2 = float(input('Qual a sua segunda nota? '))

#Processamento da média
media = (med1 + med2) / 2

#saída
print(f'Seu nome é {name} e sua idade é: {age} anos e sua altura é {height}')
print(f'Seu resultado é : {som1+som2}')
print(f'Sua altura em centimetros é: {height*100}')
print(f'Sua média é: {media}')