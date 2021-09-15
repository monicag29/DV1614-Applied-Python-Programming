from random import randint
import itertools

class Die:
    '''  Die class has 2 method which are used to rool dice and get the values '''

    def __init__(self) -> None:
        self._value=None
        

    def get_value(self) -> int:
        '''get_value method is used to get the values after rolling the dice'''
        return self._value


    def roll(self) -> None:
        ''' roll method is used  roll the dices and values are stored in self._values'''
        
        self._value=randint(1,6)

class DiceCup:
    '''Dicecups has 6 different method which act upon the values on the objects of  Die class
          dynamic way of implementataion in which the user can select the number dices to be rolled'''
    
    def __init__(self,number: int)-> None:
        self._dice=[]
        self._number=number
        self._checklist=['F','F','F','F','F']
    
        for i in range(self._number):
            dice=Die()
            self._dice.append(dice)


    def value(self,index: int) -> int:
        '''value method is used to take the value of dice based on index'''
        return self._dice[index]
        

    def bank(self,index: int) -> None:
        '''bank method is used to holds a paticular dice based on the index,
           index is given as parameter to this method
           and after holding the paticular die it replace the index position with T'''
        
        self._checklist[index]='T'
        


    def is_banked(self,index: int) -> bool:
        '''is_banked method is used to check weather the paticular index position is banked or not which gives the boolean value as output'''
        if self._checklist[index]=='T':
            return True
        else:
            return False


    def release(self,index: int) -> int:
        '''release  method used to release the banked dice of paticular index'''
        return self._dice[index]


    def release_all(self) -> None:
        '''release_all  releases all the banked dice'''
        print("releasing the dices")
        for i in range(len(self._dice)):
            print(self._dice[i])


    def roll(self) -> list:
        '''roll method makes used of objects of Die class and gathers all the values from the roll method of Die class and stores  those values in list'''
        value_list=[]
        for dice in self._dice:
            dice.roll()
            value_list.append(dice.get_value())
        return value_list
           
        
       

class ShipOfFoolsGame:
    '''ShipOfFoolsGame class is the original implementation of game which has a single method called round
          and responsible for the score of the player and also takes the object of Diecups'''
    
    def __init__(self) -> None:
        self._cup=[]
        self._dice=[]
        self._winning_score=None
      

    def round(self) -> int:
        '''
            round  method name itself denote the single round of a player which give the score of the individual player.
            each player has the chance of rolling the dices 3 times ,if the player procure the 6,5,4 in those 3 chances he/she can gain score
            and the score is calculated by integrating the values on the remaining 2 dices'''
        has_ship = False
        has_captain = False
        has_crew = False
        one_number=False
        two_number=False
        count=0
        crew=0
        
        for i in range(3):
            
            requried=int(has_ship)+int(has_captain)+int(has_crew)+int(one_number)+int(two_number)
            number=5
            d=number-requried
            self._cup=DiceCup(d)
            self._dice=self._cup.roll()
            dice=self._dice
            count=count+1
            
            
            
            if len(dice)==5:

                if count==1 : 
                    print(dice)
                    
               
                if count==2 and 6  in dice and 5  in dice and 4  in dice : 
                    pass
                else:
                    if count==2:
                        print(dice)

            if len(dice)==4:

                if count==2 and 5 not in dice:
                   dice.insert(has_ship_index,6)
                   print(dice)
                   dice.pop(has_ship_index)

                if count==2 and 5 in dice and 4 not in dice:
                    dice.insert(has_ship_index,6)
                    print(dice)
                    dice.pop(has_ship_index)
                    
            if len(dice)==3:

                if count==1 :
                   dice.insert(has_ship_index,6)
                   dice.insert(has_captain_index,5)
                   print(dice)
                   dice.pop(has_ship_index)
                   dice.pop(has_captain_index)

                if count==2 or count==3 and 4 in dice :
                    pass

                if count==2 and 4 not in dice:
                   dice.insert(has_ship_index,6)
                   dice.insert(has_captain_index,5)
                               
                   print(dice)
                   dice.pop(has_ship_index)
                   dice.pop(has_captain_index)

            if len(dice)==1:

                if count==2:
                   dice.insert(has_ship_index,6)
                   dice.insert(has_captain_index,5)
                   dice.insert(has_crew_index,4)
                   dice.insert(index_remaining,num1)
                   print(dice)
                   dice.pop(has_ship_index)
                   dice.pop(has_captain_index)
                   dice.pop(has_crew_index)
                   dice.pop(index_remaining)
           
            if not has_ship and 6 in dice:
                
                has_ship_index=dice.index(6)
                self._cup.bank(dice.index(6))
                dice.remove(6)
                has_ship=True
                
            if has_ship and  not has_captain and 5 in dice:
                
                has_captain_index=dice.index(5)
                self._cup.bank(dice.index(5))
                dice.remove(5)
                has_captain=True
                
            if has_captain and not has_crew and  4 in dice:
                
                     has_crew_index=dice.index(4)
                     self._cup.bank(dice.index(4))
                     dice.remove(4)
                     has_crew=True
                     
            if has_ship and has_captain and has_crew :
                
                
                if not one_number and not two_number:
                    

                  if dice[0]>3 and dice[1]>3:

                        if count==1 :
                            it1=iter([6,5,4])
                            it2=iter(dice)
                            print(list(itertools.chain(it1,it2)))

                        if count==2:
                            it1=iter([6,5,4])
                            it2=iter(dice)
                            print(list(itertools.chain(it1,it2))) 
                            
                        one_number=dice[0]
                        two_number=dice[1]
                        dice.remove(dice[0])
                        dice.remove(dice[0])
                        dice.insert(0,one_number)
                        dice.insert(1,two_number)
                        one_number=True
                        two_number=True      
                        break

                  if dice[0]<=3 and dice[1]<=3:

                        if count==2:
                            it1=iter([6,5,4])
                            it2=iter(dice)
                            print(list(itertools.chain(it1,it2)))

                  if dice[1]>3 and not dice[0]>3:

                        if count==2:
                            it1=iter([6,5,4])
                            it2=iter(dice)
                            print(list(itertools.chain(it1,it2)))
                            
                        two_number=dice[1]
                        index_remaining=dice.index(two_number)
                        num1=two_number
                        dice.remove(dice[1])
                        two_number=True

                  if dice[0]>3 and not dice[1]>3:

                        if count==2:
                            it1=iter([6,5,4])
                            it2=iter(dice)
                            print(list(itertools.chain(it1,it2)))
                           
                        one_number=dice[0]
                        index_remaining=dice.index(one_number)
                        num1=one_number
                        dice.remove(dice[0])
                        one_number=True
                        
                   
            if has_ship and has_captain and has_crew:
                if one_number or two_number:
                
                   if dice[0]>3:
                      num=dice[0]
                      lastnum_index=dice.index(num)
                      dice.remove(dice[0])
                
                
        if has_ship and has_captain and has_crew:

                if len(dice)<1:
                    dice.insert(lastnum_index,num)
                    dice.insert(index_remaining,num1)

                if len(dice)<2:
                    dice.insert(index_remaining,num1)
                    
                dice.insert(has_ship_index,6)
                dice.insert(has_captain_index,5)
                dice.insert(has_crew_index,4)
                
                crew=sum(dice)-15
                return crew 

        else:

            if len(dice)==4:
                dice.append(6)

            if len(dice)==3:
                dice.append(6)
                dice.append(5)
            return 0



class Player():
    '''player class represents the individual player and responsible for the score of the  individual player and stores the score in the ._score attribute'''

    def __init__(self,name : str) -> None:
        self._name=name
        self._score=0
        self._playing=None

    def set_name(self,namestring: str) -> None:
        ''' set_name method is used to set the name the player'''
        self._name=namestring

    def reset_score(self) -> None:
        '''reset_score method resets the score of the player after completion of the each single round'''
        self._score=0
         
    def play_round(self,game: ShipOfFoolsGame) -> None:
        '''play_round method make use of ShipOfFoolsGame object and assigns the round method to the each player'''
        self._playing=game.round()
        print(game._dice)
        print(self._name,game._dice)
        
        
    def  current_score(self) -> None:
        '''current_score method updates the score of the each player and stores the score in ._score attribute'''
        score=self._playing
        self._score+=score
        print(self._name ,self._score)



class Playroom:
    '''Playroom  class responsible for handling the number of player and check the score and display the winner''' 

    def __init__(self) -> None:
        self._players=[]
        self._final=None
        self._winner=None
        self._maxscores=[]

    def set_game(self,game: ShipOfFoolsGame) -> None:
        '''set_game method used to set the game that is ShipOfFoolsGame'''
        self.setgame=game

    def add_player(self,player: str) -> None:
        '''add_player method  used to add the players to the ._playersattribute'''
        self._players.append(player)

    def reset_score(self) -> None:
        '''reset_score method which resembles the functionality of the reset_score method in the Player class'''
        for player in self._players:
            player.reset_score()
    
    def play_round(self) -> None:
        '''this method is same as the player_round in Player Class but act upon on group of player'''
        for player in self._players:
            player.play_round(self.setgame)
            
    def game_finished(self) -> bool:
        '''game_finished method checks the score of the each player weather they reached more than 21 or not'''
        self._maxscores=[]
        for player in self._players:
            self._maxscores.append(player._score)

        self._final=max(self._maxscores)
        if self._final>=21:
            return True
        else:
            return False

    def print_scores(self) -> None:
        '''print_score gives the current score of the each player'''
        for player in self._players:
           player.current_score()
         
    def print_winner(self) -> None:
        '''print_winner method checks the individual score and prints the winner'''
        for player in range(len(self._players)):
            if self._maxscores[player]==self._final:
                print("winner is ",self._players[player]._name)
        
            
            
        



if __name__ == "__main__":
  room=Playroom()
  room.set_game(ShipOfFoolsGame())
  room.add_player(Player("Ling"))
  room.add_player(Player("Chang"))
  room.reset_score()
  while not room.game_finished():
      room.play_round()
      room.print_scores()
  room.print_winner()
  
 
             
