a = str(input("Начало игры в камень,ножницы,бумага.Первый игрок выбирает: "))
b = str(input("Начало игры в камень,ножницы,бумага.Второй игрок выбирает: "))
stone = "камень"
paper = "бумага"
scissors = "ножницы"

first = "победил первый игрок"
two = "победил второй игрок"
draw = "ничья"

if a == stone and b == paper:
    print(first)
elif a == stone and b == scissors:
    print(two)

elif a == paper and b == stone:
    print(two)
elif a == paper and b == scissors:
    print(first)

elif a == scissors and b == paper:
    print(first)
elif a == scissors and b == stone:
    print(two)




elif a == b:
    print(draw)
else:
    print("Введите заново")



