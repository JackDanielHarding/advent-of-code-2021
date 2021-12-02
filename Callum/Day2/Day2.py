from Submarines import SubmarinePart1, SubmarinePart2
from Command import Command

sub1 = SubmarinePart1()
sub2 = SubmarinePart2()

with open("./input.txt", "r") as inputFile:
    commandsStr = inputFile.read().splitlines()
    
for commandStr in commandsStr:
    command = Command(commandStr)
    sub1.Execute(command)
    sub2.Execute(command)
    
print(sub1)
print(sub2)