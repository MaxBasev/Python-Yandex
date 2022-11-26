#A
name = input()
how = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if how == "хорошо" or how == "Хорошо":
    print("Я за вас рада!")
elif how == "плохо" or how == "Плохо": 
    print("Всё наладится!")



#B
speed_petya = int(input())
speed_vasya = int(input())
if speed_petya > speed_vasya:
    print("Петя")
elif speed_petya < speed_vasya:
    print("Вася")


#C
speed_petya = int(input())
speed_vasya = int(input())
speed_tolya = int(input())
if speed_petya > speed_vasya and speed_petya > speed_tolya:
    print("Петя")
elif speed_petya < speed_vasya and speed_tolya < speed_vasya:
    print("Вася")
elif speed_tolya > speed_petya and speed_tolya > speed_vasya:
    print("Толя")


#D
p = int(input())
v = int(input())
t = int(input())
if p > v and p > t and v > t:
    print("1. Петя\n2. Вася\n3. Толя")
elif p > v and p > t and t > v:
    print("1. Петя\n2. Толя\n3. Вася")
elif v > p and v > t and p > t:
    print("1. Вася\n2. Петя\n3. Толя")
elif v > p and v > t and t > p:
    print("1. Вася\n2. Толя\n3. Петя")
elif t > v and t > p and v > p:
    print("1. Толя\n2. Вася\n3. Петя")
elif t > v and t > p and p > v:
    print("1. Толя\n2. Петя\n3. Вася")

#E
n = int(input())
m = int(input())
if int(n + 6) > int(m + 9):
    print("Петя")
else:
    print("Вася")


#F
y = int(input())
if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print("YES")
else:
    print("NO")



#G



#H



#I




#J



#K



#L



#M



#N



#O



#P



#Q



#R



#S



#T

