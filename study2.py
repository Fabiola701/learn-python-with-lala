def add_sprinkles(func):
    def wrapper():
        print("*you add sprinkles🎊 *")
        func()
    return wrapper

def add_fudge(func):
    def wrapper():
        print("*you add fudge🍫 *")
        func()
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream():
    print("Here's your ice cream!🍨")

get_ice_cream()