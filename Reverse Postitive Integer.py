//only for positive int

class Solution:
    
    def reverse(self, x: int) -> int:
        
        converted_num = str(x)
        num_digits = len(converted_num)
        
        finalDigit = ""
        
        if ( x = txt.isnumeric()):
            while num_digits > 0:
                lastDigit = int ()
                lastDigit = x % 10 
                lastDigit1 = str(lastDigit)

                finalDigit = finalDigit + lastDigit1 
                x = x//10
                num_digits = num_digits -1

            return finalDigit
        
        
