import customtkinter 
from CTkMessagebox import CTkMessagebox
from customtkinter import *
from PIL import Image

branco = '#FFFFFF'
roxo = '#800080'
ivory_branco = '#FFFFF0'
white_smoke = '#F5F5F5'
roxo_claro = '#9400D3'


class App():
 
    def __init__(self):
        self.janela_pri = customtkinter.CTk()
        self.janela_pri.geometry('430x300')
        self.janela_pri.resizable(False, False)
        self.janela_pri.title('Gerador de senhas')
        

        self.image_bg = customtkinter.CTkImage(light_image=Image.open('imgs/bg.jpg'), dark_image=Image.open('imgs/bg.jpg'), size=(430, 300))
        self.bg_label = customtkinter.CTkLabel(self.janela_pri, image=self.image_bg, text='')
        self.bg_label.pack()

        self.titulo_lbl = customtkinter.CTkLabel(self.bg_label,font=('Helvetica', 28,'bold'),text='* Gerador de Senhas *', width=400, height=50, corner_radius=10,
                                                  fg_color=white_smoke)
        self.titulo_lbl.place(x=15, y=15)
        self.gerador_lbl = customtkinter.CTkLabel(self.bg_label, text='', width=400, height=130, corner_radius=10,
                                                  fg_color=white_smoke)
        self.gerador_lbl.place(x=15, y=75)
        self.senha_lbl = customtkinter.CTkLabel(self.bg_label, text='', width=400, height=70, corner_radius=10,
                                           fg_color=white_smoke)
        self.senha_lbl.place(x=15, y=215)

        self.resultado_lbl = customtkinter.CTkLabel(self.senha_lbl, text='',font=('Helvetica', 26),width=280, height=70, corner_radius=10,)
        self.resultado_lbl.place(x=0, y=0)


        self.check_fraca_var = customtkinter.StringVar(value='off')
        self.check_fraca = customtkinter.CTkCheckBox(self.gerador_lbl, text='Fraca', text_color='#000000',
                                                     font=('Helvetica', 18), border_color=roxo,
                                                     checkbox_width=20, checkbox_height=20, variable=self.check_fraca_var, 
                                                     onvalue='on', offvalue='off',command=self.checar_checkbox)
        self.check_fraca.place(x=190, y=25)

        self.check_media_var = customtkinter.StringVar(value='off')
        self.check_media = customtkinter.CTkCheckBox(self.gerador_lbl, text='Média', text_color='#000000',
                                                      font=('Helvetica', 18), border_color=roxo,
                                                      checkbox_width=20, checkbox_height=20, variable=self.check_media_var,
                                                      onvalue='on', offvalue='off',command=self.checar_checkbox)
        self.check_media.place(x=190, y=55)
        
        self.check_forte_var = customtkinter.StringVar(value='off')
        self.check_forte = customtkinter.CTkCheckBox(self.gerador_lbl, text='Forte', text_color='#000000',
                                                      font=('Helvetica', 18), border_color=roxo,
                                                      checkbox_width=20, checkbox_height=20, variable=self.check_forte_var,
                                                      onvalue='on', offvalue='off',command=self.checar_checkbox)
        self.check_forte.place(x=190, y=85)

        
        self.gerar_lbl = customtkinter.CTkLabel(self.gerador_lbl,font=('Helvetica', 18), text='Digite a quantidade')
        self.gerar_lbl.place(x=20,y=20)
        self.gerar_lbl2 = customtkinter.CTkLabel(self.gerador_lbl,font=('Helvetica', 18), text='de caracteres:')
        self.gerar_lbl2.place(x=20,y=44)
        
        
        self.gerar_btn = customtkinter.CTkButton(self.gerador_lbl,text='Gerar',font=('Helvetica', 18),  width=100,height=40,fg_color=roxo,command=self.gerar)
        self.gerar_btn.place(x=280,y=25)
      
        self.copiar_btn = customtkinter.CTkButton(self.senha_lbl,text='Copiar',font=('Helvetica', 18),  width=100,height=60,fg_color=roxo,command=self.copiar)
        self.copiar_btn.place(x=280,y=5)
     
        self.sair_btn = customtkinter.CTkButton(self.gerador_lbl, text='Sair',font=('Helvetica', 18),  width=100,height=40,fg_color=roxo, command=lambda:self.janela_pri.destroy())
        self.sair_btn.place(x=280,y=70)
        
        def imp_letra(*args):
            s = var.get()
            if len(s) > 0:
                if not s[-1].isdigit():
                    var.set(s[:-1])
                else:
                    var.set(s[:tamanho_max])
                    

        tamanho_max = 2
        var = StringVar()
        var.trace('w',imp_letra)

        self.qtd_caracteres = customtkinter.CTkEntry(self.gerador_lbl, font=('Helvetica', 18), textvariable=var,width=60,height=40,border_color=roxo)
        self.qtd_caracteres.place(x=20,y=70)

    def checar_checkbox(self):
                
        if self.check_forte_var.get() == 'on' and self.check_fraca_var.get() == 'on':
            self.check_forte.deselect()
            self.check_fraca.deselect()
        if self.check_fraca_var.get() == 'on' and self.check_media_var.get() == "on":
            self.check_media.deselect()
            self.check_fraca.deselect()
        if self.check_forte_var.get() == 'on' and self.check_media_var.get() == "on":
            self.check_forte.deselect()
            self.check_media.deselect()
            
    def gerar(self,*args):
        from random import choice
        import string

        try:
            len_senha = int(self.qtd_caracteres.get())
            if len_senha < 8 or len_senha > 16:
                CTkMessagebox(title='Info',message='Não foi possivel gerar. Escolha um número entre 8 e 16.', width=150,height=100,button_width=50,button_height=30)
                self.qtd_caracteres.delete(first_index=0, last_index=50)
                return      
        
        except ValueError:
            CTkMessagebox(title='Info',message='Digite algum número entre 8 e 16 para prosseguir.', width=150,height=100,button_width=50,button_height=30)
            self.qtd_caracteres.delete(first_index=0, last_index=50)
            return
        
 

        letras = string.ascii_letters
        numeros = string.digits
        pontos = string.punctuation

        senha_segura = ''
        if self.check_fraca.get() == 'on':
            
            caracteres = letras
            for i in range(len_senha):
                senha_segura += choice(caracteres)

        if self.check_media_var.get() == 'on':
            caracteres = letras + numeros
            for i in range(len_senha):
                senha_segura += choice(caracteres)
        
        if self.check_forte_var.get() == 'on':
            caracteres = letras + numeros + pontos
            for i in range(len_senha):
                senha_segura += choice(caracteres)
                
        senha_final = f'Sua senha: {senha_segura}'
                
        self.resultado_lbl.configure(self.resultado_lbl,text=senha_segura)
        
        return senha_final
        

    def copiar(self):

        
        copia_resultado = self.resultado_lbl.cget("text")
        self.janela_pri.clipboard_clear()
        self.janela_pri.clipboard_append(copia_resultado)
        self.janela_pri.update()


    def run(self):
        self.janela_pri.mainloop()


if __name__ == "__main__":
    inicia = App()
    inicia.run()