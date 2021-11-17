print("1")

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (i != k) and (j != k):
                print(i,j,k)

'''profit = int(input("利润："))
if profit <= 100000:
    result = profit*0.1
elif profit <= 200000:
    result = 100000*0.1+(profit-100000)*0.075
elif profit <= 400000:
    result = 100000*(0.1+0.075)+(profit-200000)*0.05
elif profit <= 600000:
    result = 100000*(0.1+0.075)+200000*0.05+(profit-400000)*0.03
elif profit <= 1000000:
    result = 100000*(0.1+0.075)+200000*(0.05+0.03)+(profit-600000)*0.015
elif profit > 1000000:
    result = 100000*(0.1+0.075)+200000*(0.05+0.03)+400000*0.015+(profit-1000000)*0.01
print(result)
'''
# 利用数轴分界，列表下标
profit = int(input("please enter profit:"))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.001, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0
for i in range(0,6):
    if profit>arr[i]:
       r+=(profit-arr[i])*rat[i]
       profit = arr[i]

print(r)

