import ply.yacc as sintactico
from analyzers.lexico import tokens
import datetime, pytz


def p_cuerpo(p):  # TODOS
  '''cuerpo : imprimir
            | asignacion
            | asignacion_array
            | funcion_nparams
            | constante
            | lectura
            | operadores
            | operador_logico
            | condicion_booleana
            | bwhile
            | bfor
            | bforeach
            | btry
            | operaciones_mat
            | condicion_if
  '''


def p_imprimir(p):  #Ricardo Zaruma
  '''imprimir : ECHO valor SEMI
            | PRINT valor SEMI
            | PRINT LPAREN valor RPAREN SEMI
            | ECHO NOMBRE LBRACKET ENTERO RBRACKET SEMI
  '''


def p_valor(p):  #KEYLA FRANCO
  '''valor : numero
            | VARIABLE
            | STRING
            | NOMBRE
  '''

def p_numero(p):
  '''numero : ENTERO
          | DECIMAL'''

def p_operadores(p):  #KEYLA FRANCO
  '''operadores : SUMA 
                  | RESTA
                  | MULTIPLICACION
                  | DIVISION
                  | MODULO
  '''


def p_operador_logico(p):  #Keyla franco
  '''operador_logico :  SMALLER
                        | GREATER
                        | IS_SMALLER_OR_EQUAL
                        | IS_GREATER_OR_EQUAL
  '''
def p_condicion_if(p): #KEyla franco
  '''condicion_if :  IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE
  '''

def p_condicion_boolena(p):  #Keyla Franco
  '''condicion_booleana :  AND
                        | OR
                        | XOR
                        | IS_EQUAL
                        | IS_NOT_EQUAL
                        | IS_IDENTICAL
                        | IS_NOT_IDENTICAL
                        | BOOLEAN_NOT
  '''


def p_operaciones_mat(p): #Keyla Franco
  '''operaciones_mat :  op_basicas
                        | op_recursivas
  '''
def p_op_basicas(p): #Keyla franco
    '''op_basicas :  valor operadores valor
                      | LPAREN valor operadores valor RPAREN
  '''

def p_op_recursivas(p): #Keyla franco
  '''op_recursivas :  valor operadores op_recursivas
                    | valor LPAREN valor operadores valor RPAREN operaciones_mat
  '''

def p_asignacion(p):  # Keyla Franco
  'asignacion : VARIABLE EQUALS valor SEMI'
  p[0] = ('asignacion', p[1])
  

def p_asignacion_array(p): # Joby Farra
  'asignacion_array : VARIABLE EQUALS array_def SEMI'

def p_constante(p):  # Joby Farra
  '''constante : DEFINE LPAREN STRING COMMA valor RPAREN SEMI
          | DEFINE LPAREN NOMBRE COMMA ARRAY RPAREN SEMI'''


def p_lectura(p):  # Joby Farra
  '''lectura : READLINE LPAREN STRING RPAREN SEMI
          | READLINE LPAREN RPAREN SEMI'''

def p_param(p): # Joby Farra
  '''param : VARIABLE
          | asignacion'''

def p_funcion_nparams(p): # Joby Farra
  'funcion_nparams : FUNCTION NOMBRE LPAREN params_list RPAREN stc_bloque_def'

def p_params_list(p): # Joby Farra
  '''params_list : params_list COMMA param
                      | param'''


def p_condicion(p): # Ricardo Zaruma
  ''' condicion : VARIABLE operador_logico VARIABLE
            | valor operador_logico valor
          
  '''


def p_bwhile(p): # Ricardo Zaruma
  ''' bwhile : WHILE LPAREN condicion RPAREN LBRACE stc_bloque RBRACE
  '''


def p_bfor(p): # Joby Farra
  'bfor : FOR LPAREN asignacion SEMI condicion SEMI for_incr RPAREN stc_bloque_def'

def p_stc_bloque(p): # Joby Farra
  '''stc_bloque : stc_bloque cuerpo
        | empty'''

def p_stc_bloque_def(p): # Joby Farra
  'stc_bloque_def : LBRACE stc_bloque RBRACE'

def p_for_incr(p): # Joby Farra
  '''for_incr : VARIABLE SUMA SUMA
          | SUMA SUMA VARIABLE
          | VARIABLE RESTA RESTA
          | RESTA RESTA VARIABLE
          | VARIABLE SUMA EQUALS numero
          | VARIABLE RESTA EQUALS numero'''

def p_bforeach(p): # Joby Farra
  'bforeach :  FOREACH LPAREN VARIABLE AS VARIABLE RPAREN stc_bloque_def'

def p_array_def(p): # Joby Farra
  '''array_def : ARRAY LPAREN RPAREN 
          | ARRAY LPAREN array_elmnt RPAREN'''
def p_array_elmnt(p): # Joby Farra
    '''array_elmnt : valor
            | empty'''

def p_btry(p): # Joby Farra
  'btry : TRY LBRACE stc_bloque_def RBRACE catches'

def p_catches(p): # Joby Farra
  '''catches : catches CATCH LPAREN NOMBRE VARIABLE RPAREN stc_bloque_def
          | empty'''

def p_empty(p): # Joby Farra
  'empty : '

def add_log(s, result): 

  log = open('logs.txt', 'a')
  line = f"Input: {s}, el resultado fue: {str(result)} en {datetime.datetime.now(pytz.timezone('America/Guayaquil'))} \n"
  log.write(line)
  log.close()


def p_error(p):
  if p:
    print(
      f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}"
    )
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")


def validaRegla(s):
  result = parser.parse(s)
  add_log(s, result)
  print(result)
  print()


# Build the parser
parser = sintactico.yacc()
