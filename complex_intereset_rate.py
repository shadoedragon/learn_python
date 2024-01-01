# Purpose: use to calculate final principal after x years with compound interest
# Author: Xiaoqi Zhao

principal = 200
rate = 0.035
n = 10
result = principal

for i in range(1,n+1):
    result=result*(1+rate)
    # print("After ", i, " years, principal is ", result)
    print("after {} year, principal is {}".format(i, result))
    
print("*" * 50)
print("final= ",result)