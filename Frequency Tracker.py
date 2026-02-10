from collections import defaultdict
class FrequencyTracker(object):

    def __init__(self):
        self.freqTracker = defaultdict(int)
        self.occur =  defaultdict(int)

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        
        if self.freqTracker[number] == 0:
            self.freqTracker[number] += 1
            val = self.freqTracker[number]
            self.occur[val] += 1
        else:
            self.freqTracker[number] += 1
            val = self.freqTracker[number]
            self.occur[val] += 1
            self.occur[val-1] -= 1

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        val = self.freqTracker[number]
        if val == 0:
            return
        self.freqTracker[number] -= 1
        self.occur[val] -= 1
        self.occur[val - 1] += 1
        
        
    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if self.occur[frequency] >= 1:
            return True
        else:
            return False

        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
