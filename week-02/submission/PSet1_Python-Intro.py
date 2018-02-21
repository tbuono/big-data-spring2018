
# Problem Set 1: Intro to Python

#A1. Create a list containing any 4 strings.
mylist = ['hi', 'i love you', 'what are you doing', 'tomoatoe']

#A2. Print the 3rd item in the list - remember how Python indexes lists!
mylist[2]

#A3. Print the 1st and 2nd item in the list using [:] index slicing.
mylist[0:2]

#A4. Add a new string with text “last” to the end of the list and print the list.
append = ['last']
mylist.extend (append)
print(mylist)

#A5. Get the list length and print it.
len(mylist)
#for repetitiveness
print (len(mylist))

#A6. Replace the last item in the list with the string “new” and print
mylist[mylist.index('last')] = 'new'
print(mylist)

## B. Strings

#Given the following list of words stored as strings, complete the following tasks:
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']

#B1. Convert the list into a normal sentence with [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join), then print.
sentence = " ".join(sentence_words)
print (sentence)

#B2. Reverse the order of this list using the `.reverse()` method, then print. Your output should begin with `[“them”, ”visualize”, … ]`.
#''.reverse(sentence)
revsentence = sentence_words.reverse()
print(sentence_words)

#B3. Now use the [`.sort()` method](https://docs.python.org/3.3/howto/sorting.html) to sort the list using the default sort order.
sentence_words.sort()
sentence_words


#B4. Perform the same operation using the [`sorted()` function](https://docs.python.org/3.3/howto/sorting.html). Provide a brief description of how the `sorted()` function differs from the `.sort()` method.

## __.sort() modifies __ to be a sorted string, when __ is called.
## sorted(__) does not modify __; it merely sorts __
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
test = sorted(sentence_words)
print(test)

#B5. Extra Credit: Modify the sort to do a case [case-insensitive alphabetical sort](http://matthiaseisen.com/pp/patterns/p0005/).
sentence_words.sort()
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
case_sensitive = sorted(sentence_words, key=lambda x: x.lower())
print(case_sensitive)

## C. Random Function

#Python snippet that generates a random integer:
from random import randint
# this returns random integer: 100 <= number <= 1000
num = randint(100, 1000)
print(num)

#own function, low and high supplied by user, low number being optional (default to 0)
#http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard

# this defines randit by importing from the random library
from random import randint
# this creates a function to make user input a low and high number
def userinput():
    low = int(input("Give me one low number"))
    # avoids any negative numbers in the system
    if low < 0:
        low = 0
    high = int(input("Give me one high number"))
    return randint(low, high)
#runs the userinput function with low and high variables
userinput()

#Testing function
assert(0 <= userinput() <= 100)
assert(50 <= userinput() <= 100)

# Inputs: Two `integers` that will be used as lower and upper bounds of the function. If the user does not pass a lower bound, the default value should be zero. Outputs: Print a random number within the established bounds

## D. String Formatting Function
#Write a function that expects two inputs. The first is a title that may be multiple words, the second is a number. Given these inputs, print the following string (replacing `n` and `title` with dynamic values passed to the script).

sentence = 'The number {n} bestseller today is: {title}'
rank = input ("Rank this book between 1 and 15")
book = input ("What's your favorite book?")
Book= book.title()
response = f"The number {rank} bestseller today is: {Book}."
print(response)

# Inputs: An integer representing the position on the bestseller list and a string representing the a title. If not already titlecased, the function should [titlecase] the string. Outputs: Print a string of the format: `The number n bestseller today is: title`. You should use an `f` string or the `.format()` method to format the printed string.

## E. Password Validation Function

# Write a function that evaluates the strength of a password. Ask the user to input a password that meets the criteria listed below. You can either use the Python [`input`](https://docs.python.org/3/library/functions.html#input) built-in function, or just pass the password as a function argument. Validate that the user’s password matches this criteria. If password is valid, print a helpful success message.

def passcheck():
    pw = (input("Input a STRONG password... i.e. 1) 8-14 characters long; 2) includes at least 2 digits/numbers; 3) includes at least 1 uppercase letter; 3) includes at least 1 special character from this set: `['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']`"))
    length_pw = len(pw)
    #checks if pw is too short
    if (length_pw <8):
        print("Fail, password too short.")
    #checks if pw is too long
    if (length_pw >14):
        print("Fail, password too long")
    #checks if pw has two digits
    if sum([i.isdigit() for i in pw])<2:
        print("Fail, password needs at least two numbers.")
        #checks if pw has at least one uppercase
    if sum([i.isupper() for i in pw])<1:
        print("Fail, password needs at least one uppercase.")
    #checks to see if pw has at least one special char
    if (len(set(pw) & set('!?@#$%^&*()-_+=')))<1:
        print("Fail, password needs at least one special character")
    else:
        print ("Congrats, this is an excellent password!")
passcheck()

# Inputs: A `string` that will be tested for the password requirements. The string can be passed as an argument to the function, or as an input through the `input` function. Outputs: A success message if the password works, an error message if it fails.

## F. Exponentiation Function

# Create a function called `exp` that accepts two integers and then `return`s an exponentiation, **without using the exponentiation operator** (`**`). You may assume these are positive integers. Use at least one custom-defined function.

def exp():
    x = (int(input ("Give me one number")))
    y = (int(input ("Give me a second number, to act as the exponent")))
    temp = 1
    for i in range(y):
        temp = x * temp
    return temp
exp()


# Inputs: 1. An `integer` that will be recursively multiplied, 2. An `integer` that will define the number of times to multiply the number to get the exponentiation.
# Outputs: An `integer` that is the result of the exponentiation.

# Hint: You can recursively multiply a number. The second function parameter defines the number of times the recursive loop happens. Every time the loop happens, you can redefine the variable that gets multiplied.

## G. Extra Credit: Min and Max Functions

Write your own versions of the Python built-in functions `min()` and `max()`. They should take a list as an argument and return the minimum or maximum element. Assume lists contain numeric items only.

# min with three items in list, user input
def minn(a, b, c):
     list = [a, b, c]
     list.sort()
     return list [0]
minn(4, 6, 3)

# min with a pre-determined list, a
def minn():
     a = [5,3,6,2,4]
     a.sort()
     return a [0]
minn()

#maximum, with a pre-determined list, b
def maxx():
    b = [ 4, 6, 3, 10, 400]
    b.sort()
    b.reverse()
    return b [0]
maxx()

#trying to use the Hint, min application
#close, but no cigar
def min_new():
    c = [3, 5, 9, 1]
    #temp = c[0]
    for i in range(len(c)):
        temp = c[0]
        if temp < c[1]:
            temp = c[0]
    return temp
#print(temp)
min_new()

# Inputs: A `list` of `numbers` to be tested. Outputs: A `number` of the list that is the maximum or minimum.
# Hint: Pick the first element as the minimum/maximum and then loop through the elements. Each time you find a smaller/larger element, update your minimum/maximum.
