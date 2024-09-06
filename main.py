# Question no 1
#  If the age is 18 or above Ask if they have a nationality of "Pakistani".If yes, print "You are eligible to vote If no, print "Please obtain a valid ID to vote."

print("vote age calculator")
age=int(input("please enter your age here "))
nationality=(input("please enter your nationality here "))
if nationality=="Pakistani":
    print("You are eligible to vote")
    if age>=18:
     print("You are eligible to vote")
    elif age<18:
      print("you are not eligible to vote.")
else:
    print("Please obtain a valid ID to vote.")

# /----------------------------------------------------------------

# Question no 2
# a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
print("Age classification program")
age=int(input("Please enter your age here "))
if age<=12:
    print("You are a child")
elif age<=19:
    print("You are a teenager")
elif age<=59:
    print("You are an adult")
else:
    print("You are a senior citizen")

# /----------------------------------------------------------------

# Question no 3
# Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year  Check if a year is a leap year or not
print("Days in a month calculator")
month=int(input("Please enter the month (1-12) here "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("This month has 31 days")
elif month==2:
 print("This month has 28 days")
else:
    print("This month has 30 days")
year=int(input("Please enter the year here "))
if year%4==year%100==year%400==0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")

# /----------------------------------------------------------------

# Question no 4
# check if the number is Even or Odd Positive, Negative, or Zero Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case
num =int(input("enter a number here"))
if num%2==0:
   print("number is even ")
elif num%2!=0:
   print("nnumber is odd ")
if num >0:
   print("number is positive")
elif num < 0:
   print("number is negative")
else:
   print("number is zero")
if num%2 == 0:
   print("number is divisible by 2")
elif num%3 ==0:
   print("number is divisible by 3")
else:
   print("number is not divisible by 2 or 3")

   # /----------------------------------------------------------------
