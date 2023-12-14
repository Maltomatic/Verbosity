from goto import with_goto
import random
@with_goto
def main():
    var0 = -32
    var0 += 36
    var2 = 48 #H
    goto .line11
    var2 += 53 #101, e
    goto .line11
    var2 = 108
    goto .line11
    var8 = 113
    goto .line11
    var2 += 3
    label .line11
    print(chr(var2))
    var0 -=1
    if(var0 > 0):
        goto .(line of var0)
    print(" ")
    var0 = 87 #W
    print(chr(var0))
    var0 = 111
    print(chr(var0))
    var0 = 114
    print(chr(var0))
    var0 -= 6
    print(chr(var0))
    var0 -= 8
    print(chr(var0))
    print("\n")
    

main()