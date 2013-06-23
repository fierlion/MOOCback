
import random

def number_to_name(number):
    name = ""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "error number_to_name: " + number
    return name
    
def name_to_number(name):
    number = ""
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "error name_to_number: " + name
    return int(number)

def rpsls(name): 
    result=""
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # compute difference of player_number and comp_number modulo five
    difference = (player_number-comp_number)%5
    # use if/elif/else to determine winner
    if difference == 1 or difference == 2:
        result = "Player wins"
    elif difference == 3 or difference == 4:
        result = "Computer wins"
    elif difference == 0:
        result = "Tie"
    else:
        print "error rpsls: " + name
    # print results
    print "Player chooses: " + name
    print "Computer chooses: " + number_to_name(comp_number)
    print result + "!"

rpsls("scissors")

----
#compute value function from quiz 1
import math

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    total = present_value * math.pow((1 + rate_per_period),(periods))
    return total

print future_value(500, .04, 10, 10)
# returns: 745.317442823934
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

----
#compute polygon area from quiz 1
import math

def polygonArea(numSide, lenSide):
    denominator = math.tan(math.pi/numSide)
    total = ((0.25 * numSide) * math.pow(lenSide,2))/denominator
    return total
----
#lucky guess game (codecademy)
from random import randrange

random_number = randrange(1, 10)

count = 0
while count < 3:
    guess = int(raw_input("Enter a guess:"))
    if guess == random_number:
        print ('You win!')
        break
    count+=1
else: 
    print ('You lose.')

