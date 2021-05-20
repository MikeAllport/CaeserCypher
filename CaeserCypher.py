class CaesarCypher():
    def __init__(self, charShift: int):
        if charShift > 26 or charShift < -26:
            raise Exception("Invalid caesar shit exceeding alphabet or lower than 0")
        self.charShift = charShift
        self.caesarMessage = ""
        self.__Z = ord('z')
        self.__A = ord('a')
        
    def encodeString(self, stringToEncode: str):
        self.caesarMessage = stringToEncode
        self.__setCaesarMessage(self.charShift)
    
    def decodeString(self, stringToDecode: str):
        self.caesarMessage = stringToDecode
        self.__setCaesarMessage(-self.charShift)
        
    def __setCaesarMessage(self, shift: int):
        caesarString = ""
        for character in self.caesarMessage:
            caesarString = caesarString + self.__getCaesarConvertedAscii(character, shift)
        self.caesarMessage = caesarString
                
    def __getCaesarConvertedAscii(self, inputCharacter: str, shift: int):
        if not self.__characterInAlpha(inputCharacter):
            return inputCharacter
        
        newAsciiValue = ord(inputCharacter) + shift

        howManyGreaterThanZ = self.__asciiValueAboveZ(newAsciiValue)
        if howManyGreaterThanZ > 0:
            return chr(self.__A - 1 + howManyGreaterThanZ)
        
        howManyLessThanA = self.__asciiValueBelowA(newAsciiValue)
        if howManyLessThanA > 0:
            return chr(self.__Z + 1 - howManyLessThanA)

        return chr(newAsciiValue)
    
    def __characterInAlpha(self, char: str):
        return ord(char) in range (self.__A, self.__Z + 1)
    
    def __asciiValueAboveZ(self, asciiInput: int):
        return asciiInput - self.__Z
    
    def __asciiValueBelowA(self, asciiInput: int):
        return self.__A - asciiInput
    
    def getCaesarMessage(self):
        return self.caesarMessage