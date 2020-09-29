def printer(func) :
    def wrap() :
        print()
        print("============================")
        func()
        print("============================")
    return wrap

def message(name = "Hasan") :
    print(f"=========Hello {name}========")

me = printer(message)

me()
