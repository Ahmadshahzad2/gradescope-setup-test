def mid(s):
        
        length = len(s)
        middle_index = length // 2
    
        if length % 2 == 0:
                return ""
        else:
                result = s[middle_index]
        
        return result

if __name__=='__main__':

        print(mid('helloo'))


