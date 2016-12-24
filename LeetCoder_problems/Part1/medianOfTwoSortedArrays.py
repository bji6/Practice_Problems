class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = []
        
        # build 1 sorted array
        len1 = len(nums1)
        len2 = len(nums2)
        
        median = 0
            
        i = 0
        j = 0
        while (i < len1 or j < len2):
            #print(j)
            #print(i)
            if (j == len2):
                nums3.append(nums1[i])
                i += 1
            elif (i == len1):
                nums3.append(nums2[j])
                j += 1
            elif (nums1[i] < nums2[j]):
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        
        if ((len1 + len2) % 2 == 0):
            middle1 = int( ((len1 + len2) / 2.0) - 0.5)
            middle2 = int((len1 + len2) / 2.0)
           # print(middle1)
          #  print(middle2)
            median = (nums3[middle1] + nums3[middle2]) / 2.0
        else:
            middle = int((len1 + len2) / 2.0)
            median = nums3[middle]
            
        return median