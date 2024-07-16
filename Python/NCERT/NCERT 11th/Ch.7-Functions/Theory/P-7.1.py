h=float(input('Enter the height: '))
r=float(input('Enter the radius: '))
l=float(input('Enter the slant height: '))

area=(3.14*r*l)+(2*3.14*r*h)
print('Area of the canvas is ', area)

unit_price=float(input('Enter the unit price per m^2: '))
cost=area*unit_price
print(cost)

Total_cost=cost+(cost*18)/100
print('Net Payable amount is', Total_cost)
      
