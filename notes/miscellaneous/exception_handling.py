# exception = an event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.exception, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero IDIOT!")
except ValueError:
    print("Enter a NUMBER!")
except Exception:                   # catches all exceptions but too broad and doesn't help with debugging
    print("Something went wrong!")
finally:                            # always executes no matter if there is exception or not
    print("Do some cleanup here.")