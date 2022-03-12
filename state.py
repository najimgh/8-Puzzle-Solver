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
        :param size: The size of the puzzle (the size is always 3 in our case)
        :param parent: Represents the parent state
        :param cost: The current cost
        """
        self.currentState = currentState
        self.size = size
        self.goal = goal
        self.parent = parent
        self.children = []
        self.cost = cost
        self.cost_function = cost_function
        self.operator = operator
        self.blank_row = self.find_blank_row()
        self.blank_column = self.find_blank_column()

    def find_blank_index(self):
        for i, value in enumerate(self.currentState):
            if value == "B":
                return i
    
    def find_blank_row(self):
        blank_index = self.find_blank_index()
        blank_row = blank_index // self.size
        return blank_row
    
    def find_blank_column(self):
        blank_index = self.find_blank_index()
        blank_column = blank_index % self.size
        return blank_column

    def display_state(self):
        print(self.currentState)

    def swap(self, i, j):
        new_state = self.currentState.copy()
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def move_left(self):
        if self.blank_column == 0:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index - 1
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Left")


    def move_right(self):
        if self.blank_column == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index + 1
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Right")
    
    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index - self.size
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Up")
    
    def move_down(self):
        if self.blank_row == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index + self.size
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self.cost_function, self, cost, operator="Down")

    def expand(self):
        if len(self.children) == 0:
            self.children = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
            self.children = list(filter(None, self.children))
        return self.children

    def is_goal(self):
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
