#### Code inspired from Coloumbia Univeristy ####
#### Property belongs to ColumbiaX: CSMM.101x: Artificial Intelligence (AI) Course on EdX.

class State(object):
    """
    Represents a state in the 8-Puzzle game.
    """

    def __init__(self, currentState, size, goal, parent=None, cost=0):
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
        self.blank_row = self.find_blank_row()
        self.blank_column = self.find_blank_column()

    def find_blank_index(self):
        for i, value in enumerate(self.currentState):
            if value == 0:
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
        for i in range(self.size):
            row = []
            row_index = i * self.size
            for j in range(self.size):
                row.append(self.currentState[row_index + j])
            print(row)

    def swap(self, i, j):
        new_state = self.currentState
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
            return State(new_state, self.size, self.goal, self, cost)


    def move_right(self):
        if self.blank_column == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index + 1
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self, cost)
    
    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index - self.size
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self, cost)
    
    def move_down(self):
        if self.blank_row == self.size - 1:
            return None
        else:
            blank_index = self.find_blank_index()
            target_index = blank_index + self.size
            new_state = self.swap(blank_index, target_index)
            cost = self.cost + 1
            return State(new_state, self.size, self.goal, self, cost)

    def expand(self, DFS=False):
        if len(self.children) == 0:
            if (DFS):
                expanded = [self.move_up(), self.move_down(), self.move_left(), self.move_right()]
                expanded = list(filter(None, expanded))
                self.children.append(expanded)
            else:
                expanded = [self.move_right(), self.move_left(), self.move_down(), self.move_up()]
                expanded = list(filter(None, expanded))
                self.children.append(expanded)

        return self.children

    def is_goal(self):
        return self.currentState == self.goal
