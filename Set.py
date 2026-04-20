set1={1,3,5,7,9}
set2={1,2,4,6,8}

set_u=set1.union(set2)
print(set_u)

set_int=set1.intersection(set2)
print(set_int)

set_diff=set1.difference(set2)
print(set_diff)

set1.add(11)
set2.remove(1)
print(set1 ,set2)