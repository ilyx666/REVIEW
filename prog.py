# coding=utf8
global login
import time
import tkinter
import tkinter.messagebox
import customtkinter
import pickle
from test import preprocess_text
from PIL import Image
import csv
import os
import pandas as pd
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
yellow = "themes/yellow.json"
pink = "themes/pink.json"
red = "themes/red.json"
customtkinter.set_default_color_theme(yellow)  # Themes: "blue" (standard), "green", "dark-blue"
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
        self.attempts = 3
        super().__init__()
        self.authorization = False
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
        self.home_image = customtkinter.CTkImage(light_image=Image.open("home_dark.png"), dark_image=Image.open("home_light_yellow.png"), size=(20, 20))
        self.kab_image = customtkinter.CTkImage(light_image=Image.open("kab_dark.png"),
                                                 dark_image=Image.open("kab_light_yellow.png"), size=(20, 20))
        self.home_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Главная",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.frame_2_button = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Кабинет", image=self.kab_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"), anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.office_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

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


        # create home frame
        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=700)
        self.textbox.grid(row=0, column=1, padx=100, pady=70)

        self.entry = customtkinter.CTkEntry(self.home_frame, width=40)
        self.entry.place(relx=0.34, rely=0.67)

        self.label2 = customtkinter.CTkLabel(self.home_frame, text="Кол-во прикрепленных фото:", anchor="w")
        self.label2.place(relx=0.125, rely=0.67)

        self.label = customtkinter.CTkLabel(self.home_frame, text="Отзыв:", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.place(relx=0.13, rely=0.07)

        #self.label3 = customtkinter.CTkLabel(self.home_frame, text=f"Кол-во бесплатных попыток:{self.attempts}", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
        #self.label3.place(relx=0.55, rely=0.07)

        #create second frame
        if self.authorization == False:
            self.not_auth_label = customtkinter.CTkLabel(self.second_frame, text="Чтобы войти в кабинет, нужно:", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.not_auth_label.place(relx=0.275, rely=0.55)

            self.login_window_button = customtkinter.CTkButton(self.second_frame, text="Войти")
            self.login_window_button.place(relx=0.275, rely=0.7)

            self.reg_window_button = customtkinter.CTkButton(self.second_frame, text="Зарегистрироваться", fg_color=["white", "#171714"], border_color="yellow", border_width=2, text_color=["black", "white"])
            self.reg_window_button.place(relx=0.545, rely=0.7)

            self.or_label = customtkinter.CTkLabel(self.second_frame, text="или", font=customtkinter.CTkFont(size=25, weight="bold"))
            self.or_label.place(relx=0.463, rely=0.7)



        def button_event():
            self.attempts -= 1
            self.label3 = customtkinter.CTkLabel(self.home_frame, text=f"Кол-во бесплатных попыток:  {self.attempts}", anchor="w",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label3.place(relx=0.55, rely=0.07)
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
            if self.attempts <= 0:
                self.but.configure(state="disabled")


            self.label_rating = customtkinter.CTkLabel(self.home_frame, text=f"Rating: {rate_predict}", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label_rating.place(relx=0.12, rely=0.75)

            self.label_real = customtkinter.CTkLabel(self.home_frame, text=f"TRUE?: {real_predict}", anchor="w",
                                                       font=customtkinter.CTkFont(size=20, weight="bold"))
            self.label_real.place(relx=0.12, rely=0.825)




        self.but = customtkinter.CTkButton(self.home_frame, text='Готово', command=button_event)
        self.but.place(relx=0.735, rely=0.67)


       



        # set default values
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")
        self.select_frame_by_name("home")
        self.toplevel_window = None
        self.reg_window = None
        # self.theme_mode_optionemenu.set("yellow")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")



        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("home")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_theme_mode_event(self, new_theme_mode: str):
        customtkinter.set_default_color_theme(new_theme_mode)
        self.update()
        print(new_theme_mode)



    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")




    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def save_data(self):
        with open("data.pickle", "wb") as f:
            pickle.dump(self.attempts, f)

    def load_data(self):
        try:
            with open("data.pickle", "rb") as f:
                self.attempts = pickle.load(f)
                print(self.attempts)
        except FileNotFoundError:
            self.attempts = 3

    def update_attempts_label(self):
        self.label3 = customtkinter.CTkLabel(self.home_frame, )
        self.label3.configure(text=f"Кол-во бесплатных попыток:  {self.attempts}", anchor="w", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label3.place(relx=0.55, rely=0.07)
        if self.attempts <= 0:
            self.but.configure(state="disabled")

    def exit_program(self):
        self.save_data()
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.load_data()
    app.update_attempts_label()
    app.protocol("WM_DELETE_WINDOW", app.exit_program)
    app.mainloop()