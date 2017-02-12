class Solution(object):
    
    def recursiveCombo(self, candidates, target, cur_sum, combo, combos):
        
        # base cases
        if (cur_sum == target):
            combos.append(combo)
            return combos
        
        if (cur_sum > target):
            return combos
        
        
        for i in candidates:
            temp = [x for x in combo]
            
            temp.append(i)
            
            cur_sum += i
            
            if (cur_sum <= target):
                combos = self.recursiveCombo(candidates, target, cur_sum, temp, combos) 
                cur_sum -= i
            else:
                break
            #print(combos)

        
        return combos
    
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        
        combos = self.recursiveCombo(candidates, target, 0, [], [])

        combo_check = []

        for i in combos:
            temp = sorted(i)
            if (temp in combo_check):
                pass
            else:
                combo_check.append(temp)

        return combo_check
         
        
def main():
    test = Solution()

    candidates = [27,25,45,32,29,26,44,23,39,37,31,28,20,34,33,42,35,41,47,38,43,22,48,36,40,46,21,30,49]
    target = 74

    print(test.combinationSum(candidates, target))

main()