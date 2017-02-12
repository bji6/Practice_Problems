import pdb

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        char_count = {}
        #keep track of dupes
        for c in s:
            if (c in char_count):
                char_count[c] += 1
            else:
                char_count[c] = 1
        
        # try 1 direction
        cur_index = 0
        new_list = []
        new_string = s
        while (cur_index < len(new_string)):
            cur_char = new_string[cur_index]
            
            if (cur_index < (len(new_string) - 1)):
                #pdb.set_trace()
                offset = 1
                next_char = new_string[cur_index+offset]
                #while (char_count[next_char] > 1 and len(new_string) > (cur_index+offset)):
                #    offset += 1
                #    next_char = new_string[cur_index+offset]
                
                if (char_count[cur_char] > 1):
                    
                    #pdb.set_trace()

                    # we will remove cur_char from the string, subtract count
                    if (ord(next_char) < ord(cur_char)):
                        char_count[cur_char] -= 1
                        #build a new string without cur_char, restart process
                        for i in range(cur_index+1,len(new_string),1):
                            new_list.append(new_string[i])
                        
                        new_string = ''.join(new_list)
                        new_list = []
                        cur_index = 0
                        continue
                    else:
                        new_list.append(cur_char)
                        cur_index += 1
                    # check if we have a dupe chain, might not need this?
                    #elif (
                else:                
                    new_list.append(cur_char)
                    cur_index += 1
            else:
                new_list.append(cur_char)
                cur_index += 1

            print(new_string)
            #print(cur_index)
        
        #print(new_string)

        #now just remove remaining duplicates from end
        new_list = []
        for i in range(len(new_string)-1,-1,-1):
            if (char_count[new_string[i]] > 1):
                char_count[new_string[i]] -= 1
            else:
                new_list.append(new_string[i])

        new_list = reversed(new_list)
        new_string = ''.join(new_list)

        print(new_string)

        #try 2nd direction, might produce a better string
        cur_index = 0
        new_list = []
        
        temp = []
        #reverse string, reset char counts
        for i in range(len(s)-1,-1,-1):
            temp.append(s[i])
            char_count[s[i]] += 1

        for x in char_count:
            char_count[x] -= 1
        
        new_string2 = ''.join(temp)
        
        while (cur_index < len(new_string2)):
            cur_char = new_string2[cur_index]
            
            if (cur_index < (len(new_string2) - 1)):
                #pdb.set_trace()
                
                next_char = new_string2[cur_index+1]
                
                if (char_count[cur_char] > 1):
                    
                    #pdb.set_trace()

                    # we will remove cur_char from the string, subtract count
                    if (ord(next_char) > ord(cur_char)):
                        char_count[cur_char] -= 1
                        #build a new string without cur_char, restart process
                        for i in range(cur_index+1,len(new_string2),1):
                            new_list.append(new_string2[i])
                        
                        new_string2 = ''.join(new_list)
                        new_list = []
                        cur_index = 0
                        continue
                    else:
                        new_list.append(cur_char)
                        cur_index += 1
                    # check if we have a dupe chain, might not need this?
                    #elif (
                else:                
                    new_list.append(cur_char)
                    cur_index += 1
            else:
                new_list.append(cur_char)
                cur_index += 1

            #print(new_string2)
            #print(cur_index)
        #print(new_string2)
        #now just remove remaining duplicates from end
        new_list = []
        for i in range(len(new_string2)-1,-1,-1):
            if (char_count[new_string2[i]] > 1):
                char_count[new_string2[i]] -= 1
            else:
                new_list.append(new_string2[i])
        new_list = reversed(new_list)
        new_string2 = ''.join(new_list)
        
        new_list = []
        #put string in correct order
        for i in range(len(new_string2)-1, -1, -1):
            new_list.append(new_string2[i])
        new_string2 = ''.join(new_list)
        
        print(new_string2)

        if (new_string2 < new_string):
            #print("2 is better than 1")
            return new_string2
        
        #print("1 is better than 2")
        return new_string


def main():
    test = Solution()

    #print(test.removeDuplicateLetters("bcabcc"))

    #print(test.removeDuplicateLetters("cbacdcbc"))

    #print(test.removeDuplicateLetters("acbdacb"))

    #print(test.removeDuplicateLetters("abacb"))
    #print(test.removeDuplicateLetters("bbcaaeae"))
    print(test.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic"))

main()