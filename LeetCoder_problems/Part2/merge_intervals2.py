# Definition for an interval.
 class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        count = 0
        length = len(intervals)
        was_merged = False
        
        while (count < length):
            merger = intervals[count]
            
            for i in range(length):
                #dont try to merge with yourself
                if (i == count):
                    continue
                
                temp = intervals[i]
                
                # skip an unused interval
                if (temp.start == None):
                    continue
                
                # check for merge candidate
                if (merger.end >= temp.start and merger.start <= temp.end):
                    #print("merger start %d  end  %d " % (merger.start,merger.end))
                    #print("temp start %d  end  %d " % (temp.start,temp.end))
                    if (merger.start >= temp.start):
                        merger.start = temp.start
                    if (merger.end <= temp.end):
                        merger.end = temp.end
                    
                    intervals[count] = merger
                    #print("new start %d  end  %d " % (merger.start,merger.end))
                    
                    # set unused interval to None now, we will ignore it going forward
                    temp.start = None
                    temp.end = None
                    was_merged = True
            
            if (count > 0 and was_merged):
                count -= 1
                was_merged = False
            
            #rebuild list, recalc length
            new_list = []
            for tupp in intervals:
                if (tupp.start != None):
                    new_list.append(tupp)
            
            intervals = new_list
            length = len(intervals)
            count += 1
            
            #print(count)
            #print(length)
        
        #sort intervals before returning final list
        result = []
        for tupp in intervals:
            result.append((tupp.start,tupp))
        result.sort(key=lambda x:x[0])
        
        result2 = []
        for tupp in result:
            result2.append(tupp[1])
        
        return result2
        
        