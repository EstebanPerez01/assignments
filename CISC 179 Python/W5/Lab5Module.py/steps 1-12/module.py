# Step 3 simple print cript that can be run from both files
print("id like to be a module")
#
# # Step 5 __name__ variable prints source file
print(__name__)

# Step 6 __main___ variable used to test/check where the code has been activated
if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

# Step 7 function that prints different strings depending on the source file the code is executed on
counter = 0

if __name__ == "__main__":
    print("I prefer to be a module.")
else:
    print("I like to be a module.")

# Step 9 Code to be used for module in step 10
#!/usr/bin/env python3 (This comment specifically instructs unix and unix-like OS's like MacOS how to execute content, without this line there can be problems

""" module.py - an example of a Python module """
__counter = 0

def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)