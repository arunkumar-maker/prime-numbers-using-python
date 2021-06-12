lowervalue=int(input("lower Value is "))
uppervalue=int(input("upper value is "))
if lowervalue>1:
    flag=0
    for i in range(lowervalue,uppervalue+1):
        if(i>1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                flag+=1
                print(i)
        else:
             print("Lower Value is not invalid")
print("the total number of prime numbers in the given range are ",flag)
