

tek = [1,3,5,7]
cift = [2,4,6,8]
tek2 = list()
cift2 = list()

for i in range(len(tek)):
    tek2.append(tek[i]*2)
    cift2.append(cift[i]*2)
    print(tek2[i], type(tek2[i]))
    print(cift2[i], type(cift2[i]))

print(tek2)
print(cift2)
 
print(type(tek2))
print(type(cift2))