try:
    with open("abc.txt") as f:
        print(f.read())
except Exception as e:
    print(e)
        