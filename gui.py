import tkinter as tk
from functions import VotingSystem
class VotingApp:
    """This is how the main part of the GUI is setup within this class (this class houses multiple functions) GUI builds the graphical element"""

    def __init__(self, root):
        """Because this is the root and an intializatian of the window it starts and creates the part that users will see or kind of the framework, it also picks the size and title of the frame"""
        self.root = root
        self.votingSystem = VotingSystem()  #Nameneeded because could not get system to check without it
        self.root.title("Tallies of Voters")
        self.root.geometry("425x325")

        #BigBanner
        self.header = tk.Label(root, text="Tallies of Voters", font=("Times New Roman", 16))
        self.header.pack(pady=10)

#John'sButton
        self.buttonJohn = tk.Button(root, text="Vote for John", width=25, command=self.votingJOHN)
        self.buttonJohn.pack(pady=9)
#Jane'sButton
        self.buttonJane = tk.Button(root, text="Vote for Jane", width=23, command=self.votingJANE)
        self.buttonJane.pack(pady=10)
        self.feedback = tk.Label(root, text="", font=("Times New Roman", 15), fg="red")
        self.feedback.pack(pady=10)

        #ResultsTallied
        self.buttonOfResults = tk.Button(root, text="Show Results", width=20, command=self.TheResults)
        self.buttonOfResults.pack(pady=10)

    #EXITING
        self.buttonOfExit = tk.Button(root, text="Exit", width=20, command=root.quit)
        self.buttonOfExit.pack(pady=10)

    def votingJOHN(self):
        '''initialtes the label that lets Johns vote be cast and shown within the feedback, this is where the vote is stored'''
        self.votingSystem.WhichVote("John")
        self.feedback.config(text="Voted for John!")

    def votingJANE(self):
        """JAne vote button is counted in this function"""
        """Also says a vote has been cast"""
        self.votingSystem.WhichVote("Jane")
        self.feedback.config(text="Voted for Jane!")

    def TheResults(self):
        """This gets the correct tally numbers to appear in a feedback below the buttons and shows a str for each runners votes"""
        results = self.votingSystem.TheResults()
        self.feedback.config(text=results)