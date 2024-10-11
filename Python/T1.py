import numpy as np
import numpy_financial as npf

# Note:-
'''
-> The newton-raphson method makes use of repeated derivatives to find the sol to a function.
-> See MIT's Intro to Algo(6.006) 
    -> Under this search for numerical analysis part(Karatsuba to find easily)
'''

# Cash flows based on the user's example
cash_flows = np.array([-1000, 200, 200, 500, 500, 500])

# Calculate IRR using numpy_financial
irr = npf.irr(cash_flows)

# Convert IRR to percentage
irr_percentage = irr * 100

# Print the result
print(f"The Internal Rate of Return (IRR) is approximately: {irr_percentage:.2f}%")


