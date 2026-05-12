
# def outer(name):
#     print(f"hello {name}  from the outer function")
#     def inner():
#         print(f"hello {name} from the inner function")
#     return inner

# result = outer("abdullahi")
# result()

def dec(func):
    print("this is the first time i'm called")
    def wrapper():
        func()
        print("this is the last time you will be called")
    return wrapper
@dec
def called_func():
    print("this is the decorated function")

called_func()

is_authenticated = False
def require_auth(my_func):
    def wrapper():
        if is_authenticated:
            my_func()
        else:
            print("you are denied to access")
    
    return wrapper


@require_auth
def acess_dash():
    print("you can access the dashboard now")

acess_dash()
