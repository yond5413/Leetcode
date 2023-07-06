'''
Description
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

####
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
####
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
####
'''
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ret = strs[0] 
        for i in range(1,len(strs)):
            #if i != (len(strs)-1):
                ret += ":;"+strs[i]
        #print(ret)
        #print("encode done")
        return ret
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        ret = list()
        new = str.split(":;")
        #print(new)
        #print("decode done")
        return new#ret 
    
sol = Solution()
input = ["lint","code","love","you"]
encode = sol.encode(input)
decode = sol.decode(encode)
print("input: "+str(input))
print("encode: "+str(encode))
print("decode: "+str(decode))