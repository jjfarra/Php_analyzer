import ply.yacc as sintactico
from analyzers.lexico import tokens
#from analyzers.lexSeman import tokens

import datetime, pytz

resultado_sintactico = []
  
def p_cuerpo(p):  # TODOS
  '''cuerpo : imprimir
            | asignacion
            | funciones
            | llamada_funcion
            | constante
            | lectura
            | bwhile
            | bdo
            | bfor
            | incrementOp
            | bforeach
            | btry
            | condicion_ifelse
            | condicion_else
            | condicion_elseif
            | bswitch
            | bcase
            | bgoto
            | bcolas
            | bpila
            | bcortes
            | brand
            | escribir
            | btrim
            | otros
            | breturn
            | comment
            | casting
            | bconcat
            | simbolos
  '''
  
#REGLAS BÁSICAS
#DECLARACIÓN DE VARIABLES
def p_asignacion(p):  # Keyla Franco
  '''asignacion : VARIABLE EQUALS valor SEMI
                | VAR asignacion
                | proteccion asignacion
                | VARIABLE EQUALS brand
                | VARIABLE EQUALS escribir
                | VARIABLE EQUALS btrim
                | VARIABLE EQUALS lectura
                | VARIABLE EQUALS bconcat
                | asignacion_array
                | VARIABLE EQUALS operaciones_mat SEMI
                | aumentoCasting
  '''
#ASIGNACION DE ARRAYS


def p_asignacion_array(p):  # Joby Farra
  'asignacion_array : VARIABLE EQUALS array_def SEMI'

#ASIGNACION DE CONSTANTES
def p_constante(p):  # Joby Farra
  '''constante : DEFINE LPAREN CADENA COMMA valor RPAREN SEMI
          | DEFINE LPAREN NOMBRE COMMA ARRAY RPAREN SEMI'''


#VALORES DE UNA VARIABLE
def p_valor(p):  #KEYLA FRANCO
  '''valor : tipoDato
            | bcolas
            | bpila
  '''


#TIPOS DE DATOS
def p_tipoDato(p):  #Keyla Franco
  '''tipoDato : numero
            | CADENA
            | BOOLEANO
  '''


def p_numero(p):  #KEYLA FRANCO
  '''numero : ENTERO
          | DECIMAL
  '''


#SALIDAS DEL PROGRAMA PERMITIDAS
def p_imprimir(p):  #Ricardo Zaruma
  '''imprimir : ECHO valor SEMI
            | PRINT valor SEMI
            | PRINT LPAREN valor RPAREN SEMI
            | PRINT bconcat
            | ECHO NOMBRE LBRACKET ENTERO RBRACKET SEMI
            | ECHO bconcat
            | ECHO operaciones_mat SEMI
            | PRINT operaciones_mat SEMI
  '''


#ESTRUCTURAS DE CONTROL
#IF
def p_condicion_if(p):  #KEyla franco
  '''condicion_if :  IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE
  '''  

#elif
def p_condicion_elseif(p):  #KEyla franco
  '''condicion_elseif :  ELSEIF LPAREN condicion RPAREN LBRACE cuerpo RBRACE
  '''

#else
def p_condicion_else(p):  #KEyla franco
  '''condicion_else :  ELSE LBRACE cuerpo RBRACE
  '''


def p_condicion_ifelse(p):  # keyla franco
  '''condicion_ifelse : condicion_if
                      | condicion_if condicion_else
                      | condicion_if condicion_elseif
                      | condicion_if condicion_elseif condicion_else
  '''


def p_condicion(p):  # Ricardo Zaruma
  ''' condicion : VARIABLE operador_logico VARIABLE
            | valor operador_logico valor 
            | VARIABLE operador_logico valor
            | VARIABLE condicion_booleana VARIABLE
            | valor condicion_booleana valor
            | VARIABLE condicion_booleana valor
            | LPAREN VARIABLE operadores valor RPAREN operador_logico valor
            | LPAREN VARIABLE operadores valor RPAREN condicion_booleana valor
            | condicion condicion_booleana condicion
            | condicion condicion_booleana comprobacion
            
  '''

#FOR
def p_bfor(p):  # Joby Farra
  'bfor : FOR LPAREN asignacion condicion SEMI for_incr RPAREN stc_bloque_def'


def p_stc_bloque(p):  # Joby Farra
  '''stc_bloque : stc_bloque SEMI cuerpo
        | breturn
        '''


def p_stc_bloque_def(p):  # Joby Farra
  'stc_bloque_def : LBRACE stc_bloque RBRACE'


def p_for_incr(p):  # Joby Farra
  '''for_incr : VARIABLE SUMA SUMA
          | SUMA SUMA VARIABLE
          | VARIABLE RESTA RESTA
          | RESTA RESTA VARIABLE
          | VARIABLE SUMA EQUALS numero
          | VARIABLE RESTA EQUALS numero'''

def p_incrementOp (p):
  '''
  incrementOp : VARIABLE SUMA SUMA SEMI
              | VARIABLE RESTA RESTA SEMI
  '''
  
def p_bforeach(p):  # Joby Farra
  'bforeach :  FOREACH LPAREN VARIABLE AS VARIABLE RPAREN stc_bloque_def'


#WHILE
def p_bwhile(p):  # Ricardo Zaruma
  ''' bwhile : WHILE LPAREN condicion RPAREN LBRACE stc_bloque RBRACE 
  | WHILE LPAREN condicion RPAREN COLON stc_bloque  
  '''


def p_bdo(p):  #Keyla franco
  ''' bdo : DO LBRACE cuerpo RBRACE bwhile 
  '''


#SWITCH CASE
def p_bswitch(p):  # Ricardo Zaruma
  ''' bswitch : SWITCH LPAREN VARIABLE RPAREN LBRACE innerSwitch RBRACE'''


def p_bcase(p):
  '''bcase : CASE ENTERO COLON
          | CASE CADENA COLON '''

def p_innerSwitch(p):  # Ricardo Zaruma
  ''' innerSwitch :  bcase cuerpo BREAK SEMI
                 | bcase cuerpo BREAK SEMI innerSwitch 
  '''


#TRY CATCH
def p_btry(p):  # Joby Farra
  'btry : TRY LBRACE stc_bloque_def RBRACE catches'


def p_catches(p):  # Joby Farra
  '''catches : catches CATCH LPAREN NOMBRE VARIABLE RPAREN stc_bloque_def
          | empty'''



#OPERADORES
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


def p_incrementos_mat(p):  #Keyla FRanco
  '''incrementos_mat :  MINUS_EQUAL
                        | MOD_EQUAL
                        | MUL_EQUAL
                        | PLUS_EQUAL
                        | DIV_EQUAL
  '''


def p_condicion_boolena(p):  #Keyla Franco
  '''condicion_booleana :  AND
                        | OR
                        | XOR
                        | IS_EQUAL
                        | IS_NOT_EQUAL
                        | IS_IDENTICAL
                        | IS_NOT_IDENTICAL
  '''


def p_operaciones_mat(p):  #Keyla Franco
  '''operaciones_mat :  valor operadores valor
                        | valor operadores operaciones_mat
                        | VARIABLE operadores VARIABLE
                        | operaciones_mat_par
                       
  '''

def p_operaciones_mat_par(p):  #Keyla Franco
  '''operaciones_mat_par :  LPAREN valor operadores valor RPAREN
                          |  LPAREN valor operadores operaciones_mat_par RPAREN
                          | LPAREN VARIABLE operadores VARIABLE RPAREN
                          | LPAREN VARIABLE operadores valor RPAREN operadores valor
  '''

#FUNCIONES
def p_funciones(p):  #TODOS
  '''funciones : funcion_nparams
              | proteccion funcion_nparams
              | funcion_blank
              | proteccion funcion_blank
              | funcion_void
  '''


def p_param(p):  # Joby Farra
  '''param : VARIABLE
          | asignacion
          '''


def p_funcion_nparams(p):  # Joby Farra
  'funcion_nparams : FUNCTION NOMBRE LPAREN params_list RPAREN stc_bloque_def'


def p_params_list(p):  # Joby Farra
  '''params_list : params_list COMMA param
                 | param
  '''

def p_funcion_void(p):  #Keyla franco
  'funcion_void : FUNCTION NOMBRE LPAREN  RPAREN COLON VOID LBRACE empty RBRACE'


def p_funcion_blank(p):  #keyla Franco
  ''' funcion_blank : FUNCTION NOMBRE LPAREN  RPAREN stc_bloque_def
                    | FUNCTION NOMBRE LPAREN  RPAREN LBRACE empty RBRACE
  '''

def p_llamada_funcion(p): #Keyla Franco
  'llamada_funcion : NOMBRE LPAREN params_list RPAREN SEMI'
  
def p_brand(p):
  'brand : RAND LPAREN ENTERO COMMA ENTERO RPAREN SEMI'


def p_proteccion(p): #Keyla franco
  '''proteccion : PUBLIC
          | PRIVATE
          | PROTECTED
          | STATIC
  '''

def p_breturn(p):
  '''breturn : empty
        | RETURN SEMI 
        | RETURN NULL SEMI
        | RETURN VARIABLE SEMI
        | RETURN BOOLEANO SEMI
        '''

#ESTRUCTURA DE DATOS
#ARRAY

def p_array_def(p):  # Joby Farra
  '''array_def : ARRAY LPAREN RPAREN
          | ARRAY LPAREN array_elmnt RPAREN'''

def p_array_elmnt(p):  # Joby Farra
  '''array_elmnt : array_elmnt COMMA valor
            | valor'''

def p_empty(p):  # Joby Farra
  'empty : '


#COLAS
def p_bcolas(p):  #ricardo Zaruma
  ''' bcolas : VARIABLE EQUALS NEW SPLQUEUE LPAREN RPAREN SEMI
  '''
  
#PILAS
def p_bpila(p):  #Keyla Franco
  'bpila : VARIABLE EQUALS NEW SPLSTACK LPAREN RPAREN SEMI'


#LECTURA Y ESCRITURA
def p_lectura(p):  # Joby Farra
  '''lectura : READLINE LPAREN CADENA RPAREN SEMI
          | READLINE LPAREN RPAREN SEMI'''
  
def p_escribir (p): #KEYLA FRANCO
  '''escribir : FWRITE LPAREN NOMBRE COMMA CADENA RPAREN SEMI
   '''

def p_btrim (p): #KEYLA RANCO
  '''btrim : TRIM LPAREN NOMBRE LPAREN NOMBRE RPAREN RPAREN SEMI
   '''
  
#OTROS
def p_comment(p):
  '''comment : COMENTARIOS
              | DOC_COMENTARIOS
   '''

def p_bgoto(p):  #Keyla Franco
  'bgoto : GOTO NOMBRE SEMI'


def p_bcortes(p):  #Keyla franco
  '''bcortes : EXIT SEMI
              | BREAK SEMI
              | DEFAULT SEMI
              | CONTINUE SEMI
   '''

def p_otros(p): #kEYLA FRANCO
  '''otros : SMALLER NOMBRE GREATER
            | NOMBRE COLON 
   '''
#Nota: NOMBRE COLON hace referencia al inicio de la instrucción goto, sin ella, no tiene a donde regresar


def p_comprobacion(p): #KEYLA FRANCO
  '''
    comprobacion : NOMBRE LPAREN valor RPAREN
                  | NOMBRE LPAREN VARIABLE RPAREN
  '''
def p_simbolos(p): #KEYLA FRANCO
  '''
  simbolos : LPAREN RPAREN
            | LPAREN
            | RPAREN
            | LBRACKET RBRACKET
            | LBRACKET
            | RBRACKET
            | LBRACE RBRACE
            | LBRACE
            | RBRACE instrucciones
            | OPEN_TAG CLOSE_TAG
            | OPEN_TAG
            | CLOSE_TAG
  '''

def p_instrucciones(p):
  '''
    instrucciones : condicion_else
                  | condicion_elseif
                  | bwhile
                  | bfor
  '''
  
#REGLA SEMÁNTICA OPERACIONES ENTRE STRINGS
def p_bconcat(p): #Ricardo Zaruma
  '''bconcat : CADENA CONCAT CADENA SEMI
            |  VARIABLE CONCAT VARIABLE SEMI
            | VARIABLE CONCAT CADENA SEMI
            | VARIABLE CONCAT_EQUAL CADENA SEMI
            | CADENA CONCAT_EQUAL CADENA SEMI
            
   '''
#REGLA SEMÁNTICA CASTING
def p_tiposCast(p): #ricardo zaruma
  '''tiposCast :  STRING
            | BOOL
            | BOOLEAN
            | DOUBLE
            | FLOAT
            | ARRAY
            | OBJECT 
            | INTEGER
            | INT
        
            
   '''
  
def p_casting(p): #ricardo zaruma
  '''casting : VARIABLE EQUALS LPAREN tiposCast RPAREN VARIABLE SEMI  
              | LPAREN tiposCast RPAREN VARIABLE SEMI
   '''
def p_aumentoCasting(p): #Keyla franco
  '''
    aumentoCasting : VARIABLE incrementos_mat tipoDato SEMI
                    | VARIABLE EQUALS VARIABLE operadores tipoDato SEMI
  '''
#ERROR
def p_error(p):
  global resultado_sintactico
  resultado_sintactico.clear()
  if p:
    resultado = "Error sintactico de tipo: {} en el valor: {}".format(
      str(p.type), str(p.value))
    print(resultado)
  else:
    resultado = "Error sintactico: {}".format(p)
    print(resultado)
  resultado_sintactico.append(resultado)


#AÑADIENDO EL LOG
def add_log(s, result):

  log = open('logs.txt', 'a')
  line = f"Input: {s}, el resultado fue: {str(result)} en {datetime.datetime.now(pytz.timezone('America/Guayaquil'))} \n"
  log.write(line)

  log.close()


def validaRegla(s):
  result = parser.parse(s)
  add_log(s, result)
  print(result)
  print()


def analizador_sintactico(data):
  return parser.parse(data)


# Build the parser
parser = sintactico.yacc()
scripts = ["prueba.txt"]
archivos = ["script-zaruma.txt"]
for script in archivos:
  file = open(script, 'r')
  log = open('logs.txt', 'a')
  content = file.read()
  lines = 0
  line_log = "\nPRUEBA DE SCRIPT \n"
  log.write(line_log)
  for item in content.splitlines():
    lines += 1
    if item:
      gram = sintactico.parse(item)
      if gram is None:
        lin = f"Linea: {str(lines)} | {str(item)}| Info: No hay errores! \n"
        log.write(lin)
        print(lin)

      else:
        lin = f"Linea: {str(lines)} | Info: {str(gram)} \n"
        log.write(lin)
        print(lin)
  file.close()
  log.close()
