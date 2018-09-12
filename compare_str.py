# -*- coding: utf-8 -*-


def compare_str(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2:
        if len(str1) > len(str2):
            return 2
        elif str2 == "learn":
            return 3
        else:
            return "Условия не выполнены"


result = compare_str(1, "abcd")
print (result)
result = compare_str("abcd", "abcd")
print (result)
result = compare_str("abcde", "abcd")
print (result)
result = compare_str("abcd", "learn")
print (result)
result = compare_str("abcd", "abcde")
print (result)