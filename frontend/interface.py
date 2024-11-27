import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import tkinter as tk
from assistente import assistente_virtual
from reconhecimento_voz import ouvir_comando
from tkinter import filedialog

class AssistenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistente Virtual")

        # Frame superior (área de chat)
        top_frame = tk.Frame(root)
        top_frame.pack(pady=10)

        # Frame inferior (área de entrada e botões)
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(pady=10)

        # Área de texto para o diálogo
        self.chat_area = tk.Text(top_frame, wrap='word', height=20, width=50, state='disabled')
        self.chat_area.pack(pady=10)

        # Campo de entrada para o usuário
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(bottom_frame, textvariable=self.entry_var, width=40)
        self.entry.pack(side='left', padx=5)
        
        # Botão para enviar texto
        self.send_button = tk.Button(bottom_frame, text="Enviar", command=self.enviar_texto)
        self.send_button.pack(side='left', padx=5)

        # Botão para falar (ativar reconhecimento de voz)
        self.speak_button = tk.Button(bottom_frame, text="Falar", command=self.ativar_voz)
        self.speak_button.pack(side='left', padx=5)

        # Botão para abrir o navegador
        self.browser_button = tk.Button(root, text="Abrir Navegador", command=self.abrir_navegador)
        self.browser_button.pack(pady=5)

        # Botão para abrir uma pasta
        self.folder_button = tk.Button(root, text="Abrir Pasta", command=self.abrir_pasta)
        self.folder_button.pack(pady=5)

        # Rótulo para status de voz
        self.voice_label = tk.Label(root, text="", fg="blue")
        self.voice_label.pack(pady=5)

    def exibir_mensagem(self, texto, remetente="Você"):
        """Exibe uma mensagem no chat."""
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{remetente}: {texto}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def enviar_texto(self):
        """Envia texto digitado pelo usuário."""
        mensagem = self.entry_var.get()
        if mensagem:
            self.exibir_mensagem(mensagem, "Você")
            
            # Verificar se é um comando de pesquisa
            if "pesquisar" in mensagem:
                termo = mensagem.replace("pesquisar", "").strip()
                resultados = assistente_virtual(mensagem).split(";")
                self.mostrar_resultados(resultados)
            else:
                resposta = assistente_virtual(mensagem)  # Envia para o assistente
                self.exibir_mensagem(resposta, "Assistente")
            
            self.entry_var.set("")  # Limpa o campo de entrada

    def ativar_voz(self):
        """Ativa o reconhecimento de voz."""
        self.voice_label.config(text="Escutando...")  # Mostra o status
        self.root.update_idletasks()
        
        comando = ouvir_comando()  # Recebe o comando de voz
        self.voice_label.config(text="")  # Reseta o status após ouvir

        if comando:
            self.exibir_mensagem(comando, "Você")
            resposta = assistente_virtual(comando)
            self.exibir_mensagem(resposta, "Assistente")

    def abrir_navegador(self):
        """Abre o navegador usando o comando do assistente."""
        resposta = assistente_virtual("abrir navegador")
        self.exibir_mensagem(resposta, "Assistente")

    def abrir_pasta(self):
        """Abre uma pasta selecionada pelo usuário."""
        caminho = filedialog.askdirectory()
        if caminho:
            resposta = assistente_virtual(f"abrir pasta {caminho}")
            self.exibir_mensagem(resposta, "Assistente")

    def mostrar_resultados(self, resultados):
        """Mostra resultados de pesquisa em uma nova janela."""
        resultados_window = tk.Toplevel(self.root)
        resultados_window.title("Resultados da Pesquisa")

        text_area = tk.Text(resultados_window, wrap='word', height=20, width=50, state='normal')
        text_area.pack(pady=10)

        for i, resultado in enumerate(resultados, 1):
            text_area.insert(tk.END, f"{i}. {resultado}\n")
        text_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistenteApp(root)
    root.mainloop()
