class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_str = bin(n)[2:]
        comp = ""
        for i in bin_str:
            if i =="1":
                comp+="0"
            else:
                comp+="1"
        print(f"{comp}, {bin_str}")
        return int(comp,2)
