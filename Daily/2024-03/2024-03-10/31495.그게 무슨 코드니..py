t = input()
print(len(t.strip()))
# else:
print(t[1:-1] if t[0] == "\"" and t[-1] == "\"" else "CE")