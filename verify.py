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
    var8 = -94
    goto .line11
    var2 = 111
    label .line11
    print(chr(var2))
    var12 = 1
    var0 -= var12
    if(var0 > 0):
        goto .(line of var0)
    print(" ")
    var15 = 87 #W
    print(chr(var15))
    pass
    print(chr(var2))
    var8 -= 20
    print(chr(var8))
    var19 = 108
    print(chr(var19))
    var0 -= 8
    print(chr(var0))
    print("\n")
    

main()