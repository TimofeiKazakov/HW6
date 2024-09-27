immutable_var = 2, 3, "a", "x"
print(immutable_var)
# immutable_var[0] = 20      TypeError: 'tuple' object does not support item assignment:
# Кортеж не поддерживает обращение по элементам.
mutable_list = [1, 0, 'i', 'b']
print(mutable_list)
mutable_list[0] = 6 + 2
print(mutable_list)