
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND COMMA EXISTS FORALL ID IF LPARENT NOT NUMBER OR RPARENT SEMI STRING WITHwaeStart : wff SEMIwaeStart : quant SEMIarg : STRINGarg : NUMBERarg : IDwff : ID LPARENT wff RPARENTwff : LPARENT wff RPARENTwff : argwff : arg COMMA wffwff : wff AND wffwff : wff OR wffwff : NOT wffwff : LPARENT quant RPARENT LPARENT wff RPARENTquant : FORALL quantquant : EXISTS quantquant : arg COMMA quantquant : arg'
    
_lr_action_items = {'ID':([0,5,7,8,9,13,14,16,19,33,34,36,],[4,4,4,24,24,4,4,4,4,4,24,4,]),'LPARENT':([0,4,5,7,13,14,16,19,30,33,36,],[5,16,5,5,5,5,5,5,36,5,5,]),'NOT':([0,5,7,13,14,16,19,33,36,],[7,7,7,7,7,7,7,7,7,]),'FORALL':([0,5,8,9,19,34,],[8,8,8,8,8,8,]),'EXISTS':([0,5,8,9,19,34,],[9,9,9,9,9,9,]),'STRING':([0,5,7,8,9,13,14,16,19,33,34,36,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'NUMBER':([0,5,7,8,9,13,14,16,19,33,34,36,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'$end':([1,12,15,],[0,-1,-2,]),'SEMI':([2,3,4,6,10,11,20,21,22,23,24,25,26,27,29,31,32,35,38,],[12,15,-5,-8,-3,-4,-12,-8,-14,-17,-5,-15,-10,-11,-7,-9,-16,-6,-13,]),'AND':([2,4,6,10,11,17,20,21,26,27,28,29,31,35,37,38,],[13,-5,-8,-3,-4,13,13,-8,13,13,13,-7,13,-6,13,-13,]),'OR':([2,4,6,10,11,17,20,21,26,27,28,29,31,35,37,38,],[14,-5,-8,-3,-4,14,14,-8,14,14,14,-7,14,-6,14,-13,]),'COMMA':([4,6,10,11,21,23,24,],[-5,19,-3,-4,33,34,-5,]),'RPARENT':([4,6,10,11,17,18,20,21,22,23,24,25,26,27,28,29,31,32,35,37,38,],[-5,-8,-3,-4,29,30,-12,-8,-14,-17,-5,-15,-10,-11,35,-7,-9,-16,-6,38,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'waeStart':([0,],[1,]),'wff':([0,5,7,13,14,16,19,33,36,],[2,17,20,26,27,28,31,31,37,]),'quant':([0,5,8,9,19,34,],[3,18,22,25,32,32,]),'arg':([0,5,7,8,9,13,14,16,19,33,34,36,],[6,6,21,23,23,21,21,21,6,21,23,21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> waeStart","S'",1,None,None,None),
  ('waeStart -> wff SEMI','waeStart',2,'p_waeStart_1','WFFParser.py',5),
  ('waeStart -> quant SEMI','waeStart',2,'p_waeStart_2','WFFParser.py',9),
  ('arg -> STRING','arg',1,'p_arg_1','WFFParser.py',13),
  ('arg -> NUMBER','arg',1,'p_arg_2','WFFParser.py',17),
  ('arg -> ID','arg',1,'p_arg_3','WFFParser.py',21),
  ('wff -> ID LPARENT wff RPARENT','wff',4,'p_wff_1','WFFParser.py',25),
  ('wff -> LPARENT wff RPARENT','wff',3,'p_wff_21','WFFParser.py',29),
  ('wff -> arg','wff',1,'p_wff_2','WFFParser.py',33),
  ('wff -> arg COMMA wff','wff',3,'p_wff_3','WFFParser.py',37),
  ('wff -> wff AND wff','wff',3,'p_wff_4','WFFParser.py',41),
  ('wff -> wff OR wff','wff',3,'p_wff_5','WFFParser.py',45),
  ('wff -> NOT wff','wff',2,'p_wff_6','WFFParser.py',49),
  ('wff -> LPARENT quant RPARENT LPARENT wff RPARENT','wff',6,'p_wff_7','WFFParser.py',53),
  ('quant -> FORALL quant','quant',2,'p_quant_1','WFFParser.py',57),
  ('quant -> EXISTS quant','quant',2,'p_quant_2','WFFParser.py',61),
  ('quant -> arg COMMA quant','quant',3,'p_quant_3','WFFParser.py',65),
  ('quant -> arg','quant',1,'p_quant_4','WFFParser.py',69),
]
