class Solution:
    def intToRoman(self, num: int) -> str:
        # 硬编码
        thousands = ["","M","MM","MMM"]
        hundreds = ["","C","CC","CCC","CD", "D", "DC","DCC","DCCC","CM"]
        tens = ["","X","XX","XXX","XL","L", "LX","LXX","LXXX","XC"]
        ones = ["","I","II","III","IV","V","VI", "VII","VIII", "IX"]
        return thousands[num//1000]+hundreds[num%1000//100]+tens[num%100//10]+ones[num%10]

        # 贪心 数组：按罗马符号从大到小排列， 优先获取大的罗马符号
        """
        roman = [(1000,'M'),(900,'CM'),(500,'D'), (400,'CD'),(100, 'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        res = []
        for v, s in roman:
            if num==0: break
            count, num = divmod(num,v);
            res.append(s * count)
        return ''.join(res)
        """