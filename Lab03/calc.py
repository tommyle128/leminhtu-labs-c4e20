x = int(input("x = "))

op = input("Operation: +,-,*,/:")

y = int(input("y = "))
if op == "+":
    res = x + y
elif op == "-":
    res = x - y
elif op == "*":
    res = x * y
elif op == "/":
    res = x / y

print('*' *10)
print("{} {} {} = {}".format(x, op, y, res))
print('*' *10)
