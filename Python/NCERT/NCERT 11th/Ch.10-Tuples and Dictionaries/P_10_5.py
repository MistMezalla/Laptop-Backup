ODD={1:'one',3:'three',5:'five',7:'seven',9:'nine'}

ODD.keys()
print(ODD)

ODD.values()
print(ODD)

ODD.items()
print(ODD)

print(len(ODD))

print(7 in ODD)
print(2 in ODD)

print(ODD.get(9))
del ODD[9]
print(ODD)
