# Lab 2 Quadratic Equation 

```python
#prompts users for inputs
a = float(input("value for a: "))
b = float(input("value for b: "))
c = float(input("value for c: "))

#function to solve quadratic equation
def solveQuadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    # If discriminant is positive we have 2 real roots
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return f"{root1} and {root2}"

    # if discriminant is zero we have 1 real root  
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"{root}"
    # if discriminant is negative we have two complex roots
    else:
        real = -b / (2 * a)
        imaginary = (-discriminant) ** 0.5 / (2 * a)
        return f"{real} + {imaginary}i and {real} - {imaginary}i"

#calls function to solve equation
result = solveQuadratic(a, b, c)

print(result)
``` 
## Graph and Explanation 
### a= -1 b= 5 c= 0
![Screenshot 2024-08-31 at 7 31 31 PM](https://github.com/user-attachments/assets/b32643ac-fa13-4283-8893-d1a172f8ffaf) 
The graph above shows a parabola with a downward opening due to coefficient a being negative, parabola intersects the x-axis at 0 and 5

## What happens when b & c inputs are negative? 

### Graph a= -1 b= -1 c = -1 & Explanation
![Screenshot 2024-08-31 at 7 41 46 PM](https://github.com/user-attachments/assets/57264114-3828-4fc9-bd1a-347db21322af)

Having a negative b input moves the entire parabola to the left side of the y-axis and up the y-axis as the negative input increases.
Having a negative c input moves the entire parabola down the y-axis 
