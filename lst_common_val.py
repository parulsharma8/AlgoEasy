def commonvalues(x,y):
     result = set()
     hashset = set()

     for i in range(len(x)):
          hashset.add(x[i])
     for j in range(len(y)):
          if y[j] in hashset:
               result.add(y[j])
     return result

x = [1,2,3,4,5,6]
y = [9,8,7,6,5]

print(commonvalues(x,y))