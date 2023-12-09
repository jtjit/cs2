import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class VotingApp:
    def __init__(self, root):
        self.root = root
        self.john_votes = 0
        self.jane_votes = 0
        self.load_data()
        self.create_main_menu()

    # Updates vote counts
    def load_data(self):
        if os.path.exists("votes.json"):
            with open("votes.json", "r") as file:
                data = json.load(file)
                self.john_votes = data.get("John", 0)
                self.jane_votes = data.get("Jane", 0)

    def save_data(self):
        with open("votes.json", "w") as file:
            json.dump({"John": self.john_votes, "Jane": self.jane_votes}, file)

    def create_main_menu(self):
        self.clear_window()

        label = ttk.Label(self.root, text="Select an option:", font=("Arial", 16))
        label.pack(pady=20)

        vote_button = ttk.Button(self.root, text="Vote", command=self.create_vote_menu, style="TButton")
        vote_button.pack(pady=10)

        exit_button = ttk.Button(self.root, text="Exit", command=self.exit_app, style="TButton")  # Updated command here
        exit_button.pack(pady=10)

    
    def exit_app(self):
        print("Exiting the app...")
        self.show_results()
        self.john_votes = 0
        self.jane_votes = 0
        self.save_data()  # Save the reset votes
        self.root.destroy()

    # Displays results
    def show_results(self):
        print("Showing results...")
        total_votes = self.john_votes + self.jane_votes
        print("\nJohn: {}, Jane: {}, Total: {}".format(self.john_votes, self.jane_votes, total_votes))


    def create_vote_menu(self):
        self.clear_window()

        label = ttk.Label(self.root, text="Select a candidate:", font=("Arial", 16))
        label.pack(pady=20)

        john_button = ttk.Button(self.root, text="John", command=lambda: self.vote("John"), style="TButton")
        john_button.pack(pady=10)

        jane_button = ttk.Button(self.root, text="Jane", command=lambda: self.vote("Jane"), style="TButton")
        jane_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back", command=self.create_main_menu, style="TButton")
        back_button.pack(pady=10)
    # Voting options
    def vote(self, candidate):
        if candidate == "John":
            self.john_votes += 1
        elif candidate == "Jane":
            self.jane_votes += 1
        self.save_data()
        messagebox.showinfo("Vote Recorded", f"Vote recorded for {candidate}")
        self.create_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Voting App")
    root.geometry("400x300")
    app = VotingApp(root)
    root.mainloop()
