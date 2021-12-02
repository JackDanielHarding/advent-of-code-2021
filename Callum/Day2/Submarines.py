from Command import Command, Direction

class SubmarinePart1:
    
    def __init__(self):
        self.horizontalPos = 0
        self.depth = 0
    
    def Execute(self, command: Command):
        match command.direction:
            case Direction.FORWARD:
                self.Forward(command.magnitude)
            case Direction.DOWN:
                self.Down(command.magnitude)
            case Direction.UP:
                self.Up(command.magnitude)
    
    def Forward(self, distance: int):
        self.horizontalPos += distance
        
    def Down(self, distance: int):
        self.depth += distance
        
    def Up(self, distance: int):
        self.depth -= distance
        
    def __str__(self):
        return f'Horizontal: {self.horizontalPos}, Depth: {self.depth}, Total: {self.horizontalPos * self.depth}'
        
class SubmarinePart2:
    
    def __init__(self):
        self.horizontalPos = 0
        self.depth = 0
        self.aim = 0
    
    def Execute(self, command: Command):
        match command.direction:
            case Direction.FORWARD:
                self.Forward(command.magnitude)
            case Direction.DOWN:
                self.Down(command.magnitude)
            case Direction.UP:
                self.Up(command.magnitude)
    
    def Forward(self, distance: int):
        self.horizontalPos += distance
        self.depth += self.aim * distance
        
    def Down(self, angle: int):
        self.aim += angle
        
    def Up(self, angle: int):
        self.aim -= angle
        
    def __str__(self):
        return f'Horizontal: {self.horizontalPos}, Depth: {self.depth}, Aim: {self.aim}, Total: {self.horizontalPos * self.depth}'