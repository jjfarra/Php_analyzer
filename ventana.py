import analyzers.sintactico as sx
import analyzers.lexico as lx
import tkinter as tk

ventana = tk.Tk()

# Basic Information
ventana.title("PhP-Analyzer")
ventana.geometry("950x700+500+100")


tk.Label(ventana, text="Entrada").grid(row=0, columnspan=3)
input_scroll = tk.Scrollbar(ventana)
input_scroll.grid(row=1, column=0, rowspan=6, columnspan=3, sticky=tk.N + tk.S + tk.E)
input_code = tk.Text(ventana, height=15, width=85, 
                     yscrollcommand=input_scroll.set)
input_code.configure(relief="ridge", borderwidth=5)
input_code.grid(row=1, column=0, rowspan=6, columnspan=3, padx=20, pady=10)
input_scroll.config(command=input_code.yview)

tk.Label(ventana, text="Analizador Lexico").grid(row=7, column=0, columnspan=2)
lexicon_scroll = tk.Scrollbar(ventana)
lexicon_scroll.grid(row=8, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E)
lexicon_output = tk.Text(ventana, height=15, width=50,
                         yscrollcommand=lexicon_scroll.set)
lexicon_output.configure(relief="ridge", borderwidth=5)
lexicon_output.grid(row=8, column=0, columnspan=2, padx=0, pady=10)
lexicon_scroll.config(command=lexicon_output.yview)

tk.Label(ventana, text="Analizador Sintactico").grid(row=7, column=2, columnspan=2)
syntax_scroll = tk.Scrollbar(ventana)
syntax_scroll.grid(row=8, column=2, columnspan=2, sticky=tk.N + tk.S + tk.E)
syntax_output = tk.Text(ventana, height=15, width=50,
                        yscrollcommand=syntax_scroll.set)
syntax_output.configure(relief="ridge", borderwidth=5)
syntax_output.grid(row=8, column=2, columnspan=2, padx=0, pady=10)
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
    lines = code_to_analize.strip().split(eof)
    print(lines)

    for line in lines:
        k = line.replace("\t", "")
        if skipping_condition(k):
            continue
        if line != "\n":
            if line.startswith("for") or line.startswith("switch") or line.startswith("if"):
                index = lines.index(line) + 1
                print("Start analyzing a CONTROL STRUCTURE")
                attach = line
                while True:
                    attach += " " + lines[index]
                    index += 1
                    if index == len(lines):
                        line = attach
                        break
            print_syntax_result(line)


def print_syntax_result(code):
    syntax_result = sx.analizador_sintactico(code)
    if syntax_result is not None:
        syntax_result = prettier(syntax_result)
        syntax_result = str(syntax_result) + "\n"
        syntax_output.insert(tk.INSERT, syntax_result)
    else:
        syntax_result = "Error de sintaxis \n"
        syntax_output.insert(tk.INSERT, syntax_result)


def prettier(code):
    var = ""
    code1 = code
    counter = 0
    while len(code1) != 1:
        if not str(code1[0]).isupper():
            code1 = code1[1]
        else:
            var += tab * counter + ">>" + code1[0] + eof
            counter += 1
            code1 = code1[1]
    return var


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
button_both.grid(row=3, column=3, padx=20, pady=20)

button_clear = tk.Button(ventana, text="Limpiar", padx=40, pady=10, command=lambda: clear())
button_clear.grid(row=4, column=3, padx=20, pady=20)

ventana.mainloop()