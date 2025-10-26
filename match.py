# match function
# match expression:
# case x:
#   code block
# case y:
#   code block:
# case z:
#   code block:

day = int(input("enter the day: "))
match day: 
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Looking forward for the holidays")
