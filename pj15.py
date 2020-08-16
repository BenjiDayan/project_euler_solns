#pj15

class two_d_lattice():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lattice_list = []
        for row in range(y):
            self.lattice_list.append([0 for num in range(self.x)])
        print(self.lattice_list)
            

    def top_left_to_bottom_right_number_of_ways(self):
        """can only move left or down"""
        self.lattice_list[0][0] = 1
        for row in range(self.y):
            for column in range(self.x):
                if not column == 0:
                    left = self.lattice_list[row][column-1]
                else:
                    left = 0
                if not row == 0:
                    up = self.lattice_list[row-1][column]
                else:
                    up = 0
                self.lattice_list[row][column] += left + up
        
