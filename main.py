grades = {
    "A+": 4.33,
    "A": 4.00,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.00,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.00,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.00,
    "D-": 0.67,
    "F": 0.33,
    "U": 0.00
}

subjects = ["Math", "English","History", "Geography", "Sociology", "Economics", "Biology", "Physics", "Chemistry", "Computer Science", "Sport Science", "Drama", "Art", "Spanish",
"German", "French", "Mandarin", "Italian"]

total_score = 0
subject_count = 0

for i in subjects:
    score = input(i + ": ")
    if score != "":
        total_score += grades[score]
        subject_count += 1

print("Your GPA is: {0:.2f}".format(total_score/subject_count))
