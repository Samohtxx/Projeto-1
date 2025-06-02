#Aqui ele vai perguntar qual o seu nome e suas notas.
name = input('Qual é o seu nome? ')
nota1 = float(input('Qual a sua primeira nota?: '))
nota2 = float(input('Qual a sua segunda nota?: '))
nota3 = float(input('Qual a sua terceira nota?: '))

#Processamendo da média.
med = (nota1 + nota2 + nota3) // 3

#Irá retornar seu nome e sua média.
print (f'Olá, {name}! Sua média é {med}')

#Irá retornar uma mensagem dizendo se você passou, ficou de recuperção ou reprovou.
if med >= 6:
    print('Parabéns você foi aprovado')

if med >= 5 <6:
    print('Você ficou de recuperação.')

if med <5:
    print('Você foi reprovado, estude mais!')