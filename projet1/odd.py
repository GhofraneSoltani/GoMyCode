str="ghofrane"
res="" 
i=0
for i in range(0,len(str)):
    if i % 2 == 0:
      res = res + str[i]

print(res)