# print(ord(input().lower())-ord('a')+1)

# wd = input()
# wd = (''.join(filter(str.isalpha, wd)))
# print(sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a')-1)*len(wd))

def declare_var(word):
    sign = False
    shift = False
    if(word[0].isupper()):
        sign = True
    if(word[-1] == '.'):
        shift = True
    wd = (''.join(filter(str.isalpha, word)))
    if(shift):
        wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a'))*len(wd)
    else:
        wd = sum(bytearray(wd.lower(), encoding='utf-8')) - (ord('a')-1)*len(wd)
    if(sign):
        return wd*-1
    else:
        return wd

print(declare_var(input()))