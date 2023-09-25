
#Задание 1

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

common_elements = set(tuple1) & set(tuple2) & set(tuple3)

print("Общие элементы:", common_elements)




#Задание 2

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

unique_elements = (
    set(tuple1) - set(tuple2) - set(tuple3) |
    set(tuple2) - set(tuple1) - set(tuple3) |
    set(tuple3) - set(tuple1) - set(tuple2)
)

print("Уникальные элементы для каждого списка:", unique_elements)



#Задание 3

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)

common_elements_at_same_position = [a for a, b, c in zip(tuple1, tuple2, tuple3) if a == b == c]

print("Элементы на одинаковых позициях:", common_elements_at_same_position)


