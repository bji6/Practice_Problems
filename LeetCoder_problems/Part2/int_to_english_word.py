class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones_digit_dict = {}
        number_size_dict = {}
        tens_dict = {}
        
        if (num == 0):
            return "Zero"
        
        #ones_digit_dict[0] = ""
        ones_digit_dict[1] = "One"
        ones_digit_dict[2] = "Two"
        ones_digit_dict[3] = "Three"
        ones_digit_dict[4] = "Four"
        ones_digit_dict[5] = "Five"
        ones_digit_dict[6] = "Six"
        ones_digit_dict[7] = "Seven"
        ones_digit_dict[8] = "Eight"
        ones_digit_dict[9] = "Nine"
        
        ones_digit_dict[10] = "Ten"
        ones_digit_dict[11] = "Eleven"
        ones_digit_dict[12] = "Twelve"
        ones_digit_dict[13] = "Thirteen"
        ones_digit_dict[14] = "Fourteen"
        ones_digit_dict[15] = "Fifteen"
        ones_digit_dict[16] = "Sixteen"
        ones_digit_dict[17] = "Seventeen"
        ones_digit_dict[18] = "Eighteen"
        ones_digit_dict[19] = "Nineteen"
        
        #tens_dict[0] = ""
        tens_dict[2] = "Twenty"
        tens_dict[3] = "Thirty"
        tens_dict[4] = "Forty"
        tens_dict[5] = "Fifty"
        tens_dict[6] = "Sixty"
        tens_dict[7] = "Seventy"
        tens_dict[8] = "Eighty"
        tens_dict[9] = "Ninety"
        
        number_size_dict[3] = "Hundred"
        number_size_dict[4] = "Thousand"
        number_size_dict[7] = "Million"
        number_size_dict[10] = "Billion"
        
        
        remainders = []
        while (num > 0):
            remainders.append(num % 10)
            num /= 10
        
        #print(remainders)
        
        number_word = []
        count1 = 1
        count2 = 0
        while (count1 <= len(remainders)):
            digit = remainders[count1-1]
            
            if (count2 == 0):
                #print(count1)
                if (count1 > 3 and count1 < 7):
                    temp = remainders[3]
                    if (len(remainders) > 4):
                        temp += remainders[4]
                    if (len(remainders) > 5):
                        temp += remainders[5]
                    if (temp > 0):
                        number_word.append("Thousand")
                elif (count1 > 6 and count1 < 10):
                    temp = remainders[6]
                    if (len(remainders) > 7):
                        temp += remainders[7]
                    if (len(remainders) > 8):
                        temp += remainders[8]
                    #print("temp %d" % temp)
                    if (temp > 0):
                        number_word.append("Million")
                elif (count1 > 9 and count1 < 13):
                    temp = remainders[9]
                    if (len(remainders) > 10):
                        temp += remainders[10]
                    if (len(remainders) > 11):
                        temp += remainders[11]
                    if (temp > 0):
                        number_word.append("Billion")
                
                if (digit == 0):
                    pass
                else:
                    number_word.append(ones_digit_dict[digit])
            elif (count2 == 1):
                #special case
                if (digit == 1):
                    keyy = 10
                    if (len(number_word) > 0 and remainders[count1-2] > 0):
                        number_word.pop()
                        keyy = 10 + remainders[count1-2]
                    number_word.append(ones_digit_dict[keyy])
                elif (digit == 0):
                    pass
                else:
                    number_word.append(tens_dict[digit])
            else:
                if (digit == 0):
                    pass
                else:
                    number_word.append("Hundred")
                    number_word.append(ones_digit_dict[digit])
                
                count2 = -1
            count2 += 1
            count1 += 1
            #print(number_word)
            
        #print(number_word)
        
        number_word = reversed(number_word)
        
        result = ' '.join(number_word)
        
        return result
