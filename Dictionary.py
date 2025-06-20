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