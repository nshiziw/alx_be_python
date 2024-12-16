marks = int(input("Enter your score /100"))

if marks >= 90:
    print("Grader A")
elif marks >= 80:
    print("Grader B")
elif marks >= 70:
    print("Grader C")
elif marks >= 60:
    print("Grader D")
elif marks >= 50:
    print("Grader E")
elif marks >= 0:
    print("Failed")
else:
    print("Invalid score")