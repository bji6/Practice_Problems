# 6/22/2019
# leetcode merge sorted arrays


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        index1 = 0
        index2 = 0
        index3 = 0
        total_len = m + n
        
        if n == 0:
            return nums1
        
        while (index3 < total_len):
            
            if (m == 0):
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1
            
            elif (n == 0):
                pass
            
            elif (nums1[index1] >= nums2[index2]):
                
                # push everything up
                for i in range(total_len-1, index1, -1):
                    nums1[i] = nums1[i-1]
                
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1
                n -= 1
            
            elif (nums1[index1] < nums2[index2]):
                m -= 1
                index1 += 1
                
            #print nums1
            
            
            
            index3 += 1
                