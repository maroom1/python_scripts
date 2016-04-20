cmd = raw_input("Type of the operrations (+/-):")
if cmd == "+":
        print("Addition")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first + secund
        print result
elif cmd == "-":
        print("Subtraction")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first - secund
        print result
else:
        print("Quit!")
       