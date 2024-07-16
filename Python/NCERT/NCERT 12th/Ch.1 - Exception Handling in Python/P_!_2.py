try:
    num = int(input('Enter a number: '))
    print(num**2)
    #print("11"+num)
    print(num % 2)

except Exception as e :
    print(type(e).__name__,": plz enter int data type.")
    print(e, ": plz enter int data type.")
    print("Exception type: ",type(e).__name__)

finally:
    print("Its is default statement exe regardless of errors raised of any kind. Subsequent statements won't be exe be inside try block or after finally")

print("heelo")
