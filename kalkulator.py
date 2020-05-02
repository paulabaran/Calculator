while not input == "koniec":
    print("To ja Twój kalkulator ;)")
    wybor = input("Wybierz działanie które chcesz wykonać: \
    + - dodawannie, - -odejmowanie, * - monżenie, /- dzielenie,\
    ** - potęgowanie, % -reszta z dzielenia: ")
    a = int(input("Podaj pierszą liczbę: "))
    b= int(input("Podaj drugą liczbę: "))
    if(wybor == "+" ):
        print(a + b)
    elif(wybor == "-"):
        print (a - b)
    elif(wybor == "*"):
        print(a * b)
    elif(wybor == "/"):
        if(b == 0):
            print("Pamiętaj kolego nie dziel przez zero")
        elif(b == 0):
            print(a / b)
    elif(wybor == "**"):
        print(a ** b)
    elif(wybor == "%"):
        print(a % b)
    else:
        print("Dokonaj właściwego wyboru działania")



