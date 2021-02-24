from time import time

# Decorators

"""

You remember @classmethod and @staticmetod in OOP. So, these are decorators  and decorators look like this. They have the @ and then some sort of name following it.

Let's talk about functions and why they're so powerful at first. Functions are what we call first class citizens in Python that is they can be passed around like variables, they can be an argument inside of a function. So they act just like variables. Look at the bottom examples (Line 30).

We created hello function and then passed it to greet variable and then we printed that (Lines 34 and 33). Note that if we passed just the name of our funtion to greet1 and then print that, we would get the location of the function in memory (Lines 37 and 38). So in order to get the expect result, we should call our greet1 variable. Because it's not juat a variable. It's pointing to the location of hello function in memory and we can call it using brackets. 

Now, what if we delete hello1 with 'del' keyword? Well, if we call hello function with hello1(), we'll get this error: NameError: name 'hello1' is not defined. But if we call greet function with greet2, it works as well and we'll get the result. So why is that? So before line 50 that we used del keyword and deleted hello1, we can still call hello1 funcion with hello1(), but after that, we said that delete this name reference to this function (Line 50) and because of this if we call the hello1 function it's not working. However because greet2, a whole another variable is still pointing in memory to this function (Line 46), so Python is smart enough to say, hey you told me to delete hello and I'll delete the name hello, but I'm not going to delete the function because greet is still pointing to it. 

So functions in Python act just like variables.

Now, What if we pass functions around inside of arguments? Look at the bottom example (Line 58).  This hello2 function receives another function that calls that function. So we can create a greeting function that prints 'still here!' and then if we call hello2 function with greeting like this (Line 66) and then pass it to 'a' variable, when we print that variable, we'll see that still works. Because what happens is we say, hey call the function hello2 with argument greeting. So hello2 function calls greeting function inside itself. And we get 'still here!'. 

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

A higher order function can be one of two things. It could either be a function like goodbye that accepts another function. So this goodbye function is a higher order function. It's a function that accepts inside of it's parameters another function (Line 86). Or it could be a function like bye function that returns another function. So this bye function is a higher order function too (Line 90).

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

Let's define my_decorator and this decorator is going to accept a functionl and we know that, this is a higher order function. Now inside of our function (my_decorator), we're going to call the function that we accept (func). But before we do that we're actually going to wrap this function (func) in another function (wrap_func). And this wrap_func is going to be a function that simply runs or let's say calls this func. And then finally we'll just return wrap_func (Line 138). And notice this here, we're not calling wrap_func. We're just returning it so that later on somebody can use it. 

Now let's say we have a simple like say_hello fucntion that just prints "hello!". Now why is this (my_decorator) useful? Because now, we can use this (my_decorator) as decorator. Python as soon as we write an @ in front of this is going to say, hey this is going to be a decorator and the decorator as long as we follow this syntax (Lines 135 to 138) of accepting  a function, having a wrapper function, calling the function and then returning the wrapper function can be used.


Syntax:

def my_decorator(func):
    def wrap_func():
        func()
    return wrap_func


So if we say @my_decorator (line 141). and then cut and then past the definition of say_hello function after it (@my_decorator). So if we want to use a decorator on a function, we should define that fucntion just after that line that we wrote our decorator (Line 142). So now if we run the program we'll see that it returns 'hello!'. So this is a complete waste of time. Why did we have to all of that? We could just comment Line 135 to 137 and just runs this (Define and the call say_hello function). Well, what we just did with the decorator, hasn't changed anything. It works exactly as expected but what it allows us to do is that now we can add extra functionality. Remember how we said that decorators are functions like my_decorator that wraps another function and enhances it. So how we can enhance say_hello fucntion?

Well, we can do anything inside of this wrap function (wrap_func), for example we can say print some @ before and after calling the function that we gave to our decorator (my_decorator1) and if we run the program, we get this (Line 164) and we've just super boosted our say_hello1 function. And this is why decorators are are useful by just adding this one line (@my_decorator1 (Line 158)) we're able to super boost a function.

Now if create another fucntion that is goodnight and this goodnight is going to print "have a good night:)". If we define this function just after our say_hello2 and then call the function. We'll see that nothing changes. Because if we want to super boost this function too, we should use (@my_decorator3 (Line 208)) before defining our goodnight1 function just like say_hello3 function. Now if we call goodnight1 function, we'll see that we have super boosted this function just like say_hello3 function.

So this is the power of decorators. By just using this syntax we can add extra functionality ot other functions.

So how does Python interpreter do all of this?

Well, all we're doing is that we're wrapping our say_hello4 funcion with our my_decorator3 and then assigning it to "b" variable (Lines 232 and 233). It's the same as doing something like this (Line 235). We simply call it again.

Now the reason decorators are useful is because instead of doing like this (Lines 232 and 233 or 235), we can just add the for example @my_decorator3 before defining the function and we don't need to do all of this. Our function get automativally wrapped by our decorator. But essentially this is what the @ is doing.

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


"""

What if we have a decorator like above that is our_decorator and also have a function that is bell function that took a parameter (Like string)? Well, if we run this just like this (Lines 270 to 284), we'll get this error: TypeError: bell() missing 1 required positional argument: 'sound'. How can we make this allow arguments? When we call bell function, It says bell() missing 1 required positional argument that is sound argument. And actually when we call bell function, we're expecting to heve a parameter, but here (Line 273) that we call func in wrap_func function, we're not giving it any parameters. 


We can just simply add a parameter to our func (Line 290) and then our wrap_func function receives the parameter (Line 288). And now if we run bell1 function we get an error that says: TypeError: wrap_func() missing 1 required positional argument: 'x'. So now what we should do for solving this?

Well, we should just give the function a sound like 'jingle' when we call it (Line 309). Now if we click run it works. 

We're calling bell2 with 'jingle'. So this func (bell2) gets passed to our decorator (our_decorator1) and then we receive the x as argument. For better understanding look at these two lines (Line 316 and Line 317). So our decorator above works just like this. So like this the wrap_func accepts the parameter and then runs the func function.

What if our function (bell4) had an emoji that it accepts? Well we should create another parameter y and pass it to func and wrapp_func function just like x (Lines 321 and 323). And if we run this it works but this is hectic. Every time we need to change parameters in our function, we have to modify these two function (func and wrap_func) and What if we had a function bell5 that gets a keyword arguments like default emoji ("📣") (Line 337)? And now if we run this we get this error: TypeError: wrap_func() missing 1 required positional argument: 'y'. So now what should we do for solving these problems? Well, theer's actually a pattern here that we can use that makes thing really really simple for us. And it's this syntax:


Decorator Pattern: 

def decorator(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func


We should define our wrap_function that gets*args that it takes all positional arguments and then **kwargs that it takes all keyword arguments. And we call the function by saying func(*args, **kwargs) to unpack all the positional and keyword arguments. And now if we define a function like bell6 and then give it a keyword argument like emoji = "📣" and then call the function with and without emoji parameter, it works as well without any errors in both cases. 

So this decorator pattern gives our decorators flexibility. So that we're able to pass as many arguments as we want into our wrap_func by using *args and **kwargs and then unpacking them inside of a function (func). And this pattern or let's say this syntax is why decorators are so powerful.

"""


def our_decorator(func):
    def wrap_func():
        print("*************")
        func()
        print("*************")
    return wrap_func


@our_decorator
def bell(sound):
    print(sound)


# bell()
# TypeError: bell() missing 1 required positional argument: 'sound'


def our_decorator1(func):
    def wrap_func(x):
        print("*************")
        func(x)
        print("*************")
    return wrap_func


@our_decorator1
def bell1(sound):
    print(sound)


# bell1()
# TypeError: wrap_func() missing 1 required positional argument: 'x'


@our_decorator1
def bell2(sound):
    print(sound)


bell2("jingle")


def bell3(sound):
    print(sound)


c = our_decorator1(bell3)
c("jingle")


def our_decorator2(func):
    def wrap_func(x, y):
        print("*************")
        func(x, y)
        print("*************")
    return wrap_func


@our_decorator2
def bell4(sound, emoji):
    print(sound, emoji)


bell4("jingle", '🔔')


@our_decorator2
def bell5(sound, emoji="📣"):
    print(sound, emoji)


# bell4("jingle")
# TypeError: wrap_func() missing 1 required positional argument: 'y'


def our_decorator3(func):
    def wrap_func(*args, **kwargs):
        print("*************")
        func(*args, **kwargs)
        print("*************")
    return wrap_func


@our_decorator3
def bell6(sound, emoji="📣"):
    print(sound, emoji)


bell6("jingle", '🔔')
bell6("jingle")


print("########################################")


"""

Why do we need decorators?

Lets's talk about some of the practical application of decorators. 

We already seen them in classes. We saw how @classmethod and @staticmethod were able to create class methods and static methods on the class.

An example of a decorator:

We're going to create our own decorator. We want to create a performance decorator. This decorator can be used during testing our code, to see how fast our code runs.

We define a long_time function that takes a long time to complete. So we wnat to know how seconds it takes to be completed.

First we should do that is about modules and built in modules. So we're going to import from the time module, something called time (Line 1 -> from time import time).

Now we're going to create our decorator following the pattern that we've learned. 

Now we want to calculate from the beginning of running this function  to the end of running this function. So we can use time module to do this. For doing this, we create a variable t1 (initial time) and then equals it to time() and then we call our function and after that we create another variable t2 and then equals it to time() again. And at the end, we returned t2 - t1 that tells us the time difference (returns by second) between before and after running the function and it actually tells us how long our function took to run. 

So now we give our funcion different numbers and then we see the time diffrences among them.

Note that this performance decorator depends on the machine and how fast our CPU and memory are on our computer.

"""


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        return f"It took {t2 - t1} seconds!"
    return wrapper


@performance
def long_time(num):
    for i in range(num):
        pass
    return True


print(long_time(100000))
print(long_time(1000000))
print(long_time(10000000))
print(long_time(100000000))
print(long_time(1000000000))


print("########################################")


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:


"""

Note that in line 439 we used args[0]["valid"] instead of args["valid"]. So why we did this? Well, we passed user1 to our function that is a dictionary but because we used *args inside of our wrapper function, args is a tuple right now or it's better to say it is a tuple of dictionaries now. So if we say args["valid"], it returns error and for getting the value of valid key we should do this (args[0]["valid"]).

So remember that if we pass *arags to our function, it convert it to tuple just like this example(Lines 427 to 431).

def test_args(*args):
    print(args)

test_args({"key": 54}, 47, [45, 8, 9])
({'key': 54}, 47, [45, 8, 9])

"""


user1 = {
    'name': 'Sorna',
    'valid': True
}


# changing this will either run or not run the message_friends function (Lines 459 and 461).


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"] == True:
            fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

user1['valid'] = False

message_friends(user1)


print("########################################")
