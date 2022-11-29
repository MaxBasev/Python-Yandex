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
mynumber = input()
if (mynumber[0] == mynumber[3] and mynumber[1] == mynumber[2]):
    print("YES")
else:
    print("NO")


#H
text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")


#I
name1 = input()
name2 = input()
name3 = input()
print(min(name1, name2, name3))



#J
first = input()
x = int(first[2]) + int(first[1])
y = int(first[1]) + int(first[0])
if x > y:
    print(str(x) + str(y))
else:
    print(str(y) + str(x))


#K
x = input()
y = int(min(x[0], x[1], x[2]))
z = int(max(x[0], x[1], x[2]))
n = int(x[0]) + int(x[1]) + int(x[2]) - y - z
if ((y + z) == n * 2):
    print("YES")
else:
    print("NO")


#L
x = int(input())
y = int(input())
z = int(input())
if (x < (y + z)) and (y < (x + z)) and (z < (x + y)):    
    print("YES")
else:
    print("NO")


#M
x = input()
y = input()
z = input()
if (x[0] == y[0] == z[0]):
    print(x[0])
elif (x[1] == y[1] == z[1]):
    print(x[1])


#N
first = input()
x = int(first[0])
y = int(first[1])
z = int(first[2])
min = min(x, y, z)
max = max(x, y, z)
avg = int(x + y + z) - min - max
if min > 0 and min <= avg and avg <= max:
    print(str(min) + str(avg), str(max) + str(avg), sep=" ")
elif min == 0 and min <= avg and avg <= max:
    print(str(avg) + str(min), str(max) + str(avg), sep=" ")


#O



#P



#Q



#R



#S



#T

