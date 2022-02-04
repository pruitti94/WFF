import ply.lex as lex

reserved = { 'with': 'WITH', 'if': 'IF', 'and':'AND','not':'NOT', 'or':'OR', 'forall':'FORALL', 'exists':'EXISTS'}

tokens = ['NUMBER','ID','LPARENT','RPARENT','SEMI','STRING','COMMA'] + \
  list(reserved.values())

t_LPARENT = r'\('
t_RPARENT = r'\)'
t_SEMI = r';'
t_WITH = r'[wW][iI][tT][hH]'
t_IF = r'[iI][fF]'
t_COMMA = r','
def t_AND(t): r'[aA][nN][dD]'; return t
def t_NOT(t): r'[nN][oO][tT]'; return t
def t_OR(t):r'[oO][rR]'; return t
def t_FORALL(t):r'[fF][oO][rR][aA][lL][lL]'; return t
def t_EXISTS(t):r'[eE][xX][iI][sS][tT][sS]'; return t



def t_NUMBER(t):
  r'[-+]?[0-9]+(\.([0-9]+)?)?'
  t.value = float(t.value)
  t.type = 'NUMBER'
  return t
  
def t_STRING(t):
  r'\'[a-zA-Z0-9]*\''
  #t.type = reserved.get(t.value.lower(),'STRING')
  return t

def t_ID(t):
  r'[a-zA-Z][_a-zA-Z0-9]*'
  t.type = reserved.get(t.value.lower(),'ID')
  t.type = 'ID'
  return t

# Ignored characters
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  #t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
data = '''
(exists r,t,u,v,w,x,y,z)( employee(q,r,s,t,u,v,w,x,y,z) and not ((exists m,n,o,p)(dependent(t,m,n,o,p)) ) );'''
#
## Give the lexer some input
print("Tokenizing: ",data)
lexer.input(data)
#
## Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
