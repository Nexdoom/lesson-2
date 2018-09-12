# -*- coding: utf-8 -*-


user_age = 0
while not user_age:
    try:
        user_age = int(input("Скажи сколько тебе лет, и я скажу кто ты: "))
    except(ValueError):
        print("В значении присутствуют запрещенные символы")


def get_user_stage(age):
    if age < 7:
        return "Ты ходишь в садик"
    elif age >=7 and age < 18:
        return "Ты школьник. Чего не спишь блин блинский. Вырос что ли?"
    elif age >= 18 and age < 24:
        return "Ты студент"
    else:
        return "Ты работяга =)"


user_prof = get_user_stage(user_age)
print (user_prof)