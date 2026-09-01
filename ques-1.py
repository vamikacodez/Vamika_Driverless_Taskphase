''' Input an integer n, input n strings into a list. Create a dictionary where
the key is an alphabet and the value is how many times it appears across all
the strings. Not case sensitive. Eg for 
["Formula", "Manipal"] the output
looks like 
{'f':1, 'o':1, 'a':3 ...}'''

n = int(input("Enter an integer n: "))
l = []

for i in range(n):
    a=input("enter the string\n")
    l.append(a)

d = {}

for k in l:
    for ch in k.lower():
        if ch.isalpha():
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1

print(d)