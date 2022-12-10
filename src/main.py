import customtkinter # tkinter but with custom widgets
import pyperclip
from customtkinter import CTk as Tk
from customtkinter import CTkButton as Button, CTkLabel as Label, CTkEntry as Entry, CTkFrame as Frame, CTkSwitch as Switch, CTkTextbox as Textbox
from core import Generator as gen

customtkinter.set_appearance_mode('dark') # Set dark mode
customtkinter.set_default_color_theme('blue') # Set color theme

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.config() # configure the window properties
        
        # Widgets
        self.title = Label(self, text='Password Generator', font=('Segoe UI',20,''))
        self.title.place(x=20,y=20)
        self.line = Label(self, text='───────────────────────', font=('Segoe UI',20,''))
        self.line.place(x=20,y=45)
        self.form_title = Label(self, text="Choose the options you want:", font=('Segoe UI',15,'bold'))
        self.form_title.place(x=20,y=80)

        self.length_label = Label(self, text='Length :', font=('Segoe UI',13,''))
        self.length_label.place(x=40,y=120)

        vcmd = (self.register(self.validate), '%P')
        self.length_input_widget = Entry(self, width=50, validate="key", validatecommand=vcmd)
        self.length_input_widget.place(x=100,y=120)

        self.letters_l = Switch(self, text='Lowercase letters', font=('Segoe UI',13,''))
        self.letters_l.place(x=40,y=160)

        self.letters_u = Switch(self, text='Uppercase letters', font=('Segoe UI',13,''))
        self.letters_u.place(x=40,y=200)

        self.digits = Switch(self, text='Digits', font=('Segoe UI',13,''))
        self.digits.place(x=40,y=240)
        
        self.symbols = Switch(self, text='Symbols', font=('Segoe UI',13,''))
        self.symbols.place(x=40,y=280)

        self.generate_button = Button(self, text='Generate', font=('Segoe UI',13,''))
        self.generate_button.configure(command=self.generate_button_command)
        self.generate_button.place(x=40,y=320)

        self.password_box = Textbox(self, width=self.winfo_width()-40, height=80, font=('Segoe UI',14,'italic'))

        self.password_box.configure(state='normal')
        self.password_box.place(x=20,y=380)

        self.copy_button = Button(self, text='Copy',width=100, font=('Segoe UI',13,''))
        self.copy_button.configure(command=self.copy_to_clipboard)
        self.copy_button.place(x=20,y=480)

        self.save_button = Button(self, text='Save',width=100, font=('Segoe UI',13,''))
        self.save_button.configure(command=self.save_to_file)
        self.save_button.place(x=140,y=480)
  

    def config(self):
        self.geometry('500x600+400+40') # Set window size
        self.resizable(False, False) # Disable resizing
        self.title('Password Generator') # Set window title

    def validate(self, P):
        """Function to validate the input of the length input widget"""
        if len(P) == 0:
            return True
        elif len(P) <= 2 and P.isdigit():
            return True
        else:
            return False
    
    def generate_password(self) -> str:
        """Function to generate the password"""

        if self.length_input_widget.get() == '' or not any([self.letters_l.get(), self.letters_u.get(), self.digits.get(), self.symbols.get()]):
            return ''
        else:
            password = gen(length=int(self.length_input_widget.get()),
                        letters_l=self.letters_l.get(), 
                        letters_u=self.letters_u.get(), 
                        digits=self.digits.get(), 
                        symbols=self.symbols.get()
                        ).generate_password()
            
            return password
    
    def copy_to_clipboard(self):
        pyperclip.copy(self.password_box.get(0.0,customtkinter.END))

    def save_to_file(self):
        file = customtkinter.filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if file:
            file.write(self.password_box.get(0.0,customtkinter.END))
            file.close()
    
    def generate_button_command(self):
        self.password_box.delete(0.0,customtkinter.END)
        self.password_box.insert(0.0, self.generate_password())

if __name__ == '__main__':
    window = Window()
    window.mainloop()
