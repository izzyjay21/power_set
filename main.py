def flips(num1,num2):
  flip =0  
  while (num1 >0 or num2>0):
    t1 = num1 & 1
    t2 = num2 & 1
    if t1 != t2:
     
     flip +=1 
    num1>>=1
    num2>>=1
  return flip

print(flips(13,12))
#print(bin(12))