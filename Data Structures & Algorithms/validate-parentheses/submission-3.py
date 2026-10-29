class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.insert(0, i)
                print(stack)
            elif i == ')' or i == ']' or i == '}':
                if stack == []:
                    return False
                top = stack[0]
                st = top + i
                if st != '()' and st != '[]' and st != '{}':
                    return False
                else:
                    stack = stack[1:]
        if stack != []:
            return False
        return True