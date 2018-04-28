# dict and list for grade values and classes
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

# incrementing variables for calculating the average GPA
total_score = 0
subject_count = 0 # not all students take all the classes

print("""Hello. This script will measure your GPA on a 4.0 scale. Please enter
alphabetical grades and do not enter anything for classes you do not take.
""")

for subject in subjects:
    while True: # run until the user enters correct information
        try:
            score = input(subject + ": ")
            if (score not in grades) and (score != ""):
                raise ValueError # empty value is stll correct
            try:
                total_score += grades[score]
                subject_count += 1
            except KeyError: # if the value is empty, pass.
                pass
            break # break out of the WHILE TRUE
        except ValueError:
            print("Please enter a correct grade!")



print("Your GPA is: {0:.2f}".format(total_score/subject_count))
