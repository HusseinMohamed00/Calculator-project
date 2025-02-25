import tkinter as tk
import math

calculation = ""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_display(calculation)
    
def apply_trigonometry(trig_function):
    global calculation
    
    try:
        val = float(calculation)
        rad = math.radians(val)
        if trig_function == "sin":
            result = math.sin(rad)
        elif trig_function == "cos":
            result = math.cos(rad)
        elif trig_function == "tan":
            result = math.tan(rad)
        
        calculation = str(result)
        update_display(result)

    except:
        clear_filed()
        update_display("Error")

def evaluation_calculation():
    global calculation 
    try:
        result = str(eval(calculation))
        calculation = result
        update_display(result)
    except:
        clear_filed()
        update_display("Error")

def clear_filed():
    global calculation
    calculation = ""
    update_display("")

def update_display(value):
    
    text_res.config(state="normal")  
    text_res.delete(1.0, "end")
    text_res.insert(1.0, value)
    text_res.config(state="disabled")  



root = tk.Tk()
root.geometry("350x375")
root.title("Calculator")
root.configure(bg="#1B2631")


text_res = tk.Text(root, height=2, width=16, font=("Arial", 24, "bold"), bg="#2C3E50", fg="white", bd=5 )
text_res.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

number_style = { 
    "width": 5, "height": 2, "font": ("Arial", 14, "bold"), "bd": 3, "relief": tk.RAISED,
    "bg": "#5DADE2", "fg": "black", "activebackground": "#85C1E9", "activeforeground": "black"
}
operator_style = {
    "width": 5, "height": 2, "font": ("Arial", 14, "bold"), "bd": 3, "relief": tk.RAISED,
    "bg": "#F4D03F", "fg": "black", "activebackground": "#F7DC6F", "activeforeground": "black"
}
special_style = { 
    "width": 5, "height": 2, "font": ("Arial", 14, "bold"), "bd": 3, "relief": tk.RAISED,
    "bg": "#E74C3C", "fg": "white", "activebackground": "#EC7063", "activeforeground": "white"
}
equal_style = {  
    "width": 5, "height": 2, "font": ("Arial", 14, "bold"), "bd": 3, "relief": tk.RAISED,
    "bg": "#2ECC71", "fg": "black", "activebackground": "#58D68D", "activeforeground": "white"
}

# Numbers
btn_1 = tk.Button(root, text ="1", command=lambda: add_to_calculation(1), **number_style)
btn_1.grid(row =2, column=1, padx=5, pady=5)
btn_2 = tk.Button(root, text ="2", command=lambda: add_to_calculation(2), **number_style)
btn_2.grid(row =2, column=2, padx=5, pady=5)
btn_3 = tk.Button(root, text ="3", command=lambda: add_to_calculation(3), **number_style)
btn_3.grid(row =2, column=3, padx=5, pady=5)
btn_4 = tk.Button(root, text ="4", command=lambda: add_to_calculation(4), **number_style)
btn_4.grid(row =3, column=1 , padx=5, pady=5)
btn_5 = tk.Button(root, text ="5", command=lambda: add_to_calculation(5), **number_style)
btn_5.grid(row =3, column=2 , padx=5, pady=5)
btn_6 = tk.Button(root, text ="6", command=lambda: add_to_calculation(6), **number_style)
btn_6.grid(row =3, column=3 , padx=5, pady=5)
btn_7 = tk.Button(root, text ="7", command=lambda: add_to_calculation(7), **number_style)
btn_7.grid(row =4, column=1 , padx=5, pady=5)
btn_8 = tk.Button(root, text ="8", command=lambda: add_to_calculation(8),  **number_style)
btn_8.grid(row =4, column=2 , padx=5, pady=5)
btn_9 = tk.Button(root, text ="9", command=lambda: add_to_calculation(9),  **number_style)
btn_9.grid(row =4, column=3 , padx=5, pady=5)
btn_0 = tk.Button(root, text ="0", command=lambda: add_to_calculation(0),  **number_style)
btn_0.grid(row =5, column=1, padx=5, pady=5)
btn_decimal = tk.Button(root, text =".", command=lambda: add_to_calculation("."), **number_style)
btn_decimal.grid(row =5, column=3)
# Parentheses
btn_open = tk.Button(root, text ="(", command=lambda: add_to_calculation("("),  **operator_style)
btn_open.grid(row =1, column=2)
btn_close = tk.Button(root, text =")", command=lambda: add_to_calculation(")"),  **operator_style)
btn_close.grid(row =1, column=3)
# Operators
btn_plus = tk.Button(root, text ="+", command=lambda: add_to_calculation("+"), **operator_style)
btn_plus.grid(row =4, column=4)
btn_minus = tk.Button(root, text ="-", command=lambda: add_to_calculation("-"),  **operator_style)
btn_minus.grid(row =3, column=4)
btn_divide = tk.Button(root, text ="/", command=lambda: add_to_calculation("/"),  **operator_style)
btn_divide.grid(row =1, column=4)
btn_multiply = tk.Button(root, text ="*", command=lambda: add_to_calculation("*"), **operator_style)
btn_multiply.grid(row =2, column=4)
btn_equals = tk.Button(root, text ="=", command=evaluation_calculation,  **equal_style)
btn_equals.grid(row =5, column=4)
btn_sin = tk.Button(root, text ="sin", command=lambda: apply_trigonometry("sin"), **operator_style)
btn_sin.grid(row =5, column=5)
btn_cos = tk.Button(root, text ="cos", command=lambda: apply_trigonometry("cos"), **operator_style)
btn_cos.grid(row =4, column=5)
btn_tan = tk.Button(root, text ="tan", command=lambda: apply_trigonometry("tan"), **operator_style)
btn_tan.grid(row =3, column=5)

# Special
btn_clear = tk.Button(root, text ="C", command=clear_filed, **number_style)
btn_clear.grid(row =1, column=1)

root.mainloop()