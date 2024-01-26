
# this is my first python project.

# I created a variable 'a' to store the welcome text and headline
a='Welcome to the quiz \n'

#printed the variable a by aligning it and converting the text into uppercase text.
print(a.center(55).upper())

#created a list to store questions
questions= ['1. What is the largest internal organ in the human body?','2. What is the percentage of the Earth covered by water?', '3. What was the name of Drake’s 2023 album?']


#a list to store the options/answers
answers=['1.Lungs','2.Heart','3.Kidneys','4.Liver','1. 51%','2. 61%','3. 71%','4. 81%','1. Take Care','2. Scorpion','3. For All The Dogs','4. Views']


#defined a function 'game'
def game():
  #a variable earnings to store the total earning
  earnings=0
   
  #i just created a for loop, even i dont know the reason why i created this loop. Task was still success without for loop.
  
  for i in range(len(questions)):
      
    if i == 0:
      
      print('\n',questions[0])
      print( '\n',answers[0],'\n',answers[1],'\n',answers[2],'\n',answers[3],'\n')
      
      b=eval(input('\nWrite your answers in number as indicated : '))
      
      if b == 4:
       print('\nCongratulation, You won the first round')
       earnings += 1000
       print('\nYou Earned',earnings)
      

       i=1
        
      else:
        x=f'\nYou Lose the Games \n\nYour Earned {earnings}'
        return print(x)
        
        
    elif i==1:
      print('\n************ Welcome To The Second Round ***********')
      print('\n',questions[1])
      print( '\n',answers[4],'\n',answers[5],'\n',answers[6],'\n',answers[7],'\n')

      b=eval(input('\nWrite your answers in number as indicated : '))

      if b==3:
        print('\nCongratulation, You won the first round')
        earnings += 1000
        print('\nYou Earned',earnings)

        i=2

      else:
        x=f'\nYou Lose the Games \n\nYour Earned {earnings}'
        return print(x)

    elif i==2:
      print('\n********** Welcome To The Third Round **********')
      print('\n',questions[2])
      print( '\n',answers[8],'\n',answers[9],'\n',answers[10],'\n',answers[11],'\n')

      b=eval(input('\nWrite your answers in number as indicated : '))

      if b==3:
        print('\nCongratulation, You won the first round')
        earnings += 1000
        print('\nYou Earned',earnings)
        i=2

      else:
        x=f'\nYou Lose the Games \n\nYour Earned {earnings}'
        return print(x)
      
game()


  





