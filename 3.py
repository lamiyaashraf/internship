def shout(text):
    return text.upper()

print(shout('hello'))
yell = shout
print(yell('hello'))
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def greet(func):
    greeting= func("""hi, iam created by a function passed as an argument.""")
    print(greeting)
greet(shout)
greet(whisper)
def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_15=create_adder(15)
print(add_15(10))
def hello_decorator(func):
    def inner1():
        print("Hello,this is before function execution")
        func()
        print("this is after function execution")
        return inner1
        def function_to_be_used():
            print("this is inside the function!!")
function_to_be_used=hello_decorator("function_to_be_used")
function_to_be_used()



    
        