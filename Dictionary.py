#Create a dictionary named student_schores where keys are student names and values are their schored (integers).
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88,
    "Frank": 70 # Added an extra student for more datea
}

print("----initital student scores---")
#Iterate through the dictionarly and print each student's name and the scores
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")

# Add a new student and their score to the dictionary.
new_student_name = "Grace"
new_student_score = 90
student_scores[new_student_name] = new_student_score
print(f"----Added New Student: {new_student_name} with score {new_student_score}")
for name, score in student_scores.items():
    print(f"{name}: {score}")
print("\n")

#Update the score for an existing student.

# Find the student with the highet score and print their name and score
if student_scores: # Ensure the dictionalry is not empty
    highest_score = 0
    highest_scorer_name = ""
    for name, score in student_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer_name = name
    print(f"---Studnet with the Highest Score ---")
    print(f"{highest_scorer_name} : {highest_score}\n")
else:
    print("The dictionary is empty, cannot find the highet score.\n")


# Create a new dictionary containd only students who scored 90 or more
high_achievers = {}