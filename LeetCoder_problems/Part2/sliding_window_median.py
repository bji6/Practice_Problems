class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        median_list = []
        isOdd = True
        # print(len(nums))
        
        if (k % 2 == 0):
            isOdd = False
        
        lastindex = len(nums) - k + 1
        sub_sorted = nums[0:k]
        
        for i in range(0,lastindex,1):
            end = i + k
            #print(sub_list)
            sub_sorted = sorted(sub_sorted)
            if (isOdd):
                median_index = k / 2
                median = sub_sorted[median_index]
            else:
                median_index1 = int(k / 2.0)
                median_index2 = median_index1 - 1
                #print(median_index1)
                #print(median_index2)
                median = (sub_sorted[median_index1] + sub_sorted[median_index2]) / 2.0
            median_list.append(float(median))

            sub_sorted.remove(nums[i])
            if (i+k < len(nums)):
                sub_sorted.append(nums[i+k])
        
        return median_list
                    
