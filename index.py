

def main():
    #open text file
    import files
    x = "r"
    files.thefile(x, x, x)

    # ask to add new names
    add = str(input("1 - to add a new name x - to exit\n"))

    # If 1 then print to file
    if add == 1 or add == "1":
        f_name = str(input("First: ")).capitalize().strip()
        m_name = str(input("Middle: ")).capitalize().strip()
        l_name = str(input("Last: ")).capitalize().strip()

        #first name
        f_n = len(f_name)
        f_letter = f_n - 1
        a = f_name[0]

        #middle name
        m_n = len(m_name)
        m_letter = m_n -1

        #last name
        l_n = len(l_name)
        l_letter = l_n -1

        #alphabet
        alp = "abcdefghijklmnopqrstuvwxyz"
        xx = list(alp)
        #y = len(x)
        #y -= 1

        #initials
        f = a
        m = m_name[0]
        l = l_name[0]

        #print out to text file
        code = f + xx[f_letter] + m + xx[m_letter] + l + xx[l_letter]
        x = "a"
        files.thefile(f_name, code, x)
        
    # if else then no print
    else:
        print("Ok, bye then!")
        exit()

main()



