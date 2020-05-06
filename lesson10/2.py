username=""
password=""
#оба поля пусты то тогда Заполните все поля
#если пусто только username Заполните поле username
if username=="" and password=="":
    print("Заполните все поля")
elif username=="":
    print("Заполните поле username")
elif password=="":
    print("Заполните поле password")