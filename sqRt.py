def average (*args):
	return sum(args)/ len(args)

def improve (guess, x):
	return average(guess, x/guess)

def abs(x):
	if (x<0):
		return -(x)
	return x

def goodEnough (guess, x):
	d = abs(guess*guess - x)
	return (d < 0.001)

def sqRt(guess, x):
	while (not goodEnough(guess, x)):
		guess = improve(guess, x)
	return guess

#sqRt for very large or very small
def neoSqRt(guess, x):
	oldGuess = 1
	newGuess = 2
	difference = 1
	while (difference > 0.001):
		oldGuess+=newGuess
		newGuess+=improve(guess, x)
		difference+=newGuess-oldGuess
	return guess 

