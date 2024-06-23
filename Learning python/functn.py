# def greetHello(a):
#     while a in range (7):
#         print("Hello, how you doin?")
#         a+=1

# a= int(input("Enter a number: ") )

# greetHello(a)

# Following is a function that calculates averages of numbers in a list

list=[]
n=input("Enter the number of elements in the list: ")

for i in range(int(n)):
    list.append(int(input("Enter the number: ")))

def average(list):
    return sum(list)/int(n)

print("The average of the list is: ", average(list))
