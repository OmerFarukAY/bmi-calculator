from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)


def Calculate():
    Height = HeightEntry.get()
    Weight = WeightEntry.get()

    if Weight == "" or Height == "":
        CalculationLabel.config(text="Enter both weight and height!")
    else:
        try:
         bmi = float(Weight) / (float(Height) / 100) ** 2
         ResultString = Results(bmi)
         CalculationLabel.config(text=ResultString)
        except:
            CalculationLabel.config(text="Enter a valid number!")



#Weight Label
WeightLabel = Label(text="Enter Your Weight (kg)",font=("Arial", 10))
WeightLabel.pack()

#Weight Entry
WeightEntry = Entry(width=10)
WeightEntry.get()
WeightEntry.pack()


#Height Label
HeightLabel = Label(text="Enter Your Height (m)",font=("Arial", 10))
HeightLabel.pack()

#Height Entry
HeightEntry = Entry(width=10)
HeightEntry.pack()


#Button
CalculateButton = Button(text="Calculate",command=Calculate)
CalculateButton.pack()

#Calculatin Label
CalculationLabel = Label(font=("Arial", 10))
CalculationLabel.pack()

def Results(bmi):
    ResultString = f"Your BMI is: {bmi:.2f}. You are  "
    if bmi < 16:
        ResultString += "Severely underweight"
    elif 16 <= bmi < 18.4:
        ResultString += "Underweight"
    elif 18.5 <= bmi < 24.9:
        ResultString += "Normal"
    elif 25 <= bmi < 29.9:
        ResultString += "Overweight"
    elif 30 <= bmi < 34.9:
        ResultString += "Moderately obese"
    elif 35 <= bmi < 39.9:
        ResultString += "Severely obese"
    else:
        ResultString += "Morbidly obese"

    return ResultString

window.mainloop()