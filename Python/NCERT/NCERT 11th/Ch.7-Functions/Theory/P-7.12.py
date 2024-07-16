def right_circular_cone(r,h):
    l=((r**2)+(h**2))**0.5

    CSA=3.14*r*l
    SA=CSA+(3.14*r*r)
    Vol=(3.14*r*r*h)/3
    
    return(CSA,SA,Vol)

radius=float(input('Enter the radius: '))
height=float(input('enter the height: '))

CSA,SA,Vol=right_circular_cone(radius,height)

print(CSA)
print(SA)
print(Vol)


