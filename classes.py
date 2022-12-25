from datetime import date

#need to make dateMove into a string formatted date time stamp when the rack was created
class Rack():
    def __init__(self, ID, tare, currLoc='Kepner', dateMove):
        self.ID = ID
        self.tare = tare
        self.currLoc = currLoc
        self.dateMove = dateMove
        self.moveHistory = [(1, dateMove, currLoc),]

    def addMoveTuple(self):
        """Adds a new tuple entry to the 'moveHistory' list with the integer ID of the unique movement record ID number, 
        and the location and date of the last move that the new move replaces."""
        moveID = []
        for move in self.moveHistory:
            for a, b, c in move:
                moveID.append(a)
        newMoveID = max(moveID) + 1
        newMoveTuple = (newMoveID, self.dateMove, self.currLoc)
        self.moveHistory.append(newMoveTuple)

    def changeLocation(self, newLoc, newDateMove):
        """Changes the current rack location and date of that change. Changes the values of the Rack class object 
        attributes 'currLoc' and 'dateMove' to the user entered values."""
        
        self.currLoc = newLoc
        self.dateMove = newDateMove

    

