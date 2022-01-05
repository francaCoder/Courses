"""
Read the IMC and show:
18.5 - Under weight
Among 18.5 and 25 - Ideal weight
Among 25 and 30 - Overweight
Among 30 and 40 - Obese
Above 40 - Morbid obesity
"""

weight = float(input("Put your weight: "))
height = float(input("Put your height: "))
IMC = weight / (height ** 2)

if IMC < 18.5:
    print("Under weight")
elif 18.5 <= IMC <= 25:
    print("Ideal weight")
elif IMC > 25 or IMC <= 30:
    print("Overweight")
elif IMC > 30 or IMC <= 40:
    print("Obese")
elif IMC > 40:
    print("Morbid obesity")




