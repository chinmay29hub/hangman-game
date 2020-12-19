import random



name = input("What is your name ? --->> ")
print("\n")
print("It's time to play Hangman "+name)

print("Good Luck\n")


words = ['program', 'trees', 'computer', 'python', 'java', 'syntax',            # Insert n number of words here
         'house', 'linux', 'system', 'science', 'code', 'network', 'planet']                                 
                                       
                                       
word = random.choice(words)




# we will you use while loop for the condition till the turns are 0

def game():
   
    print("-------------------------------START----------------------------\n")
    print("Start guessing the characters\n")
    
    
    noofguesses = ''
    
    turns = 13         #these are the no of chances the player will get, you can add yours
    while turns > 0:
      
      
          guess = input("Guess a character --->  ")
          print("\n")                    
          noofguesses += guess
      
          failed = 0
      
          for char in word:
              if char in noofguesses:
                 print(char)
           
              else:
                  print("_")
              
                  failed += 1
              
          if failed == 0:
           
             print("You have won the game ")
         
             print("The Word Is -----> ", word)
             exit()
              
                  
          
    
             
             
      
      
      
          if guess not in word :
        
             turns -= 1
         
             print("Wrong Guess :( ")
             print("\n")
             print("You have ",+turns,"chances left")
             print("\n")
         
         
             if turns == 0:
                print("You have lost")
                print("The correct word was ----> ",word)

game()

            

 
            
            
            
      	                  
            

           
      
