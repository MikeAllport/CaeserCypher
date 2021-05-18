class CaesarCypher():
    def __init__(self, charShift: int):
        if charShift > 26 or charShift < 0:
            raise Exception("Invalid caesar shit exceeding alphabet or lower than 0")
        self.charShift = charShift
        self.caesarMessage = ""
        self.__Z = 122
        self.__A = 97
        
    def encodeString(self, stringToEncode: str):
        self.caesarMessage = stringToEncode
        self.__setCaesarMessage()
    
    def decodeString(self, stringToDecode: str):
        self.caesarMessage = stringToDecode
        self.__invertCharShift()
        self.__setCaesarMessage()
        self.__invertCharShift()
        
    def __invertCharShift(self):
        self.charShift = -self.charShift
        
    def __setCaesarMessage(self):
        caesarString = ""
        for character in self.caesarMessage:
            caesarString = caesarString + self.__getCaesarConvertedAscii(character)
        self.caesarMessage = caesarString
                
    def __getCaesarConvertedAscii(self, inputCharacter: str):
        newAsciiValue = ord(inputCharacter) + self.charShift
        
        howManyGreaterThanZ = self.__asciiValueAboveZ(newAsciiValue)
        if howManyGreaterThanZ > 0:
            return chr(self.__A - 1 + howManyGreaterThanZ)
        
        howManyLessThanA = self.__asciiValueBelowA(newAsciiValue)
        if howManyLessThanA > 0:
            return chr(self.__Z + 1 - howManyLessThanA)

        return chr(newAsciiValue)
    
    def __asciiValueAboveZ(self, asciiInput: int):
        return asciiInput - self.__Z
    
    def __asciiValueBelowA(self, asciiInput: int):
        return self.__A - asciiInput
    
    def getCaesarMessage(self):
        return self.caesarMessage
