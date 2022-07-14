# symbols used in conditional statements

"""
> - greater than
>= - greater than or equal to 

< - less than 
<= - less than or equal to 

== - equal to

!= - not equal to 
"""

x = int(input("What is x? "))
y = int(input("What is y? "))

if (x < y):
    print(f'{x} is less than {y}')

elif (x == y):
    print(f'{x} is equal to {y}')

elif (x > y):
    print(f'{x} is greater than {y}')
