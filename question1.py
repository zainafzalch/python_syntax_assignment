#ask 1: Code Correction Below is a piece of Python code with incorrect indentation. Your task is to correct it.

#weather = "sunny"

#if weather == "sunny":
#print("Wear sunglasses!")
#else:
#print("Take an umbrella!")

weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

#Task 2: Your Mood Today Ask the user how they feel today.\
#If they say "happy", print "That's great to hear!", and if they say "sad", print "I hope your day gets better!".
#Ensure your if statement is properly indented. HINT: Use the input() function to ask the user how they feel!

mood = input("How do you feel today? ")

if mood == "happy" or "Happy":
    print("Thats great to hear")
elif mood == "ok" or "Ok":
    print("is everything ok?")
else:
    print("I hope your day gets better!")