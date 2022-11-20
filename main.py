from analyzers.lexico import tokens, lexer


#Construya el lexer

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
  f = open(script, "r")
  lines = f.readlines()
  for line in lines:
    print("\n", line, "\n")
    lexer.input(line)
    while True:
      tok = lexer.token()
      if not tok:
        break
      print(">>", tok)
  print("============================================================")

