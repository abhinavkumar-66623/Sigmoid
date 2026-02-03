
# print("hello world")
# try:
#     print(10/0)
# except:
#     print("division not possible,continue ")


# print("hello world")

try:
    num1=int(input("Enter the num1: "))
    num2=int(input("Enter the num2: "))
    print(num1/num2)
except ZeroDivisionError:
    print("cannot divide")
except ValueError:
    print("please enter valid integer")
except:
    print("unexpected error")
finally:
    print("cleanup code")
print("code completed")
