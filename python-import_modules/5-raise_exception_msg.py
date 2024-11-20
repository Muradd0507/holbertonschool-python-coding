#!/usr/bin/python3
def raise_exception_msg(message = ""):
    if message == "C is fun":
        raise NameError("C is fun")
    else:
        print(message)
    return 0
