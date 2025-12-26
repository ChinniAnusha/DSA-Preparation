# Problem: Two sum
# Platform: LeetCode
# optimal approach: sort the array and keep 2 pointers at begining and ending add then sum should be equal to target

def twosum(arr,t):
  #logic
    arr.sort()
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

# Time Complexity: O(nlogn) due to sorting
# Space Complexity: O(1)
