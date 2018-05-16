#Q1
class Solution01:
    def complexity(self):
        print('n**2')

#Q2
class Solution02:
    def addDigits(self, num):
        temp = str(num)
        ans=0
        for i in range(len(temp)):
            ans+=int(temp[i])
            
        if ans<10:
            return ans
        else:
            return self.addDigits(ans)

#Q3
class Solution02_Re:
    def addDigits(self,num):
        return -((1-num)-int((1-num)/9)*9) + 1


#Q4
class Solution04:
    def isPalindrome(self,s):
        s = s.split(' ')
        s = ''.join(s)
        l = len(s)
        for i in range(int(l/2)):
            if s[i] != s[l-1-i]:
                return False
                break
        else:
            return True


#Q5
class Solution04_stack:
    def isPalidrome(self,s):
        stack = []
        temp = ''
        for i in s:
            if i!=' ':
                stack.append(i)
        for j in range(len(stack)):
            temp+=stack.pop()
        if s==temp:
            return True
        else:
            return False    
        
