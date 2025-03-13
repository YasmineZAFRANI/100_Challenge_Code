#https://ascii.co.uk/art/treasureisland
s = r"""__________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|"""

print(s)
print("Welcome to treasure island")
direction1 = input('You\'re at a crossroad, where do you want to go ? Type "left" or "right".').lower()

if direction1 == "left":
    direction2 =input('You\'ve come to a lake. There is an island in the middle of the lake.'
          'Type "wait" to wait for a boat. Type "swim" to swim across.').lower()
    if direction2 == "wait":
        direction3 =input('There is a house with 3 doors.Choose on door either "Red", "Blue" or "Yellow"').lower()
        if direction3 =="yellow":
            print("You win! ")
        else:
            print("You got attacked. Game over!")
    else:
        print ("Shark attack. Game over!!")

else:
    print("You fell into a hole. Game over!")