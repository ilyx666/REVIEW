# coding=utf8
import tkinter
import pickle
import customtkinter
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
from test import preprocess_text
import time



app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("900x600")
with open("rating_model.pickle", "rb") as f:
    model = pickle.load(f)
with open("victor.pickle", "rb") as f:
    vectorizer = pickle.load(f)
with open("victor_dudka.pickle", "rb") as f:
    vectorizer2 = pickle.load(f)
with open("isReal_model.pickle", "rb") as f:
    gb = pickle.load(f)



def button_function():
    try:
        amountPhoto = int(ap.get())
    except ValueError:
        amountPhoto = 0
    print(amountPhoto)
    ap.delete(0, len(ap.get()))
    if review.get() != '':

        text_review = review.get()
        print(text_review)
        review.delete(0, len(review.get()))
    else:
        text_review = ''
    text = f"{preprocess_text(text_review)} Amount Photo: {amountPhoto} Len Review: {len(preprocess_text(text_review))}"

    vectorized_text = vectorizer.transform([text])

    label = customtkinter.CTkLabel(app, text="CTkLabel", fg_color="transparent", font=(None, 20))
    label.configure(text=f"Рейтинг: {model.predict(vectorized_text)[0]}")
    label.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    text = f"{preprocess_text(text_review)} Rating: {model.predict(vectorized_text)[0]} Amount Photo: {amountPhoto} Len Review: {len(preprocess_text(text_review))}"
    vectorized_text = vectorizer2.transform([text])
    label2 = customtkinter.CTkLabel(app, text="CTkLabel", fg_color="transparent", font=(None, 20))
    t = 0
    if gb.predict(vectorizer2.transform([text])[0]) == 1:
        t = 'ДА'
    else:
        t = 'НЕТ'
    label2.configure(text=f"Настоящий ли: {t}")
    label2.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Готово", command=button_function)

ap = customtkinter.CTkEntry(master=app,
                               placeholder_text="Количество прикрепленных фото",
                               width=300,
                               height=40,
                               border_width=2,
                               corner_radius=10)
review = customtkinter.CTkEntry(master=app,
                               placeholder_text="Введите отзыв",
                               width=300,
                               height=40,
                               border_width=2,
                               corner_radius=10)
review.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
ap.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)













app.mainloop()