class Solution(object):
    def subdomainVisits(self,cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        mydict = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domainsplit = domain.split(".") 
            for i in range(len(domainsplit)):
                word = domainsplit[i:]
                subDomain = ".".join(word)
                if  subDomain not in mydict:
                    mydict[subDomain] = count
                else:
                    mydict[subDomain] += count
        output = []
        for subDomain, count in mydict.items():
            cpdomain = "{} {}".format(count, subDomain)
            output.append(cpdomain)
        return output

                
                



                

        
