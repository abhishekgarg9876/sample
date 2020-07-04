#hello this is change from git directly
p={1:["abhi",420,"garg"],2:["intern",789,"kaaam kro"]}

p.setdefault(3,["aaaabhi"]).append(-1)
print(p)

a=p.get(1)
print(a)

q=("qw",'er','ty')
a=0
b=p.fromkeys(q,a)
print(b)

a=p.pop(1)
print(a)
print(p)

a=p.values()
for i in a:
    for j in range(i.__len__()):
        print(i[j])

print('items-----',p.items())
print(p.keys())

p.update({8:"e"})
print(p)

p.popitem()
print(p)
