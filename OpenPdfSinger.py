import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import fitz  
from docx import Document
from docx.shared import Inches

class SignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Assinatura Digital")
        self.root.geometry("800x800")
        self.root.configure(bg='#f5f5f5')

        self.pdf_canvas = tk.Canvas(root, bg='#ffffff', width=540, height=750)
        self.pdf_canvas.pack(pady=20)

        self.signature_img = None
        self.signature_img_id = None
        self.signature_position = (50, 50)  

        self.button_frame = tk.Frame(root, bg='#f5f5f5')
        self.button_frame.pack()

        self.load_pdf_button = tk.Button(self.button_frame, text="Carregar PDF", command=self.load_pdf,
                                         bg='#6a0dad', fg='#ffffff')
        self.load_pdf_button.grid(row=0, column=0, padx=10)

        self.load_signature_button = tk.Button(self.button_frame, text="Carregar Assinatura", command=self.load_signature,
                                               bg='#6a0dad', fg='#ffffff')
        self.load_signature_button.grid(row=0, column=1, padx=10)

        self.save_pdf_button = tk.Button(self.button_frame, text="Salvar PDF Assinado", command=self.save_signed_pdf,
                                         bg='#6a0dad', fg='#ffffff')
        self.save_pdf_button.grid(row=0, column=2, padx=10)

        self.previous_page_button = tk.Button(self.button_frame, text="Página Anterior", command=self.previous_page,
                                              bg='#6a0dad', fg='#ffffff')
        self.previous_page_button.grid(row=1, column=0, padx=10, pady=5)

        self.next_page_button = tk.Button(self.button_frame, text="Próxima Página", command=self.next_page,
                                          bg='#6a0dad', fg='#ffffff')
        self.next_page_button.grid(row=1, column=1, padx=10, pady=5)

        self.pdf_document = None
        self.signature_path = None
        self.current_page_number = 0

        self.pdf_canvas.bind("<B1-Motion>", self.move_signature)

    def load_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.pdf_document = fitz.open(pdf_path)
            self.current_page_number = 0
            self.display_pdf_page(self.current_page_number)

    def load_signature(self):
        self.signature_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        if self.signature_path:
            self.signature_img = Image.open(self.signature_path).convert("RGBA")
            self.signature_img = self.signature_img.resize((100, 50), Image.Resampling.LANCZOS)
            self.signature_tk_img = ImageTk.PhotoImage(self.signature_img)
            if self.signature_img_id:
                self.pdf_canvas.delete(self.signature_img_id)
            self.signature_img_id = self.pdf_canvas.create_image(self.signature_position[0], self.signature_position[1], image=self.signature_tk_img, anchor='nw')

    def display_pdf_page(self, page_number):
        self.pdf_canvas.delete("all")
        page = self.pdf_document.load_page(page_number)
        zoom = 750 / page.rect.height  # Ajustar a altura
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.pdf_img = ImageTk.PhotoImage(img)
        self.pdf_canvas.create_image(0, 0, image=self.pdf_img, anchor='nw')
        if self.signature_img:
            self.signature_img_id = self.pdf_canvas.create_image(self.signature_position[0], self.signature_position[1], image=self.signature_tk_img, anchor='nw')

    def move_signature(self, event):
        if self.signature_img_id:
            self.pdf_canvas.coords(self.signature_img_id, event.x, event.y)
            self.signature_position = (event.x, event.y)

    def save_signed_pdf(self):
        if not self.pdf_document or not self.signature_path or not self.signature_position:
            messagebox.showerror("Erro", "Por favor, carregue um PDF, uma assinatura e posicione a assinatura.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            page = self.pdf_document.load_page(self.current_page_number)
            page_width, page_height = page.rect.width, page.rect.height

            # Calcular a posição da assinatura no PDF
            canvas_width, canvas_height = self.pdf_canvas.winfo_width(), self.pdf_canvas.winfo_height()
            scale_x = page_width / canvas_width
            scale_y = page_height / canvas_height

            x0, y0 = self.signature_position[0] * scale_x, self.signature_position[1] * scale_y
            x1, y1 = x0 + self.signature_img.width * scale_x, y0 + self.signature_img.height * scale_y
            rect = fitz.Rect(x0, y0, x1, y1)

            page.insert_image(rect, filename=self.signature_path)
            self.pdf_document.save(output_path)
            messagebox.showinfo("Sucesso", "Assinatura aplicada com sucesso ao PDF!")

    def clear_canvas(self):
        self.pdf_canvas.delete("all")
        self.signature_img = None
        self.signature_img_id = None
        self.signature_position = (50, 50)

    def previous_page(self):
        if self.pdf_document and self.current_page_number > 0:
            self.current_page_number -= 1
            self.display_pdf_page(self.current_page_number)

    def next_page(self):
        if self.pdf_document and self.current_page_number < len(self.pdf_document) - 1:
            self.current_page_number += 1
            self.display_pdf_page(self.current_page_number)

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()
