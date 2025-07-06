import tkinter as tk
from tkinter import font
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("科学计算器")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # 初始化变量
        self.current_input = ""
        self.total_expression = ""
        self.result = ""
        
        # 设置字体
        self.large_font = font.Font(size=20)
        self.small_font = font.Font(size=16)
        
        # 创建UI
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        # 总表达式显示
        self.total_label = tk.Label(
            self.root, text=self.total_expression, 
            anchor=tk.E, bg="#f0f0f0", fg="#666666",
            padx=20, font=self.small_font
        )
        self.total_label.pack(fill=tk.X, ipady=10)
        
        # 当前输入显示
        self.input_label = tk.Label(
            self.root, text=self.current_input, 
            anchor=tk.E, bg="#f0f0f0", fg="#000000",
            padx=20, font=self.large_font
        )
        self.input_label.pack(fill=tk.X, ipady=20)
    
    def create_buttons(self):
        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True)
        
        # 按钮布局
        buttons = [
            ('sin', 'cos', 'tan', '√', 'π'),
            ('7', '8', '9', '/', '^'),
            ('4', '5', '6', '*', 'log'),
            ('1', '2', '3', '-', 'ln'),
            ('0', '.', '=', '+', 'C')
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(
                    button_frame, text=text, 
                    font=self.small_font,
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                button_frame.grid_columnconfigure(j, weight=1)
            button_frame.grid_rowconfigure(i, weight=1)
    
    def on_button_click(self, value):
        if value == "=":
            self.calculate_result()
        elif value == "C":
            self.clear_all()
        elif value == "√":
            self.current_input = str(math.sqrt(float(self.current_input or 0)))
            self.update_display()
        elif value == "π":
            self.current_input = str(math.pi)
            self.update_display()
        elif value == "sin":
            self.current_input = str(math.sin(math.radians(float(self.current_input or 0))))
            self.update_display()
        elif value == "cos":
            self.current_input = str(math.cos(math.radians(float(self.current_input or 0))))
            self.update_display()
        elif value == "tan":
            self.current_input = str(math.tan(math.radians(float(self.current_input or 0))))
            self.update_display()
        elif value == "log":
            self.current_input = str(math.log10(float(self.current_input or 1)))
            self.update_display()
        elif value == "ln":
            self.current_input = str(math.log(float(self.current_input or 1)))
            self.update_display()
        elif value == "^":
            self.total_expression = self.current_input
            self.current_input = ""
            self.total_expression += "^"
            self.update_display()
        else:
            self.current_input += str(value)
            self.update_display()
    
    def calculate_result(self):
        try:
            # 处理指数运算
            if "^" in self.total_expression:
                base, _ = self.total_expression.split("^")
                exponent = self.current_input
                self.result = str(float(base) ** float(exponent))
            else:
                self.total_expression += self.current_input
                self.result = str(eval(self.total_expression))
            
            self.current_input = self.result
            self.total_expression = ""
            self.update_display()
        except Exception:
            self.current_input = "错误"
            self.update_display()
    
    def clear_all(self):
        self.current_input = ""
        self.total_expression = ""
        self.result = ""
        self.update_display()
    
    def update_display(self):
        self.input_label.config(text=self.current_input)
        self.total_label.config(text=self.total_expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()