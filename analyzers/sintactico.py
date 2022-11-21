import ply.yacc as sintactico
from analyzers.lexico import tokens
import datetime, pytz
resultado_sintactico = []

def p_cuerpo(p):  # TODOS
  '''cuerpo : imprimir
            | asignacion
            | asignacion_array
            | funciones
            | constante
            | lectura
            | operadores
            | operador_logico
            | condicion_booleana
            | bwhile
            | bdo
            | bfor
            | bforeach
            | btry
            | operaciones_mat
            | condicion_ifelse 
            | bswitch
            | bgoto
            | bcolas
            | bpila
            | incrementos_mat
            | bcortes
            | brand
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
          | DECIMAL
  '''


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
  '''


def p_condicion_if(p):  #KEyla franco
  '''condicion_if :  IF LPAREN condicion RPAREN LBRACE cuerpo RBRACE
  '''


def p_condicion_elseif(p):  #KEyla franco
  '''condicion_elseif :  ELSEIF LPAREN condicion RPAREN LBRACE cuerpo RBRACE
  '''


def p_condicion_else(p):  #KEyla franco
  '''condicion_else :  ELSE LBRACE cuerpo RBRACE
  '''


def p_condicion_ifelse(p):  # keyla franco
  '''condicion_ifelse :  condicion_if
                      | condicion_if condicion_else
                      | condicion_if condicion_elseif
                      | condicion_if condicion_elseif condicion_else
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


def p_operaciones_mat(p):  #Keyla Franco
  '''operaciones_mat :  valor operadores valor
                        | valor operadores operaciones_mat
                        | operaciones_mat_par
                       
  '''


def p_operaciones_mat_par(p):  #Keyla Franco
  '''operaciones_mat_par :  LPAREN valor operadores valor RPAREN
                          |  LPAREN valor operadores operaciones_mat_par RPAREN
                          |  valor operadores operaciones_mat_par 
  '''


def p_asignacion(p):  # Keyla Franco
  '''asignacion : VARIABLE EQUALS valor SEMI
                | VAR asignacion
                | proteccion asignacion
  '''


def p_asignacion_array(p):  # Joby Farra
  'asignacion_array : VARIABLE EQUALS array_def SEMI'


def p_constante(p):  # Joby Farra
  '''constante : DEFINE LPAREN STRING COMMA valor RPAREN SEMI
          | DEFINE LPAREN NOMBRE COMMA ARRAY RPAREN SEMI'''


def p_lectura(p):  # Joby Farra
  '''lectura : READLINE LPAREN STRING RPAREN SEMI
          | READLINE LPAREN RPAREN SEMI'''


def p_brand(p):
  'brand : RAND LPAREN ENTERO COMMA ENTERO RPAREN SEMI'


def p_proteccion(p):
  '''proteccion : PUBLIC
          | PRIVATE
          | PROTECTED
          | STATIC
  '''


def p_funciones(p):  #TODOS
  '''funciones : funcion_nparams
              | proteccion funcion_nparams
              | funcion_blank
              | proteccion funcion_blank
              | funcion_void
  '''


def p_param(p):  # Joby Farra
  '''param : VARIABLE
          | asignacion'''


def p_funcion_nparams(p):  # Joby Farra
  'funcion_nparams : FUNCTION NOMBRE LPAREN params_list RPAREN stc_bloque_def'


def p_params_list(p):  # Joby Farra
  '''params_list : params_list COMMA param
                      | param'''


def p_funcion_void(p):  #Keyla franco
  'funcion_void : FUNCTION NOMBRE LPAREN  RPAREN COLON VOID LBRACE empty RBRACE'


def p_funcion_blank(p):  #keyla Franco
  ''' funcion_blank : FUNCTION NOMBRE LPAREN  RPAREN stc_bloque_def
                    | FUNCTION NOMBRE LPAREN  RPAREN LBRACE empty RBRACE
  '''


def p_condicion(p):  # Ricardo Zaruma
  ''' condicion : VARIABLE operador_logico VARIABLE
            | valor operador_logico valor 
            | VARIABLE operador_logico valor
  '''


def p_bwhile(p):  # Ricardo Zaruma
  ''' bwhile : WHILE LPAREN condicion RPAREN LBRACE stc_bloque RBRACE 
  | WHILE LPAREN condicion RPAREN COLON stc_bloque  
  '''


def p_bdo(p):  #Keyla franco
  ''' bdo : DO LBRACE cuerpo RBRACE bwhile 
  '''


def p_bswitch(p):  # Ricardo Zaruma
  ''' bswitch : SWITCH LPAREN VARIABLE RPAREN LBRACE innerSwitch RBRACE'''


def p_innerSwitch(p):  # Ricardo Zaruma
  ''' innerSwitch : CASE ENTERO COLON cuerpo BREAK SEMI
    | CASE ENTERO COLON cuerpo BREAK SEMI innerSwitch 
  '''


def p_bcolas(p):  #ricardo Zaruma
  ''' bcolas : VARIABLE EQUALS NEW SPLQUEUE LPAREN RPAREN SEMI
  '''


def p_bfor(p):  # Joby Farra
  'bfor : FOR LPAREN asignacion condicion SEMI for_incr RPAREN stc_bloque_def'


def p_stc_bloque(p):  # Joby Farra
  '''stc_bloque : stc_bloque SEMI cuerpo
        | empty
        | RETURN
        | RETURN NULL
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


def p_bforeach(p):  # Joby Farra
  'bforeach :  FOREACH LPAREN VARIABLE AS VARIABLE RPAREN stc_bloque_def'


def p_array_def(p):  # Joby Farra
  '''array_def : ARRAY LPAREN RPAREN
          | ARRAY LPAREN array_elmnt RPAREN'''


def p_array_elmnt(p):  # Joby Farra
  '''array_elmnt : array_elmnt COMMA valor
            | valor'''


def p_btry(p):  # Joby Farra
  'btry : TRY LBRACE stc_bloque_def RBRACE catches'


def p_catches(p):  # Joby Farra
  '''catches : catches CATCH LPAREN NOMBRE VARIABLE RPAREN stc_bloque_def
          | empty'''


def p_empty(p):  # Joby Farra
  'empty : '


def p_bgoto(p):  #Keyla Franco
  'bgoto : GOTO NOMBRE SEMI'


def p_bpila(p):  #Keyla Franco
  'bpila : VARIABLE EQUALS NEW SPLSTACK LPAREN RPAREN SEMI'


def p_bcortes(p):  #Keyla franco
  '''bcortes : EXIT SEMI
              | BREAK SEMI
              | DEFAULT SEMI
              | CONTINUE SEMI
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


# Build the parser
parser = sintactico.yacc()
archivos = ["script-farra.txt","script-franco.txt","script-zaruma.txt"]
for script in archivos:
  file = open(script, 'r')
  log = open('logs.txt', 'a')
  content = file.read()
  lines = 0
  line_log= "\nPRUEBA DE SCRIPT \n"
  log.write(line_log)
  for item in content.splitlines():
    lines += 1
    if item:
      gram = sintactico.parse(item)
      if gram is None:
        lin=f"Linea: {str(lines)} | {str(item)}| Info: No hay errores! \n"
        log.write(lin)
        print(lin)
        
      else:
        lin = f"Linea: {str(lines)} | Info: {str(gram)} \n"
        log.write(lin)
        print(lin)
  file.close()
  log.close()