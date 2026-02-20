'''

def Sum():
    a =int(input("input a: "))
    b =int(input("input b: "))
    #print ("Sum is: ",a+b)
    return a+b

Sum()
Sum()
Sum()
Sum()
A=Sum()

print(A)

def area_of_rectangle(length, width):
    
     return length * width
    

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

Area = area_of_rectangle(length, width)

print("The area of the rectangle is:", Area)

def greet(name, greeting = "Hello"):
    
    print(name + ", " + greeting + "!")

greet('Alzam')    

def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
print(sum(999))  '''


def sum(n):
    if n == 0:
        return 1
    else:
        
        for i in range(1, n+1):
            i += i
        return i
                    

result = sum(4)
print(result)	





                