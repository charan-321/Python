#i=1
# j=2
# print(i)
# print(j)
# while(i>=0):
#     print(i)
#     if(i%2==0):
#         print("not possible")
#     else:
#         print(i*j)
# else:
#     print(" ")
# i=1
# while(i<4):
#     print(i) for this the output will be 1,2,3 and 8
#     i=i+1
# else:
#     print(i*2)
# i=1
# while(i<4):
#     print(i) executes and in the output we will get infinite loop 
#     i=i+1
# else:
#     print(i*2)
# i=1
# j=4
# while(i<4):
#     if(i%2==0):
#         print("not possible")
#         i=i+1
#     else:
#         print(j,end=" ")
#         i=i+2
# else:
#     print(i+j)
i=1
j=4
while(i<4):
    while(j>1):
        if(j%i==0):
            print("not possible")
        elif(j%i==2):
            print(i)
            j=j-2
        else:
            print(i*j)    
            j=j-3
    else:
        print(" ")