class Solution(object):
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        op_list = ['+', '-', '*','/']
        for token in tokens:
            if token not in op_list:
                stack.append(int(token))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                res = 0
                if token == '+':
                    res = v1 + v2
                elif token == '-':
                    res = v2 - v1
                elif token == '*':
                    res = v1 * v2
                else:
                    if v1 < 0 and v2 < 0:
                        res = (abs(v2) // abs(v1))
                    elif v1 < 0 and v2 > 0:
                        res = (v2 // abs(v1))*(-1)
                    elif v1 > 0 and v2 < 0:
                        res = (abs(v2) // v1)*(-1)
                    else:
                        res = v2 // v1
                stack.append(res)

            print(f"Element: {token}, Stack: {stack}")
        return stack[-1]

obj = Solution()
print(obj.evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))
