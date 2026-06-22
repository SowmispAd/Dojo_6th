def restoreIPAddress(s):
    result = []
    def valid(part):
        if not part or len(part) > 3:
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        return int(part) <= 255
    def backtrack(index, path):
        if len(path) == 4:
            if len(s) == index:
                result.append(".".join(path))
                return
            
        for length in range(1,4):
            if index + length >len(s):
                break
            part = s[index:index+length]
            if valid(part):
                backtrack(index+length,path+[part])
    backtrack(0,[])
    return result 
s = input()
print(restoreIPAddress(s))