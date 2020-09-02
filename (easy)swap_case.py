# tenbeller üçün :D

# ==> n = input("yazi daxil edin : ") #
# ==> print(n.swapcase()) #

# orta çalışqan üçün

def lower_to_upper(s):
    myStr = ""
    for i in s:
        if i.islower():
            myStr += i.upper()
        else:
            myStr += i.lower()
    return myStr

s=input()
print(lower_to_upper(s))