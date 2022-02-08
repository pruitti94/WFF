import ply.yacc as yacc
from WFFLexer import tokens

def p_waeStart_1(p):
  'waeStart : wff SEMI'
  p[0] = p[1]

def p_waeStart_2(p):
  'waeStart : quant SEMI'
  p[0] = p[1]
  
def p_arg_1(p):
  'arg : STRING'
  p[0] = p[1]
  
def p_arg_2(p):
  'arg : NUMBER'
  p[0] = p[1]

def p_arg_3(p):
  'arg : ID'
  p[0] = p[1]
  
def p_wff_1(p):
  'wff : ID LPARENT wff RPARENT'
  p[0] = ['WFF', p[3]]
  
def p_wff_21(p):
  'wff : LPARENT wff RPARENT'
  p[0] = ['WFF', p[2]]
    
def p_wff_2(p):
  'wff : arg'
  p[0] = [p[1]]

def p_wff_3(p):
  'wff : arg COMMA wff'
  p[0] = [p[1]] + p[3]

def p_wff_4(p):
  'wff : wff AND wff'
  p[0] = p[1]+p[3]

def p_wff_5(p):
  'wff : wff OR wff'
  p[0] = p[1]+p[3]

def p_wff_6(p):
  'wff : NOT wff'
  p[0] = p[2]

def p_wff_7(p):
  'wff : LPARENT quant RPARENT LPARENT wff RPARENT'
  p[0] = [['QUANT',p[2]],p[5]]

def p_quant_1(p):
  'quant : FORALL quant'
  p[0] = p[2]
  
def p_quant_2(p):
  'quant : EXISTS quant'
  p[0] = p[2]
  
def p_quant_3(p):
  'quant : arg COMMA quant'
  p[0] = [p[1]] + p[3]

def p_quant_4(p):
  'quant : arg'
  p[0] =[p[1]]
  

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

