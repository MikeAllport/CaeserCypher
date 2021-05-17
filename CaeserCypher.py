class CaeserCypher():
    def __init__(self, charShift: int):
        if charShift > 26 or charShift < 0:
            raise Exception("Invalid caeser shit exceeding alphabet or lower than 0")
        self.__CHAR_SHIFT = charShift
        self.__Z = 122
        self.__A = 97
        
    def getCaeserFromString(self, inputStr: str, toEncode: bool):
        caeserString = ""
        for character in inputStr:
            caeserString = caeserString + self.__getCaeserConverterAscii(character, toEncode)
        return caeserString
                
    def __getCaeserConverterAscii(self, inputCharacter: str, toEncode: bool):
        # are we encoding or decoding
        if toEncode:
            newAsciiValue = ord(inputCharacter) + self.__CHAR_SHIFT
        else:
            newAsciiValue = ord(inputCharacter) - self.__CHAR_SHIFT
            
        # handle if encoded > z
        howManyGreaterThanZ = self.__asciiValueAboveZ(newAsciiValue)
        if howManyGreaterThanZ > 0:
            return chr(self.__A - 1 + howManyGreaterThanZ)
        
        # handle if < a
        howManyLessThanA = self.__asciiValueBelowA(newAsciiValue)
        if howManyLessThanA > 0:
            return chr(self.__Z + 1 - howManyLessThanA)

        # its fine
        return chr(newAsciiValue)
            
    
    def __asciiValueAboveZ(self, asciiInput: int):
        return asciiInput - self.__Z
    
    def __asciiValueBelowA(self, asciiInput: int):
        return self.__A - asciiInput