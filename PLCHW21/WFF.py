import re
from WFFParser import parser

def eval(tree):
  counter = 0
  listOfElementsInWrongPlace = []
  elementsOfWFF = []
  elementsOfQuant = []
  listOfFreeVariables = []
  #print('TIME TO EVALUATE')
  #print('*************')
  if(tree[0]) == 'WFF':
    elementsOfWFF = eval_wff(tree)
    #print('THESE ARE THE ELEMENTS WE EXTRACTED')
    #print(elementsOfWFF)
  if(tree[0][0] == 'QUANT'):
    #print('WE HAVE A QUANT STATEMENT WITH THE FOLLOWING ELEMENTS!')
    #print(tree[0][1])
    elementsOfQuant = eval_quant(tree[0][1])
    elementsOfWFF = eval_wff(tree[1])
  #print('ALL OF THE QUANT STATEMENTS')
  #print(elementsOfQuant)
  #print('ALL OF THE WFF STATEMENTS')
  #print(elementsOfWFF)
  #print('HOWEVER, WE STILL NEED TO FINISH CLEANING THIS SHIT UP')
  for x in elementsOfWFF:
    m = re.match("MaRkEd", x)
    if m:
      #print('THIS IS IN THE WRONG PLACE!!!')
      #print(x)
      elementsOfQuant.append(x)
      counter = counter + 1
  for x in range((len(elementsOfQuant)-counter),len(elementsOfQuant)):
    #print(elementsOfQuant[x])
    value = elementsOfQuant[x]
    elementsOfQuant[x] = value[6:]
  for x in (range(len(elementsOfWFF))):
    m = re.match("MaRkEd", elementsOfWFF[x])
    if m:
        #print('I NEED TO REMOVE THIS ELEMENT')
        listOfElementsInWrongPlace.append(x)
  for x in range(len(listOfElementsInWrongPlace)):
      elementsOfWFF[listOfElementsInWrongPlace[x]] = ''
  #for x in elementsOfWFF:
    #if x not in elementsOfQuant:
      #print(str(x) + ' is a free variable!')
  #print(listOfElementsInWrongPlace)
  #print('QUANT VARIABLES: ' + str(elementsOfQuant))
  #print('WFF VARIABLES: '+ str(elementsOfWFF))
  for x in elementsOfWFF:
    if x != '':
        first_char = x[0]
        if x not in elementsOfQuant and first_char != '\'':
          #print(str(x) + ' is a free variable!')
          listOfFreeVariables.append(x.upper())
   
  if len(listOfFreeVariables) != 0:
    return('OPEN WFF with Free Variables: ' + str(listOfFreeVariables))
  else:
    return('CLOSED WFF')
  return(listOfFreeVariables)


      
def eval_wff(tree):
  #print('EVALUATING A WFF!!!')
  listOfElementsInWFF = []
  for x in range(len(tree)):
    if x%2 == 1:
      #print('THESE ARE THE ELEMENTS FROM WFF NUMBER ' + str(((x-1)/2)+1))
      #print(tree[x])
      for y in tree[x]:
        if isinstance(y,str):
          listOfElementsInWFF.append(y)
        if isinstance(y,float):
          yNew = '\'' + str(y) + '\''
          listOfElementsInWFF.append(yNew)
        else:
          if y[0] == 'QUANT':
            #print('WE HAVE AN ISSUE HERE!!!!!')
            #print(str(y) + ' is not element but is a QUANT!')
            #print(str(y[1]) + ' are all elements that we will have to add to the bound variables')
            for q in range(len(y[1])):
              #print('original variable is '+ str(y[1][q]))
              y[1][q] = 'MaRkEd'+(y[1][q])
              #print('new variable is ' + y[1][q])
              listOfElementsInWFF.append(y[1][q])

          if y[0] == 'WFF':
            #print(str(y) + ' is not element but is a WFF!')
            for z in range(len(y[1])):
              listOfElementsInWFF.append(y[1][z])
  return listOfElementsInWFF

def eval_quant(tree):
  listOfElementsInQuant = []
  for x in range(len(tree)):
    listOfElementsInQuant.append(tree[x])
  return listOfElementsInQuant

def read_input():
  result = ''
  while True:
    data = input('WAE: ').strip() 
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
  return result

def main():
  while True:
    data = read_input() 
    if data == 'exit;':
      break
    try:
      tree = parser.parse(data)
    except Exception as inst:
      print(inst.args[0])
      continue
    #print(tree)
    try:
     answer = eval(tree)
     if isinstance(answer,str):
       print(answer)
     else:
       print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
