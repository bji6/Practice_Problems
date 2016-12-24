class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_check = {}
        
        string_len = len(s)
        start_index = 0
        temp_str = ""
        largest = 0
        largest_substr = ""
        count = 0

        while ((start_index + largest) < string_len):
            for i in range(start_index, string_len, 1):
                char = s[i]
                #found repeated character, break loop
                if (char in unique_check):
                    start_index = unique_check[char] + 1  # skip past first instance of repeated character
                    
                    # this part of the code optimizes in the case where the largest substring is continually repeated in the string
                    # we skip past duplicates
                    end_index = i + largest
                    temp2 = s[i:end_index]
                    went_into_while = 0
                    while (temp2 == largest_substr):
                        start_index = end_index
                        end_index += largest
                        temp2 = s[start_index:end_index]
                        went_into_while = 1
                    #only do this if we had to skip past duplicates, start 1 pattern length back from where we skipped to
                    #so we dont miss a new longer pattern
                    if(went_into_while):
                        start_index -= largest
                    
                    break
                else:
                    unique_check[char] = i
                    temp_str += char
                    #print("temp str %s" % temp_str)
                    count += 1
                    if (count > largest):
                        largest = count
                        largest_substr = temp_str
            
            # found a new largest substring
            if (count > largest):
                largest = count
                largest_substr = temp_str
                
            # reset variables
            temp_str = ""
            count = 0
            unique_check = {}
        
        return largest