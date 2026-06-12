"""
This is an example of Bad design that violates OCP.
We alter a core class every time new requirements are introduced.
Here is a discount system; every time you add a new customer_type shows up, 
we need to edit the same function.

Note: Use of if-else statements is a common sign of OCP violation, 
as it often indicates that the code is not designed to accommodate new functionality without modification.
"""

def calculate_price(price,customer_type):
    if customer_type == "regular":
        return price * 0.9
    elif customer_type == "premium":
        return price * 0.8
    elif customer_type == "vip":
        return price * 0.5
    
# Consider, a new coustomer type: "first_timer" is added, we need to add another elif clause and edit the same function again, which violates OCP.
'''
    elif customer_type == "first_timer":
        return price 
'''
# This clearly violates OCP: new discount ⇒ modify this function and redeploy it.


