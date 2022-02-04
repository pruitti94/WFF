from WFFParser import parser

def eval_expression(tree):
  numOfElements= len(tree)
  print('We have ' + str(numOfElements) + ' elements in our treee!')
  print('The elements are the following')
  for x in range(len(tree)):
    print(tree[x])
  if tree[0] == 'WFF':
    print('THIS IS  A WFF')
    for x in range(len(tree[1])):
      value = tree[1][x][0]
      if value == 'variable':
              print('this is a variable ' + tree[1][x][1])
  if tree[0] == 'exists':
    print('This is a quant statement.')
    print('The quant statment applies to the following:')
    for x in range(len(tree[1])):
      print(tree[1][x])


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
     answer = eval_expression(tree)
     if isinstance(answer,str):
       print('\nEVALUATION ERROR: '+answer+'\n')
     else:
       print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
