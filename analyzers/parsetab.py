
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY AS AT BOOL BOOLEAN_NOT BREAK CASE CATCH CLASS CLASS_C CLOSE_TAG COLON COMENTARIOS COMMA CONCAT CONSTANT_ENCAPSED_STRING CONTINUE CURLY_OPEN DECIMAL DEFAULT DEFINE DIR DIVISION DIV_EQUAL DO DOC_COMENTARIOS DOUBLE ECHO ELSE ELSEIF ENCAPSED_AND_WHITESPACE ENTERO EQUALS EXIT FALSE FILE FLOAT FOR FOREACH FUNCTION FUNC_C GLOBAL GOTO GREATER HALT_COMPILER IF INT IS_EQUAL IS_GREATER_OR_EQUAL IS_IDENTICAL IS_NOT_EQUAL IS_NOT_IDENTICAL IS_SMALLER_OR_EQUAL LBRACE LBRACKET LINE LPAREN METHOD_C MINUS_EQUAL MODULO MOD_EQUAL MULTIPLICACION MUL_EQUAL NEW NOMBRE NOT NS_C NS_SEPARATOR NULL NUM_STRING OBJECT OPEN_TAG OR PLUS_EQUAL PRINT PRIVATE PROTECTED PUBLIC RBRACE RBRACKET READLINE REQUIRE RESTA RETURN RPAREN SEMI SMALLER STATIC STRING SUMA SWITCH TRUE TRY VAR VARIABLE VOID WHILE XORcuerpo : imprimir\n            | asignacion\n            | asignacion_array\n            | funcion_nparams\n            | constante\n            | lectura\n            | operadores\n            | operador_logico\n            | condicion_booleana\n            | bwhile\n            | bfor\n            | bforeach\n            | btry\n            | operaciones_mat\n            | condicion_if\n  imprimir : ECHO valor SEMI\n            | PRINT valor SEMI\n            | PRINT LPAREN valor RPAREN SEMI\n            | ECHO NOMBRE LBRACKET ENTERO RBRACKET SEMI\n  valor : numero\n            | VARIABLE\n            | STRING\n            | NOMBRE\n  numero : ENTERO\n          | DECIMALoperadores : SUMA \n                  | RESTA\n                  | MULTIPLICACION\n                  | DIVISION\n                  | MODULO\n  operador_logico :  SMALLER\n                        | GREATER\n                        | IS_SMALLER_OR_EQUAL\n                        | IS_GREATER_OR_EQUAL\n  condicion_if :  IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE\n  condicion_booleana :  AND\n                        | OR\n                        | XOR\n                        | IS_EQUAL\n                        | IS_NOT_EQUAL\n                        | IS_IDENTICAL\n                        | IS_NOT_IDENTICAL\n                        | BOOLEAN_NOT\n  operaciones_mat :  op_basicas\n                        | op_recursivas\n  op_basicas :  valor operadores valor\n                      | LPAREN valor operadores valor RPAREN\n  op_recursivas :  valor operadores op_recursivas\n                    | valor LPAREN valor operadores valor RPAREN operaciones_mat\n  asignacion : VARIABLE EQUALS valor SEMIasignacion_array : VARIABLE EQUALS array_def SEMIconstante : DEFINE LPAREN STRING COMMA valor RPAREN SEMI\n          | DEFINE LPAREN NOMBRE COMMA ARRAY RPAREN SEMIlectura : READLINE LPAREN STRING RPAREN SEMI\n          | READLINE LPAREN RPAREN SEMIparam : VARIABLE\n          | asignacionfuncion_nparams : FUNCTION NOMBRE LPAREN params_list RPAREN stc_bloque_defparams_list : params_list COMMA param\n                      | param condicion : VARIABLE operador_logico VARIABLE\n            | valor operador_logico valor\n          \n   bwhile : WHILE LPAREN condicion RPAREN LBRACE stc_bloque RBRACE\n  bfor : FOR LPAREN asignacion SEMI condicion SEMI for_incr RPAREN stc_bloque_defstc_bloque : stc_bloque cuerpo\n        | emptystc_bloque_def : LBRACE stc_bloque RBRACEfor_incr : VARIABLE SUMA SUMA\n          | SUMA SUMA VARIABLE\n          | VARIABLE RESTA RESTA\n          | RESTA RESTA VARIABLE\n          | VARIABLE SUMA EQUALS numero\n          | VARIABLE RESTA EQUALS numerobforeach :  FOREACH LPAREN VARIABLE AS VARIABLE RPAREN stc_bloque_defarray_def : ARRAY LPAREN RPAREN \n          | ARRAY LPAREN array_elmnt RPARENarray_elmnt : valor\n            | emptybtry : TRY LBRACE stc_bloque_def RBRACE catchescatches : catches CATCH LPAREN NOMBRE VARIABLE RPAREN stc_bloque_def\n          | emptyempty : '
    
_lr_action_items = {'ECHO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[17,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,17,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,17,-19,-58,17,-49,-52,-53,-63,-74,-35,-64,-80,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[19,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,19,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,19,-19,-58,19,-49,-52,-53,-63,-74,-35,-64,-80,]),'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,57,58,60,62,66,67,68,70,71,73,74,76,78,82,93,97,98,101,102,103,108,111,113,114,115,116,117,118,119,120,125,126,132,135,136,141,142,143,144,145,146,147,149,153,154,158,159,160,161,166,168,172,173,174,175,186,],[23,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,56,56,56,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,56,56,56,56,88,91,92,88,-16,-46,-48,-17,56,106,-82,56,56,-50,-51,56,56,-55,137,56,88,56,140,23,-66,-82,-18,-47,106,-54,-82,-67,-65,-79,-81,23,-19,56,-58,23,163,-49,-52,-53,-63,-74,-35,180,181,182,-64,-80,]),'FUNCTION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[24,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,24,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,24,-19,-58,24,-49,-52,-53,-63,-74,-35,-64,-80,]),'DEFINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[25,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,25,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,25,-19,-58,25,-49,-52,-53,-63,-74,-35,-64,-80,]),'READLINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[27,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,27,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,27,-19,-58,27,-49,-52,-53,-63,-74,-35,-64,-80,]),'SUMA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,61,71,73,74,75,76,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,149,153,154,158,159,160,161,163,164,166,168,170,175,186,],[28,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,28,-23,-24,-21,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,28,-16,28,-48,28,-17,-82,-50,-51,-55,28,-66,-82,28,-18,-47,-54,-82,-67,-65,-79,-81,28,-19,-58,28,164,-49,-52,-53,-63,170,172,-74,-35,176,-64,-80,]),'RESTA':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,61,71,73,74,75,76,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,149,153,154,158,159,160,161,163,165,166,168,171,175,186,],[29,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,29,-23,-24,-21,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,29,-16,29,-48,29,-17,-82,-50,-51,-55,29,-66,-82,29,-18,-47,-54,-82,-67,-65,-79,-81,29,-19,-58,29,165,-49,-52,-53,-63,171,173,-74,-35,178,-64,-80,]),'MULTIPLICACION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,61,71,73,74,75,76,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[30,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,30,-23,-24,-21,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,30,-16,30,-48,30,-17,-82,-50,-51,-55,30,-66,-82,30,-18,-47,-54,-82,-67,-65,-79,-81,30,-19,-58,30,-49,-52,-53,-63,-74,-35,-64,-80,]),'DIVISION':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,61,71,73,74,75,76,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[31,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,31,-23,-24,-21,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,31,-16,31,-48,31,-17,-82,-50,-51,-55,31,-66,-82,31,-18,-47,-54,-82,-67,-65,-79,-81,31,-19,-58,31,-49,-52,-53,-63,-74,-35,-64,-80,]),'MODULO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,61,71,73,74,75,76,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[32,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,32,-23,-24,-21,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,32,-16,32,-48,32,-17,-82,-50,-51,-55,32,-66,-82,32,-18,-47,-54,-82,-67,-65,-79,-81,32,-19,-58,32,-49,-52,-53,-63,-74,-35,-64,-80,]),'SMALLER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,88,89,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[33,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,33,33,-82,-50,-51,-55,33,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,33,-19,-58,33,-49,-52,-53,-63,-74,-35,-64,-80,]),'GREATER':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,88,89,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[34,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,34,34,-82,-50,-51,-55,34,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,34,-19,-58,34,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_SMALLER_OR_EQUAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,88,89,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[35,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,35,35,-82,-50,-51,-55,35,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,35,-19,-58,35,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_GREATER_OR_EQUAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,88,89,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[36,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,36,36,-82,-50,-51,-55,36,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,36,-19,-58,36,-49,-52,-53,-63,-74,-35,-64,-80,]),'AND':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[37,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,37,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,37,-19,-58,37,-49,-52,-53,-63,-74,-35,-64,-80,]),'OR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[38,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,38,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,38,-19,-58,38,-49,-52,-53,-63,-74,-35,-64,-80,]),'XOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[39,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,39,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,39,-19,-58,39,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_EQUAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[40,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,40,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,40,-19,-58,40,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_NOT_EQUAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[41,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,41,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,41,-19,-58,41,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_IDENTICAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[42,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,42,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,42,-19,-58,42,-49,-52,-53,-63,-74,-35,-64,-80,]),'IS_NOT_IDENTICAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[43,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,43,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,43,-19,-58,43,-49,-52,-53,-63,-74,-35,-64,-80,]),'BOOLEAN_NOT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[44,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,44,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,44,-19,-58,44,-49,-52,-53,-63,-74,-35,-64,-80,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[45,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,45,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,45,-19,-58,45,-49,-52,-53,-63,-74,-35,-64,-80,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[46,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,46,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,46,-19,-58,46,-49,-52,-53,-63,-74,-35,-64,-80,]),'FOREACH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[47,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,47,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,47,-19,-58,47,-49,-52,-53,-63,-74,-35,-64,-80,]),'TRY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[48,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,48,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,48,-19,-58,48,-49,-52,-53,-63,-74,-35,-64,-80,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,101,102,111,118,119,120,125,126,135,136,141,142,143,144,145,146,149,153,158,159,160,161,166,168,175,186,],[51,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,-50,-51,-55,51,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,51,-19,-58,51,-49,-52,-53,-63,-74,-35,-64,-80,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,56,63,71,73,74,76,81,93,101,102,111,118,119,120,123,125,126,135,136,141,142,143,144,145,146,147,149,153,156,158,159,160,161,166,168,175,186,],[20,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,58,60,-23,-24,-21,64,-22,65,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,66,67,68,-44,-45,70,-20,-25,-21,82,-16,58,-48,-17,103,-82,-50,-51,-55,20,-66,-82,58,-18,-47,-54,-82,-67,-65,-79,-81,20,-19,20,-58,20,167,-49,-52,-53,-63,-74,-35,-64,-80,]),'STRING':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,57,58,60,62,64,65,66,70,71,73,74,76,78,93,97,98,101,102,103,108,111,114,115,116,118,119,120,125,126,135,136,141,142,143,144,145,146,147,149,153,158,159,160,161,166,168,175,186,],[26,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,26,26,26,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,26,26,26,26,83,85,26,26,-16,-46,-48,-17,26,-82,26,26,-50,-51,26,26,-55,26,26,26,26,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,26,-19,26,-58,26,-49,-52,-53,-63,-74,-35,-64,-80,]),'NOMBRE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,24,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,57,58,60,62,64,66,70,71,73,74,76,78,93,97,98,101,102,103,108,111,114,115,116,118,119,120,125,126,135,136,141,142,143,144,145,146,147,149,153,158,159,160,161,166,167,168,175,186,],[21,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,55,21,21,-23,-24,63,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,21,21,21,21,84,21,21,-16,-46,-48,-17,21,-82,21,21,-50,-51,21,21,-55,21,21,21,21,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,21,-19,21,-58,21,-49,-52,-53,-63,-74,174,-35,-64,-80,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,57,58,60,62,66,70,71,72,73,74,76,78,93,97,98,101,102,103,108,111,114,115,116,118,119,120,125,126,135,136,141,142,143,144,145,146,147,149,153,158,159,160,161,166,168,175,177,179,186,],[22,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,22,22,22,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,22,22,22,22,22,22,-16,96,-46,-48,-17,22,-82,22,22,-50,-51,22,22,-55,22,22,22,22,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,22,-19,22,-58,22,-49,-52,-53,-63,-74,-35,-64,22,22,-80,]),'DECIMAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,57,58,60,62,66,70,71,73,74,76,78,93,97,98,101,102,103,108,111,114,115,116,118,119,120,125,126,135,136,141,142,143,144,145,146,147,149,153,158,159,160,161,166,168,175,177,179,186,],[53,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,53,53,53,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,53,53,53,53,53,53,-16,-46,-48,-17,53,-82,53,53,-50,-51,53,53,-55,53,53,53,53,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,53,-19,53,-58,53,-49,-52,-53,-63,-74,-35,-64,53,53,-80,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,101,102,111,120,125,126,135,141,143,144,146,149,158,159,160,161,166,168,175,186,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-50,-51,-55,-82,-18,-47,-54,-67,-79,-81,-19,-58,-49,-52,-53,-63,-74,-35,-64,-80,]),'RBRACE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,22,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,49,50,52,53,56,71,73,74,76,93,94,101,102,111,118,119,120,125,126,135,136,141,142,143,144,146,149,153,157,158,159,160,161,166,168,175,186,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-23,-24,-22,-26,-27,-28,-29,-30,-31,-32,-33,-34,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-20,-25,-21,-16,-46,-48,-17,-82,120,-50,-51,-55,141,-66,-82,-18,-47,-54,-82,-67,-65,-79,-81,-19,-58,161,168,-49,-52,-53,-63,-74,-35,-64,-80,]),'SEMI':([21,22,26,52,53,54,55,56,59,79,80,86,90,99,101,110,122,127,137,138,139,148,151,152,],[-23,-24,-22,-20,-25,71,-23,-21,76,101,102,111,115,125,-50,135,146,-75,-61,-62,154,-76,159,160,]),'RPAREN':([21,22,26,52,53,56,65,77,85,87,95,100,101,103,104,105,106,107,124,128,129,130,133,134,137,138,140,150,162,176,178,180,181,182,183,184,],[-23,-24,-22,-20,-25,-21,86,99,110,112,121,126,-50,127,131,-60,-56,-57,147,148,-77,-78,151,152,-61,-62,155,-59,169,-68,-70,-69,-71,185,-72,-73,]),'EQUALS':([23,91,106,170,171,],[62,116,116,177,179,]),'LBRACE':([48,69,112,121,131,155,169,185,],[69,93,136,145,93,93,93,93,]),'LBRACKET':([55,],[72,]),'ARRAY':([62,109,],[81,134,]),'COMMA':([83,84,101,104,105,106,107,150,],[108,109,-50,132,-60,-56,-57,-59,]),'AS':([92,],[117,]),'RBRACKET':([96,],[122,]),'CATCH':([120,141,143,144,186,],[-82,-67,156,-81,-80,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,118,145,153,],[1,142,157,142,]),'imprimir':([0,118,145,153,],[2,2,2,2,]),'asignacion':([0,67,82,118,132,145,153,],[3,90,107,3,107,3,3,]),'asignacion_array':([0,118,145,153,],[4,4,4,4,]),'funcion_nparams':([0,118,145,153,],[5,5,5,5,]),'constante':([0,118,145,153,],[6,6,6,6,]),'lectura':([0,118,145,153,],[7,7,7,7,]),'operadores':([0,18,61,73,75,118,123,145,153,],[8,57,78,97,98,8,97,8,8,]),'operador_logico':([0,88,89,118,145,153,],[9,113,114,9,9,9,]),'condicion_booleana':([0,118,145,153,],[10,10,10,10,]),'bwhile':([0,118,145,153,],[11,11,11,11,]),'bfor':([0,118,145,153,],[12,12,12,12,]),'bforeach':([0,118,145,153,],[13,13,13,13,]),'btry':([0,118,145,153,],[14,14,14,14,]),'operaciones_mat':([0,118,145,147,153,],[15,15,15,158,15,]),'condicion_if':([0,118,145,153,],[16,16,16,16,]),'valor':([0,17,19,20,57,58,60,62,66,70,78,97,98,103,108,114,115,116,118,145,147,153,],[18,54,59,61,73,75,77,79,89,89,100,123,124,129,133,138,89,79,18,18,18,18,]),'op_basicas':([0,118,145,147,153,],[49,49,49,49,49,]),'op_recursivas':([0,57,97,118,145,147,153,],[50,74,74,50,50,50,50,]),'numero':([0,17,19,20,57,58,60,62,66,70,78,97,98,103,108,114,115,116,118,145,147,153,177,179,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,183,184,]),'array_def':([62,],[80,]),'condicion':([66,70,115,],[87,95,139,]),'stc_bloque_def':([69,131,155,169,185,],[94,149,166,175,186,]),'params_list':([82,],[104,]),'param':([82,132,],[105,150,]),'stc_bloque':([93,136,],[118,153,]),'empty':([93,103,120,136,],[119,130,144,119,]),'array_elmnt':([103,],[128,]),'catches':([120,],[143,]),'for_incr':([154,],[162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> imprimir','cuerpo',1,'p_cuerpo','sintactico.py',7),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',8),
  ('cuerpo -> asignacion_array','cuerpo',1,'p_cuerpo','sintactico.py',9),
  ('cuerpo -> funcion_nparams','cuerpo',1,'p_cuerpo','sintactico.py',10),
  ('cuerpo -> constante','cuerpo',1,'p_cuerpo','sintactico.py',11),
  ('cuerpo -> lectura','cuerpo',1,'p_cuerpo','sintactico.py',12),
  ('cuerpo -> operadores','cuerpo',1,'p_cuerpo','sintactico.py',13),
  ('cuerpo -> operador_logico','cuerpo',1,'p_cuerpo','sintactico.py',14),
  ('cuerpo -> condicion_booleana','cuerpo',1,'p_cuerpo','sintactico.py',15),
  ('cuerpo -> bwhile','cuerpo',1,'p_cuerpo','sintactico.py',16),
  ('cuerpo -> bfor','cuerpo',1,'p_cuerpo','sintactico.py',17),
  ('cuerpo -> bforeach','cuerpo',1,'p_cuerpo','sintactico.py',18),
  ('cuerpo -> btry','cuerpo',1,'p_cuerpo','sintactico.py',19),
  ('cuerpo -> operaciones_mat','cuerpo',1,'p_cuerpo','sintactico.py',20),
  ('cuerpo -> condicion_if','cuerpo',1,'p_cuerpo','sintactico.py',21),
  ('imprimir -> ECHO valor SEMI','imprimir',3,'p_imprimir','sintactico.py',26),
  ('imprimir -> PRINT valor SEMI','imprimir',3,'p_imprimir','sintactico.py',27),
  ('imprimir -> PRINT LPAREN valor RPAREN SEMI','imprimir',5,'p_imprimir','sintactico.py',28),
  ('imprimir -> ECHO NOMBRE LBRACKET ENTERO RBRACKET SEMI','imprimir',6,'p_imprimir','sintactico.py',29),
  ('valor -> numero','valor',1,'p_valor','sintactico.py',34),
  ('valor -> VARIABLE','valor',1,'p_valor','sintactico.py',35),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',36),
  ('valor -> NOMBRE','valor',1,'p_valor','sintactico.py',37),
  ('numero -> ENTERO','numero',1,'p_numero','sintactico.py',41),
  ('numero -> DECIMAL','numero',1,'p_numero','sintactico.py',42),
  ('operadores -> SUMA','operadores',1,'p_operadores','sintactico.py',45),
  ('operadores -> RESTA','operadores',1,'p_operadores','sintactico.py',46),
  ('operadores -> MULTIPLICACION','operadores',1,'p_operadores','sintactico.py',47),
  ('operadores -> DIVISION','operadores',1,'p_operadores','sintactico.py',48),
  ('operadores -> MODULO','operadores',1,'p_operadores','sintactico.py',49),
  ('operador_logico -> SMALLER','operador_logico',1,'p_operador_logico','sintactico.py',54),
  ('operador_logico -> GREATER','operador_logico',1,'p_operador_logico','sintactico.py',55),
  ('operador_logico -> IS_SMALLER_OR_EQUAL','operador_logico',1,'p_operador_logico','sintactico.py',56),
  ('operador_logico -> IS_GREATER_OR_EQUAL','operador_logico',1,'p_operador_logico','sintactico.py',57),
  ('condicion_if -> IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE','condicion_if',7,'p_condicion_if','sintactico.py',60),
  ('condicion_booleana -> AND','condicion_booleana',1,'p_condicion_boolena','sintactico.py',64),
  ('condicion_booleana -> OR','condicion_booleana',1,'p_condicion_boolena','sintactico.py',65),
  ('condicion_booleana -> XOR','condicion_booleana',1,'p_condicion_boolena','sintactico.py',66),
  ('condicion_booleana -> IS_EQUAL','condicion_booleana',1,'p_condicion_boolena','sintactico.py',67),
  ('condicion_booleana -> IS_NOT_EQUAL','condicion_booleana',1,'p_condicion_boolena','sintactico.py',68),
  ('condicion_booleana -> IS_IDENTICAL','condicion_booleana',1,'p_condicion_boolena','sintactico.py',69),
  ('condicion_booleana -> IS_NOT_IDENTICAL','condicion_booleana',1,'p_condicion_boolena','sintactico.py',70),
  ('condicion_booleana -> BOOLEAN_NOT','condicion_booleana',1,'p_condicion_boolena','sintactico.py',71),
  ('operaciones_mat -> op_basicas','operaciones_mat',1,'p_operaciones_mat','sintactico.py',76),
  ('operaciones_mat -> op_recursivas','operaciones_mat',1,'p_operaciones_mat','sintactico.py',77),
  ('op_basicas -> valor operadores valor','op_basicas',3,'p_op_basicas','sintactico.py',80),
  ('op_basicas -> LPAREN valor operadores valor RPAREN','op_basicas',5,'p_op_basicas','sintactico.py',81),
  ('op_recursivas -> valor operadores op_recursivas','op_recursivas',3,'p_op_recursivas','sintactico.py',85),
  ('op_recursivas -> valor LPAREN valor operadores valor RPAREN operaciones_mat','op_recursivas',7,'p_op_recursivas','sintactico.py',86),
  ('asignacion -> VARIABLE EQUALS valor SEMI','asignacion',4,'p_asignacion','sintactico.py',90),
  ('asignacion_array -> VARIABLE EQUALS array_def SEMI','asignacion_array',4,'p_asignacion_array','sintactico.py',95),
  ('constante -> DEFINE LPAREN STRING COMMA valor RPAREN SEMI','constante',7,'p_constante','sintactico.py',98),
  ('constante -> DEFINE LPAREN NOMBRE COMMA ARRAY RPAREN SEMI','constante',7,'p_constante','sintactico.py',99),
  ('lectura -> READLINE LPAREN STRING RPAREN SEMI','lectura',5,'p_lectura','sintactico.py',103),
  ('lectura -> READLINE LPAREN RPAREN SEMI','lectura',4,'p_lectura','sintactico.py',104),
  ('param -> VARIABLE','param',1,'p_param','sintactico.py',107),
  ('param -> asignacion','param',1,'p_param','sintactico.py',108),
  ('funcion_nparams -> FUNCTION NOMBRE LPAREN params_list RPAREN stc_bloque_def','funcion_nparams',6,'p_funcion_nparams','sintactico.py',111),
  ('params_list -> params_list COMMA param','params_list',3,'p_params_list','sintactico.py',114),
  ('params_list -> param','params_list',1,'p_params_list','sintactico.py',115),
  ('condicion -> VARIABLE operador_logico VARIABLE','condicion',3,'p_condicion','sintactico.py',119),
  ('condicion -> valor operador_logico valor','condicion',3,'p_condicion','sintactico.py',120),
  ('bwhile -> WHILE LPAREN condicion RPAREN LBRACE stc_bloque RBRACE','bwhile',7,'p_bwhile','sintactico.py',126),
  ('bfor -> FOR LPAREN asignacion SEMI condicion SEMI for_incr RPAREN stc_bloque_def','bfor',9,'p_bfor','sintactico.py',131),
  ('stc_bloque -> stc_bloque cuerpo','stc_bloque',2,'p_stc_bloque','sintactico.py',134),
  ('stc_bloque -> empty','stc_bloque',1,'p_stc_bloque','sintactico.py',135),
  ('stc_bloque_def -> LBRACE stc_bloque RBRACE','stc_bloque_def',3,'p_stc_bloque_def','sintactico.py',138),
  ('for_incr -> VARIABLE SUMA SUMA','for_incr',3,'p_for_incr','sintactico.py',141),
  ('for_incr -> SUMA SUMA VARIABLE','for_incr',3,'p_for_incr','sintactico.py',142),
  ('for_incr -> VARIABLE RESTA RESTA','for_incr',3,'p_for_incr','sintactico.py',143),
  ('for_incr -> RESTA RESTA VARIABLE','for_incr',3,'p_for_incr','sintactico.py',144),
  ('for_incr -> VARIABLE SUMA EQUALS numero','for_incr',4,'p_for_incr','sintactico.py',145),
  ('for_incr -> VARIABLE RESTA EQUALS numero','for_incr',4,'p_for_incr','sintactico.py',146),
  ('bforeach -> FOREACH LPAREN VARIABLE AS VARIABLE RPAREN stc_bloque_def','bforeach',7,'p_bforeach','sintactico.py',149),
  ('array_def -> ARRAY LPAREN RPAREN','array_def',3,'p_array_def','sintactico.py',152),
  ('array_def -> ARRAY LPAREN array_elmnt RPAREN','array_def',4,'p_array_def','sintactico.py',153),
  ('array_elmnt -> valor','array_elmnt',1,'p_array_elmnt','sintactico.py',155),
  ('array_elmnt -> empty','array_elmnt',1,'p_array_elmnt','sintactico.py',156),
  ('btry -> TRY LBRACE stc_bloque_def RBRACE catches','btry',5,'p_btry','sintactico.py',159),
  ('catches -> catches CATCH LPAREN NOMBRE VARIABLE RPAREN stc_bloque_def','catches',7,'p_catches','sintactico.py',162),
  ('catches -> empty','catches',1,'p_catches','sintactico.py',163),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',166),
]
