# Syntactic Rules for Verbosity

## General
- Line numbering starts from index 0
- Variables are indicated by words in the poem
    - If the variable is indicated by just one word, the targeted variable is the sum of the indicator word's character values from 1 to 26 modulo the line number of the line in which the indicating word is placed.
        - eg. "life" on line 3 gets 32%3 = 2, and so indicates the variable declared on line 2
    - If indicated by multiple words, the targeted variable is the sum of the character values of all the indicator words modulo the line number of the line in which the indicating words are placed.
        - eg. "for life" on line 6 gets 71%6 = 5, and so indicates the variable declared on line 5

## Line operations
### lines of length = 1: declare a variable
 - The variable is addressed as the poem line number at which it is created, starting with index 0
- The initialization value is the sum of its character values from 1 to 26. 
- If capitalized, the variable is negative. If the line ends in '.', the character values shift to range from 0 to 25 so a/A = 0 instead
    - eg. "doom" on line 2 is equivalent to `var2 = 47`
    - eg. "Doom." on line 2 is equivalent to `var2 = -43`
### lines of length = 2: output a variable
- A capitalized first word outputs the variable indicated by the second word, modulo 26, as a char. The sign value is ignored.
- A lowercase first word outputs the variable indicated by the second word as an integer.
### lines of length >= 3 are operations
Function of lines are determined by the POS of their first word
 - nouns indicate mathematical operations. Two operands only; the result is assigned to the first operand
    - the operation is determined by the ending punctuation
    - '.': subtraction // ',': addition // '!': multiplication // '?': division // ';': modulo
    - other punctuation marks are ignored for mathematical operations
    - if the line has an even number of words, the second operand is read as a variable
        - for a line with length L:
            - the first L/2 words indicate the first variable
            - the second L/2 words indicate the second variable
    - if the line has an odd number of words, the second operand is read as a integer
        - for a line with length L+1:
            - the first L/2 words form the first variable
            - the second L/2 words form the integer
            - the integer is the sum of the words' character values from 1 to 26, then divided by L/2
- verbs 
