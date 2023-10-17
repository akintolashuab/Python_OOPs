# The code below will crash the code thereby raising error but in the next code we can customize the error
# v = 10/0
# print(v) 

# try:
#     v = 10/0 # Division by Zero
#     my_list = [1,2,3]
#     my_list[3]
# except ZeroDivisionError:
#     print("ZeroDivisionError: You cannot divide a value by Zero")
# except IndexError:
#     print("IndexError: The index is out of range")

# To use the general class attribute error, that tells what happened without specification:
try:
    my_list = [1,2,y]
    v = 10/0 # Division by Zero
    my_list[3]
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide a value by Zero")
except IndexError:
    print("IndexError: The index is out of range")
except Exception as e:
    print("ValueError:", e)
finally:
    print("Done Checking for errors")
    
