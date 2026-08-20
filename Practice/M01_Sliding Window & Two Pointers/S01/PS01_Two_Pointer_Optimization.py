'''
input : [12,45,36,9,54,20,11]
output: [12,36,54,20]


arr = list(map(int, input().split()))
res=[]
for ele in  arr:
    if ele%2 ==0:
        res.append(ele)
print(res)  

nums = list(map(int, input().split()))
i=0
for j in range(len(nums)):
    if nums[j]%2==0:
       nums[i] = nums[j]
       i+=1
print(nums[:i])'''
s = input()
chars = list(s)
left = 0
right = len(chars)-1
while left<right:
    chars[left],chars[right] = chars[right],chars[left]
    left+=1
    right-=1
print(''.join(chars))