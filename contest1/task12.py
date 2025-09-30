# print("Умеет ли существо плавать?",
#       "Есть ли у него крылья?",
#       "Длинная ли у него шея?")

data = input().split()

answer1 = data[0]
answer2 = data[1]
answer3 = data[2]

if(answer1.lower() == "да"):
    if(answer2.lower() == "да"):
        if(answer3.lower() == "да"):
            print("Утка")
        else:
            print("Пингвин")
    else:
        if(answer3.lower() == "да"):
            print("Плезиозавры")
        else:
            print("Дельфин")
else:
    if(answer2.lower() == "да"):
        if(answer3.lower() == "да"):
            print("Страус")
        else:
            print("Курица")
    else:
        if(answer3.lower() == "да"):
            print("Жираф")
        else:
            print("Кот")