ظظ  # Decorators

"""

You remember @classmethod and @staticmetod in OOP. So, these are decorators  and decorators look like this. They have the @ and then some sort of name following it.

Let's talk about functions and why they're so powerful at first. Functions are what we call first class citizens in Python that is they can be passed around like variables, they can be an argument inside of a function. So they act just like variables. Look at the bottom examples (Line 28).

We created hello function and then passed it to greet variable and then we printed that (Lines 32 and 33). Note that if we passed just the name of our funtion to greet1 and then print that, we would get the location of the function in memory (Lines 35 and 36). So in order to get the expect result, we should call our greet1 variable. Because it's not juat a variable. It's pointing to the location of hello function in memory and we can call it using brackets. 

Now, what if we delete hello1 with 'del' keyword? Well, if we call hello function with hello1(), we'll get this error: NameError: name 'hello1' is not defined. But if we call greet function with greet2, it works as well and we'll get the result. So why is that? So before line 48 that we used del keyword and deleted hello1, we can still call hello1 funcion with hello1(), but after that, we said that delete this name reference to this function (Line 48) and because of this if we call the hello1 function it's not working. However because greet2, a whole another variable is still pointing in memory to this function (Line 44), so Python is smart enough to say, hey you told me to delete hello and I'll delete the name hello, but I'm not going to delete the function because greet is still pointing to it. 

So functions in Python act just like variables.

Now, What if we pass functions around inside of arguments? Look at the bottom example (Line 56).  This hello2 function receives another function that calls that function. So we can create a greeting function that prints 'still here!' and then if we call hello2 function with greeting like this (Line 64) and then pass it to 'a' variable, when we print that variable, we'll see that still works. Because what happens is we say, hey call the function hello2 with argument greeting. So hello2 function calls greeting function inside itself. And we get 'still here!'. 

Decorators are only possible because of these features above. This ability fo functions to act like variables, act like first class citizens in Python. Decorators are using this power of functions.

Decorators supercharge our functions. By adding some sort of decorator we can supercharge our function and add extra functionality to it.

@decorator
def func():
    pass

"""


def hello():
    print("hellooooooooooo")


greet = hello()
print(greet)

greet1 = hello
print(greet1)
print(greet1())


def hello1():
    print("hello.")


greet2 = hello1()

print(hello1())

del hello1

# print(hello1())
# NameError: name 'hello1' is not defined

print(greet2)


def hello2(func):
    func()


def greeting():
    print('still here!')


a = hello2(greeting)
print(a)


print("########################################")


# Higher Order Functions (HOC):

"""

We have to understand this idea of higher order function, that is HOC for short. 

A higher order function can be one of two things. It could either be a function like goodbye that accepts another function. So this goodbye function is a higher order function. It's a function that accepts inside of it's parameters another function (Line 84). Or it could be a function like bye function that returns another function. So this bye function is a higher order function too (Line 88).

So a higher order function is any function that either accepts a function as a parameter or returns a function. For example map(), filter() and reduce() are higher order functions. Because they accept a function as a parameter.

"""


def goodbye(func):
    func()


def bye():
    def func():
        return 5
    return func


print("########################################")
