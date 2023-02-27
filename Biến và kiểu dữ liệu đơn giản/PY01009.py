s = input()
lw, up = 0, 0
for i in range(len(s)):
    if s[i].islower(): lw += 1
    else: up += 1
print(s.lower()) if lw >= up else print(s.upper())