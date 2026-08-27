# Using Built-in Modules and dir()

import math
import datetime

# Using functions from math module
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)
print("Power of 2^3:", math.pow(2, 3))

# Using datetime module
current_date = datetime.datetime.now()
print("Current Date and Time:", current_date)

# Display names available in math module
print("\nNames available in math module:")
print(dir(math))