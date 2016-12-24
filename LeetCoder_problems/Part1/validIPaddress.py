class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        
        #check if IP is valid IPv4
        str_list = IP.split('.')
        
        ip4 = True
        
        if (len(str_list) != 4):
            ip4 = False
        else:
            for s in str_list:
                if (s[0] == "0" and len(s) > 1):
                    ip4 = False
                    break
                if (s.isdigit() == False):
                    ip4 = False
                    break
                if (int(s) > 255):
                    ip4 = False
                    break
        
        if (ip4):
            return "IPv4"
        
        #check for IPv6
        str_list = IP.split(':')
        
        ip6 = True
        
        if (len(str_list) != 8):
            ip6 = False
        else:
            for s in str_list:
                if (len(s) > 4):
                    ip6 = False
                    break
                try:
                    temp = int(s, 16)
                    if (temp > 65535):
                        ip6 = False
                        break
                except ValueError:
                    ip6 = False
                    break
                if (s.count("-") > 0):
                    ip6 = False
                    break
        
        if (ip6):
            return "IPv6"
            
        return "Neither"
