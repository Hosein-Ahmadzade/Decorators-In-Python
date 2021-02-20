# Decorators

"""

You remember @classmethod and @staticmetod in OOP. So, these are decorators  and decorators look like this. They have the @ and then some sort of name following it.

Let's talk about functions and why they're so powerful at first. Functions are what we call first class citizens in Python that is they can be passed around like variables, they can be an argument inside of a function. So they act just like variables. Look at the bottom examples (Line ***).

We created hello function and then passed it to greet variable and then we printed that (Line ). Note that if we passed just the name of our funtion to greet and then print that, we would get the location of the function in memory (Line ***). So in order to get the expect result, we should call our greet variable. Because it's not juat a variable. It's pointing to the location of hello function in memory and we can call it using brackets. 

Now, what if we delete hello with 'del' keyword? Well, if we call hello function with hello(), we'll get this error: NameError: name 'hello' is not defined. But if we call greet function with greet(), it works as well and we'll get the result. So why is that? So before line *** that we used del keyword and deleted hello, we can still call hello funcion with hello(), but after that, we said that delete this name reference to this function (Line ***) and because of this if we call the hello function it's not working. However because greet, a whole another variable is still pointing in memory to this function (Line **), so Python is smart enough to say, hey you told me to delete hello and I'll delete the name hello, but I'm not going to delete the function because greet is still pointing to it. 

So functions in Python act just like variables.

Now, What if we pass functions around inside of arguments? Look at the bottom example (Line ***).



"""


def hello():
    print("hellooooooooooo")


greet = hello()
print(greet)

greet1 = hello
print(greet1)
print(greet1())

del hello

# print(hello())
# NameError: name 'hello' is not defined

print(greet1())


def hello2(func):
    func()


def greeting():
    print('still here!')


a = hello2(greeting)
print(a)
