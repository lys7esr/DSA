# Stack used
# From reading question, it was understood that stack will be used i.e. list
# Here, operations contain string value so try-except block was used
# int(i) for considering both negative and positive as i.isdigit() will be false for negative values
# ValueError is raised if we try to convert C into integer so except block

class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for i in operations:
            try:
                n=int(i)
                stack.append(n)
            except ValueError:
                if i=='C':
                    stack.pop()
                elif i=='D':
                    n=2*stack[-1]
                    stack.append(n)
                elif i=='+':
                    n=stack[-1]+stack[-2]
                    stack.append(n)
        return sum(stack)            
    
# Time-complexity: O(N)
# Space-complexity: O(N), worst case