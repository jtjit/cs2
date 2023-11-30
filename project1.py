import tkinter as tk

class VotingApp:
    def __init__(self):
        self.john_votes = 0
        self.jane_votes = 0
        self.candidate_choice = None

    def vote_menu(self):
        root = tk.Tk()
        root.title("VOTE MENU")

        label = tk.Label(root, text="Select an option:")
        label.pack()

        vote_button = tk.Button(root, text="Vote", command=lambda: self.set_vote('v', root))
        vote_button.pack()

        exit_button = tk.Button(root, text="Exit", command=lambda: self.set_vote('x', root))
        exit_button.pack()

        root.mainloop()

    def candidate_menu(self):
        root = tk.Tk()
        root.title("CANDIDATE MENU")

        label = tk.Label(root, text="Select a candidate:")
        label.pack()

        john_button = tk.Button(root, text="John", command=lambda: self.set_candidate(1, root))
        john_button.pack()

        jane_button = tk.Button(root, text="Jane", command=lambda: self.set_candidate(2, root))
        jane_button.pack()

        root.mainloop()

    def set_vote(self, option, root):
        root.destroy()
        if option == 'v':
            self.candidate_menu()
        elif option == 'x':
            self.show_results()

    def set_candidate(self, candidate, root):
        self.candidate_choice = candidate
        root.destroy()

    def show_results(self):
        total_votes = self.john_votes + self.jane_votes
        print("\nJohn-{}, Jane-{}, Total-{}".format(self.john_votes, self.jane_votes, total_votes))

    def run(self):
        while True:
            self.vote_menu()
            if self.candidate_choice == 1:
                self.john_votes += 1
            elif self.candidate_choice == 2:
                self.jane_votes += 1
            elif self.candidate_choice is None:
                break
            else:
                print("Error in candidate selection.")

if __name__ == "__main__":
    app = VotingApp()
    app.run()
