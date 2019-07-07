import math
import re
from operator import itemgetter
'''
#1 Question
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
numberlst = range(2000,3200)
outputnumberlst = []

for number in numberlst:
    result = number / 7
    if result%7 == 0:
        outputnumberlst.append(str(number))

print("1#")
print(",".join(outputnumberlst))
print("\n")


'''
#2 Question
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
#factorialNumber = int(input("factorial from n="))
factorialNumber = 8
factorial = 1
for num in range(1,factorialNumber+1):
    factorial = factorial * num

print("#2")
print("factorial from {} is {}".format(factorialNumber,factorial))
print("\n")


'''
#3 Question
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
integralDic = {}
i = 8
for num in range(1,i):
    integralDic[num] = num * num

print("#3")
print(integralDic)
print("\n")



'''
#4 Question
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
input = "34,67,55,33,12,98"
splitInput = input.split(",")
splitInputtpl = tuple(splitInput)

print("#4")
print(splitInput)
print(splitInputtpl)
print("\n")



'''
#5 Question
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class stringhandler:

    def __init__(self,input, changedStringupper = "", changedStringlower =""  ):
        self.input = input
        self.changedStringupper = changedStringupper
        self.changedStringlower = changedStringlower

    def returnlower(self):
        self.changedStringlower = self.input.lower()

    def returnupper(self):
        self.changedStringupper = self.input.upper()

FirstStringElement = stringhandler("das soll alles gross geschrieben werden 1 ")
FirstStringElement.returnupper()
print("#5")
print(FirstStringElement.changedStringupper)

SecondStringElement = stringhandler("Das SOLL in alles klein geschrieben WERDEN 2")
SecondStringElement.returnlower()
print(SecondStringElement.changedStringlower)
print("\n")



'''
#6 Question
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
def calculate(lst,C=50,H=30):
    Resultlst = []
    for num in lst:
        Q = (2*C*num)/H
        Result = math.sqrt(Q)
        Resultlst.append(int(Result))
    return Resultlst

numlst = [100,150,180]

print("#6")
print(calculate(numlst))
print("\n")



'''
#7 # QUESTION:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
printThe element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a
console input in a comma-separated form.
'''
def twodimarray(x,y):
    rownum = x
    colnum = y
    twodimarray = [[0 for ynum in range(0,colnum)]for xnum in range(0,rownum)]
    for row in range(0,rownum):
        for col in range(0,colnum):
            twodimarray[row][col] = row*col
    return twodimarray

print('#7')
print(twodimarray(3,8))
print('\n')

'''
#8 # QUESTION:
Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a
console input.
'''
wordinput = 'Hello,Bag,House,Asphalt'
wordlst = wordinput.split(',')
wordsort = sorted(wordlst)

print('#8')
print(','.join(wordsort))
print('\n')

'''
#9 # QUESTION:
'''
Sentancelst = ['Hello my name is Lukas', 'Hello my name is luisa']
print('#9')
for sentance in Sentancelst:


    print(sentance.upper())
print('\n')

'''
#10 # QUESTION:
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to
be a console input.
We use set container to remove duplicated data automatically and then use
sorted() to sort the data.
'''
sentence = 'hello world and practice makes perfect and hello world again'
words = sentence.split(' ')
wordlst = []

for word in words:
    if word not in wordlst:
        wordlst.append(word)
sortedwords = sorted(wordlst)

print('#10')
print(' '.join(sortedwords))
print('\n')

'''
#11 # QUESTION:
Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question,
it should be assumed to be a console input.
'''
numbers = '0101,0011,1010,1001'
numberslst = numbers.split(',')
results = []
for number in numberslst:
    if int(number) % 5 == 0:
        results.append(number)

print('#11')
print(results)
print('\n')



'''
#12 # QUESTION:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
numlst = []
for num in range(1000,3000):
    if num % 2 == 0:
        numlst.append(num)

print('#12')
print(numlst)
print('\n')



'''
#13 # QUESTION:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
str = 'hello world! 123'
letters = []
digits = []

for letter in str:

    if letter.isalpha():
        letters.append(letter)
    elif letter.isdigit():
        digits.append(letter)

print('#13')
print('we found {} letters and {} Digits'.format(len(letters),len(digits)))
print('\n')

'''
#14 # QUESTION:
Write a program that accepts a sentence and calculate the number of upper case letters
and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
str = 'Hello world!'
upper = []
lower = []

for letter in str:
    if letter.isupper():
        upper.append(letter)
    elif letter.islower():
        lower.append(letter)

print('#14')
print('we found {} upper letters and {} lower letters'.format(len(upper),len(lower)))
print('\n')



'''
#15 # QUESTION:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
def addition(a):
    n0 = a
    n1 = int('%s%s' % (a,a))
    n2 = int('%s%s%s' % (a,a,a))
    n3 = int('%s%s%s%s' % (a,a,a,a))

    result = n0+n1+n2+n3
    return result

print('#15')
print(addition(9))
print('\n')


'''
#16 # QUESTION:
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''
lst16 = [1,2,3,4,5,6,7,8,9,10]
lstcom = [x**2 for x in lst16 if x %2 == 0]

print('#16')
print(lstcom)
print('\n')

'''
#17 # QUESTION:
Write a program that computes the net amount of a bank account based a transaction log
from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
banklog = {'D1':300, 'D2':300, 'W1':200, 'D3':100}
D =0
W =0
for log in banklog:
    if 'D' in log:
        D = D + banklog[log]
    elif 'W' in log:
        W = W + banklog[log]

bankaccount = D - W

print('#17')
print('Your account has {} Euro'.format(bankaccount))
print('\n')


'''
#18 # QUESTION:
A website requires the users to input username and password to register.
Write a program to check the
validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords
and will check them according to the above criteria. Passwords that match
the criteria are to be printed,
each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1 reg regex regx
'''
passwordlst = ['ABd1234@1','aF16','2w3E*','We3345']

print('#18')
for password in passwordlst:
    if len(password) < 6 or len(password) > 12:
        continue
    if not re.search('[a-z]',password):
        continue
    if not re.search('[0-9]',password):
        continue
    if not re.search('[A-Z]',password):
        continue
    if not re.search('[$@#]',password):
        continue
    print('{} is a password'.format(password))
print('\n')

'''
#19 # QUESTION:
You are required to write a program to sort the (name, age, height) tuples
by ascending order where name
is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85ß
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
('Json', '21', '85'), ('Tom', '19', '80')]
'''
datatpl = (
('Tom',19,80),
('John',20,90),
('Jony',17,91),
('Jony',17,93),
('Json',21,85)
)
datatplsort = sorted(datatpl, key=itemgetter(0,1,2))

print('#18')
print(datatplsort)
print('\n')


'''
#20 # QUESTION:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.
'''
class math20:
    def __init__(self,x,lst=[]):
        self.x = x
        self.lst = lst

    def divider(self):
        for num in range(0,self.x):
            if num % 7 == 0:
                self.lst.append(num)

calculation1 = math20(100)
calculation1.divider()

print('#20')
str20 = 'we found {} numbers that can be divided by {} this are the numbers {}'
print(str20.format(len(calculation1.lst),calculation1.x,calculation1.lst))
