# uses python2
import sys

def FizzBuzz(number):
    #result = []
    for i in range(1,number+1):
        if i%15 == 0:
            #result.append("FizzBuzz")
            print "FizzBuzz"
        elif i%5 == 0:
            #result.append("Buzz")
            print "Buzz"
        elif i %3 == 0:
            #result.append("Fizz")
            print "Fizz"
        else:
            print i
    print
    print "Thanks for playing!"
    return

flag = False
user_input = ""

if len(sys.argv[1:]) == 1:
    try:
        user_input = int(sys.argv[1])
        print "Running FizzBuzz on numbers 1 through {}".format(sys.argv[1])
        print
        flag = True
    except:
        print "Looks like there may have been an issue with the supplied input./nPlease enter an integer value to set the upper limit for this round of FizzBuzz."
        try:
            user_input = int(raw_input())
            flag = True
        except:
            print "Oops, looks like an invalid input was provided again."
else:
    print "Please enter a single integer value and press 'Enter' to set the upper limit for this round of FizzBuzz."
    try:
        user_input = int(raw_input())
        flag = True
    except:
        print "Oops, looks like an invalid input was provided."

if flag:            
    FizzBuzz(user_input)
    print
else:
    print "Ending the program now, please try again."