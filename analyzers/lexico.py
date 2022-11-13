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
