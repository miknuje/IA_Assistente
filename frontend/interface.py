import sys
sys.path.append('./src')
import tkinter as tk
from assistente import assistente_virtual 
from reconhecimento_voz import ouvir_comando

class AssistenteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assistente Virtual")

        # Área de texto para o diálogo
        self.chat_area = tk.Text(root, wrap='word', height=20, width=50, state='disabled')
        self.chat_area.pack(pady=10)

        # Campo de entrada para o usuário
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, width=40)
        self.entry.pack(pady=5)
        
        # Botão para enviar texto
        self.send_button = tk.Button(root, text="Enviar", command=self.enviar_texto)
        self.send_button.pack(pady=5)

        # Botão para falar (ativar reconhecimento de voz)
        self.speak_button = tk.Button(root, text="Falar", command=self.ativar_voz)
        self.speak_button.pack(pady=5)

    def exibir_mensagem(self, texto, remetente="Você"):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{remetente}: {texto}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def enviar_texto(self):
        # Obtém o texto do campo de entrada
        mensagem = self.entry_var.get()
        if mensagem:
            self.exibir_mensagem(mensagem, "Você")
            resposta = assistente_virtual(mensagem)  # Envia a mensagem para o assistente
            self.exibir_mensagem(resposta, "Assistente")
            self.entry_var.set("")

    def ativar_voz(self):
        self.exibir_mensagem("Escutando...", "Assistente")
        comando = ouvir_comando()  # Recebe o comando de voz
        resposta = assistente_virtual(comando)
        self.exibir_mensagem(comando, "Você")
        self.exibir_mensagem(resposta, "Assistente")

if __name__ == "__main__":
    root = tk.Tk()
    app = AssistenteApp(root)
    root.mainloop()