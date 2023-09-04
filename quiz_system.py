import tkinter as tk
from tkinter import messagebox
import csv

class QuizSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz System")
        self.root.geometry("600x400")

        # Create variables to store the current question and user's score
        self.current_question = 0
        self.score = 0

        # Load questions from the CSV file
        self.questions = self.load_questions("mcq.csv")

        # Create widgets
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack()

        # Start the quiz
        self.display_question()

    def load_questions(self, filename):
        questions = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                question = {
                    "text": row[0],
                    "options": row[1:5],
                    "correct_answer": int(row[5])
                }
                questions.append(question)
        return questions

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["text"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_result()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        correct_answer = question_data["correct_answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1
        self.display_question()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}")
        self.root.destroy()

def start_quiz():
    root = tk.Tk()
    app = QuizSystem(root)
    root.mainloop()

if __name__ == "__main__":
    start_quiz()
