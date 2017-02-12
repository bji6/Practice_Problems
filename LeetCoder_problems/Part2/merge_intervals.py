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
        
        # calc interval distances
        
        sorted_intervals = []
        
        for i in intervals:
            tupp = (i.end - i.start, i)
            sorted_intervals.append(tupp)
        
        sorted_intervals.sort(key=lambda x: x[0], reverse=True)
        
        #print(sorted_intervals)
        
        count = 0
        
        length = len(sorted_intervals)
        
        while (count < length):
            merger = sorted_intervals[count][1]
            
            was_merged = False
            for i in range(length):
                
                #dont try to merge with yourself
                if (i == count):
                    continue
                
                temp = sorted_intervals[i][1]
                
                # skip an unused interval
                if (temp.start == None):
                    continue
                
                # check for merge candidate
                if (merger.end >= temp.start and merger.start <= temp.end):
                    #print("merger start %d  end  %d " % (merger.start,merger.end))
                   # print("temp start %d  end  %d " % (temp.start,temp.end))
                    if (merger.start >= temp.start):
                        merger.start = temp.start
                    if (merger.end <= temp.end):
                        merger.end = temp.end
                    sorted_intervals[count] = (merger.end - merger.start, merger)
                   # print("new start %d  end  %d " % (merger.start,merger.end))
                    # set unused interval to None now, we will ignore it going forward
                    temp.start = None
                    temp.end = None
                    was_merged = True
            
            if (count > 0 and was_merged):
                count -= 1
                was_merged = False
            
            #rebuild list, recalc length
            new_list = []
            for tupp in sorted_intervals:
                temp = tupp[1]
                if (temp.start != None):
                    new_list.append(tupp)
            
            sorted_intervals = new_list
            length = len(sorted_intervals)
            count += 1
            
          #  print(count)
           # print(length)
            
        result = []
        for tupp in sorted_intervals:
            result.append((tupp[1].start,tupp[1]))
            
        result.sort(key=lambda x:x[0])
        
        result2 = []
        for tupp in result:
            result2.append(tupp[1])
        
        return result2
        
        