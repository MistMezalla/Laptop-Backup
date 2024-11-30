import numpy as np
import numpy_financial as npf

# Note:-
'''
-> The newton-raphson method makes use of repeated derivatives to find the sol to a function.
-> See MIT's Intro to Algo(6.006) 
    -> Under this search for numerical analysis part(Karatsuba to find easily)
'''

# Cash flows based on the user's example
cash_flows = np.array([-8500000,	-494813,	802152,	2304810,	3430770,	4632756,	-1855887,	5821140,	7814708,	2486001,	7603695
])

cash_inflows = np.array([0,	2000000,	4730000,	7889185,	12212970,	16310220,	23563080,	26025120,	30760035,	36248450,	40643280

])

cash_outflows = np.array([8500000,	2494813,	3927848,	5584375,	8782199,	11677463,	25378534,	20166718,	22906392,	33849379,	33036629

])
# Calculate IRR using numpy_financial
irr = npf.irr(cash_flows)

# Convert IRR to percentage
irr_percentage = irr * 100

discount_rate = 3.5/100

# Calculate NPV using numpy_financial
npv = npf.npv(discount_rate, cash_flows)

# Calculate present value of inflows (benefits) and outflows (costs)
pv_inflows = npf.npv(discount_rate, cash_inflows)
pv_outflows = npf.npv(discount_rate, cash_outflows)

# Calculate Benefit-Cost Ratio (BCR)
bcr = pv_inflows / abs(pv_outflows)

# Print the result
print(f"The Internal Rate of Return (IRR) is approximately: {irr_percentage:.3f}%")
print(f"The Net Present Value (NPV) is: ₹{npv:.2f}")
print(f"The Benefit-Cost Ratio (BCR) at {discount_rate * 100:.0f}% discount rate is: {bcr:.6f}")


