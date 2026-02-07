# a=(1,2,3)
# print(a)
# print(type(a))
# l=list(a)
# print(l)
# print(type(l))
# l.append(6)
# print(l)
# l.remove(3)
# l.remove(2)
# print(l)
# a=tuple(l)
# print(type(a))
# print(a)
# a=(1,2,(10,20,(300,400,500,(6000,7000,8000))))
# print(a[2][2][0])
# a=(1,2,[0,20,[300,400,500,(6000,7000,8000)]])
#print(a[2][2][0])
#print(a[2][2][2])
# print(type(a))
# l=list(a)
# print(l)
# l.remove(1)
# print(l)
# del l[2][2][1]      
# print(l[2][2][1])
# del l[2][2][1]
# print(l)
#packing the tuple
# t=(1,2,3,4,5)
# print(t)
#unpacking the tuple
# (a,b,c,d,e)=a
# print(a)
# (a,b,c)=a
# print(a)
# (*a, )=t
# print(a)
# b=(1,2,34,6,6,7)
# print(type(b))
# (a,*b,c)=b
# print(a)
# print(b)
# print(c)
# (a,b,c)=b too many values to unpack
# print(a)
# print(b)
# print(c)
# (a,b,c,d,e,f,g,h)=b` not enough values to unpack`
# print(a)
# s=("python")
# print(type(s)) the type wil be string because the by default it will consider it as string
# to make the the s to be of tuple data type then we need to put comm after the element inside the parenthesis
# s=("python",)
# print(s)
# print(type(s))
# print(s[0])
# if there is no nesting then there is no need to use ()parenthesis for tuple
s=1,2,3,4,[1,2,3]
print(type(s))
print(s[4][0])