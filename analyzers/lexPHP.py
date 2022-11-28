import ply.lex as lex

# Start Joby Farra

reserved = {
  # Control Structures
  "if": "IF",
  "else": "ELSE",
  "elseif": "ELSEIF",
  #"endif": "ENDIF",
  "break": "BREAK",
  "do": "DO",
  "as": "AS",
  "continue": "CONTINUE",
  "default": "DEFAULT",
  "return": "RETURN",
  #"require": "REQUIRE",
  "define" : "DEFINE",
  "SplQueue" : "SPLQUEUE",
  "SplStack" : "SPLSTACK",
  # Loop Structure
  "for": "FOR",
  "while": "WHILE",
  "switch": "SWITCH",
  "case": "CASE",
  "foreach": "FOREACH",
  "rand": "RAND",
  #"match": "MATCH",
  #"endfor": "ENDFOR",
  #"endwhile": "ENDWHILE",
  #"endswitch": "ENDSWITCH",

  # Data Types
  "int": "INT",
  "double": "DOUBLE",
  "float": "FLOAT",
  "bool": "BOOL",
  "string": "STRING",
  "var": "VAR",
  "void": "VOID",
  "null": "NULL",
  "true": "TRUE",
  "false": "FALSE",
  #"enum": "ENUM",
  #"resource": "RESOURCE",
  #"iterable": "ITERABLE",

  # Declaration words
  "function": "FUNCTION",
  "array": "ARRAY",
  #"object": "OBJECT",
  "public": "PUBLIC",
  "private": "PRIVATE",
  "static": "STATIC",
  "protected": "PROTECTED",
  #"class": "CLASS",
  "new": "NEW",
  "at": "AT",
  #"implements": "IMPLEMENTS",
  #"extends": "EXTENDS",

  # Match Functions
  #"sqrt": "SQRT",
  #"abs": "ABS",
  "rand": "RAND",
  #"min": "MIN",
  #"max": "MAX",
  #"pi": "PI",

  # Handle Error
  "try": "TRY",
  "catch": "CATCH",

  # Other words
  "exit": "EXIT",
  #"global": "GLOBAL",
  "goto": "GOTO",
  "print": "PRINT",
  "echo": "ECHO",
  "readline":"READLINE",
  "fwrite":"FWRITE",
  "trim" : "TRIM"
}

# END Joby Farra


#START Keyla Franco
tokens = [
  'NOMBRE',
  #Operadores
  'SUMA',
  'RESTA',
  'MULTIPLICACION',
  'DIVISION',
  'MODULO',
  'AND',
  'OR',
  'NOT',
  'XOR',
  'SMALLER',
  'GREATER',
  'IS_SMALLER_OR_EQUAL',
  'IS_GREATER_OR_EQUAL',
  'IS_EQUAL',
  'IS_NOT_EQUAL',
  'IS_IDENTICAL',
  'IS_NOT_IDENTICAL',
  'BOOLEAN_NOT',
  #Tipos de datos
  #'DIR',
  #'FILE',
  #'LINE',
  #'FUNC_C',
  #'CLASS_C',
  #'METHOD_C',
  #'NS_C',
  #'HALT_COMPILER',
  'VARIABLE',
  'ENTERO',
  'DECIMAL',
  #'NUM_STRING',
  #'CONSTANT_ENCAPSED_STRING',
  #'ENCAPSED_AND_WHITESPACE',
  #'CURLY_OPEN',
  #Comparadores
  'EQUALS',
  'MUL_EQUAL',
  'DIV_EQUAL',
  'MOD_EQUAL',
  'PLUS_EQUAL',
  'MINUS_EQUAL',
  #ignorar comentarios
  'COMENTARIOS',
  'DOC_COMENTARIOS',
  #DELIMITADORES
  'LPAREN',
  'RPAREN',
  'LBRACKET',
  'RBRACKET',
  'LBRACE',
  'RBRACE',
  'COMMA',
  'CONCAT',
  'CONCAT_EQUAL',
  'COLON',
  'SEMI',
  #'AT',
  #'NS_SEPARATOR',
  #PHP TAGS
  'OPEN_TAG',
  'CLOSE_TAG'
] + list(reserved.values())

t_ignore = ' \t'
#END Keyla Franco

# Start Ricardo Zaruma

#OPERADORES

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'
t_AND = r'&'
t_OR = r'\|'
t_NOT = r'~'
t_XOR = r'\^'
t_BOOLEAN_NOT = r'!'
t_IS_SMALLER_OR_EQUAL = r'<='
t_IS_GREATER_OR_EQUAL = r'>='
t_IS_EQUAL = r'=='
t_IS_NOT_EQUAL = r'(!=(?!=))|(<>)'
t_IS_IDENTICAL = r'==='
t_IS_NOT_IDENTICAL = r'!=='


# COMPARADORES
t_EQUALS = r'='
t_MUL_EQUAL = r'\*='
t_DIV_EQUAL = r'/='
t_MOD_EQUAL = r'%='
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_CONCAT_EQUAL = r'\.='

# DELIMITADORES
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_CONCAT = r'\.(?!\d|=)'
t_COLON = r':'
t_SEMI = r';'
t_AT = r'@'


# Comentarios

def t_DOC_COMENTARIOS(t):
    r'/\*\*(.|\n)*?\*/'
    t.lexer.skip(1)

def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/ | //([^?%\n]|[?%](?!>))*\n? | \#([^?%\n]|[?%](?!>))*\n?'
    t.lexer.skip(1)

#DELIMITADORES

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_LBRACE(t):
    r'\{'
    return t

def t_RBRACE(t):
    r'\}'
    return t
  
#php tags
def t_OPEN_TAG(t):
  r'(<\?(php)?)'
  return t

def t_CLOSE_TAG(t):
    r'\?>'
    return t


# END Ricardo Zaruma

# START Joby Farra
def t_STRING(t):
  r'(("[^"]*")|(\'[^\']*\'))'
  t.value = t.value[1:-1]
  return t

def t_NOMBRE(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "NOMBRE")
    return t

def t_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    return t

def t_DECIMAL(t):
    r'(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d+)? | (\d+[Ee][+-]?\d+)'
    return t

def t_ENTERO(t):
    r'(0b[01]+)|(0x[0-9A-Fa-f]+)|\d+'
    return t

#END Joby Farra

#START KEYLA FRANCO
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
  
  
def t_error(t):
    print("No es reconocido '%s'" %t.value[0])
    t.lexer.skip(1)

  
#Construya el lexer
lexer = lex.lex()
def analizar(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
      
#Lea el archivo y retorne los tokens
scripts = ["script-farra.txt", "script-franco.txt", "script-zaruma.txt"]
for script in scripts:
  f = open(script,"r")
  lines = f.readlines()
  for line in lines:
    print("\n",line,"\n")
    lexer.input(line)
    while True:
      tok=lexer.token()
      if not tok:
        break
      print(">>",tok)
  print("============================================================")

# END KEYLA FRANCO