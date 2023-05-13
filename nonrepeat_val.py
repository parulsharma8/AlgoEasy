
def nonrepeat_sval(name):
     res = dict()
     for i in range(len(name)):
          d = name[i]
          if d in res:
               res[d] = res[d] + 1
          else:
               res[d] = 1

     for i in range(len(name)):
          d = name[i]
          if res[d] == 1:
               return name[i]
     return -1

name = 'TTala'

print(nonrepeat_sval(name))