class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                result.append(int(token))
            else:
                num1 = result[-2]
                num2 = result[-1]
                result = result[0:-2]
                if token == '+':
                    value = num1 + num2
                elif token == '-':
                    value = num1 - num2
                elif token == '*':
                    value = num1 * num2
                elif token == '/':
                    value = math.trunc(num1 / num2)
                result.append(value)
                # print(result)
        return result[0]