import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp:
    def init(self, master):
        self.master = master
        self.master.title("Language Translator")

        self.translator = Translator()

        self.create_widgets()

    def translate_text(self):
        text_to_translate = self.input_text.get("1.0", "end-1c")
        source_lang = self.source_language.get()
        target_lang = self.target_language.get()

        translated_text = self.translator.translate(text_to_translate, src=source_lang, dest=target_lang)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated_text.text)

    def create_widgets(self):
        source_label = ttk.Label(self.master, text="Source Language:")
        source_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.source_language = ttk.Combobox(self.master, values=["en", "fr", "es", "de", "zh", "ja", "ko"])
        self.source_language.set("en")
        self.source_language.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        target_label = ttk.Label(self.master, text="Target Language:")
        target_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.target_language = ttk.Combobox(self.master, values=["en", "fr", "es", "de", "zh", "ja", "ko"])
        self.target_language.set("fr")
        self.target_language.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.input_text = tk.Text(self.master, height=10, width=50)
        self.input_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        translate_button = ttk.Button(self.master, text="Translate", command=self.translate_text)
        translate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.output_text = tk.Text(self.master, height=10, width=50)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

def main():
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

if name == "main":
    main()