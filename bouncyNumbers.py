#Bouncy numbers
#Problem 112
#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#Find the least number for which the proportion of bouncy numbers is exactly 99%.


def isBouncy(num):
    # convert input number in to list of characters
    charList = list(str(num))
    # sor
    charListAsc = sorted(charList)
    charListDsc = sorted(charList, reverse = True)
    # check if number is bouncy
    if charList != charListAsc and charList != charListDsc: return True
    else: return False
      
# Find the least number for which the proportion of bouncy numbers is the given percentage (eg:99%). #Euler112
def getLeastNumber(percentage):

    # variable to set the number that needs to be checked for bounce :). Since there are no bouncy numbers below 100, so the number is defaulted to 100.
    number = 101
    # variable to count the number of bouncy numbers upto the given number 
    bouncyCount = 0
    # variable to hold the proportion
    proportiion = 0

    # loop through all numbers and check if a given number is bouncy and update count accordingly
    while True:
        if isBouncy(number): bouncyCount += 1
        # calculate proportion of bouncy numbers
        porportion = bouncyCount / number
        # check if proportion matches specified percentage
        # exit the loop if matched, check next number if not
        if porportion == percentage/100: break
        else: number += 1
            
    return number
  
def main():
  print ('The least number for which the proportion of bouncy numbers first reaches 50% is: ', getLeastNumber(50)) #538
  print ('The least number for which the proportion of bouncy numbers first reaches 90% is: ', getLeastNumber(90)) #21780
  print ('The least number for which the proportion of bouncy numbers first reaches 99% is: ', getLeastNumber(99)) #1587000
