import unittest
import HW05_Qi_Zhao as HW05
'''
class C1:
    def __init__(self,gg):
        self.gg = gg
    def ss2(self):
        print(self.gg)

aaa = C1(22)
input("222:")
aaa.ss2()
'''
grid =[[0,1,0,0],[0,0,0,0]]
index =[0,0]
cnt = 0
#def find_neighbor(grid,index):
    #grid is a 2d list and index is like (a,b) represents the index
for i in [-1,0,1]:
    for j in [-1,0,1]:
        if i == j == 0:
            continue
        if i+index[0]<0 or j+index[1]<0:
            continue
        if i+index[0]>=len(grid) or j+index[1]>=len(grid[0]):
            continue
        if grid[i][j] == 1:
            cnt += 1

def twoSum(nums: [int], target: int) -> [int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            else:
                hashmap[nums[i]] = i
                
        return [-1, -1]

ab = twoSum([3,3,3,3,5,5,7],6)
#print(ab)

a = "aaasasaaaa"
a = a+"cc"
HW05.rev
print(list(HW05.rev_en))