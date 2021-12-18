from Packet import Packet

with open("./input.txt", "r") as inputFile:
    input = inputFile.read()
    
inputBits = bin(int('1'+input, 16))[3:]
packet = Packet(inputBits)

print(f'Sum of version numbers of all contained packets: {packet.NestedVersionSum()}')
print(f'Packet value: {packet.PacketValue()}')