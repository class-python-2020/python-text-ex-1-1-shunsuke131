x,y, exp = 2,5,32
ans  = my_pow(x,y)
print("test my_pow({},{})-> {},exp: {} ----".format(x,y,ans,exp),end = "")
if ans == exp:
    print("test ok")
else:
    print("test fail")