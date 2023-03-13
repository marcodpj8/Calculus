# -*- coding: utf-8 -*-

import math as mt
from numpy import pi, abs

#sum of subsequent cubes

def f(x,y):    
  if x > y:
    return 0
  else:
    return x**3 + f(x+1, y)

#the same function using an internal function to do the sum

def F(x,y):    
  def g(x,y,z):
    if x > y:
      return z
    else:
      return g(x+1,y,(x**3)+z)
  return g(x,y,0)

print(f(2,6), F(2,6))

#approximation of pi using leibniz formula, the error depend by the size of n

def PI(n):      
  def sommapi(x,y):
    if x > y:
      return 0
    else:
      return 1/(x*(x+2)) + sommapi(x+4,y)
  return 8*(sommapi(1,n))

print(PI(100))

#writing a general function that can be used to define different types of sums

def sigma(x, y, F, Next):
    if x > y:
        return 0
    else:
        return F(x) + sigma(Next(x), y, F, Next)

#sum of subsequent cubes using sigma

def next(x):
    return x + 1
def cube(x):
    return x**3

def cubesum(x,y):
    return sigma(x, y, cube, next)

print(f(2,7), cubesum(2,7))

#approximation of pi with leibniz formula using sigma

def next1(x):
    return x + 4
def term(x):
    return 1/(x*(x+2))

def Leibnizformula(n):
    return 8*sigma(1, n, term, next1)

print(PI(1000), Leibnizformula(1000))

#we can use this concept to write a function that calculates the definite integral in a range[a,b]

def integral(a, b, F, dx = 0.01):
    def next(x):
        return x + dx
    def localarea(x):
        return F(x)*dx

    return sigma(a, b, localarea, next)     
        

print(integral(0, pi/2, mt.cos))

#3 different ways of calculating the square root of a number

#1 brute force, works only with perfect squares
# this function gives you an error if you ask it to calculate non perfect squares

def square(x):
    def rec(x,y):
        if y*y == x:
            return y
        else:
            return rec(x, y+1)
    if x < 0:
        return None
    elif x == 0:
        res = 0
    elif x == 1:
        res = 1
    else:
        res = rec(x, 2) 
    return res

    
print(square(16))

#2 defining a new function which calculates the square root of a number using bisection algorithm

def radicebisezione(x, eps=1e-7):
    def rec(a,b):
        c = (a+b)/2
        if abs(c*c -x) < eps:
            return c
        elif c*c > x:
            return rec(a,c)
        else:
            return rec(c,b)
    if x == 0:
        res = 0
    elif x == 1:
        res = 1
    elif x < 0:
        return None
    else:
        res = rec(1,x)
    return res
            
print(radicebisezione(-5)) 

#3 defining a function that calculates the square root of a number using newton algorithm
def newtonsquaret(x,eps=1e-7):
    def rec(y):
        z = 0.5*(y + (x/y))
        if abs(z*z -x) < eps:
            return z
        else:
            return rec(z)
    return rec(1)

print(newtonsquaret(25))

#finding the greatest common divisor using Euclid algorithm
def MCD(x,y):
    if x > y:
        r = x%y
        if r == 0:
            return y
        else:
            return MCD(r,y)
    else:
        r = y%x
        if r == 0:
            return x
        else:
            return MCD(r,x)


print(MCD(5,25))

#writing a function that calculates the factorial of a number using an iterative method
def fact(n):
    c = 1
    while n > 1:
        c = c*n
        n = n-1
    return c

print(fact(5))

#writing a function that calculates the factorial of a number using a recursive method

def factor(n):
    if n == 1:
        return 1
    else:
        return n*factor(n-1)

print(factor(5))

#writing a function that calculates the n-est term of fibonacci sequence using a recursive method

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))

#writing a function that calculates the n-est term of fibonacci sequence using an iterative method

def fib1(n):
    if n == 1 or n == 0:
        return 1
    else:
        c = 1
        d = 1
        i = 0
        while i < n-1:
            q = d
            d = c + d
            c = q
            i = i+1
        return d

print(fib1(2))

#defining a function that given two integers as imput calculates the exponential

def exp(b,n):
    c = b
    for i in range(0, n-1, 1):
        c = c*b
    return c

print(exp(2,3))
print(exp(4,3))

#defining the same function but using a recursive method

def expo(b,n):
    if n == 0:
        return 1
    else:
        return b*expo(b,n-1)

print(expo(2,3))
print(expo(4,3))

#defining a function that calculates the value of the n-est term of a sequence
#which is similar to fibonacci's one (f(n)=f(n-1)+2f(n-2)+3f(n-3)if n>=3 n if n<3)

#using a recursive method

def h(n):
    def rec(a,b,c,l):
        if l == n-2:
            return a
        else:
            return rec(a+2*b+3*c,a,b,l+1)
    if n < 3:
        return n
    else:
        return rec(2,1,0,0)

#same function

def g(n):
    if n < 3:
        return n
    else:
        return g(n-1)+2*g(n-2)+3*g(n-3)

print(h(5), g(6))

#the same function with an iterative method TO DO


#writing a function that calculates the average value of a list of numbers

def average(ls:list)->int:
    n = len(ls)
    c = 0
    for i in range(0, n, 1):
        c = c + ls[i]
    av = c/n
    return av

t = [10, 20, 10, 20, 10, 20]
print(average(t))

#writing a function that computes the standard deviation of a list of numbers

def standarddev(ls:list)->int:
    n = len(ls)
    u = average(ls)
    c = 0
    for i in range(0, n, 1):
        c = c + (ls[i]-u)**2
    z = mt.sqrt(c/n)
    return z

print(standarddev(t))



