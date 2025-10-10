print("Вы будете задавать любые ЦЕЛЫЕ числа и эта программа будет определять, какой это треугольник")

tria = int(input("Задайте длину для A: "))
trib = int(input("Задайте длину для B: "))
tric = int(input("Задайте длину для C: "))

# равнобедренный
# разносторонний
# равносторонний
if tria == trib == tric:
    print("равносторонний", "a =", tria, "b =", trib, "c =", tric)
elif tria == 0 or trib == 0 or tric == 0:
    print("одно из значений равны нулю, треугольника не существует")
elif trib >= tria+tric or tria >= trib+tric or tric >= trib+tria:
    print("такого треугольника не существует", "a =", tria, "b =", trib, "c =", tric)
elif tria == trib or trib == tric or tria == tric:
    print("равнобедренный", "a =", tria, "b =", trib, "c =", tric)
else:
    print("разносторонний", "a =", tria, "b =", trib, "c =", tric)
if tria == 0 and trib == 0 and tric == 0:
    print("БАГ! все значения равны нулю, поэтому равностороннего треугольника нет")
