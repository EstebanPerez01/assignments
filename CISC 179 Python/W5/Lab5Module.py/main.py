# Step 2 importing module contents from module.py file
import module

# Step 4 run print("id like to be a module") from this file

# Step 8 main.py file accesses moduile.py counter variable
print(module.counter)

# Step 10 code from step 9 in this module import
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

# step 11 & 12 append() is used in path.append('C:\\Users\\user\\py\\modules') to create a new path that directly
# looks into modules folder and imports module located in that file