# cerner_2^5_2020
list1 = [100,220,10,20,500,600] 
  
mx=max(list1[0],list1[1])  
secondmax=min(list1[0],list1[1])  
n =len(list1) 
for i in range(2,n):  
    if list1[i]>mx:  
        secondmax=mx 
        mx=list1[i]  
    elif list1[i]>secondmax and mx != list1[i]:  
        secondmax=list1[i] 
    else: 
        if secondmax == mx: 
            secondmax = list1[i] 
  
print("Second highest number is : ",str(secondmax)) 