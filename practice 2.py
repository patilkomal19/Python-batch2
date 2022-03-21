from xml.dom.expatbuilder import theDOMImplementation


a = 30
b = 40
lower_value = a if a < b else b
#print(lower_value)
#print(id(a))
#print(id(b))

#print(a is b)

a = "komal patil"

#print("komal" in a)

x = 10
y = 20
#print(f"the sum of {x} and {y} is {x+y}")

#print("the sum of x and y is",x+y)

#x = eval(input("enter the list :" ))
#exp = 1
#for i in x:
 #   exp = i**2
 #   print(exp)  

x = eval(input("enter the list :" ))      #[1,2,3]
mul = 1
for i in x:
    mul = i*1

    print(mul)
