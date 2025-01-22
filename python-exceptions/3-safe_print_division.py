#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b

    except ZeroDivisionError:
        result = None

    finally:
        if result is None:
            print("Inside the result: None")
        else:
            print("Inside the result: {:.2f}".format(result))
    return result
