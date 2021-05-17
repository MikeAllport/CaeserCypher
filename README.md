# CaeserCypher class  
This class encodes or decodes a string with a caeser shift, where shift must be 0>= shift <= 26 else error will be thrown.  
Have tried using CleanCode practice with naming conventions, magic numbers etc, and refactored a couple of times. \__getCaeserConverterAscii definitely could be refactored a bit more as it has more than one purpose. But yeah. Simple class 

## Usage  
Create a CaeserCypher instance passing the shift value as argument.  
Method 'getCaeserFromString' takes the input string, and a boolean 'toEncode' indicating whether this is to encoded or decoded. This returns the encoded or decoded string
