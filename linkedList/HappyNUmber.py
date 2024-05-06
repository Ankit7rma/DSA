# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n 
        fast = n 
        def findSq(num):
            ans = 0
            while num>0:
                rem=num%10
                ans += rem*rem
                num = int(num/10)
            return ans 
        while True:
            slow = findSq(slow)
            fast = findSq(findSq(fast))
            if slow == fast:
                break
        if slow == 1:
            return True
      
        return False
         

