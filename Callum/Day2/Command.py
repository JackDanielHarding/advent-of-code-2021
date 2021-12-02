from enum import Enum

class Command:
    def __init__(self, commandStr: str):
        commandStrSplit = commandStr.split(" ")
        self.direction = Command.GetDirectionFromStr(commandStrSplit[0])
        self.magnitude = int(commandStrSplit[1])
    
    def GetDirectionFromStr(directionStr: str):
        match directionStr:
            case 'forward':
                return Direction.FORWARD
            case 'down':
                return Direction.DOWN
            case 'up':
                return Direction.UP
            case _:
                raise ValueError()
            
class Direction(Enum):
    UNKNOWN = 0
    FORWARD = 1
    DOWN = 2
    UP = 3