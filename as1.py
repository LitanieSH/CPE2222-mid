n = int(input("your number :"))
T=[]
for m in range (0,n):
    if m==0:
        T.append(0)
    elif m==1:
        T.append(0)
    elif m==2:
        T.append(1)    
    else :
        X = T[m-3] + T[m-2] + T[m-1]
        T.append(X)
        
TP = tuple (T)
print("A tuple is ",TP)