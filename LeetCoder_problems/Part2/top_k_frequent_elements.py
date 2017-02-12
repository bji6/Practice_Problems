import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # total runtime = O(N + 2Q + K) ~= O(N) as N grows very large
        
        #my dictionary
        num_dict = {}
        # my priority queue
        heap = []
        
        # O(N)
        for i in nums:
            if (i not in num_dict):
                num_dict[i] = 1
            else:
                num_dict[i] += 1
        
        # O(Q), Q = unique integers in nums
        for key in num_dict:
            heapq.heappush(heap, (num_dict[key], key))
        
        result = []
        
        # O(Q), Q = unique integers in nums
        while (len(heap) > 0):
            result.append(heapq.heappop(heap)[1])
        
        result2 = []
        index = len(result) - 1
        
        # O(K)
        while (len(result2) < k):
            result2.append(result[index])
            index -= 1
        
        return result2
