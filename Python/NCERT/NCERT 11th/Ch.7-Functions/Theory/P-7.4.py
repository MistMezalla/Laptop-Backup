def sum_1st_n_numbers(n):
    sum_1=0
    for i in range (1,n+1):
        sum_1=sum_1+i
    print(sum_1)

sum_1st_n_numbers(int(input('Enter the number whose sum is to be found: ')))
