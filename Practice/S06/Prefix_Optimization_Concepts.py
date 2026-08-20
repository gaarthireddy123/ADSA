nums = [1,2,3,4]
n = len(nums)
res = [0] * n
for i in range(n):
    s = 0
    for j in range(0,i+1):
        s += nums[j]
    res[i] = s
print(res) 

'''
Input: nums = [1,2,3,4]
def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
'''''

'''' 
Input: gain = [-5,1,5,0,-7]
def largestAltitude( gain: List[int]) -> int:
        n = len(gain)
        alt = [0] * (n+1)
        for i in range(1,n+1):
            alt[i] = alt[i-1] + gain[i-1]
        return max(alt)
''' 