print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇


print("You're at a cross road. Where do you want to go?")
position=input("     Type \"left\" or \"right\".\n")
position=position.lower()
if position=="left":
 print("You've come to a lake. There is an island in the middle of the lake.")
 swim_or_wait=input("  Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
 swim_or_wait=swim_or_wait.lower()
 if swim_or_wait=="wait":
  print("You arrived at the island unharmed. There is a house with 3 doors.")   
  color=input(" One red, one yellow and one blue. Which colour do you choose?\n")
  color=color.lower()
  if color=="red": 
   print("It's a room full of fire. Game Over.")     
  elif color=="blue":
   print("You enter a room of beasts. Game Over.")  
  elif color=="yellow":    
   print("You found the treasure! You win!")   
 else: 
  print("You get attecked by an angry trout.Game Over.")               
else:  
 print("You fell into a hole. Game Over.")         
          