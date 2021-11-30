#Damian Oportus

def sequenceDesDeux(x):
     '''(list)-> bool
      return true if there is at least a sequence of 2
      consecutive elements and False if not
      '''
     truth = False #set initial variable to be false
     for i in range(0,len(x)-1):
          if x[i] == x[i+1]: #if at least 2 consecutive elements that are equal, variable set to TRUE
               truth = True
     return truth #return the truth
          
q = list(input("Please enter a list of values separated by a comma: ").split(',')) #ask for input au clavier
w = sequenceDesDeux(q) #call f(x) with input au clavier
print(w) 


