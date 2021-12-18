from functools import reduce

class Packet():
    def __init__(self, bits: str):
        
        self.version = int(bits[0:3], 2)
        self.type = int(bits[3:6], 2)
        self.subPackets = []
        
        if self.type == 4:
            index = 6
            val = ""
            while True:
                firstBit = bits[index]
                val += bits[index+1:index+5]
                index += 5
                if firstBit == '0':
                    self.literal = int(val, 2)
                    self.lastIndex = index
                    break
        else:
            self.lType = bits[6]
            if self.lType == '0':
                index = 22
                subPacketBits = bits[7:index]
                subPacketBitsInt = int(subPacketBits, 2)
                parsedBits = 0
                while True:
                    subPacket = Packet(bits[index:index+subPacketBitsInt])
                    self.subPackets.append(subPacket)
                    parsedBits += subPacket.lastIndex
                    index += subPacket.lastIndex
                    if parsedBits >= subPacketBitsInt:
                        self.lastIndex = index
                        break
            else:
                index = 18
                subPackets = int(bits[7:index], 2)
                parsedSubPackets = 0
                while True:
                    subPacket = Packet(bits[index:])
                    self.subPackets.append(subPacket)
                    parsedSubPackets += 1
                    index += subPacket.lastIndex
                    if parsedSubPackets >= subPackets:
                        self.lastIndex = index
                        break
                    
    def NestedVersionSum(self) -> int:
        return self.version + sum(packet.NestedVersionSum() for packet in self.subPackets)
    
    def PacketValue(self) -> int:
        subPacketValues = (packet.PacketValue() for packet in self.subPackets)
        match self.type:
            case 0:
                return sum(subPacketValues)
            case 1:
                return reduce(lambda x, y: x * y, subPacketValues)
            case 2:
                return min(subPacketValues)
            case 3:
                return max(subPacketValues)
            case 4:
                return self.literal
            case 5:
                return 1 if next(subPacketValues) > next(subPacketValues) else 0
            case 6:
                return 1 if next(subPacketValues) < next(subPacketValues) else 0
            case 7:
                return 1 if next(subPacketValues) == next(subPacketValues) else 0