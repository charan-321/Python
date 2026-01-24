'''a=0o10;
print(a);
print(type(a));
e=bin(a);
print(e);
b=0x1A;
print(b);
print(type(b));
c=0b1101;
print(c);
print(type(c));
d=12345678;
print(d);
print(type(d));
a=10;
b=20;
print(a+b);#arithmetic operator
if a>=b:# comparison operator
    print("true");
else:
    print("false");
# assignment operator
a=5;
b=3;
b-=3;
print(b);
print(a);
a=1000;
b=20;
if a and b:
    print("true");
else:
    print("false");
a=1000; bitwise operator
b=20;
if a & b:
    print("true");
else:
    print("false");
a=[10,20,30]; membership operator
if 30 in a:
    print("true");
else:
    print("false");'''
a=["hi","hey","hello"];
b=["hi","hey","how are you??"];
if a is b:
    print("true");
else:
    print("false");
