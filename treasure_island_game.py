print("Welcome to the treasure Island!!\nYour mission is to find the treausre")
step_one = input("Where do you want to go?\nLeft or Right??\n").lower()

if step_one == "right":
  print("You fell in a ditch! Game Over! ")
else:
  print("You are moving to the next step!")
  step_two = input("Do you want to swim or wait for a boat?\n").lower()
  if step_two == "swim":
    print("The crocodile in the water ate you! Game Over!")
  else:
    print("You have moved on to the next step.")
    print("There are 3 doors in front of you")
    step_three = input("Which color door do you want to open?\nRed,Blue,Yellow?\n").lower()
    if step_three == "red":
      print("You have drowned in mud! Game Over!")
    if step_three == "yellow":
      print("You have been trapped! Game Over!")
    else:
      print("You have found the treasure!\nCongratulations!\nYou Win!")
