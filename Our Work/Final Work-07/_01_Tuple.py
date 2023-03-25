"""
Tuple :

1. Ordered
2.Unchangeable [immutable]
3.Allow duplicate data

List:

1. Ordered
2.Changeable [Mutable]
3.Allow duplicate data
"""

# Declare

tuple_1 = ()

print(type(tuple_1))  # <class 'tuple'>
print(tuple_1)  # ()

tuple_2 = tuple()

print(type(tuple_2))  # <class 'tuple'>
print(tuple_2)  # ()

tuple_1 = ("Python", 10, 10.5, [10, 20, 30], (10, 20, 30, 40))
print(tuple_1)  # ("Python", 10, 10.5, [10, 20, 30], (10, 20))

#  Accessing of Tuple

print(tuple_1[0])
print(tuple_1[-1])  # (10, 20)
print(tuple_1[0:3])  #
print(tuple_1[2:])  #
print(tuple_1[:4])  #

print(tuple_1[-1][0:2])
print(tuple_1[-1][1:])

print(tuple_1[4][1:])


tuple_1 = ("Python", 10, 10.5, [10, 20, 30], (10, 20, 30, 40))

# tuple_1[0] = "Java"  # Unchangeable [immutable]

#  del tuple_1

tuple_3 = (10, 20)
tuple_3 = (tuple_1 + tuple_3)

tuple_4 = tuple_1 + tuple([10, 40])

print(tuple_3)
print(tuple_4)


#-------------------------------------

lst = [10, 20, 30]
print(lst)

tpl = tuple(lst)
print(tpl)

lst_2 = list(tpl)
print(lst_2)

lst_2.append(20)

tuple_2 = tuple(lst_2)
print(tuple_2)

