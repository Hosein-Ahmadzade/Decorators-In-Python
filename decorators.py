# Decorators

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


"""

Writing our own decorators:

Remember a decorator super charges our function. It's simply a function that wraps another function and enhances it or changes it.

Let's define my_decorator and this decorator is going to accept a functionl and we know that, this is a higher order function. Now inside of our function (my_decorator), we're going to call the function that we accept (func). But before we do that we're actually going to wrap this function (func) in another function (wrap_func). And this wrap_func is going to be a function that simply runs or let's say calls this func. And then finally we'll just return wrap_func (Line 136). And notice this here, we're not calling wrap_func. We're just returning it so that later on somebody can use it. 

Now let's say we have a simple like say_hello fucntion that just prints "hello!". Now why is this (my_decorator) useful? Because now, we can use this (my_decorator) as decorator. Python as soon as we write an @ in front of this is going to say, hey this is going to be a decorator and the decorator as long as we follow this syntax (Lines 133 to 136) of accepting  a function, having a wrapper function, calling the function and then returning the wrapper function can be used.


Syntax:

def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func


So if we say @my_decorator (line 139). and then cut and then past the definition of say_hello function after it (@my_decorator). So if we want to use a decorator on a function, we should define that fucntion just after that line that we wrote our decorator (Line 140). So now if we run the program we'll see that it returns 'hello!'. So this is a complete waste of time. Why did we have to all of that? We could just comment Line 133 to 136 and just runs this (Define and the call say_hello function). Well, what we just did with the decorator, hasn't changed anything. It works exactly as expected but what it allows us to do is that now we can add extra functionality. Remember how we said that decorators are functions like my_decorator that wraps another function and enhances it. So how we can enhance say_hello fucntion?

Well, we can do anything inside of this wrap function (wrap_func), for example we can say print some @ before and after calling the function that we gave to our decorator (my_decorator1) and if we run the program, we get this (Line 162) and we've just super boosted our say_hello1 function. And this is why decorators are are useful by just adding this one line (@my_decorator1 (Line 156)) we're able to super boost a function.

Now if create another fucntion that is goodnight and this goodnight is going to print "have a good night:)". If we define this function just after our say_hello2 and then call the function. We'll see that nothing changes. Because if we want to super boost this function too, we should use (@my_decorator3 (Line 206)) before defining our goodnight1 function just like say_hello3 function. Now if we call goodnight1 function, we'll see that we have super boosted this function just like say_hello3 function.

So this is the power of decorators. By just using this syntax we can add extra functionality ot other functions.

So how does Python interpreter do all of this?

Well, all we're doing is that we're wrapping our say_hello4 funcion with our my_decorator3 and then assigning it to "b" variable (Lines 230 and 231). It's the same as doing something like this (Line 233). We simply call it again.

Now the reason decorators are useful is because instead of doing like this (Lines 230 and 231 or 233), we can just add the for example @my_decorator3 before defining the function and we don't need to do all of this. Our function get automativally wrapped by our decorator. But essentially this is what the @ is doing.

"""


def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func


@my_decorator
def say_hello():
    print("hello!")


say_hello()
# hello!


def my_decorator1(func):
    def wrap_func():
        print("@@@@@@@@@@@@@@@@@@@")
        func()
        print("@@@@@@@@@@@@@@@@@@@")
    return wrap_func


@my_decorator1
def say_hello1():
    print("hello1!")


say_hello1()
# @@@@@@@@@@@@@@@@@@@
# hello1!
# @@@@@@@@@@@@@@@@@@@


def my_decorator2(func):
    def wrap_func():
        print("@@@@@@@@@@@@@@@@@@@")
        func()
        print("@@@@@@@@@@@@@@@@@@@")
    return wrap_func


@my_decorator2
def say_hello2():
    print("hello2!")


def goodnight():
    print("have a good night:)")


say_hello2()
# @@@@@@@@@@@@@@@@@@@
# hello2!
# @@@@@@@@@@@@@@@@@@@

goodnight()
# have a good night:)


def my_decorator3(func):
    def wrap_func():
        print("@@@@@@@@@@@@@@@@@@@")
        func()
        print("@@@@@@@@@@@@@@@@@@@")
    return wrap_func


@my_decorator3
def say_hello3():
    print("hello3!")


@my_decorator3
def goodnight1():
    print("have a good night:)._.")


say_hello3()
# @@@@@@@@@@@@@@@@@@@
# hello3!
# @@@@@@@@@@@@@@@@@@@

goodnight1()
# @@@@@@@@@@@@@@@@@@@
# have a good night:)._.
# @@@@@@@@@@@@@@@@@@@


def say_hello4():
    print("hello4!")


def goodnight2():
    print("have a good night:)(:")


b = my_decorator3(say_hello4)
b()

my_decorator3(goodnight2)()


print("########################################")
