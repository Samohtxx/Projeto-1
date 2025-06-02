#Aqui ele vai perguntar qual o seu nome, peso e altura. Peso e altura estão com a função de receber números decimais.
name = input('Qual é o seu nome?: ')
weight = float(input('Qual é o seu peso?: '))
height = float(input('Qual é a sua altura?: '))

#Processar IMC
imc = weight / (height*height)

#Irá mostrar na tela o seu nome e seu IMC.
print(f'Olá {name}! Seu IMC é {imc}')

#Estrutura de decisão.
if imc <18.5:
  print('Abaixo do peso.')

if imc >= 18.5 <24.9:
  print ('Seu peso está normal.')

if imc >=25 <29.9:
  print ('Você está sobrepeso!')

if imc >=30 <34.9:
  print('Obeso grau 1')

if imc >=35 <39.9:
  print('Obeso grau 2')

if imc >=40:
  print('Obeso grau 3')
