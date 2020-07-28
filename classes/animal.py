import datetime
import math
class animal:
    def __init__(self,name,hunger=5.0,energy=5.0):
        self.name=name
        self.hunger=hunger
        self.energy=energy

    def __str__(self):
        return "the",self.name," hunger is:","the",self.hunger," energy is:",self.energy

    def eat(self,food_wheight):
        while(food_wheight>0 and self.hunger>0.02 and self.energy>0.01):
            food_wheight=food_wheight-1
            self.hunger=self.hunger-0.02
            self.energy=self.energy-0.01
        if(food_wheight!=0 and self.hunger==0 or self.energy==0):
            return "the ",self.name,"haven't finish the food and is not hungry any more"
        if(self.energy==0):
            return "tne", self.name, "has no energy"
        return self.__str__(), "you have",food_wheight, "food left"

    def play(self,play_time):
        while(play_time>0 and self.hunger<10 and self.energy>0.2):
            play_time=play_time-1
            self.hunger = self.hunger + 0.2
            self.energy = self.energy - 0.2
        if (play_time != 0 and self.hunger < 0 or self.energy<0):
            return "the ", self.name, "haven't finish to olay and is no energy any more"
        if (self.energy> 0):
            return "tne", self.name, "has no energy"
        return self.__str__(), "you have", play_time, "play time left"

    def rest(self,rest_time):
        while(rest_time>0 and self.hunger<9.7 and self.energy <9.8):
            rest_time=rest_time-1
            self.hunger=self.hunger+0.3
            self.energy=self.energy+0.2
        if(rest_time!=0 and self.hunger==0 or self.energy==0):
            return "the ",self.name,"haven't finish the food and is not hungry any more"
        if(self.energy>=9.7):
            return "the", self.name, "has full energy"
        return self.__str__(), "you have",rest_time, "rest time left"

