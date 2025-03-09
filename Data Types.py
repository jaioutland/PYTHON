# Literal
a = 9
b = 10
x = 12
y = 25
print("Literal:", x,y,a,b)
print("Nine - {a}, cannot live wihout {b} and {x} cannot live without {y}." .format(a=a,b=b,x=x,y=y))
print()

# Integer
y = 2
x = -2
a = 4
b = -4
print("Integer:", y,x,a,b)
print("A positive {2}, minus a negative {2} equals a positive{4} and negative {2} plus a negative {2} equals a negative {4}." .format(y,x,a,x,x,b))

# Float
z = 99.99
t = 89.90
x = 59.95
print("\nFloat:", z,t,x)
print("\nI saw three different color pairs of shoes I would like, the leopard print is {z}, the green is {t} and the red is {x}." .format(z=z,t=t,x=x))


# String
First_Name = "Jai"
Last_Name = "Outland"
print("How old are you?")
Age = "I will never tell"
print("\nMy age?", Age, end="!")
print("\nYou look like a teenager", end="!")
print("\nThanks! That's how I continue to look this way!")
print("\nBy never telling 🙂")

# Boolean
is_active = True
print("So, you're 27?,")
print("{},Exactly 👏!" .format(is_active))