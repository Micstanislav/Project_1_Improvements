import tkinter as tk
from gui import VotingApp

def main():
    """ This starts the main bit of programming, it will make a window then startthe class called 'VotingApp'"""
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()
"""It will alsostart what tkinteer does that will handle how what the operator presses"""
if __name__ == "__main__":
    """This tells the program that this is the true main page and not another one, with this the program will first attempt to run this if statement that results in 'main()' being called"""
    main()