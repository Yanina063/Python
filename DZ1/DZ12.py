#Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = input('x - ').lower() == "true"
y = input('y - ').lower() == "true"
z = input('z - ').lower() == "true"

print("----------------------")

print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))

leftResult = not (x and y and z)
rigthResult = not x or not y or not z 

print("----------------------")

print("leftResult = " + str(leftResult))
print("rigthResult = " + str(rigthResult))