# Pypy 3 Solution

if __name__ == '__main__':
    s = input()
    
    def control_any(func, string):
        for char in string:
            if func(char):
                return True
            
        return False
    
    print(control_any(str.isalnum, s))
    print(control_any(str.isalpha, s))
    print(control_any(str.isdigit, s))
    print(control_any(str.islower, s))
    print(control_any(str.isupper, s))
