import json


def prob_13_12():
    st = input("Enter the string: ")
    words = st.split()
    d = {}

    for ch in words:
        key = ch
        if key not in d:
            cnt = words.count(ch)
            d[key] = cnt

    print(json.dumps(d, indent=4))


prob_13_12()
