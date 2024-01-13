# #task_1
#
# lst = [1, 4, 5, 3, 13, 7]
# result = 0
#
#
# def find(lst, result):
#     for x in lst:
#         result += x
#     print(result)
#
#
# print(find(lst, result))


# task_2
#
# lst = ["Xushnoza", "Sardor", "Odina", "Asad", "Malika", "Asliddin"]
# txt = input("Enter the letter:")
# result = []
#
#
# def find_order(lst, txt):
#
#     for x in lst:
#         if txt in x:
#             result.append(x)
#     return sorted(result)
#
#
# print(find_order(lst, txt))


# Task_3

#
# Names = ["Della", "Jim", "Anne", "Jack"]
#
#
# def where_is_Della(Names):
#     for x in Names:
#         if "Della" in x:
#             return Names.index("Della")
#         else:
#             return -1
#
#
# print(where_is_Della(Names))


# def find_bob(names):
#     if "Della" in names:
#         return names.index("Della")
#     else:
#         return -1
#
#
# print(find_bob(names))


# task_4
lst_1 = [1, 2, 3, 4, 5]
lst_2 = [0, 1, 2, 3, 4]


def simon_says(lst_1, lst_2):
    for n in range(len(lst_1)):
        if lst_1[n] == lst_2[n + 1]:
            return True
        else:
            return False


print(simon_says(lst_1, lst_2))

# task_5
list = [1, 2, 3, 4]
res = []


def clone_a_list(list):
    for x in list:
        res.append(x)
    res.append(list)
    return res

print(clone_a_list(list))


# task_6
lst = [-5, -3, 7, -12, 5, -1, 3]
lst2 = []


def more_than0(msv, msv2):
    for num in msv:
        if num > 0:
            lst2.append(num)


print(more_than0(msv=lst, msv2=lst2))

# Task_7
d = [1, 2, 3, 4, 5]
a = []


def high_low(d):
    result = max(d)
    result1 = min(d)
    a.append(result)
    a.append(result1)
    print(a)


print(high_low(d))
