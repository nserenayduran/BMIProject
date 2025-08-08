from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.minsize(400,400)


label=Label(text="Enter your height",font=("Verdana",12),fg="purple")
label.pack(padx=10,pady=10)

entry_1=Entry(width=20)
entry_1.pack(padx=10,pady=10)

label_2=Label(text="Enter your weight",font=("Verdana",12),fg="purple")
label_2.pack(padx=10,pady=10)

entry_2=Entry(width=20)
entry_2.pack(padx=10,pady=10)


def bmi_calculate():
    try:
            height = float(entry_1.get())
            weight = float(entry_2.get())
            bmi = weight / height ** 2

            if bmi<18.5:
                label_3.config(text=f"Your BMI is {bmi}, you are under weight")

            elif bmi>=18.5 and bmi<=24.9:
                label_3.config(text=f"Your BMI is {bmi}, you are normal weight")

            elif bmi>=25 and bmi<=29.9:
                label_3.config(text=f"Your BMI is {bmi}, you are overweight")

            elif bmi>=30 and bmi<=34.9:
                label_3.config(text=f"Your BMI is {bmi}, you are obese class 1")

            elif bmi>=35 and bmi<=39.9:
                label_3.config(text=f"Your BMI is {bmi}, you are obese class 2")

            elif bmi>=40 and bmi<=44.9:
                label_3.config(text=f"Your BMI is {bmi}, you are obese class 3")

    except:
        label_3.config(text="Error please enter correct values ")


button=Button(text="Calculate",command=bmi_calculate)
button.pack(padx=10,pady=10)

label_3=Label(font=("Verdana",12))
label_3.pack(padx=10,pady=10)


window.mainloop()