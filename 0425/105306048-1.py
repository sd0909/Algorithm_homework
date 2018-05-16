rli1 = list(range(9, -1, -1))
rli2 = list(range(9, -1, -1))
rli3 = list(range(9, -1, -1))
class Solution01:

    def swap(self,li,i,j):
        tmp = li[i]
        li[i] = li[j]
        li[j] = tmp

    def bubbleT(self, li):
        num = 0
        for i in range(len(li)):
            for j in range(i):
                if li[i] < li[j]:
                    self.swap(li,i,j)
                    num += 1 
                    print(li)
        return  num

    def selectionT(self, li):
        num = 0
        i = 0
        while i < len(li):
            j = i
            minIndex = j
            while j < len(li):
                if li[j] < li[minIndex]:
                    minIndex = j
                j += 1
            if minIndex != i:
                self.swap(li, minIndex, i)
                print(li)
                print(minIndex,i)
                num += 1
            i += 1 

        return num 
    def insertionT(self, li):
        num = 0
        for sortedIndex in range(0, len(li)-1):
            targetIndex = sortedIndex + 1
            for i in range(0,sortedIndex):
                if li[targetIndex] > li[i]:
                    pass
                else:
                    self.swap(li,i,targetIndex)
                    num += 1
                    print(li)
        return num
    def myInsertionT(self, li):
        num = 0
        for i in range(len(li)):
            sortIndex = i
            for j in range(i,-1,-1):
                
class Solution02:
    def why(self):
        print('因為selection sort最多要排n**2/2次，而insertion sort 最多排(n**2 - n)/2次')
'''
class Solution03:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (low + high)/2
            if nums[mid] == target
                return mid
            elif nums[mid] > target:
                high = mid -1
            else low = mid + 1
        return low
'''
class Solution04:
    def singleNonDuplicate (self, nums):
        a = 0
        b = len(nums)
        while a < b:
            m = (a+b)/2
            if nums[2*m]!=nums[2*m+1]:
                b = m
            else:
                a = m+1
           
        return nums[2*b]
a = Solution01()
print(a.bubbleT(rli1))
print(a.selectionT(rli2))
print(a.insertionT(rli3))
