import analyzers.sintactico as sx
import analyzers.lexico as lx
import tkinter as tk
from analyzers.sintactico import resultado_sintactico
ventana = tk.Tk()

# Basic Information
ventana.title("PhP-Analyzer")
width= ventana.winfo_screenwidth()
height= ventana.winfo_screenheight()
#ventana.attributes('-fullscreen', True)
ventana.geometry("%dx%d" % (width, height))
eof='\n'
tab='\t'

tk.Label(ventana, text="Entrada").grid(row=0, columnspan=5)

input_scroll = tk.Scrollbar(ventana)
input_scroll.grid(row=1, column=0, rowspan=6, columnspan=3, sticky=tk.N + tk.S + tk.E)
input_code = tk.Text(ventana, height=15, width=100,
                     yscrollcommand=input_scroll.set)
input_code.configure(relief="ridge", borderwidth=5)
input_code.grid(row=1, column=0, rowspan=6, columnspan=3, padx=10, pady=10)
input_scroll.config(command=input_code.yview)

tk.Label(ventana, text="Analizador Lexico").grid(row=7, column=0, columnspan=2)
lexicon_scroll = tk.Scrollbar(ventana)
lexicon_scroll.grid(row=8, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E)
lexicon_output = tk.Text(ventana, height=35, width=60,
                         yscrollcommand=lexicon_scroll.set)
lexicon_output.configure(relief="ridge", borderwidth=5)
lexicon_output.grid(row=8, column=0, columnspan=2, padx=0, pady=10)
lexicon_scroll.config(command=lexicon_output.yview)

tk.Label(ventana, text="Analizador Sintactico").grid(row=7, column=2, columnspan=2)
syntax_scroll = tk.Scrollbar(ventana)
syntax_scroll.grid(row=8, column=4, columnspan=3, sticky=tk.N + tk.S + tk.E)
syntax_output = tk.Text(ventana, height=35, width=80,
                        yscrollcommand=syntax_scroll.set)
syntax_output.configure(relief="ridge", borderwidth=5)
syntax_output.grid(row=8, column=3, columnspan=1, padx=0, pady=10)
syntax_scroll.config(command=syntax_output.yview)


def lexicon(code):
    lexicon_output.delete('1.0', tk.END)
    code_to_analize = code.get("1.0", 'end-1c')
    lexicon_result = lx.analizador_lexico(code_to_analize)
    for result in lexicon_result:
        lexicon_output.insert(tk.INSERT, result)
    # print(code_to_analize)


def skipping_condition(text):
    end_of_structure = text == "}"
    if_structure = text == "} else {" or text == "}else{" or text.__contains__("else if")
    switch_structure = text == "default:" or text.__contains__("case")
    return end_of_structure or if_structure or switch_structure


def syntax(code):
    syntax_output.delete('1.0', tk.END)
    code_to_analize = code.get("1.0", 'end-1c')
    lines = code_to_analize.strip().splitlines()
    for idx in range(0,len(lines)):
        print_syntax_result(lines[idx])


def print_syntax_result(code):
    syntax_result = sx.analizador_sintactico(code)
    error = resultado_sintactico[-1] if len(resultado_sintactico)==1 else 'No hay error'
    syntax_result = f"Linea: {str(code)} | Resultado: {str(syntax_result)} | {error}\n"
    syntax_output.insert(tk.INSERT, syntax_result)





def both(code):
    lexicon(code)
    syntax(code)


def clear():
    input_code.delete('1.0', tk.END)

    lexicon_output.delete('1.0', tk.END)
    syntax_output.delete('1.0', tk.END)


button_lex = tk.Button(ventana, text="Analizador Lexico", padx=40, pady=10, command=lambda: lexicon(input_code))
button_lex.grid(row=1, column=3, padx=20, pady=20)

button_syntax = tk.Button(ventana, text="Analizador Sintactico", padx=40, pady=10, command=lambda: syntax(input_code))
button_syntax.grid(row=2, column=3, padx=20, pady=20)

button_both = tk.Button(ventana, text="Analizar Ambos", padx=40, pady=10, command=lambda: both(input_code))
button_both.grid(row=3, column=3, padx=40, pady=20)

button_clear = tk.Button(ventana, text="Limpiar", padx=60, pady=10, command=lambda: clear())
button_clear.grid(row=4, column=3, padx=20, pady=20)

ventana.mainloop()