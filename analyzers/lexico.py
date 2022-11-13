import ply.lex as lex

# Start Joby Farra

reserved = {
    # Control Structures
    "if": "IF",
    "else": "ELSE",
    "elseif": "ELSEIF",
    "endif": "ENDIF",
    "break": "BREAK",
    "pass": "PASS",
    "conntinue": "CONTINUE",
    "default": "DEFAULT",
    "return": "RETURN",
    "require": "REQUIRE",

    # Loop Structure
    "for": "FOR",
    "while": "WHILE",
    "switch": "SWITCH",
    "case": "CASE",
    "foreach": "FOREACH",
    "match": "MATCH",
    "endfor": "ENDFOR",
    "endwhile": "ENDWHILE",
    "endswitch": "ENDSWITCH",

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
    "enum": "ENUM",
    "resource": "RESOURCE",
    "iterable": "ITERABLE",

    # Declaration words
    "function": "FUNCTION",
    "array": "ARRAY",
    "object": "OBJECT",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "static": "STATIC",
    "protected": "PROTECTED",
    "class": "CLASS",
    "new": "NEW",
    "implements": "IMPLEMENTS",
    "extends": "EXTENDS",

    # Match Functions
    "sqrt": "SQRT",
    "abs": "ABS",
    "rand": "RAND",
    "min": "MIN",
    "max": "MAX",
    "pi": "PI",

    # Handle Error
    "try": "TRY",
    "catch": "CATCH",

    # Other words
    "exit": "EXIT",
    "global": "GLOBAL",
    "goto": "GOTO",
    "print": "PRINT",
    "echo": "ECHO",
}

# END Joby Farra


#START Keyla Franco
tokens = [
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
  'SL',
  'SR',
  'BOOLEAN_AND',
  'BOOLEAN_OR',
  'BOOLEAN_NOT',
  'IS_SMALLER',
  'IS_GREATER',
  'IS_SMALLER_OR_EQUAL',
  'IS_GREATER_OR_EQUAL',
  'IS_EQUAL',
  'IS_NOT_EQUAL',
  'IS_IDENTICAL',
  'IS_NOT_IDENTICAL',

  #Tipos de datos
  'DIR',
  'FILE',
  'LINE',
  'FUNC_C',
  'CLASS_C',
  'METHOD_C',
  'NS_C',
  'LOGICAL_AND',
  'LOGICAL_OR',
  'LOGICAL_XOR',
  'HALT_COMPILER',
  'VARIABLE',
  'ENTERO',
  'DECIMAL',
  'NUM_STRING',
  'CONSTANT_ENCAPSED_STRING',
  'ENCAPSED_AND_WHITESPACE',
  'QUOTE',
  'DOLLAR_OPEN_CURLY_BRACES',
  'STRING_VARNAME',
  'CURLY_OPEN',
  #Comparadores
  'EQUALS',
  'MUL_EQUAL',
  'DIV_EQUAL',
  'MOD_EQUAL',
  'PLUS_EQUAL',
  'MINUS_EQUAL',
  'SL_EQUAL',
  'SR_EQUAL',
  'AND_EQUAL',
  'OR_EQUAL',
  'XOR_EQUAL',
  'CONCAT_EQUAL',
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
  'DOLLAR',
  'COMMA',
  'CONCAT',
  'QUESTION',
  'COLON',
  'SEMI',
  'AT',
  'NS_SEPARATOR',
  #PHP TAGS
  'OPEN_TAG',
  'CLOSE_TAG',
  #ESPACIO EN BLANCO
  'WHITESPACE'
] + list(reserved.values())

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
t_SL = r'<<'
t_SR = r'>>'
t_BOOLEAN_AND = r'&&'
t_BOOLEAN_OR = r'\|\|'
t_BOOLEAN_NOT = r'!'
t_IS_SMALLER = r'<'
t_IS_GREATER = r'>'
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
t_SL_EQUAL = r'<<='
t_SR_EQUAL = r'>>='
t_AND_EQUAL = r'&='
t_OR_EQUAL = r'\|='
t_XOR_EQUAL = r'\^='
t_CONCAT_EQUAL = r'\.='

# DELIMITADORES
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOLLAR = r'\$'
t_COMMA = r','
t_CONCAT = r'\.(?!\d|=)'
t_QUESTION = r'\?'
t_COLON = r':'
t_SEMI = r';'
t_AT = r'@'
t_NS_SEPARATOR = r'\\'

# Comentarios

def t_DOC_COMENTARIOS(t):
    r'/\*\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/ | //([^?%\n]|[?%](?!>))*\n? | \#([^?%\n]|[?%](?!>))*\n?'
    t.lexer.lineno += t.value.count("\n")
    return t

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
    r'<[?%]((php[ \t\r\n]?)|=)?'
    if '=' in t.value: t.type = 'OPEN_TAG_WITH_ECHO'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_CLOSE_TAG(t):
    r'[?%]>\r?\n?'
    t.lexer.lineno += t.value.count("\n")
    return t


# END Ricardo Zaruma

# START Joby Farra

def t_INLINE_HTML(t):
    r'([^<]|<(?![?%]))+'
    t.lexer.lineno += t.value.count("\n")
    return t
  
def t_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    return t

def t_FLOATNUMBER(t):
    r'(\d*\.\d+|\d+\.\d*)([Ee][+-]?\d+)? | (\d+[Ee][+-]?\d+)'
    return t

def t_INTNUMBER(t):
    r'(0b[01]+)|(0x[0-9A-Fa-f]+)|\d+'
    return t

def t_QUOTE(t):
    r'"'
    t.lexer.push_state('quoted')
    return t

#END Joby Farra

#START KEYLA FRANCO
def t_newline(t):
    r'[\r\n]+'
    t.lexer.lineno += len(t.value)
  
def t_WHITESPACE(t):
    r'[ \t\r\n]+'
    t.lexer.lineno += t.value.count("\n")
    return t
  
def t_quoted_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    return t

def t_quoted_CURLY_OPEN(t):
    r'\{(?=\$)'
    return t
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
f = open("script-keylafranco.txt","r")
lines = f.readlines()
for line in lines:
  print("\n",line,"\n")
  lexer.input(line)
  while True:
    tok=lexer.token()
    if not tok:
      break
    print(">>",tok)

# END KEYLA FRANCO
