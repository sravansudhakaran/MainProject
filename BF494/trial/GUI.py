from tkinter import *
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk
from tkinter import ttk
import Predict_BF494

class firstWindow(object):
    def __init__(self, parent):
        win = parent
        maincolor='#CFD8DC'
        win.configure(bg=maincolor)
        win.title("Reliability Test")
        win.attributes('-fullscreen', True)
        text =Label(win, text="Reliability Prediction",bd=1,bg='blue',fg = 'white',font=("Courier", 50),height=2).pack(fill=X)
        soft_text="►   Predicts the remaining useful life of a BF494 transistor"
        soft_text1="►   Remaining useful life is predicted as the percentage lifetime remaining"
        soft_text2="►   Vce,Vbe and Ambient temperature is measured Other parameters are programatically"
        soft_text3="►   calculated The Deep Neural Network model has 0.08 RMSE"
        soft_text4="►   Astable Multivibrator is used to generate the drive signal"
        soft_text5="►   Arduino samples the analog values and converts to digital values"
        soft_text6="►   Raspberry Pi reads the samples using serial port"
        soft =Label(win, text=soft_text,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=200)
        soft1 =Label(win, text=soft_text1,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=220)
        soft2 =Label(win, text=soft_text2,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=240)
        soft3 =Label(win, text=soft_text3,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=260)
        soft4 =Label(win, text=soft_text4,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=280)
        soft5 =Label(win, text=soft_text5,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=300)
        soft6 =Label(win, text=soft_text6,bd=1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=320)
        hard_text="■   Click the 'Predict' button to run the model"
        hard_text1="■   Click the 'Exit' button to close the program"
        componentstext =Label(win,bd=1,text=hard_text,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=550)
        componentstext1 =Label(win,bd=1,text=hard_text1,fg = 'black',font=("Helvetica", 10,"bold"),height=1).place(x=20,y=570)
        imagemain=Image.open("screencircuit1.png")
        photomain = ImageTk.PhotoImage(imagemain)
        labelmain = Label(win,image=photomain,height=400,width=600,bg=maincolor)
        labelmain.image = photomain
        labelmain.place(x=700, y=170)



        def exit():
            win.destroy()
        def hide():
            win.withdraw()
        def Prediction_window():
            prediction_screen= Toplevel(win)
            app = predictionScreen(prediction_screen)
            hide();

        prediction =Button(win, text ="PREDICT", command = Prediction_window,height =3,width =10,bg='green',font=("Courier"),fg='white').place(x=400,y=650)
        mainexit =Button(win, text ="EXIT", command = exit,bg='orange',font=("Courier"),fg='white',height = 3, width = 10).place(x=800,y=650)

class predictionScreen:
    def __init__(self,predictionmaster):
        self.predictionmaster=predictionmaster
        predictionmaster.attributes('-fullscreen', True)
        bgcolor='#FFFFFF'
        predictionmaster.configure(bg=bgcolor)
        def onCloseOtherFrame():
            predictionmaster.destroy()
            win.update()
            win.deiconify()
        text =Label(predictionmaster, text="BF494 Reliability Prediction",bd=1,bg='blue',fg = 'white',font=("Courier", 20),height=1).pack(fill=X)
        back =Button(predictionmaster, text ="<<", command = onCloseOtherFrame,bg='black',font=("Courier"),fg='white',height = 1, width = 1).place(x=0,y=0)

        vce_max,vce_min,vbe_max,vbe_min,temp,rul=Predict_BF494.predict_rul()



        figvbe = Figure(figsize=(6,4), dpi=75)
        axvbe = figvbe.add_subplot(111)
        axvbe.set_xlabel("Frequency")
        axvbe.set_ylabel("Voltage")
        axvbe.set_ylim(0,5)
        axvbe.set_xlim(0,10)
        t = np.linspace(0, 10, 1000, endpoint=True)
        axvbe.grid()

        graphvbe = FigureCanvasTkAgg(figvbe, master=predictionmaster)
        graphvbe.get_tk_widget().place(x=850,y=50)

        figvce = Figure(figsize=(6,4), dpi=75)
        axvce = figvce.add_subplot(111)
        axvce.set_xlabel("Frequency")
        axvce.set_ylim(0,15)
        axvce.set_xlim(0,10)
        axvce.set_ylabel("Voltage")
        t = np.linspace(0, 10, 1000, endpoint=True)
        axvce.grid()

        graphvce = FigureCanvasTkAgg(figvce, master=predictionmaster)
        graphvce.get_tk_widget().place(x=850,y=410)




        text =Label(predictionmaster, text="Emitter-Base Voltage",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=1000,y=370)


        text =Label(predictionmaster, text="Collector-Emitter Voltage",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=980,y=730)
        update=round(.4*rul)+1

        image=Image.open("meter.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(predictionmaster,image=photo,height=300,width=450,bg=bgcolor)
        label.image = photo
        label.place(x=100, y=50)

        meter_image=['meter_0.jpg','meter_1.jpg','meter_2.jpg','meter_3.jpg','meter_4.jpg','meter_5.jpg','meter_6.jpg','meter_7.jpg','meter_8.jpg','meter_9.jpg','meter_10.jpg','meter_11.jpg','meter_12.jpg',
        'meter_13.jpg','meter_14.jpg','meter_15.jpg','meter_16.jpg','meter_17.jpg','meter_18.jpg','meter_19.jpg','meter_20.jpg','meter_21.jpg','meter_22.jpg','meter_23.jpg','meter_24.jpg','meter_25.jpg',"meter_26.jpg",
        "meter_27.jpg","meter_28.jpg","meter_29.jpg","meter_30.jpg","meter_31.jpg","meter_32.jpg","meter_33.jpg","meter_34.jpg","meter_35.jpg","meter_36.jpg","meter_37.jpg","meter_38.jpg","meter_39.jpg","meter_40.jpg",]

        text =Label(predictionmaster, text="Measuring transistor parameters",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=20,y=370)
        text =Label(predictionmaster, text="Collect-Emitter Voltage(Vpp):",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=20,y=400)
        text_vce =Label(predictionmaster, text="0v",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor)
        text_vce.place(x=300,y=400)

        text =Label(predictionmaster, text="Emitter-Base Voltage(Vpp):",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=20,y=430)
        text_vbe =Label(predictionmaster, text="0v",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor)
        text_vbe.place(x=300,y=430)

        text =Label(predictionmaster, text="Ambient Temperature(°C):",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=20,y=460)
        text_temp =Label(predictionmaster, text="0°C",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor)
        text_temp.place(x=300,y=460)

        text =Label(predictionmaster, text="Running DNN Model:",bd=1,fg = 'black',font=("Courier", 10),height=1,bg=bgcolor).place(x=20,y=490)


        text =Label(predictionmaster, text="Remaining Useful Life:",bd=1,fg = 'black',font=("Helvetica", 15,"bold"),height=1,bg=bgcolor).place(x=160,y=650)
        text_rul =Label(predictionmaster, text=" 0%",bd=1,fg = 'black',font=("Courier", 15),height=1,bg=bgcolor)
        text_rul.place(x=430,y=650)

        progressbar=ttk.Progressbar(predictionmaster,orient="horizontal",length=300,mode="determinate")
        progressbar.place(x=300,y=370)

        progressbardnn=ttk.Progressbar(predictionmaster,orient="horizontal",length=300,mode="determinate")
        progressbardnn.place(x=300,y=490)

        currentValue=0
        maxValue=100
        def progress(currentValue):
            progressbar["value"]=currentValue
        divisions=10
        for i in range(divisions):
            currentValue=currentValue+10
            progressbar.after(1000, progress(currentValue))
            progressbar.update()
        progressbar["value"]=currentValue
        progressbar["maximum"]=maxValue

        if currentValue==maxValue:
            text_vce.configure(text=str(vce_max)+"v")
            text_vbe.configure(text=str(vbe_max)+"v")
            text_temp.configure(text=str(temp)+"c")



            figvbe = Figure(figsize=(6,4), dpi=75)
            axvbe = figvbe.add_subplot(111)
            axvbe.set_xlabel("Frequency")
            axvbe.set_ylabel("Voltage")
            axvbe.set_ylim(0,5)
            axvbe.set_xlim(0,10)
            t = np.linspace(0, 10, 1000, endpoint=True)
            axvbe.grid()
            axvbe.plot(t,vbe_max*signal.square(2 * np.pi * 1000 * t))
            graphvbe = FigureCanvasTkAgg(figvbe, master=predictionmaster)
            graphvbe.get_tk_widget().place(x=850,y=50)

            figvce = Figure(figsize=(6,4), dpi=75)
            axvce = figvce.add_subplot(111)
            axvce.set_xlabel("Frequency")
            axvce.set_ylim(0,15)
            axvce.set_xlim(0,10)
            axvce.set_ylabel("Voltage")
            t = np.linspace(0, 10, 1000, endpoint=True)
            axvce.grid()
            axvce.plot(t, vce_max*signal.square(2 * np.pi * 1000 * t))
            graphvce = FigureCanvasTkAgg(figvce, master=predictionmaster)
            graphvce.get_tk_widget().place(x=850,y=410)





            currentValuednn=0
            maxValuednn=100
            def progressdnn(currentValuednn):
                progressbardnn["value"]=currentValuednn
            divisionsdnn=10
            for i in range(divisionsdnn):
                currentValuednn=currentValuednn+10
                progressbardnn.after(500, progressdnn(currentValuednn))
                progressbardnn.update()
            progressbardnn["value"]=currentValuednn
            progressbardnn["maximum"]=maxValuednn

            if currentValuednn==maxValuednn:
                text_rul.configure(text=str(rul)+"%")
                for i in range(0,update):
                    image=Image.open(meter_image[i])
                    indication = ImageTk.PhotoImage(image)
                    label.image=indication
                    label.configure(image=indication)
                    predictionmaster.update()
                    time.sleep(.05)

if __name__ == "__main__":
    win =Tk()

    first = firstWindow(win)
    win.mainloop()
