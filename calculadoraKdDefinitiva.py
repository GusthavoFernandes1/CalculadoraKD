import tkinter as tk
from tkinter import messagebox



fundo = "#dde"
letra = "#000"





def calcular_kd():
    nickname = entry_nickname.get()
    mapa     = entry_mapa.get()
    kills    = int(entry_kills.get())
    deaths   = int(entry_deaths.get())
    


    if deaths == 0:
        messagebox.showerror("Erro", "Deaths não pode ser Zero.")
        return
    
    assists  = int(entry_assists.get())

    kd  = kills / deaths
    kdr = (kills + assists) / deaths

# Salvar no arquivo de texto
    with open(f"{nickname}.txt", "a") as arquivo:
        arquivo.write(f"Data: {data_var.get()}\n")
        arquivo.write(f"Nickname: {nickname}\n")
        arquivo.write(f"Mapa: {mapa}\n")
        arquivo.write(f"Kills: {kills}\n")
        arquivo.write(f"Deaths: {deaths}\n")
        arquivo.write(f"Assists: {assists}\n")
        arquivo.write(f"Seu KD: {kd:.2f}\n")
        arquivo.write(f"Seu KDA: {kdr:.2f}\n\n")

    # Limpar os campos
    entry_nickname.delete(0, tk.END)
    entry_mapa.delete(0, tk.END)
    entry_kills.delete(0, tk.END)
    entry_deaths.delete(0, tk.END)
    entry_assists.delete(0, tk.END)

# Abrir o arquivo

    try:
        with open(f"{nickname}.txt", "r") as arquivo:
            arquivo_content = arquivo.read()
            messagebox.showinfo("Arquivo", arquivo_content)
    except FileNotFoundError:
        messagebox.showinfo("Arquivo", "O arquivo não foi encontrado.")


# Configurar a janela principal
app = tk.Tk()
app.title("Calculadora KD e KDA")
app.geometry("400x300")
app.configure(background= fundo)

# Labels

label_data = tk.Label(app, text="Data:", bg= fundo, fg= letra)
label_nickname = tk.Label(app, text="Nickname:", bg= fundo, fg= letra)
label_mapa = tk.Label(app, text="Nome do Mapa", bg= fundo, fg= letra)
label_kills = tk.Label(app, text="Kills:", bg= fundo, fg= letra)
label_deaths = tk.Label(app, text="Deaths:", bg= fundo, fg= letra)
label_assists = tk.Label(app, text="Assists:", bg= fundo, fg= letra)

# Entradas de texto

data_var = tk.StringVar()
entry_data = tk.Entry(app, textvariable=data_var)
entry_nickname = tk.Entry(app)
entry_mapa = tk.Entry(app)
entry_kills = tk.Entry(app)
entry_deaths = tk.Entry(app)
entry_assists = tk.Entry(app)

# Botão para calcular KD/KDR e salvar no arquivo

calcular_botao = tk.Button(app, text="Calcular KD/KDA", command=calcular_kd)

# Posicionamento dos widgets usando o método place
label_data.place(x=20, y=20)
label_nickname.place(x=215, y=20)
label_mapa.place(x=145, y=60)
label_kills.place(x=50, y=130)
label_deaths.place(x=125, y=130)
label_assists.place(x=220, y=130)

entry_data.place(x=55, y=23, width= 65)
entry_nickname.place(x=280, y=23, width= 90)
entry_mapa.place(x=128, y=80)
entry_kills.place(x=80, y=133, width= 24)
entry_deaths.place(x=170, y=133, width= 24)
entry_assists.place(x=265, y=133, width= 24)

calcular_botao.place(x=130, y=200)


app.mainloop()