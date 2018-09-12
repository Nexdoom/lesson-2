# -*- coding: utf-8 -*-


try:
    num_one = float(input("Введите первое слогаемое: "))
    num_one = round(num_one)

    num_two = float(input("Введите второе слогаемое: "))
    num_two = round(num_two)

except ValueError:
    exit("Слогаемое не является числом")


def get_summ(num_one, num_two):
    summ = num_one + num_two
    return summ


summ = get_summ(num_one, num_two)
print(summ)