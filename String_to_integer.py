Python program for implementation of atoi 
  
# A utility function to check whether x is numeric 
def isNumericChar(x): 
    if (x >= '0' and x <= '9'): 
        return True
    return False
  
# A simple atoi() function. If the given string contains 
# any invalid character, then this function returns 0 
def myAtoi(string): 
    if len(string) == 0: 
        return 0
  
    res = 0
    # initialize sign as positive 
    sign = 1
    i = 0
  
    # if number is negative then update sign 
    if string[0] == '-': 
        sign = -1
        i+= 1
  
    # Iterate through all characters of input string and update result 
    for j in xrange(i, len(string)): 
        # You may add some lines to write error message to error stream 
        if isNumericChar(string[j] == False): 
            return 0
  
        res = res * 10 + (ord(string[j]) - ord('0')) 
  
    return sign * res 
  
# Driver program 
string = "-134"
print myAtoi(string) 