Questions = ["What is the capital of Nigeria?", "Which colors are in the Nigerian flag?", "Nigeria is under which Continent?", "Which country is often referred to as the Giant of Africa?", "Which state is the most populated in Nigeria?"]
score = 0

for question in Questions:
    print(f"\n{question}")
    Answer = str(input())

    if Answer == "Abuja":
        point = 1
        score += 1
        print("\nCorrrect! ", "You have", point, "point")

    elif Answer == "Green and white":
        point = 1
        score += 1
        print("\nCorrect!", "You have", point, "points")

    elif Answer == "Africa":
        point = 1
        score += 1
        print ("\nCorrect!", "You have", point, "points")

    elif Answer == "Nigeria":
        point = 1
        score += 1
        print("\nCorrect!", "You have", point, "points")

    elif Answer == "Kano":
         point = 1
         score += 1
         print("\nCorrect!", "You have", point, "points")


    else:
        print("\nWrong answer!", "You can do better!",  
              "(Tip: Start your answers with a capital letter)")
print(f"\n\nTotal points = {score}")

