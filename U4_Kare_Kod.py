import qrcode
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
#-------------------------------------------------------------------------------------------------------------
class QRKODYAPICI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR KOD YAPICI")

        self.data_label = ttk.Label(root, text="Veri Girişi:")
        self.data_label.grid(row=0, column=0, padx=10, pady=10)

        self.data_entry = ttk.Entry(root)
        self.data_entry.grid(row=0, column=1, padx=30, pady=10)

        self.file_label = ttk.Label(root, text="Dosya Adı:")
        self.file_label.grid(row=1, column=0, padx=10, pady=10)

        self.file_entry = ttk.Entry(root)
        self.file_entry.grid(row=1, column=1, padx=30, pady=10)

        self.generate_button = ttk.Button(root, text="QR Kodu Oluştur", command=self.generate_qr_code)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)
#-------------------------------------------------------------------------------------------------------------
    def generate_qr_code(self):
        data_to_encode = self.data_entry.get()
        file_name = self.file_entry.get()

        if not data_to_encode or not file_name:
            tk.messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            return
#-------------------------------------------------------------------------------------------------------------
        # Dosya adına ".png" ekleniyor.
        file_name += '.png'

        # QRCode nesnesi oluşturuluyor.
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
#-------------------------------------------------------------------------------------------------------------
        # Veri QR koduna ekleniyor.
        qr.add_data(data_to_encode)

        # QR kodu oluşturuluyor.
        qr.make()
#-------------------------------------------------------------------------------------------------------------
        # Oluşturulan QR kodu bir görüntüye dönüştürülüyor.
        img = qr.make_image(fill_color="black", back_color="white")

        # Görüntü belirtilen dosya adıyla kaydediliyor.
        img.save(file_name)

        # Kullanıcıya başarılı bir şekilde kaydedildiğine dair bir mesaj gösteriliyor.
        tk.messagebox.showinfo("TAMAMLANDI!", f"QR kod '{file_name}' başarıyla kaydedildi.")
        
        self.data_entry.delete(0, tk.END)
        self.file_entry.delete(0, tk.END)
#-------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QRKODYAPICI(root)
    root.mainloop()
