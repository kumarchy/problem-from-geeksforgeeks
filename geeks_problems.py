# def add():
#     a=int(input("enter any no."))
#     b=int(input("enter any no."))
#     c=a+b
#     print("the value is:",c)
# add()

#next for factorial of number
# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1);
# num=5;
# print("factorial of ",num,"is",factorial(num))


#next#

# def factorial(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         fact=1
#         while(n>1):
#             fact*=n
#             n-=1
#         return fact
# num=5;
# print("factorial of ",num,"is",factorial(num))
        
#next#

# n=int(input("enter the any for factorial :"))
# factorial=1
# for i in range(1,n):
#     factorial*=n
#     n-=1
# print(factorial)


#next#
# def factorial(n):
#     res=1
#     for  i in range(2,n+1):
#         res*=i
#     return res
# num=5
# print("factorial of ",num,"is",factorial(num))

#--------------------------------------------------------

# def factorial(n):
#     if n<0:
#         return 0
#     elif n==0 or n==1:
#         return 1
#     else:
#         fact=1
#         while(n>1):
#             fact*=n
#             n-=1
#         return fact
# num=5
# print("factorial of",num ,"is ",factorial(num))

# next
# def factorial(n):
#     res=1
#     for i in range(2,n+1):
#         res*=i
#     return res
# num=int(input("enter the number:"))
# print("factorial  of ",num,"is",factorial(num))

# next
# def factorial(n):
#     return 1 if (n==1 or n==0) else n*factorial(n-1)
# num=5
# print("factorial of ",num,"is",factorial(num))

# next
# import math
# def factorial(n):
#     return (math.factorial(n))
# num=5
# print("factorial of",num,"is",factorial(num))


# next for simple interest
# def simple_interest(p,t,r):
#     print("the principle is :",p)
#     print("the time is:",t)
#     print("the rate is:",r)
#     si=(p*t*r)/100
#     print("the simple interest is:",si)
    
# simple_interest(8,6,8)


# next for compound interest

# def  compound_interest(principle,rate,time):
#     amount=principle*(pow((1+rate/100),time))
#     CI=amount-principle
#     print("compound interest is",CI)
# compound_interest(10000,10.25,5)

# next
# p=1200
# t=2
# r=5.4
# a=p*(1+(r/100))**t
# ci=a-p
# print(ci)

# next to find the armstrong number

# n=153
# s=n
# b=len(str(n))
# sum1=0
# while n!=0:
#     r=n%10
#     sum1=sum1+(r **b)
#     n=n//10
# if s==sum1:
#     print("the given number",s,"is armstrong number")
# else:
#     print("the given number",s,"is not armstrong number")


# next
# def findArea(r):
#     pi=3.14
#     return pi*r*r
# print("area is ",findArea(5))

# import math
# def area(r):
#     area=math.pi*(pow(r,2))
#     print("area of circle is :",area)
# area(4)

# next

# def Fibonacci(n):
#     if n<=0:
#         print("incorrect input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# print(Fibonacci(10))


# next

# FibArray=[0,1]
# def fibonacci(n):
#     if n<0:
#         print("incorrect input")
#     elif n<=len(FibArray):
#         return FibArray[n-1]
#     else:
#         temp_fib=fibonacci(n-1)+fibonacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib
# print(fibonacci(9))


# next
# def fibonacci(n):
#     if n<=0:
#         return "incorrect output"
#     data=[0,1]
#     if n>2:
#         for i in range(2,n):
#             data.append(data[i-1]+data[i-2])
#     return data[n-1]
# print(fibonacci(10))

#next#

# c='g'
# print("The ASCII value of '" + c+"' is",ord(c))

#next#
# print("enter a string :",end="")
# text=input()
# textlength=len(text)
# for char in text:
#     ascii=ord(char)
#     print(char,"\t",ascii)


#next for sum of square of natural no.#

# n=int(input("enter  a number :"))
# x=0
# for i in range(1,n+1):
#     s=i**2
#     x+=s
# print(x)
   
#for cube of sum of natural no.
# n=int(input("enter  a number :"))
# x=0
# for i in range(1,n+1):
#     s=i**3
#     x+=s
# print(x)
   
    
#next#
# n=int(input("enter the no.:"))
# s=0
# for i in range(1,n+1):
#     s=s+pow(i,3)
# print(s)

#next python program to find position of n'th multiple of a number k in fibonacci series

def findposition(k,n):
    f1=0
    f2=1
    i=2
    while i!=0:
        f3=f1+f2
        f1=f2
        f2=f3
        if f2%k==0:
            return n*i
        i+=1
    return 
n=5
k=4
print("position of n\'th multiple of k in ""fibonacci series is",findposition(k,n))
