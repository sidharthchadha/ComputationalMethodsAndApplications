import random
class TextGenerator:
    #defing constructor to perform dict making operation
    def __init__(self):

        self.prefix_dict = {}
     #creating a dictionary of tuple-to-list of words
     # tuple is key for the list of words.
        with open("sherlock.txt", 'r') as file:
            text = file.read()
            words = text.split()
            for i in range(len(words) - 2):
                 pref = (words[i], words[i+1])
                  #checking for the current tuple of words is already present in dictionary or not
                 if pref not in self.prefix_dict: 
                     self.prefix_dict[pref] = [words[i+2]]     #appending in the list as not present      
                 else:
                    self.prefix_dict[pref].append(words[i+2])
                    
    def generate(self, num, startword = None ):
        
        if startword is not None and startword not in [i[0] for i in self.prefix_dict.keys()]: #exceptions
             raise Exception("<class 'Exception'>\nUnable to produce text with the specified start word.")
        
        txt = ""    
        
        if startword is not None:
            temp = []
            for i in self.prefix_dict.keys():
                if i[0] == startword:
                    temp.append(i)

            Curr = random.choice(temp)
            txt += startword + " " + Curr[1]
            
        else:  #if startword is none then doing random select
            Curr = random.choice(list(self.prefix_dict))
            txt +=  Curr[0] + " " + Curr[1]
        
        for i in range(num - 2):
            NextWord = random.choice(self.prefix_dict[Curr])
            txt += ' ' + str(NextWord)
            Curr = (Curr[1] ,NextWord)
        print(txt)

var = TextGenerator()
var.generate(100  , "Watson")