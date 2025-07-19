# Simple Multiple-Choice Quiz App

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 5", "B. 8", "C. 10", "D. 15"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    }
]

score = 0

def run_quiz():
    global score
    print("=== Welcome to the Quiz ===\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer is {q['answer']}.\n")

    print(f"🎉 Quiz finished! Your score: {score} out of {len(questions)}")

run_quiz()