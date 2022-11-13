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

# Start Ricardo Zaruma

# OPERADORES
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
t_INI_COMMENT = r'/*'
t_FIN_COMMENT = r'*/'
t_COMMENT = r'#'

# Comentarios


def t_DOC_COMENTARIOS(t):
    r'/\*\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_COMENTARIOS(t):
    r'/\*(.|\n)*?\*/ | //([^?%\n]|[?%](?!>))*\n? | \#([^?%\n]|[?%](?!>))*\n?'
    t.lexer.lineno += t.value.count("\n")
    return t
# DELIMITADORES


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
# php tags


def t_OPEN_TAG(t):
    r'<[?%]((php[ \t\r\n]?)|=)?'
    if '=' in t.value:
        t.type = 'OPEN_TAG_WITH_ECHO'
    t.lexer.lineno += t.value.count("\n")
    return t


def t_CLOSE_TAG(t):
    r'[?%]>\r?\n?'
    t.lexer.lineno += t.value.count("\n")
    return t

# END Ricardo Zaruma
