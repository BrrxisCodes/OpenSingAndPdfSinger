import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw

class SignatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desenhar Assinatura")
        self.root.geometry("600x400")
        self.root.configure(bg='#f5f5f5')

        self.canvas = tk.Canvas(root, bg='#ffffff', width=500, height=300)
        self.canvas.pack(pady=20)

        self.button_frame = tk.Frame(root, bg='#f5f5f5')
        self.button_frame.pack()

        self.save_button = tk.Button(self.button_frame, text="Salvar Assinatura", command=self.save_signature,
                                     bg='#6a0dad', fg='#ffffff')
        self.save_button.grid(row=0, column=0, padx=10)

        self.clear_button = tk.Button(self.button_frame, text="Limpar Última Ação", command=self.clear_last_action,
                                      bg='#6a0dad', fg='#ffffff')
        self.clear_button.grid(row=0, column=1, padx=10)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonPress-1>", self.start_paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.canvas.bind_all("<Control-z>", self.undo)

        self.image = Image.new("RGBA", (500, 300), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)

        self.lines = []

    def start_paint(self, event):
        self.lines.append([])

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        line = self.canvas.create_oval(x1, y1, x2, y2, fill="black", width=2)
        self.draw.line([x1, y1, x2, y2], fill="black", width=2)
        self.lines[-1].append(line)

    def reset(self, event):
        pass

    def undo(self, event=None):
        if self.lines:
            last_action = self.lines.pop()
            for line in last_action:
                self.canvas.delete(line)
            self.redraw_image()

    def save_signature(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image.save(file_path)
            messagebox.showinfo("Salvo", "Assinatura salva com sucesso!")

    def clear_last_action(self):
        self.undo()

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGBA", (500, 300), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.lines = []

    def redraw_image(self):
        self.image = Image.new("RGBA", (500, 300), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        for action in self.lines:
            for line in action:
                coords = self.canvas.coords(line)
                if coords:
                    x1, y1, x2, y2 = coords
                    self.draw.line([x1, y1, x2, y2], fill="black", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()
