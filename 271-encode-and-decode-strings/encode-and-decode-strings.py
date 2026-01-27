class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ""
        for i in range(len(strs)):
            ret+= strs[i]+",/!!" if i !=len(strs)-1 else strs[i]
        return ret

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split(",/!!")
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))