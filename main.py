import analyzers.sintactico as sintactico

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  sintactico.validaRegla(s)


