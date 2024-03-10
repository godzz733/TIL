t = input()
if len(t[1:-1].strip()) == 0:
    print("CE")
else:
    print(t[1:-1] if t[0] == "\"" and t[-1] == "\"" else "CE")