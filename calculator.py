import tkinter
from tkinter import *
import tkinter.messagebox
import math

# Defined the Constants.
LFONT = ("Arial", 40, "bold")
SFONT = ("Arial", 16)
DIGIT_FONT = ("Arial", 24, "bold")
DEFAULT_FONT = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(root):
        root.window = tkinter.Tk()
        root.window.geometry("370x670+400+100")
        root.window.resizable(False, False)
        root.window.title("Calculator")

        root.total_expression = ""
        root.current_expression = ""
        root.display_frame = root.create_display_frame()

        root.total_label, root.label = root.create_display_labels()

        root.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        root.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        root.buttons_frame = root.create_buttons_frame()

        root.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            root.buttons_frame.rowconfigure(x, weight=1)
            root.buttons_frame.columnconfigure(x, weight=1)
        root.create_digit_buttons()
        root.create_operator_buttons()
        root.create_special_buttons()
        root.bind_keys()

    def bind_keys(root):
        root.window.bind("<Return>", lambda event: root.evaluate())
        for key in root.digits:
            root.window.bind(str(key), lambda event, digit=key: root.add_to_expression(digit))

        for key in root.operations:
            root.window.bind(key, lambda event, operator=key: root.append_operator(operator))

    def create_special_buttons(root):
        root.create_clear_button()
        root.create_equals_button()
        root.create_square_button()
        root.create_sqrt_button()

    def create_display_labels(root):
        total_label = tkinter.Label(root.display_frame, text=root.total_expression, anchor=tkinter.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SFONT)
        total_label.pack(expand=True, fill='both')

        label = tkinter.Label(root.display_frame, text=root.current_expression, anchor=tkinter.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LFONT)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(root):
        frame = tkinter.Frame(root.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def add_to_expression(root, value):
        root.current_expression += str(value)
        root.update_label()

    def create_digit_buttons(root):
        for digit, grid_value in root.digits.items():
            button = tkinter.Button(root.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT,
                               borderwidth=0, command=lambda x=digit: root.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tkinter.NSEW)

    def append_operator(root, operator):
        root.current_expression += operator
        root.total_expression += root.current_expression
        root.current_expression = ""
        root.update_total_label()
        root.update_label()

    def create_operator_buttons(root):
        i = 0
        for operator, symbol in root.operations.items():
            button = tkinter.Button(root.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                               borderwidth=0, command=lambda x=operator: root.append_operator(x))
            button.grid(row=i, column=4, sticky=tkinter.NSEW)
            i += 1

    def clear(root):
        root.current_expression = ""
        root.total_expression = ""
        root.update_label()
        root.update_total_label()

    def create_clear_button(root):
        button = tkinter.Button(root.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=root.clear)
        button.grid(row=0, column=1, sticky=tkinter.NSEW)

    def square(root):
        root.current_expression = str(eval(f"{root.current_expression}**2"))
        root.update_label()

    def create_square_button(root):
        button = tkinter.Button(root.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=root.square)
        button.grid(row=0, column=2, sticky=tkinter.NSEW)

    def sqrt(root):
        root.current_expression = str(eval(f"{root.current_expression}**0.5"))
        root.update_label()

    def create_sqrt_button(root):
        button = tkinter.Button(root.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=root.sqrt)
        button.grid(row=0, column=3, sticky=tkinter.NSEW)

    def evaluate(root):
        root.total_expression += root.current_expression
        root.update_total_label()
        try:
            root.current_expression = str(eval(root.total_expression))

            root.total_expression = ""
        except Exception as e:
            root.current_expression = "Error!"
        finally:
            root.update_label()

    def create_equals_button(root):
        button = tkinter.Button(root.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=root.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tkinter.NSEW)

    def create_buttons_frame(root):
        frame = tkinter.Frame(root.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(root):
        expression = root.total_expression
        for operator, symbol in root.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        root.total_label.config(text=expression)

    def update_label(root):
        root.label.config(text=root.current_expression[:11])

    def run(root):
        root.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()