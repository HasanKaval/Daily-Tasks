try:
    with open("ffrg.csv", "r", newline = "", encoding="utf-8") as f:
        print(f.read())
except Exception as e:
    counter += 1
    print(type(e))
    with open("error.txt", "a", encoding = "utf-8") as file:
        file.write("Hatali giris sayisi :" + str(counter) + "Hata : " + str(e) + "\n")
    print(e)
