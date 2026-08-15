class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = len(nums)
        for i in range(x):
            for j in range(i+1,x):
                if nums[i] == nums[j]:
                    return True
        return False

    #and this was my first proposed solution 
    #seems just fine

    #since it's about compairing and finding whether there has 
    #repetition or not.. 

    #i decided to simply use 2 loops.
    # first i find how many of the number there are using len

    #i loop from 0 to x-1

    #and i essentially compare them.

    #but the problem is line no.9 and no.9
    #what if there are billion numbers?
    #do we compare each and every one of them everytime ?

    #so it's not a good solution we need another one.