# 1. Define the quiz data using a list of dictionaries
quiz_data = [
    {
        "question": "What is the correct extension for Python files?",
        "options": ["A. .pt", "B. .py", "C. .pyt", "D. .txt"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True or False values?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. List"],
        "answer": "C"
    },
    {
        "question": "How do you start a 'for' loop in Python?",
        "options": ["A. for x in y:", "B. for x each y", "C. loop x in y", "D. for x loop y"],
        "answer": "A"
    }
]

print("=== Welcome to the Python Basics Quiz! ===\n")
score = 0

# 2. Loop through each question dynamically
for index, item in enumerate(quiz_data):
    print(f"Question {index + 1}: {item['question']}")
    
    # Print the multiple-choice options
    for option in item["options"]:
        print(option)
        
    # 3. Take user input and clean it up
    user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
    
    # 4. Check if the answer is correct
    if user_answer == item["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer was {item['answer']}.\n")

# 5. Calculate and display final results
total_questions = len(quiz_data)
percentage = (score / total_questions) * 100

print("=== Quiz Complete ===")
print(f"Your final score is: {score}/{total_questions}")
print(f"Percentage: {percentage:.1f}%")
