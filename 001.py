#A
print("Привет, Яндекс!")
#B
youname = input()
print("Как Вас зовут?")
print("Привет, " + str(youname))
#C
info = input()
print((info + "\n") * 3)
#D
money = float(input())
cost = float(2.5 * 38)
total = float(money) - float(cost)
print(int(total))
#E
price = float(input())
ves = float(input())
money = float(input())
total = float(money) - (float(ves) * float(price))
print(int(total))
#F
item_name = str(input())
price = int(input())
ves = int(input())
money = int(input())
allprice = int(ves) * int(price)
total = int(money) - (int(ves) * int(price))
print(f"Чек\n{item_name} - {ves}кг - {price}руб/кг\nИтого: {allprice}руб\nВнесено: {money}руб\nСдача: {total}руб")
#G
n = int(input())
print("Купи слона!\n" * n)
#H
n = int(input())
text = input()
print((f'Я больше никогда не буду писать "{text}"!\n') * n)
#I
n = int(input())
m = int(input())
total = int(n * m / 2)
print(total)
#J
child_name = input()
child_cabinet = int(input())
group = int(child_cabinet // 10 // 10) 
cabinet = int(child_cabinet // 10 % 10) 
child_number = int(child_cabinet % 10)
bed = int(child_cabinet // 10 % 10 % 10) 
print(f"Группа №{group}.\n{child_number}. {child_name}.\nШкафчик: {child_cabinet}.\nКроватка: {bed}.")
#K
first = int(input())
number1 = str(first // 1000)
number2 = str(first // 100 % 10)
number3 = str(first // 10 % 10)
number4 = str(first % 10)
print(number2 + number1 + number4 + number3)
#L
first = int(input())
number1 = str(first // 1000)
number2 = str(first // 100 % 10)
number3 = str(first // 10 % 10)
number4 = str(first % 10)
print(number2 + number1 + number4 + number3)
#M
child_count = int(input())
sweet_count = int(input())
total = int(sweet_count // child_count)
total_end = int(sweet_count % child_count)
print(total)
print(total_end)
#N
red = int(input())
green = int(input())
blue = int(input())
total = int(red) + int(blue)
print(int(total + 1))
#O
n = int(input())
m = int(input())
t = int(input())
now_hours = int(n * 60)
now_time = int(now_hours + m)
end_time = int(now_time + t)
time_delivery_hours = int(end_time // 60 % 24)
time_delivery_min = int(end_time % 60 % 60)
if time_delivery_hours < 10 and time_delivery_min < 10:
    print(f"0{time_delivery_hours}:0{time_delivery_min}")
elif time_delivery_hours < 10 and time_delivery_min >= 10: 
    print(f"0{time_delivery_hours}:{time_delivery_min}")
elif time_delivery_hours >= 10 and time_delivery_min < 10:
    print(f"{time_delivery_hours}:0{time_delivery_min}")
else:
    print(f"{time_delivery_hours}:{time_delivery_min}")

#P
a = float(input())
b = float(input())
c = float(input())
distance = float(b) - float(a)
total = float(distance) / float(c) 
print("%.2f" % total)
#R
x = int(input())
y = int(input())
y2 = int(str(y), 2)
total = x + y2
print(total)
#S
x = int(input())
y = int(input())
x2 = int(str(x), 2)
total = y - x2
print(total)

#T

