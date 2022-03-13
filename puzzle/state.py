#### Code inspired from Coloumbia Univeristy ####
#### Property belongs to ColumbiaX: CSMM.101x: Artificial Intelligence (AI) Course on EdX.

class State(object):
    """
    Represents a state in the 8-Puzzle game.
    """

    def __init__(self, currentState, size, goal, cost_function=None, parent=None, cost=0, operator="Root"):
        """
        Constructor for the State object

        :param currentState: The current state of the puzzle
        :param size: The size of the puzzle
        :param goal: The goal state
        :param cost_function: the cost function used to calculate total cost (for Informated Search algorithms)
        :param parent: Represents the parent state
        :param cost: The current cost
        :param operator: The action taken ["Left", "Right", "Up", "Down"]
        """
        self.currentState = currentState
        self.size = size
        self.goal = goal
        self.parent = parent
        # The children states of the current state
        self.children = []

        self.cost = cost
        self.cost_function = cost_function
        self.operator = operator
        self.blank_row = self.find_blank_row()
        self.blank_column = self.find_blank_column()

    def find_blank_index(self):
        """
        Finds the index of the blank tile
        """
        for i, value in enumerate(self.currentState):
            if value == "B":
                return i
    
    def find_blank_row(self):
        """
        Finds the index of the row where the blank tile is
        """
        blank_index = self.find_blank_index()
        blank_row = blank_index // self.size
        return blank_row
    
    def find_blank_column(self):
        """
        Finds the index of the column where the blank tile is
        """
        blank_index = self.find_blank_index()
        blank_column = blank_index % self.size
        return blank_column

    def display_state(self):
        """
        Prints the configuration of the puzzle
        """
        print(self.currentState)

    def swap(self, i, j):
        """
        Swaps tile i with tile j
        """
        # Copying the original configuration so as to not modify it.
        new_state = self.currentState.copy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def move_left(self):
        """
        Moves the blank tile to the left by swapping

        :return: Returns a new state with the tiles swapped
        """
        # Check if move is possible
        if self.blank_column == 0:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index - 1
            new_state = self.swap(blank_index, target_index)
            # Add a cost of +1 for the move
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Left")


    def move_right(self):
        """
        Moves the blank tile to the right by swapping
        
        :return: Returns a new state with the tiles swapped
        """
        # Check if move is possible
        if self.blank_column == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index + 1
            new_state = self.swap(blank_index, target_index)
            # Add a cost of +1 for the move
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Right")
    
    def move_up(self):
        """
        Moves the blank tile up by swapping
        
        :return: Returns a new state with the tiles swapped
        """
        # Check if move is possible
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.find_blank_index()
            # A move up is -size (e.g. -3 for 8-Puzzle)
            target_index = blank_index - self.size
            new_state = self.swap(blank_index, target_index)
            # Add a cost of +1 for the move
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Up")
    
    def move_down(self):
        """
        Moves the blank tile down by swapping
        
        :return: Returns a new state with the tiles swapped
        """
        # Check if move is possible
        if self.blank_row == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            # A move down is +size (e.g. +3 for 8-Puzzle)
            target_index = blank_index + self.size
            new_state = self.swap(blank_index, target_index)
            # Add a cost of +1 for the move
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Down")

    def expand(self):
        """
        Successor State Generator
        
        Finds the children states of the current state by
        applying moves Up, Down, Left and Right and filtering results which return None

        :return: Returns a list of children states
        """
        if len(self.children) == 0:
            self.children = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
            self.children = list(filter(None, self.children))
        return self.children

    def is_goal(self):
        """
        Check wether current state is the goal state
        """
        return self.currentState == self.goal

    def __lt__(self, other):
        """
        Function used by the PriorityQueue to compare cost values
        """
        return self.cost_function(self) < self.cost_function(other)

    def __le__(self, other):
        """
        Function used by the PriorityQueue to compare cost values
        """
        return self.cost_function(self) <= self.cost_function(other)
