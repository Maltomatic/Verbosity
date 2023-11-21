# Syntactic Rules for Verbosity

## General
- Non-alphabetic characters are ignored unless otherwise specified
- Only the last punctuation character is recognized
- Line numbering starts from index 0
- Variables are indicated by words in the poem
    - If the variable is indicated by just one word, the targeted variable is the sum of the indicator word's character values from 1 to 26 modulo the line number of the line in which the indicating word is placed.
        - eg. "life" on line 3 gets 32%3 = 2, and so indicates the variable declared on line 2
    - If indicated by multiple words, the targeted variable is the sum of the character values of all the indicator words modulo the line number of the line in which the indicating words are placed.
        - eg. "for life" on line 6 gets 71%6 = 5, and so indicates the variable declared on line 5
- Supported operations:
    - variable declaration, assignment
    - output
    - mathematical operations
        - add/sub/mul/div/mod/equal
    - goto by line number
    - if/else
        - if (var > 0 or var > var) goto, else goto
        - if (var > 0 or var > var) execute, else execute
- Auxilary verbs and conjunctions are special print characters and are ignored in other processing.
    - That is, they are not included in the indication of variables or values.
    - If they are at the beginning of a line, the line is treated as starting from the second word.
    - Each time an auxilary verb is encountered, print a space.
    - Each time a conjunction is encountered, print a linebreak. 

## Line operations
The length is counted after stripping non-alphabetic characters from the line.
    - eg. "1, 2, 3" has length 0
    - eg. "This is a 4-word-line" is viewed as 4 words, as "3-word-line" is one singular element
### lines of length = 0: special action depends on the ending punctuation
- '?': generate a random value between 0 and 1024, then assign to the last created variable
    - if there is no last variable, the value is printed directly
- '!': exit program unconditionally
- the rest are ignored, but this line still factors into the line count
### lines of length = 1: declare a variable
- The variable is addressed as the poem line number at which it is created, starting with index 0
- The initialization value is the sum of its character values from 1 to 26. 
- If capitalized, the variable is negative. If the line ends in '.', the character values shift to range from 0 to 25 so a/A = 0 instead
    - eg. "doom" on line 2 is equivalent to `var2 = 47`
    - eg. "Doom." on line 2 is equivalent to `var2 = -43`
### lines of length = 2: output a variable, or generate a random value
- A capitalized first word outputs the variable indicated by the second word, modulo 26, as a char. The sign value is ignored.
- A lowercase first word outputs the variable indicated by the second word as an integer.
- If the line ends in a question mark, generate a random value between 0 and 1024.
    - assign the value to the variable indicated by the two words
### lines of length >= 3 are operations
Function of lines are determined by the POS of their first word
- Nouns indicate mathematical operations. Two operands only; the result is assigned to the first operand
    - the operation is determined by the ending punctuation
    - '.': subtraction / ',': addition / '!': multiplication / '?': division / ';': modulo / none: assignment
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
- Adverbs indicate goto
    - jump to the line indicated by the sum of the words' character values modulo the number of lines in the poem
    - you cannot jump to a variable declaration
- Verbs indicate if/else: goto statements
    - jump if the variable indicated by the first two words is greater than 0, if the sentence is indented by >4 spaces
    - jump if the variable indicated by the first word is greater than the variable indicated by the second word, if the sentence is not indented
    - the next line is an else clause if the statement ends in a period
        - the clause is parsed as any other statement
    - if the comparison is true, the goto method is determined by the POS of the third word
        - if it is an adverb, then the remainder of the line starting from the adverb is parsed as an adverb goto statement
        - otherwise, jump to the line of the value of the variable indicated by the remaining words
            - if there is no such line, the program proceeds directly skipping the if (and else, if any) statement(s)
    - if it is not true, continue from the next line
- Adjectives indicate if/else: execute statements
    - execute the remainder of the statement if the variable indicated by the first two words is greater than 0, if the sentence is indented by >4 spaces
    - execute if the variable indicated by the first word is greater than the variable indicated by the second word, if the sentence is not indented
    - execution excludes the first two words
        - that is, determination of action starts from the third word in the line, and computation of word/char length starts from the third word in the line to the end of the line 
    - the next line is an else clause if the statement ends in a period
        - the clause is parsed as any other statement
- Opening words with other POS tags are ignored

