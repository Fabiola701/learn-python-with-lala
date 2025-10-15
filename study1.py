def add_sprinkles(cake):
    return cake + " with sprinkles"

def add_icing(cake):
    return cake + " with icing"
def add_chocolate(cake):
    return cake + " with chocolate"


@add_sprinkles
@add_icing
@add_chocolate
def make_cake():
    cake = "cake"
    cake = add_sprinkles(cake)
    cake = add_icing(cake)
    cake = add_chocolate(cake)
    return cake

make_cake()