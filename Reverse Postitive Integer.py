class Solution:
    
    def reverse(self, x: int) -> int:
        
        x_string = str(x)
        length = len(x_string)
        stack = [] 
        while length > 0:
            last_char = x_string[-1]
            x_string = x_string[0:len(x_string) - 1]
            stack.append(last_char)
            length = length -1 
        
        length1 = len(str(x))
        returnString = ""
        while length1 > 0:
            returnString += (stack.pop())
            length1 = length1 - 1
            
        return returnString
