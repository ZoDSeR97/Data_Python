class Solution:
    def intToRoman(self, num: int) -> str:
        ItoR = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        ans = ""
        for i in ItoR.keys():
            if num >= i:
                ans = ans+(num//i)*ItoR[i]
                num = num%i
                if num == 0:
                    break
        return ans
    
if __name__ == "__main__":
    num = 1994
    expected = "MCMXCIV"
    print(Solution().intToRoman(num) == expected)