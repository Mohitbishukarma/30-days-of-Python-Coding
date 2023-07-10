import re # importting regex 

"""
Top Regular Expressions : Cheat Sheet
Character classes
.	            ->  any character except newline
\w \d \s	    ->  word, digit, whitespace
\W \D \S        ->	not word, digit, whitespace
[abc]	        ->  any of a, b, or c
[^abc]	        ->  not a, b, or c
[a-g]	        ->  character between a & g

Anchors
^abc$	       ->   start / end of the string
\b	           ->   word boundary

Escaped characters
\. \* \\	   ->   escaped special characters
\t \n \r	   ->   tab, linefeed, carriage return
\u00A9	       ->   unicode escaped ©

Groups & Lookaround
(abc)	       ->   capture group
\1	           ->   backreference to group #1
(?:abc)        ->	non-capturing group
(?=abc)	       ->   positive lookahead
(?!abc)        ->	negative lookahead

Quantifiers & Alternation
a* a+ a?       ->	0 or more, 1 or more, 0 or 1
a{5} a{2,}     -?	exactly five, two or more
a{1,3}         ->	between one & three
a+? a{2,}?     ->	match as few as possible
ab|cd          ->	match ab or cd

"""


# Creating regex objects
# pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
# phoneNumRegex = re.compile(pattern)

# Matching Regex objects
# mo = phoneNumRegex.search("THis is phone number 845-345-4534")
# print("Phne Number Found: "+mo.group())

# More pattern matching with regular ecpressions
# Grouping with parenthisis
# pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
# phoneNumRegex = re.compile(pattern)
# mo = phoneNumRegex.search("THis is phone number 845-345-4534")
# print("Phone Number Found: "+mo.group())
# print("Area Code: "+mo.group(1))
# print("Remaining Num: "+mo.group(2))


# mo.groups() -> returns a tuple of groups
# print(mo.groups())


# Matching Multiple groups with Pipe
# | -> character is called a Pipe (eg r'Mohit|Rajan' will match Mohit or Rajan based on first occurance)

# nameRegex = re.compile(r'Mohit|Rajan')
# mo = nameRegex.search("Mohit and Rajan are good friends.")
# print(mo.group())

# mo = nameRegex.search("Rajan and Mohit  are good friends.")
# print(mo.group())

# eg
# heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = heroRegex.search(" I am a Batcopter")
# print(mo.group())


# Optional matching with ? -> match one or zero
# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneRegex.search("This is my phone 978-452-4564")
# print(mo.group())
# mo = phoneRegex.search("This is my phone 452-4564")
# print(mo.group())

# Matching Zero or More with the star (* -> match zero or more)
# heroRegex = re.compile(r'Bat(wo)*man')
# mo = heroRegex.search("I am a Batman")
# print(mo.group())
# mo = heroRegex.search("I am a Batwoman")
# print(mo.group())
# mo = heroRegex.search("I am a Batwowowowoman")
# print(mo.group())


# Matching One or More with the Plus
# heroRegex = re.compile(r'Bat(wo)+man')
# mo = heroRegex.search("I am a Batman") # will return None
# mo = heroRegex.search("I am a Batwoman")
# print(mo.group())
# mo = heroRegex.search("I am a Batwowowowoman")
# print(mo.group())