# CaeserCypher class  
This class encodes and decodes a string with a caeser shift, where shift must be -26>= shift <= 26 else error will be throw.  
Have tried using CleanCode practice with naming conventions, magic numbers etc, and tried refactoring it a couple of times. __getCaeserConverterAscii definitely could be refactored a bit more as it has more than one purpose. But yeah. Simple class 

## Usage  
Create a CaeserCypher instance passing the shift value as argument.  
Method 'encodeString' takes the input string and sets member variable caesarMessage to encoded message  
Method 'decodeString' takes the input string and decodes same as above  
Method 'getCaesarMessage' returns the encoded/decoded message  

Example
```python
cypher = CaesarCipher(3)
cypher.encodeString("zab")
print(cypher.getCaesarMessage())
# outputs “cde”

cypher.decodeString("zab")
print(cypher.getCaesarMessage())
#outputs “wxy”
```
  
## Things to keep in mind  
This assumes every input character is is within the alphabet range of 'a' - 'z', given quick google of the definition states that was the intent of the caeser cypher, though some places used captilized alphabet some lowercase. Can extend the range of characters able to encode-decode by ammending self.__A self.__Z in class instantiation