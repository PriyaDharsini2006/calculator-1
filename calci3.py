from tkinter import*
import tempfile, base64, zlib
import math

ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)



calc = Tk()
calc.title("Calculator")
calc.iconbitmap('calci.ico')
label = Label(calc, text="Window with transparent icon.")


operator = ""
text_input = StringVar()
converter_var = StringVar()

# Function to handle button clicks
def bttnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

# Function to clear the entry field
def bttnClear():
    global operator
    operator = ""
    text_input.set("")
    result_label.config(text="")

# Function to perform the calculation
def bttnEquals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""

# Placeholder conversion functions
def currency_converter(amount, from_currency, to_currency):
    conversion_rate = 1.18  # Replace with actual conversion rate
    converted_amount = amount * conversion_rate
    return converted_amount

def length_converter(value, from_unit, to_unit):
    conversion_rates = {'meters_to_feet': 3.28084, 'feet_to_meters': 0.3048}
    converted_value = value * conversion_rates[f'{from_unit}_to_{to_unit}']
    return converted_value

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    else:
        return value
    
def volume_converter(value, from_unit, to_unit):
    if from_unit == 'litre' and to_unit == 'ml':
        return value*1000
    elif from_unit == 'ml' and to_unit == 'litre':
        return value/1000
    else:
        return value

def weight_converter(value, from_unit, to_unit):
    if from_unit == 'Kg' and to_unit == 'g':
        return value*1000
    elif from_unit == 'g' and to_unit == 'Kg':
        return value/1000
    else:
        return value

def sqrt_converter(value):
        return math.sqrt(value)

# Function to handle menu item clicks
def menuItemClick(menu_item):
    if menu_item == "Standard":
        expression = entry.get()
        result = standard_calculator_logic(expression)
        text_input.set(result)

    elif menu_item == "Scientific":
        expression = entry.get()
        result = scientific_calculator_logic(expression)
        text_input.set(result)

    elif menu_item == "Currency":
        amount = float(entry.get())
        from_currency = 'USD'  # Replace with actual from currency
        to_currency = 'EUR'  # Replace with actual to currency
        result = currency_converter(amount, from_currency, to_currency)
        text_input.set(result)

    elif menu_item == "Length":
        value = float(entry.get())
        from_unit = 'meters'  # Replace with actual from unit
        to_unit = 'feet'  # Replace with actual to unit
        result = length_converter(value, from_unit, to_unit)
        text_input.set(result)

    elif menu_item == "Temperature":
        value = float(entry.get())
        from_unit = 'Celsius'  # Replace with actual from unit
        to_unit = 'Fahrenheit'  # Replace with actual to unit
        result = temperature_converter(value, from_unit, to_unit)
        text_input.set(result)

    elif menu_item == "volume":
        value = float(entry.get())
        from_unit = 'litre'  # Replace with actual from unit
        to_unit = 'ml'  # Replace with actual to unit
        result = volume_converter(value, from_unit, to_unit)
        text_input.set(result)

    elif menu_item == "weight":
        value = float(entry.get())
        from_unit = 'Kg'  # Replace with actual from unit
        to_unit = 'g'  # Replace with actual to unit
        result = weight_converter(value, from_unit, to_unit)
        text_input.set(result)

    elif menu_item == "sqrt":
        value = float(entry.get())
        result = sqrt_converter(value)
        text_input.set(result)



# Placeholder for Standard Calculator Logic
def standard_calculator_logic(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# Placeholder for Scientific Calculator Logic
def scientific_calculator_logic(expression):
        result = eval(expression)
        if "sqrt" in expression:
            result = math.sqrt(result)
        elif "sin" in expression:
            result = math.sin(math.radians(result))
        elif "cos" in expression:
            result = math.cos(math.radians(result))
        elif "tan" in expression:
            result = math.tan(math.radians(result))
        return str(result)

# Function to perform the conversion
def convert():
    selected_converter = converter_var.get()
    input_value = float(entry.get())
    if selected_converter == "Feet to Meters":
        result = length_converter(input_value, 'feet', 'meters')
        result_label.config(text=f"{result} meters")
    elif selected_converter == "Meters to Feet":
        result = length_converter(input_value, 'meters', 'feet')
        result_label.config(text=f"{result} feet")
    elif selected_converter == "Celsius to Fahrenheit":
        result = temperature_converter(input_value, 'Celsius', 'Fahrenheit')
        result_label.config(text=f"{result} Fahrenheit")
    elif selected_converter == "Fahrenheit to Celsius":
        result = temperature_converter(input_value, 'Fahrenheit', 'Celsius')
        result_label.config(text=f"{result} Celsius")
    elif selected_converter == "USD to EUR":
        result = currency_converter(input_value, 'USD', 'EUR')
        result_label.config(text=f"{result} EUR")
    elif selected_converter == "EUR to USD":
        result = currency_converter(input_value, 'EUR', 'USD')
        result_label.config(text=f"{result} USD")
    elif selected_converter == "litre to ml":
        result = volume_converter(input_value, 'litre', 'ml')
        result_label.config(text=f"{result} ml")
    elif selected_converter == "ml to litre":
        result = volume_converter(input_value, 'ml', 'litre')
        result_label.config(text=f"{result} litre")
    elif selected_converter == "Kg to g":
        result = weight_converter(input_value, 'Kg', 'g')
        result_label.config(text=f"{result} g")
    elif selected_converter == "g to Kg":
        result = weight_converter(input_value, 'g', 'Kg')
        result_label.config(text=f"{result} Kg")
    elif selected_converter == "sqrt":
        result = sqrt_converter(input_value)
        result_label.config(text=f"{result}")
    
    text_input.set("")
# Create the menu bar
menubar = Menu(calc)
calc.config(menu=menubar)

# Create the File menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=calc.destroy)

# Create the Scientific menu
scientific_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Scientific", menu=scientific_menu)
scientific_menu.add_command(label="sqrt", command=lambda: converter_var.set("sqrt"))

# Create the Converter menu
converter_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Converters", menu=converter_menu)

# Submenu for Length conversion
length_menu = Menu(converter_menu, tearoff=0)
converter_menu.add_cascade(label="Length", menu=length_menu)
length_menu.add_command(label="Feet to Meters", command=lambda: converter_var.set("Feet to Meters"))
length_menu.add_command(label="Meters to Feet", command=lambda: converter_var.set("Meters to Feet"))

# Submenu for Temperature conversion
temp_menu = Menu(converter_menu, tearoff=0)
converter_menu.add_cascade(label="Temperature", menu=temp_menu)
temp_menu.add_command(label="Celsius to Fahrenheit", command=lambda: converter_var.set("Celsius to Fahrenheit"))
temp_menu.add_command(label="Fahrenheit to Celsius", command=lambda: converter_var.set("Fahrenheit to Celsius"))

temp_menu = Menu(converter_menu, tearoff=0)
converter_menu.add_cascade(label="currency", menu=temp_menu)
temp_menu.add_command(label="USD to EUR", command=lambda: converter_var.set("USD to EUR"))
temp_menu.add_command(label="EUR to USD", command=lambda: converter_var.set("EUR to USD"))

temp_menu = Menu(converter_menu, tearoff=0)
converter_menu.add_cascade(label="volume", menu=temp_menu)
temp_menu.add_command(label="Litre to ML", command=lambda: converter_var.set("litre to ml"))
temp_menu.add_command(label="ML to Litre", command=lambda: converter_var.set("ml to litre"))

temp_menu = Menu(converter_menu, tearoff=0)
converter_menu.add_cascade(label="weight", menu=temp_menu)
temp_menu.add_command(label="Kg to g", command=lambda: converter_var.set("Kg to g"))
temp_menu.add_command(label="g to Kg", command=lambda: converter_var.set("g to Kg"))

# Create the entry field
entry = Entry(calc, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='white', justify='right')
entry.grid(row=0, column=0, columnspan=4)

result_label = Label(calc, text="", font=('arial', 16),bg='white')
result_label.grid(row=0, column=0, columnspan=4, pady=20)

convert_button = Button(calc, padx=10, pady=5, bd=8, fg='black', font=('arial', 20, 'bold'), text='Convert', bg='powder blue', command=convert)
convert_button.grid(row=5, column=1, columnspan=2)

#=============================================FIRST ROW==========================================================================#
button_7 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', bg='white', command=lambda: bttnClick(7))
button_7.grid(row=1, column=0)

button_8 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', bg='white', command=lambda: bttnClick(8))
button_8.grid(row=1, column=1)

button_9 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', bg='white', command=lambda: bttnClick(9))
button_9.grid(row=1, column=2)

Addition_button = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', bg='white', command=lambda: bttnClick('+'))
Addition_button.grid(row=1, column=3)

#===============================================SECOND ROW==========================================================================#

button_4 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', bg='white', command=lambda: bttnClick(4))
button_4.grid(row=2, column=0)

button_5 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', bg='white', command=lambda: bttnClick(5))
button_5.grid(row=2, column=1)

button_6 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', bg='white', command=lambda: bttnClick(6))
button_6.grid(row=2, column=2)

Subtraction_button = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', bg='white', command=lambda: bttnClick('-'))
Subtraction_button.grid(row=2, column=3)

#===============================================THIRD ROW==========================================================================#

button_3 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', bg='white', command=lambda: bttnClick(3))
button_3.grid(row=3, column=0)

button_2 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', bg='white', command=lambda: bttnClick(2))
button_2.grid(row=3, column=1)

button_1 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', bg='white', command=lambda: bttnClick(1))
button_1.grid(row=3, column=2)

Multiplication_button = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='*', bg='white', command=lambda: bttnClick('*'))
Multiplication_button.grid(row=3, column=3)

#===============================================FOURTH ROW==========================================================================#

button_0 = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', bg='white', command=lambda: bttnClick(0))
button_0.grid(row=4, column=0)

button_Clear = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', bg='white', command=bttnClear)
button_Clear.grid(row=4, column=1)

button_Equals = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', bg='powder blue', command=bttnEquals)
button_Equals.grid(row=4, column=3)

Division_button = Button(calc, padx=25, pady=10, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', bg='white', command=lambda: bttnClick('/'))
Division_button.grid(row=4, column=2)

calc.mainloop()