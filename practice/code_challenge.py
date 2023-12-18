import re
class Picker:
    """The solution code for the block moving game"""
    def choose(self, nb_blocks, grid:[]):
        block = 0
        while nb_blocks:
            if any([str(block) in row for row in grid]):
                if self.up(block, grid):
                    return f"{block} UP"
                elif self.down(block, grid):
                    return f"{block} DOWN"
                elif self.left(block, grid):
                    return f"{block} LEFT"
                elif self.right(block, grid):
                    return f"{block} RIGHT" 
            block += 1
    
    def up(self, block, grid):
        indices = [(i,j) for i,row in enumerate(grid) for j, x in enumerate(row) if str(block) == x]
        return all([
            grid[i][indi[1]] == "." or grid[i][indi[1]] == str(block)
            for indi in indices
            for i in range(0, indi[0])
        ])

    def down(self, block, grid):
        indices = [(i,j) for i,row in enumerate(grid) for j, x in enumerate(row) if str(block) == x]
        return all([
            grid[i][indi[1]] == "." or grid[i][indi[1]] == str(block)
            for indi in indices
            for i in range(indi[0], len(grid))
        ])

    def left(self, block, grid):
        indices = [(i,j) for i,row in enumerate(grid) for j, x in enumerate(row) if str(block) == x]
        return all([
            grid[indi[0]][i] == "." or grid[indi[0]][i] == str(block)
            for indi in indices
            for i in range(0, indi[1])
        ])

    def right(self, block, grid):
        indices = [(i,j) for i,row in enumerate(grid) for j, x in enumerate(row) if str(block) == x]
        return all([
            grid[indi[0]][i] == "." or grid[indi[0]][i] == str(block)
            for indi in indices
            for i in range(indi[1], len(grid[0]))
        ])

class MoveBlocks(Picker):
    """The block mover game that requires user to populate choose function in Picker"""
    def __init__(self) -> None:
        assert(hasattr(super(), 'choose'), "solution should be provided in the method 'choose'")
        self.cases = [
            [
                'x...x',
                '.0...',
                '..12.',
                'x...x'
            ],
            [
                'x....x',
                '..0...',
                '..011.',
                'x.333x'
            ],
            [
                'x....x',
                '..11..',
                '..011.',
                'x.333x'
            ],
            [
                'x....x',
                '..333.',
                '..001.',
                'x....x'
            ],
            [
                'x....x',
                '..333.',
                'X.201.',
                'x..11x'
            ],
        ]

    def evacuate_grid(self):
        """A function of the game that runs the solution for different configurations of the grid"""
        for case in self.cases:
            print("------ ---- ---- ---- ----")
            self.move(case)
    
    def move(self, grid:[]):
        """move is a function of the game that removes blocks selected by the solution code"""
        while (nb_blocks := self.get_number_of_blocks(grid)):
            choice = self.choose(nb_blocks, grid)
            [print(row) for row in grid]
            print(choice)
            grid = [row.replace(choice[0], ".") for row in grid]
    
    def get_number_of_blocks(self, grid):
        """nb_blocks is an input to the game. This function helps set up the input"""
        # returns the count of unique digits found (via regex and "set")
        return len({
            number
            for row in grid
            for number in re.findall(r"(\d)", row)
            if re.findall(r"(\d)", row)
        })
    



if __name__ == "__main__":
    blockMover = MoveBlocks()
    blockMover.evacuate_grid()