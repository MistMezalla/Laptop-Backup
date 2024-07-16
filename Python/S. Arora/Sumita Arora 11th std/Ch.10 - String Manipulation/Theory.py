def prob_10_3():
    n = int(input("Enter the number: "))
    s = str(n)
    '''
    for ch in s:
        if (ch == '0'):
            print("Present")
        else :
            print("Absent")
    '''
    # Better Code
    if '0' in s:
        print("Present")
    else:
        print("Absent")


def solv_prob_11():
    st = input("Enter the string: ")
    st.lower()
    vow = 'aeiouAEIOU'
    sub1 = []
    sub2 = []
    for ch in st:
        if ch not in vow:
            sub1.append(ch)
        else:
            if len(sub1) >= len(sub2):
                sub1, sub2 = sub2, sub1
                sub1 = []

    return sub2


# prob_10_3()
for ch in solv_prob_11():
    print(ch, end='')
