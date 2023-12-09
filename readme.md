# Syntactic Rules for Verbosity

## General
- All printing outputs do not automatically have a line break
- Contractions do not count towards the number of words in a line, but they affect the character sum
- Non-alphabetic characters are ignored unless otherwise specified
- Only the last punctuation character is recognized
- Line numbering starts from index 0
- Variables are indicated by words in the poem
    - If the variable is indicated by just one word, the targeted variable is the sum of the indicator word's character values from 1 to 26 modulo the line number of the line in which the indicating word is placed.
        - eg. "life" on line 3 gets 32%3 = 2, and so indicates the variable declared on line 2
    - If indicated by multiple words, the targeted variable is the sum of the character values of all the indicator words' first character multiplied by the number of words, modulo the line number of the line in which the indicating words are placed.
        - eg. "for life" on line 6 gets (6+12)*2%6 = 0, and so indicates the variable declared on line 0
- Supported operations:
    - variable declaration, assignment
    - output
    - mathematical operations
        - add/sub/mul/div/mod/equal
    - goto by line number
    - if/else
        - if (var > 0 or var > var) goto, else goto
        - if (var > 0 or var > var) execute, else execute
        - directly nested if statements are not supported, but you can jump to another if statement after evaluation
- Conjunctions are special print characters and are ignored if in the beginning of a line.
    - The line is treated as starting from the first non-auxilary, conjunction, determiner, or adposition word.
    - For each line, if the second to last word is a conjunction, print a linebreak. This is done before any outputs from the line itself.
    - For each line, if the last word is a conjunction, print a space. This is done after any outputs from the line itself. This is invalid if there are punctuation marks past the last word
- Determiners(articles, quantifiers, etc.) and adpositions (in, to, etc.) are ignored when at the beginning of a line.
    - The line is treated as starting from the first non-auxilary, conjunction, determiner, or adposition word.

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
- A capitalized first word outputs the variable indicated by the second word as a ASCII character. The sign value is ignored, and floats are rounded down.
- A lowercase first word outputs the variable indicated by the second word as an integer.
- If the line ends in a question mark, generate a random value between 0 and 1024.
    - assign the value to the variable indicated by the two words
### lines of length >= 3 are operations
Function of lines are determined by the POS of their first word
- Nouns indicate mathematical operations. Two operands only; the result is assigned to the first operand
    - the operation is determined by the ending punctuation
    - '.': subtraction / ',': division / '!': multiplication / '?': modulo / ';': division and rounded down to full number / none: addition
    - other punctuation marks are viewed as assignment for mathematical operations
    - if the line has an even number of words, the second operand is read as a variable
        - for a line with length L:
            - the first L/2 words indicate the first variable
            - the second L/2 words indicate the second variable
    - if the line has an odd number of words, the second operand is read as a integer
        - for a line with length L+1:
            - the first (L-1)/2 words (floor first half) indicate the first variable
            - the second (L+1)/2 words form the integer
            - the integer is the sum of the words' character values from 1 to 26, then divided by (L-1)/2
- Adverbs indicate goto
    - jump to the line indicated by the sum of the words' first character's values multiplied by the number of words in the line, modulo the number of lines in the poem
    - you cannot jump to a variable declaration
    - jumping to an "if" statement does not circumvent conditional evaluation, but jumping to and "else" statement enforces execution of the "else" without conditional evaluation
- Verbs indicate if/else: goto statements
    - jump if the variable indicated by the first two words is greater than 0, if the sentence is indented by any number of tabs or >4 spaces
    - jump if the variable indicated by the first word is greater than the variable indicated by the second word, if the sentence is not indented
    - the next line is an else clause if the statement ends in a period
        - execute the next line as any statement, unless it is an if statement, in which case the statement is evaluated in the same way as an adverb jump statement
        - the else line counts towards the number of lines in the poem
    - if the comparison is true, the goto method is determined by the POS of the third word
        - if it is an adverb, then the remainder of the line starting from and including the adverb is parsed as an adverb goto statement
        - otherwise, jump to the line of the value of the variable indicated by the remaining words
- Adjectives indicate if/else: goto statements that are the inverse of verb statements
    - jump if the variable indicated by the first two words is less than or equal to 0, if the sentence is indented by any number of tabs or >4 spaces
    - jump if the variable indicated by the first word is less than or equal to the variable indicated by the second word, if the sentence is not indented
    - the next line is an else clause if the statement ends in a period
        - execute the next line as any statement, unless it is an if statement, in which case the statement is evaluated in the same way as an adverb jump statement
        - the else line counts towards the number of lines in the poem
    - if the comparison is true, the goto method is determined by the POS of the third word
        - if it is a verb, then the remainder of the line starting from and including the verb is parsed as an adverb goto statement
        - otherwise, jump to the line of the value of the variable indicated by the remaining words
- Opening words with other POS tags are ignored
    - the whole line is discarded in computation, but still counts towards the line count
    - these lines can be jumpeed to, but still do nothing