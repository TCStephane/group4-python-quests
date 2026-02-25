your_score = int(input("Enter your score: "))
if your_score >= 90 and your_score <= 100:
    print("You passed with an A ")
elif your_score >= 80 and your_score <= 89:
    print("You passed with a B")
elif your_score >= 70 and your_score <= 79:
    print("You passed with a C")
else:
    print("You need to improve")