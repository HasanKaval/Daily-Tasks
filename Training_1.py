def date_switcher() :
    date_1 = (input("Please enter a date DD/MM/YYYY : ")).split("/")
    date_2 = [date_1[2],date_1[0],date_1[1]]
    return "".join(date_2)
