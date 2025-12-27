# Problem: Two sum
# Platform: LeetCode
# optimal approach: sort the array and keep 2 pointers at begining and ending add then sum should be equal to target
#🔴 Two pointers only if array is already sorted

def twosum(arr,t):
  #logic
    n = len(arr)
    l = 0  #left pointerr
    r = n - 1  #right pointer
    while l < r:
        a = arr[l] + arr[r]
        if a == t:
            return "Yes"
        elif a > t:
            r -= 1
        elif a < t:
            l += 1
    return "No"
    
    
arr = list(map(int,input().split()))
t = int(input())
print(twosum(arr,t))



#Problem : Two sum
#Approach:Hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          n = len(nums)
          hashing = {}
          rem = 0
          for i in range(n):
            rem = target - nums[i]
            if rem in hashing:
                return [hashing[rem],i]
            if nums[i] not in hashing:
                hashing[nums[i]] = i


#Time Complexity (TC) : O(n) You traverse the array once.
#Space Complexity (SC):O(n) In the worst case, you store all n elements in the hashmap.
#source:Leetcode,Striver A to Z sheet

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(1)
