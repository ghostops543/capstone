import tkinter
from tkinter import Toplevel

import customtkinter
from PIL import  Image


import Patient
from database import predict, plots, get_score, get_matrix, get_report

window = customtkinter.CTk()
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
def startGUI():



    window.geometry(f"{300}x{150}")
    window.title("my capstone project")
    window.grid_columnconfigure((0), weight=1)
    window.grid_rowconfigure((0,1,2), weight=0)

    customtkinter.CTkLabel(window, text="take ASQ-10").grid(row = 0, column = 0,padx = 100, pady = (5,0) ,sticky="w")
    AQ_test = customtkinter.CTkButton(window, text = "take ASQ-10", command=AQ_test_start)
    AQ_test.grid(row = 1, column = 0,padx = (70,100), pady = (0,5) ,sticky="w")



    def show_results():
        newpatient = Patient.prepatient(Patient.scores)
        #print([newpatient.A1_Score, newpatient.A2_Score, newpatient.A3_Score, newpatient.A4_Score, newpatient.A5_Score,
        #                   newpatient.A6_Score, newpatient.A7_Score, newpatient.A8_Score, newpatient.A9_Score, newpatient.A10_Score, newpatient.total])
        result = predict([[newpatient.A1_Score, newpatient.A2_Score, newpatient.A3_Score, newpatient.A4_Score, newpatient.A5_Score,
                           newpatient.A6_Score, newpatient.A7_Score, newpatient.A8_Score, newpatient.A9_Score, newpatient.A10_Score, newpatient.total]])
        window.withdraw()
        results_start(result)

        #patient = Patient(706,AQ_scores,gender,)
    #insert button
    insert = customtkinter.CTkButton(window, text="submit", command= show_results)
    insert.grid(row =2, column = 0,padx = (70,100), pady = (5,0) ,sticky="w")
    window.mainloop()



def AQ_test_start():
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")

    test = Toplevel(window)
    test.geometry("900x568")
    test.configure(background="dark blue")
    test_image = customtkinter.CTkImage(light_image= Image.open("data set/Screenshot 2025-02-24 122322.png"),
                                        dark_image= Image.open("data set/Screenshot 2025-02-24 122322.png"), size=(368,468))
    image_label = customtkinter.CTkLabel(test, image=test_image,text="")
    image_label.pack(side="left", pady = (0,100))


    def question_convert(var):
        if "Definitely Agree" == var or "Slightly Agree" == var:
            var = 0
        elif "Slightly Disagree" == var or "Definitely Disagree" == var:
            var = 1
        return(var)

    def button1(var):
         Patient.insert_scores(question_convert(var), 1)
    AQ1_var = customtkinter.StringVar()
    AQ1 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button1, variable= AQ1_var)
    AQ1.place(x= 400, y = 5)

    def button2(var):
         Patient.insert_scores(question_convert(var), 2)
    AQ2_var = customtkinter.StringVar()
    AQ2 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button2, variable= AQ2_var)
    AQ2.place(x= 400, y = 50)

    def button3(var):
         Patient.insert_scores(question_convert(var), 3)
    AQ3_var = customtkinter.StringVar()
    AQ3 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button3, variable= AQ3_var)
    AQ3.place(x= 400, y = 95)

    def button4(var):
         Patient.insert_scores(question_convert(var), 4)
    AQ4_var = customtkinter.StringVar()
    AQ4 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button4, variable= AQ4_var)
    AQ4.place(x= 400, y = 140)

    def button5(var):
         Patient.insert_scores(question_convert(var), 5)
    AQ5_var = customtkinter.StringVar()
    AQ5 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button5, variable= AQ5_var)
    AQ5.place(x= 400, y = 185)

    def button6(var):
         Patient.insert_scores(question_convert(var), 6)
    AQ6_var = customtkinter.StringVar()
    AQ6 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button6, variable= AQ6_var)
    AQ6.place(x= 400, y = 230)

    def button7(var):
         Patient.insert_scores(question_convert(var), 7)
    AQ7_var = customtkinter.StringVar()
    AQ7 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button7, variable= AQ7_var)
    AQ7.place(x= 400, y = 275)

    def button8(var):
         Patient.insert_scores(question_convert(var), 8)
    AQ8_var = customtkinter.StringVar()
    AQ8 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button8, variable= AQ8_var)
    AQ8.place(x= 400, y = 335)

    def button9(var):
         Patient.insert_scores(question_convert(var), 9)
    AQ9_var = customtkinter.StringVar()
    AQ9 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button9, variable= AQ9_var)
    AQ9.place(x= 400, y = 385)

    def button10(var):
         Patient.insert_scores(question_convert(var), 10)
    AQ10_var = customtkinter.StringVar()
    AQ10 = customtkinter.CTkSegmentedButton(test, values=["Definitely Agree", "Slightly Agree", "Slightly Disagree", "Definitely Disagree" ], command= button10, variable= AQ10_var)
    AQ10.place(x= 400, y = 440)

    def submit():

        test.destroy()
    sub_button = customtkinter.CTkButton(test, text="submit", command = submit)
    sub_button.place(x=400,y=500)




    test.mainloop()

def results_start(result):
    results = Toplevel(window)
    results.geometry("300x300")
    results.title("results")
    results.configure(background="light blue")





    rtitle = customtkinter.CTkLabel(results, text="your results are in", text_color="black")
    rtitle.pack()
    rresults = customtkinter.CTkLabel(results, text=result, text_color="black")
    rresults.pack()

    plot_button = customtkinter.CTkButton(results, text= 'show ML plots', text_color='black', command=plots )
    plot_button.pack()

    line1 = customtkinter.CTkLabel(results, text='show machine learning statistics\n (displays in console)', text_color="black")

    line2 = customtkinter.CTkButton(results, text='show score', text_color="black", command= get_score)
    line3 = customtkinter.CTkButton(results, text='show confusion matrix', text_color="black", command= get_matrix)
    line4 = customtkinter.CTkButton(results, text='show classification report', text_color="black", command= get_report)
    line5 = customtkinter.CTkButton(results, text='exit', text_color="black", command= exit)
    line1.pack(pady = 5)
    line2.pack(pady = 5)
    line3.pack(pady = 5)
    line4.pack(pady = 5)
    line5.pack(pady = 5)

    results.mainloop()


#AQ_test_start()
