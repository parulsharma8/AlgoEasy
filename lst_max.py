def maximum(lst):
     x = -100000000000000
     for i in range(0, len(lst)):
         if x < lst[i]:
             x = lst[i]
     return x

lst =[1,3,4,5,6,7,13,16,-10]
print(maximum(lst))