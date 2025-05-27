import random

def welcome():
    print("🎉 Welcome to the Advanced PC Quiz!")
    playing = input("Do you want to play? (Y/N): ").strip().lower()
    return playing == 'y'

def ask_question(question_data):
    print("\n" + question_data["question"])
    for key, value in question_data["options"].items():
        print(f"  {key}) {value}")
    
    answer = input("Your answer (A/B/C/D): ").strip().lower()
    if answer == question_data["answer"]:
        print("✅ Correct!")
        return True
    else:
        correct_option = question_data["answer"]
        print(f"❌ Incorrect. The correct answer was {correct_option.upper()}) {question_data['options'][correct_option]}")
        return False

def quiz():
    questions = [
        {
            "question": "What does CPU stand for?",
            "options": {
                "a": "Central Processing Unit",
                "b": "Computer Personal Unit",
                "c": "Central Performance Utility",
                "d": "Control Processing Unit"
            },
            "answer": "a"
        },
        {
            "question": "What does GPU stand for?",
            "options": {
                "a": "Graphics Peripheral Unit",
                "b": "Graphical Processing User",
                "c": "Graphics Processing Unit",
                "d": "Gaming Performance Unit"
            },
            "answer": "c"
        },
        {
            "question": "What does RAM stand for?",
            "options": {
                "a": "Random Access Memory",
                "b": "Rapid Application Module",
                "c": "Remote Access Memory",
                "d": "Run Active Memory"
            },
            "answer": "a"
        },
        {
            "question": "What does PSU stand for?",
            "options": {
                "a": "Power System Unit",
                "b": "Power Supply Unit",
                "c": "Processing Storage Unit",
                "d": "Primary Supply Unit"
            },
            "answer": "b"
        },
        {
            "question": "Which part is primarily responsible for rendering images in games?",
            "options": {
                "a": "CPU",
                "b": "RAM",
                "c": "Motherboard",
                "d": "GPU"
            },
            "answer": "d"
        }
    ]

    random.shuffle(questions)
    score = 0
    for q in questions:
        if ask_question(q):
            score += 1

    print("\n🎯 Quiz Completed!")
    print(f"✅ You got {score} out of {len(questions)} correct.")
    print(f"📊 Your score: {round((score / len(questions)) * 100)}%")

    if score == len(questions):
        print("🏆 Perfect score! You're a PC master!")
    elif score >= len(questions) // 2:
        print("👍 Good job! You know quite a bit.")
    else:
        print("📚 Keep learning – you'll get better!")

def main():
    while True:
        if not welcome():
            print("Goodbye! 👋")
            break
        quiz()
        again = input("\nWould you like to play again? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
