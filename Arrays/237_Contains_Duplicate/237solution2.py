class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = set()
        #we use the property of set .i.e. whether it is present or not ..?
        #but 1st , we need loop for this comparison and we need the number itself.
        for number in nums:
            if number in seen:
                #so we are asking here is the number in nums[] in seen ?
                #if it is we return True value
                return True
            else:
                #if the number is not inside nums[] ; we need to add that number inside seen
                seen.add(number)

        #if at the end we still cannot find the repetition we need to return False.        
        return False