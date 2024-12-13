class VotingSystem:
    """This class sets up the whole logic behind how the votes are stored, itll make a dictionary for the count and add +1 to it per vote"""
    def __init__(self):
        """starts the voting system but zeroes it out"""
        self.votes = {"John": 0, "Jane": 0}

    def WhichVote(self, candidate):
        """This was said above but it refers to adding the +1 to the vote count for the candidate, also makes sure each user is John or Jane"""

        if candidate in self.votes:
            self.votes[candidate] += 1

    def TheResults(self):
        """Gets the results ready and shows them when the user wants to see this, shown in a big long Fstring"""
        total_votes = sum(self.votes.values())
        return f"John: {self.votes['John']} votes, Jane: {self.votes['Jane']} votes, Total: {total_votes} votes"