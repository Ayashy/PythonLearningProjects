print("Welcome to Pythagorean Triple app !! ")

a=int(input("Enter the first triangle side"))
b=int(input("Enter the second triangle side"))
c=int(input("Enter the third triangle side"))

list=[a,b,c]
m=max(list)
list.remove(m)
if m^2 == list[0]^2+list[1]^2:
    print("The triangle is Pythagorean ")
else:
    print("The triangle is not Pythagorean ")