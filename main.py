#Exercício1
bornData = int(input("Qual ano do seu nascimento ?"))

todayYear = 2022
age = todayYear - bornData

print("A sua idade é de: ", age, "anos")

#Exercício2

carroValue = 100.0
days = int(input("por quantos dias o carro será alugado?"))

totalValue = carroValue * days

print("O total da diárias fica em R$:", totalValue)

#Exercício3

celsiuTemperature = float(input("Qual a temperatura atual em Celsiu ?"))

fahrenheitTemperature = (celsiuTemperature * 9/5) + 32

print("A temperauta em Fahrenheit é de:",fahrenheitTemperature)

#Exercício4

grade1 = int(input("Qual valor da primeira nota ?"))
grade2 = int(input("Qual valor da segunda nota ?"))
grade3 = int(input("Qual valor da terceira nota ?"))
grade4 = int(input("Qual valor da quarta nota ?"))

mediaDasNotas = (grade1+grade2+grade3+grade4)/4

print("A Média foi de:", mediaDasNotas)

#Exercício5

myAge = int(input("Qual sua idade ?"))
actualyDate = int(input("Em que ano estamos ?"))
ageInMonth = (actualyDate-myAge) * 12
print("Você tem",ageInMonth, "meses de idade")

#Exercício6

productWeight = float(input("Quantos kilos deu o produto na balança ?"))
totalValueProduct = productWeight * 7.75

print("considerando que nosso produto vale R$7,75 por Kg, o preço total do produto foi de R$:", totalValueProduct)










