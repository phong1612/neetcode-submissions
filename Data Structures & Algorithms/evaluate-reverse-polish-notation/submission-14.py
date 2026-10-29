class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        operand = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operand:
                result.append(int(token))
            else:
                num2 = result.pop()
                num1 = result.pop()
                if token == '+':
                    value = num1 + num2
                elif token == '-':
                    value = num1 - num2
                elif token == '*':
                    value = num1 * num2
                elif token == '/':
                    value = int(num1 / num2)
                result.append(value)
        return result[0]