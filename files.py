
def thefile(f_name, code, x):
    tt = open("codes.txt", x)
    if x == "r":
        print(tt.read())
    else:
        tt.write("\n" + f_name + ": \n" + code + "\n")
    tt.close()
