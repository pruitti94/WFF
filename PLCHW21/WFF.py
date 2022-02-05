from WFFParser import parser

def eval(tree):
  #print('OUR TREE HAS ' + str(len(tree)) + ' elements')
  if(tree[0]) == 'WFF':
   eval_wff(tree)
  
    
def eval_wff(tree):
  #print(tree[1])
  print(len(tree[1]))
  print(tree[1])
  return(print('DONE'))
  
def eval_quant(tree):
  return(print('THIS IS A QUANTIFIER'))
  
  #boundVariableList = []
  #numOfElements= len(tree)
  #print('WE HAVE ' + str(numOfElements) + ' ELEMENTS IN OUR TREE!')
  #for x in range(len(tree)):
    #print('#' + str(x) + ' element is ' + str(tree[x]))
#    if tree[x][0] == 'EXISTS':
#        print('WE HAVE AN EXIST QUANTIFIER HERE')
#        print('THIS APPLIES TO THE FOLLOWING VARIABLES')
#        for y in range(len(tree[x][1])):
#            print(tree[x][1][y])
#            boundVariableList.append(tree[x][1][y][1])
#    if tree[x][0] == 'FORALL':
#        print('WE HAVE A FORALL QUANTIFIER HERE')
#        print('THIS APPLIES TO THE FOLLOWING VARIABLES')
#        for y in range(len(tree[x][1])):
#            print(tree[x][1][y])
#            boundVariableList.append(tree[x][1][y])
#    if tree[x][0] == 'NOT':
#        print('WE HAVE A NOT STATEMENT HERE')
#
#  print('ALL OF THE BOUND VARIABLES ARE BELOW')
#  print('************************************')
#  print(boundVariableList)

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
    print(tree)
    try:
     answer = eval(tree)
     if isinstance(answer,str):
       print('\nEVALUATION ERROR: '+answer+'\n')
     else:
       print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
