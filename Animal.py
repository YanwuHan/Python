__author__ = 'hanyw'
class Animal:
    def __init__(self,name):
        self.name=name
        self.hints=[]
        print("Enter three hints of",name)
        self.hints.append(input("1.: "))
        self.hints.append(input("2.: "))
        self.hints.append(input("3.: "))

    def guess_who_am_i(self):
        print("I will give your 3 hints, guess what animal I am\n")
        for i in range(0,3):
            print(self.hints[i])
            ans=input("Who an I?:")
            if ans == self.name:
                print("You got it! I am ",ans,"\n")
                return
            else:
                print("Nope, try again!\n")
        print("I'm out of hints! The answer is:",self.name,"\n")
a=Animal("tiger")
b=Animal("elephant")
a.guess_who_am_i()
b.guess_who_am_i()