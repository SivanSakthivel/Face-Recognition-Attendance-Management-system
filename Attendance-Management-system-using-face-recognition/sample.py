n=13
fis=1
sec=2
num=[1,2]
i=0

while(i<n):
    tot=fis+sec
    num.append(tot)
    fis=sec
    sec=tot
    i=tot
print(num)

count=0
for i in num:
    count=count+1
print(count)

num.reverse()
print(num)

for i in range(0,count):
    for j in range(0,i+1):
        print(num[i],end="")
    print()
