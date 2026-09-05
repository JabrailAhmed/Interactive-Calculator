import tkinter as tk


# ----------------------------------------------------
# Core Math Functions
# ----------------------------------------------------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#0d1f11")  # Deep forest black-green background
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar()
        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = tk.Frame(self.root, bg="#0d1f11")
        display_frame.pack(expand=True, fill="both")

        display_entry = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 28, "bold"),
            bg="#0d1f11",
            fg="#2ecc71",  # Vibrant neon green text
            bd=0,
            justify="right",
            insertbackground="#2ecc71"
        )
        display_entry.pack(expand=True, fill="both", padx=24, pady=10)

    def create_buttons(self):
        buttons_frame = tk.Frame(self.root, bg="#0d1f11")
        buttons_frame.pack(expand=True, fill="both")

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

        button_layout = [
            ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('⌫', 4, 2), ('=', 4, 3)
        ]

        for text, row, col in button_layout:
            if text == 'C':
                bg_color, hover_color = "#c0392b", "#a93226"  # Red for clear
            elif text == '=':
                bg_color, hover_color = "#2ecc71", "#27ae60"  # Emerald green for equal
            elif text in ['/', '*', '-', '+']:
                bg_color, hover_color = "#1e824c", "#145a32"  # Forest green for operators
            elif text in ['(', ')', '⌫']:
                bg_color, hover_color = "#193322", "#22442e"  # Deep green for utility keys
            else:
                bg_color, hover_color = "#1f3a52", "#2c5275"  # Deep blue background for numbers

            btn = tk.Label(
                buttons_frame,
                text=text,
                bg=bg_color,
                fg="#ffffff",
                font=("Arial", 18, "bold"),
                relief="flat",
                cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

            btn.bind("<Button-1>", lambda e, t=text: self.on_button_click(t))
            btn.bind("<Enter>", lambda e, b=btn, h=hover_color: b.config(bg=h))
            btn.bind("<Leave>", lambda e, b=btn, o=bg_color: b.config(bg=o))

    def calculate_expression(self, expression_str):
        """
        Safely parses the calculation using our explicit math functions
        instead of dangerous global eval commands.
        """
        # Dictionary linking text operators to actual standalone functions
        operators = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }

        # Handle operators in Order of Operations (PEMDAS - Multiplication/Division first)
        for op_group in [('/', '*'), ('+', '-')]:
            tokens = self.tokenize(expression_str)
            i = 0
            while i < len(tokens):
                if tokens[i] in op_group:
                    op_char = tokens[i]
                    # Fetch values surrounding operator token
                    left_val = float(tokens[i - 1])
                    right_val = float(tokens[i + 1])

                    # Compute using explicit function reference
                    result = operators[op_char](left_val, right_val)

                    # Clean up decimal point display if integer
                    if result.is_integer():
                        result = int(result)

                    # Splice calculated result back into expression list
                    tokens[i - 1: i + 2] = [str(result)]
                    i -= 1
                i += 1
            expression_str = "".join(tokens)

        return expression_str

    def tokenize(self, expr_str):
        """Splits raw math text into numeric strings and operator elements."""
        tokens = []
        current_num = ""
        for char in expr_str:
            if char in ['+', '-', '*', '/']:
                if current_num:
                    tokens.append(current_num)
                    current_num = ""
                tokens.append(char)
            else:
                current_num += char
        if current_num:
            tokens.append(current_num)
        return tokens

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '⌫':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                if not self.expression.strip():
                    return
                # Routes expression structure safely to our calculation method
                result = self.calculate_expression(self.expression)
                self.expression = result
            except ZeroDivisionError:
                self.expression = "Error: Div by 0"
            except Exception:
                self.expression = "Error"
        elif char in ['(', ')']:
            # Utility brackets bypass standard calculations for text display
            self.expression += str(char)
        else:
            if "Error" in self.expression:
                self.expression = ""
            self.expression += str(char)

        self.display_var.set(self.expression)


if __name__ == "__main__":
    window = tk.Tk()
    app = Calculator(window)
    window.mainloop()
