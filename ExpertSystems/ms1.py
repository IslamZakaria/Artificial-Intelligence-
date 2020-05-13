from pyknow import *
from random import choice
import re

old=6
class RobotCrossStreet(KnowledgeEngine):
    lowShuger = 0
    highsuger = 0
    cold = 0
    measles=0
    mum=0
    adflu=0
    chflu=0

    @Rule(Fact(name='shakiness'))
    def incLowSuger(self):
        self.lowShuger += 1
        if self.lowShuger > 2 and old <6:
            y=input('Is one of your parents has diabetic ? y/n \n')
            if y=='y' :
                print('You have low sugar and you could be diabetic.')
    @Rule(Fact(name='hunger'))
    def incLowSuger1(self):
        self.lowShuger += 1
        if self.lowShuger > 2 and old <6:
            y=input('Is one of your parents has diabetic ? y/n \n')
            if y=='y' :
                print('You have low sugar and you could be diabetic.')
    @Rule(Fact(name='sweating'))
    def incLowSuger2(self):
        self.lowShuger += 1
        if self.lowShuger > 2  and old <6:
            y=input('Is one of your parents has diabetic ? y/n \n')
            if y=='y':
                print('You have low suger and you could be diabetic.')
    @Rule(Fact(name='headache'))
    def incLowSuger3(self):
        self.lowShuger += 1
        self.highsuger += 1
        if self.highsuger > 2 and old < 6:
            print('Has a  high Sugar 3')
        if self.lowShuger > 2 and old <6:
            y = input('Is one of your parents has diabetic ? y/n \n')
            if y == 'y':
                print('You have low sugar and you could be diabetic.')

    @Rule(Fact(name='pale'))
    def incLowSuger4(self):
        self.lowShuger += 1
        if self.lowShuger > 2 and old <6:
            y=input('Is one of your parents has diabetic ? y/n \n')
            if y=='y' :
                print('You have low sugar and you could be diabetic.')

    @Rule(Fact(name='thirst'))
    def inchiSuger(self):
        self.highsuger += 1
        if self.highsuger > 2 and old <6:
            print('Has a high Sugar ')

    @Rule(Fact(name='dry mouth'))
    def inchiuger1(self):
        self.highsuger += 1
        if self.highsuger > 2 and old <6:
            print('Has a  high Sugar ')

    @Rule(Fact(name='blurred vision'))
    def inchiSuger2(self):
        self.highsuger += 1
        if self.highsuger > 2 and old <6:
            print('Has a high Sugar ')

    @Rule(Fact(name='shortness of breath'))
    def inchiSuger3(self):
        self.highsuger += 1
        if self.highsuger > 2 and old <6:
            print('Has a  high Sugar ')

    @Rule(Fact(name='smelling breath'))
    def inchiSuger4(self):
        self.highsuger += 1
        if self.highsuger> 2 and old <6:
            print('Has a  high Sugar ')

    @Rule(Fact(name='runny nose'))
    def cold1(self):
        self.cold += 1
        if self.cold == 2:
            print('Has a cold ')
        if self.measles == 4 and self.cold ==2 and old<6:
            print('Has a measles')
        if self.chflu == 4 and old < 6 and self.cold == 2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold == 2:
            print('Has an Adult Flu')

    @Rule(Fact(name='harsh cough'))
    def cold2(self):
        self.cold += 1
        if self.cold == 2:
            print('Has a cold ')
        if self.measles == 4 and self.cold ==2 and old<6:
            print('Has a measles')
        if self.chflu == 4 and old < 6 and self.cold == 2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold == 2:
            print('Has an Adult Flu')

    @Rule(Fact(name='brownish-pink rash'))
    def measles1(self):
        self.measles += 1
        if self.measles == 4 and self.cold ==2 and old<6:
            print('Has a measles')
    @Rule(Fact(name='High and fast tempreture'))
    def measles2(self):
        self.measles += 1
        if self.measles == 4 and self.cold ==2 and old<6:
            print('Has a measles')
    @Rule(Fact(name='bloodshot eyes'))
    def measles3(self):
        self.measles += 1
        if self.measles == 4 and self.cold ==2 and old<6:
            print('Has a measles')

    @Rule(Fact(name='bloodshot eyes'))
    def measles4(self):
        self.measles += 1
        if self.measles == 4 and self.cold == 2 and old < 6:
            print('Has a measles')

    @Rule(Fact(name='moderate temperature'))
    def mumps(self):
        self.mum += 1
        if self.mum==4 and old < 6:
            print('Has a mumps')

    @Rule(Fact(name='saliva is not normal'))
    def mumps1(self):
        self.mum += 1
        if self.mum==4 and old < 6:
            print('Has a mumps')

    @Rule(Fact(name='swollen lymph nodes in neck'))
    def mumps2(self):
        self.mum += 1
        if self.mum==4 and old < 6:
            print('Has a mumps')
    @Rule(Fact(name='mouth dry'))
    def mumps3(self):
        self.mum += 1
        if self.mum==4 and old < 6:
            print('Has a mumps')

    @Rule(Fact(name='conjunctives'))
    def acflu(self):
        if old < 6:
            self.chflu += 1
        else:
            self.adflu += 1
        if self.chflu == 4 and old < 6 and self.cold==2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold==2:
            print('Has a Adult Flu')
    @Rule(Fact(name='strong body aches'))
    def acflu1(self):
        if old < 6:
            self.chflu += 1
        else:
            self.adflu += 1
        if self.chflu == 4 and old < 6 and self.cold ==2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold ==2:
            print('Has a Adult Flu')
    @Rule(Fact(name='weakness'))
    def acflu2(self):
        if old < 6:
            self.chflu += 1
        else:
            self.adflu += 1
        if self.chflu == 4 and old < 6 and self.cold==2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold==2:
            print('Has a Adult Flu')
    @Rule(Fact(name='vomiting'))
    def acflu3(self):
        if old < 6:
            self.chflu += 1
        else:
            self.adflu += 1
        if self.chflu == 4 and old < 6 and self.cold==2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold==2:
            print('Has a Adult Flu')

    @Rule(Fact(name='sore throat and sneezing'))
    def acflu4(self):
        if old < 6:
            self.chflu += 1
        else:
            self.adflu += 1
        if self.chflu == 4 and old < 6 and self.cold==2:
            print('Has a Child Flu')
        if self.adflu == 4 and old >= 6 and self.cold==2:
            print('Has an Adult Flu')

class PlantDiagnosesExpertSystem(KnowledgeEngine):

    @Rule(Fact(temperature='high' , humidity='normal' , tuber_color='reddish-brown' ,  tuber='spots'))
    def plane(self):
        print('the plant has black heart')

    @Rule(Fact(temperature='low', humidity='high', tuber_color='normal', tuber='spots'))
    def plane1(self):
        print('the plant has late blight')

    @Rule(Fact(temperature='high', humidity='normal', tuber_color='dry', tuber='circles'))
    def plane2(self):
        print('the plant has dry rot')

    @Rule(Fact(temperature='normal', humidity='normal', tuber_color='brown', tuber='wrinkles'))
    def plane3(self):
        print('the plant has early blight')

def main():
    print('Enter (1) For Testing [Medical Expert Systems] , (2) For Testing [Plant Diagnoses Expert System]')
    number=int(input())

    if(number==1):
        engine = RobotCrossStreet()
        engine.reset()
        print('How old are you ?')
        old = int(input())
        while 1:
            print('Type a symptom or 0 To End !')
            inp = input()
            if inp == '0':
                break
            else:
                engine.declare(Fact(name=inp))
                engine.run()

    elif(number==2):
        engine = PlantDiagnosesExpertSystem()
        engine.reset()
        print('What Is The Plan Temperature ?')
        temp = input()
        print('What Is The Plan Humidity ?')
        hum = input()
        print('What Is The Plan Tuber Color ?')
        tub_col = input()
        print('What Is The Plan Tuber ?')
        tub = input()
        engine.declare(Fact(temperature=temp, humidity=hum, tuber_color=tub_col, tuber=tub))
        engine.run()

main()