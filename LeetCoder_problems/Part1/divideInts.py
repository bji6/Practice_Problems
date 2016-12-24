import pdb

class Solution(object):

    # function that does signed integer division quickly, no divide, multiply or mod operators used
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # largest 32 bit signed numbers
        max_int = 2147483647
        min_int = -2147483648

        count = 0

        if (divisor == 0):
            return 0

        sign_converter = False

        if (dividend < 0 and divisor < 0):
            dividend = abs(dividend)
            divisor = abs(divisor)
        elif (dividend < 0 or divisor < 0):
            dividend = abs(dividend)
            divisor = abs(divisor)
            sign_converter = True

        if (divisor > dividend):
            return 0

        if (divisor == 1):
            if (sign_converter):
                answer = (0 - dividend)
                if (answer > max_int):
                    return max_int
                elif (answer < min_int):
                    return min_int
                else:
                    return answer
            else:
                if (dividend > max_int):
                    return max_int
                elif (dividend < min_int):
                    return min_int
                else:
                    return dividend

        total = dividend

        divider = divisor
        count = 1
        total_count = 0

        # O(log n) division check, figures out how much we can divide by, by constantly doubling our divisor
        while (True):

            while (divider <= total):
                divider += divider
                count += count
            
            # divide count and divider by 2
            count = count >> 1
            divider = divider >> 1
            
            total_count += count
            
            # find next largest divisor
            total -= divider

            while (divider > total):
                divider = divider >> 1
                count = count >> 1

            # if our divider is smaller than original divisor, we cant divide any more
            if (divider < divisor):
                break

        if (sign_converter == False and total_count > max_int):
            return max_int
        elif (sign_converter == False and total_count < min_int):
            return min_int
        
        if (sign_converter):
            return 0 - total_count

        return total_count


def main():
    test = Solution()

    print(test.divide(5,2))

    print(test.divide(10,2))

    print(test.divide(8,3))

    print(test.divide(2147483647,-2))

main()