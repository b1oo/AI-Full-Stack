"""In this example, the get_score function is used to prompt the user to enter their exam score. The get_grade function takes the score as input and uses an if-elif statement to determine the corresponding grade, which is then returned. The grade is then printed to the screen along with the message "Your grade is:"."""

def get_score():
    return int(input("Enter your exam score: "))

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = get_score()
grade = get_grade(score)

print("Your grade is:", grade)