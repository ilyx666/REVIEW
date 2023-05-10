import tkinter
import tkinter.messagebox
import customtkinter
import pickle
from test import preprocess_text
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
with open("model/rating_model.pickle", "rb") as f:
    model = pickle.load(f)
with open("model/victor.pickle", "rb") as f:
    vectorizer = pickle.load(f)
with open("model/victor_dudka.pickle", "rb") as f:
    vectorizer2 = pickle.load(f)
with open("model/isReal_model.pickle", "rb") as f:
    gb = pickle.load(f)



class App(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        self.attempts = 1
        # configure window
        self.title("AuthenticFeedback")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="AuthenticFeedback", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        global textbox


        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=700)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0))

        self.entry = customtkinter.CTkEntry(self, width=40)
        self.entry.place(relx=0.46, rely=0.52, anchor=tkinter.CENTER)

        self.label2 = customtkinter.CTkLabel(self)
        self.label2 = customtkinter.CTkLabel(self, text="Кол-во прикрепленных фото:", anchor="w")
        self.label2.place(relx=0.355, rely=0.52, anchor=tkinter.CENTER)


        self.label = customtkinter.CTkLabel(self, text="Отзыв:", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.place(relx=0.31, rely=0.1, anchor=tkinter.CENTER)

        self.label3 = customtkinter.CTkLabel(self, text=f"Кол-во бесплатных попыток:{self.attempts}", anchor="w",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label3.place(relx=0.7675, rely=0.1, anchor=tkinter.CENTER)


        def button_event():
            self.attempts -= 1
            self.label3 = customtkinter.CTkLabel(self, text=f"Кол-во бесплатных попыток:{self.attempts}", anchor="w",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label3.place(relx=0.7675, rely=0.1, anchor=tkinter.CENTER)
            textbox_content = self.textbox.get("0.0", "end")
            print(textbox_content)
            self.textbox.delete("0.0", "end")
            try:
                entry_content = self.entry.get()
            except ValueError:
                entry_content = 0
            print(entry_content)
            self.entry.delete(0, "end")

            text = f"{preprocess_text(textbox_content)} Amount Photo: {entry_content} Len Review: {len(preprocess_text(textbox_content))}"
            vectorized_text = vectorizer.transform([text])
            rate_predict = model.predict(vectorized_text)[0]

            text = f"{preprocess_text(textbox_content)} Rating: {model.predict(vectorized_text)[0]} Amount Photo: {entry_content} Len Review: {len(preprocess_text(textbox_content))}"
            vectorized_text = vectorizer2.transform([text])
            real_predict = gb.predict(vectorizer2.transform([text])[0])
            if len(textbox_content) == 1:
                real_predict = 0
            if len(entry_content) <= 1:
                rate_predict = 0
            if real_predict == 1:
                real_predict = 'YES'
            else:
                real_predict = 'NO'
            if self.attempts == 0:
                self.but.configure(state="disabled")


            self.label_rating = customtkinter.CTkLabel(self, text=f"Rating: {rate_predict}", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label_rating.place(relx=0.3115, rely=0.6, anchor=tkinter.CENTER)

            self.label_real = customtkinter.CTkLabel(self, text=f"TRUE?: {real_predict}", anchor="w",
                                                       font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label_real.place(relx=0.32, rely=0.65, anchor=tkinter.CENTER)




        self.but = customtkinter.CTkButton(self, text='Готово', command=button_event, )
        self.but.place(relx=0.847, rely=0.52, anchor=tkinter.CENTER)


       



        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")





    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)





if __name__ == "__main__":
    app = App()
    app.mainloop()