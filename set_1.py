# s={10,20,30,10,20,10,30,10,40}
# print(s)
# print(type(s))
# print(len(s))
# s.add(50)
# print(s)
# s.discard(50)
# print(s)
# s.remove(30)
# print(s)
#update is used to add a set into another set...
# s1={"hi","hello","welcome"}
# s.update(s1)
# print(s)
#METHODS IN SETS
#using index to change the value in a set
t={1,2,3,4,5}
# print(t)
# t[3]=6
# print(t)
#using index changing the value is not possible
#union
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# c=a.union(b)
# print(c)
# print(a.union(b))
# intersection
# print(a)
# print(b)
# c=a.intersection(b)
# print(c)
#intersection update
# c=a.intersection_update(b)
# print(c)
#pop()- can remove any element from the set
# d=a.pop()
# print(d)
# print(a)
#symmetric difference-elements which are not in common will only be displayed
# s={1,2,3,4,5}
# t={4,5,6,7,8}
# d=s.symmetric_difference(t)
# print(d)
# e=s.difference(t)
# print(e)
# s={11,22,33,44,55,66,77,88,99}
# t={22,44,66,88,110,132}
# x=s-t
# print(x)
# y=t-s
# print(y)
# d=s&t
# print(d)
# e=s | t
# print(e)
p={1,2,3,4,5}
q={3,2,5,4,1}
r={4,5,6,7,8}
# if(p==q):
#     print("p and q are equal")
# else:
#     print("p and q are not equal")
# if(p==r):
#     print("p and r are equal")
# else:
#     print("p and r are not equal")
y={1,2,3,4}
y=y | {5}
print(y)