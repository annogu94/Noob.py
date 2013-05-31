pyg = 'ay'

# The equivalent of gets.chomp in Ruby
original = raw_input('Enter a word:')
# Downcases input string
word = original.lower()
# Stores first character of string in memory
first = str(word[0])
vowel = ['a', 'e', 'i', 'o', 'u']


if len(original) > 0 and original.isalpha():
    # If the variable 'first' is an element of the list vowel, do the following
    if first in vowel:
        print word + pyg
    else:
    # If it is not, do the following
        new_word = str(word[1:]) + first + pyg
        print new_word
else:
  # If user types nothing, print 'empty'
    print 'empty'
