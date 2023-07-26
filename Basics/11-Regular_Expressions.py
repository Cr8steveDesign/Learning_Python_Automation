from locale import atoi
import re
# Regular Expressions 
# Funny aspect of programming


#Practicing Pattern Matching with Regex

regtext = """
Sure! Below is a regular 15Telephone 478 expressions cheatsheet with some common metacharacters and their meanings. Keep in mind that different 95458 programming languages and tools might have slight variations in syntax and supported features, but these should 19 60 cover the basics
"""

for word in regtext.lstrip().split(" "):
    if word.isdigit():
        print(word)


#Regex not so interesting



"""
Sure! Below is a regular expressions cheatsheet with some common metacharacters and their meanings. Keep in mind that different programming languages and tools might have slight variations in syntax and supported features, but these should cover the basics:

1. **Metacharacters:**
   - `.`: Matches any character except a newline.
   - `^`: Matches the start of a line (or string).
   - `$`: Matches the end of a line (or string).
   - `\`: Escapes a metacharacter (e.g., `\.` matches a literal period).
   - `[]`: Matches any character inside the brackets (e.g., `[aeiou]` matches any vowel).
   - `[^]`: Matches any character not inside the brackets (e.g., `[^0-9]` matches anything except digits).

2. **Quantifiers:**
   - `*`: Matches zero or more occurrences of the previous character/group.
   - `+`: Matches one or more occurrences of the previous character/group.
   - `?`: Matches zero or one occurrence of the previous character/group.
   - `{n}`: Matches exactly 'n' occurrences of the previous character/group.
   - `{n,}`: Matches 'n' or more occurrences of the previous character/group.
   - `{n,m}`: Matches between 'n' and 'm' occurrences of the previous character/group.

3. **Alternation and Grouping:**
   - `|`: Acts as an OR operator (e.g., `cat|dog` matches "cat" or "dog").
   - `()`: Groups patterns together (e.g., `(ab)+` matches "ab", "abab", "ababab", etc.).

4. **Special Sequences:**
   - `\d`: Matches any digit (0-9).
   - `\D`: Matches any non-digit character.
   - `\w`: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore).
   - `\W`: Matches any non-alphanumeric character.
   - `\s`: Matches any whitespace character (space, tab, newline).
   - `\S`: Matches any non-whitespace character.
   - `\b`: Matches a word boundary (position between \w and \W).

5. **Modifiers:**
   - `i`: Case-insensitive matching.
   - `g`: Global matching (matches all occurrences, not just the first one).

6. **Anchors:**
   - `\A`: Matches the start of a string (works like `^` but doesn't depend on the multiline mode).
   - `\Z`: Matches the end of a string (works like `$` but doesn't depend on the multiline mode).
   - `\b`: Matches a word boundary (position between \w and \W).
   - `\B`: Matches a non-word boundary.

7. **Escaped Characters:**
   - `\`: Escapes a special character to match it literally (e.g., `\.` matches a period).

Regular expressions are a powerful tool for pattern matching and text manipulation. However, they can become complex for more advanced patterns, so always refer to the documentation of your programming language or tool for more details and specific syntax rules.

"""