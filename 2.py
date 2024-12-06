weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
def calculate_bmi(weight,height):
    bmi=weight/(height*height)
    return bmi
result=calculate_bmi(weight,height)
print(result)