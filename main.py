from tkinter import *
from tkinter import ttk
from numpy import arange
from math import pi, sin, cos, tan
import random
import matplotlib.pyplot as plt
import datetime


def table():
    table_root = Toplevel()
    table_root.title("Trigonometric Table")
    table_root.geometry("400x125")
    table_root.resizable(False, False)

    # Internal function
    def calculate():
        duplicate = False
        # Function to count the trig func
        trig_result = f"The result of {trig_strvar.get()} {num_strvar.get()} is "
        angle = int(num_strvar.get())

        # Solution to similar trig functions
        if angle >= 210:
            angle_double = {210: 150,
                            225: 135,
                            240: 120,
                            270: 90,
                            300: 60,
                            315: 45,
                            330: 30,
                            360: 0}
            duplicate = True
            # Convert the initial angle from key to value
            if angle in angle_double:
                angle = angle_double[angle]

        if trig_strvar.get() == "Sin":
            match angle:
                case 0:
                    trig_res_num = "0"
                case 30:
                    trig_res_num = "1/2"
                case 45:
                    trig_res_num = "1/√2"
                case 60:
                    trig_res_num = "√3/2"
                case 90:
                    trig_res_num = "1"
                case 120:
                    trig_res_num = "√3/2"
                case 135:
                    trig_res_num = "1/√2"
                case 150:
                    trig_res_num = "1/2"
                case 180:
                    trig_res_num = "0"
                case _:
                    trig_res_num = "How are you even here"

        elif trig_strvar.get() == "Cos":
            match angle:
                case 0:
                    trig_res_num = "1"
                case 30:
                    trig_res_num = "√3/2"
                case 45:
                    trig_res_num = "1/√2"
                case 60:
                    trig_res_num = "1/2"
                case 90:
                    trig_res_num = "0"
                case 120:
                    trig_res_num = "-1/2"
                case 135:
                    trig_res_num = "-1/√2"
                case 150:
                    trig_res_num = "-√3/2"
                case 180:
                    trig_res_num = "1"
                case _:
                    trig_res_num = "How are you even here"

        else:
            match angle:
                case 0:
                    trig_res_num = "0"
                case 30:
                    trig_res_num = "1/√3"
                case 45:
                    trig_res_num = "1"
                case 60:
                    trig_res_num = "√3"
                case 90:
                    trig_res_num = "Undetermined"
                case 120:
                    trig_res_num = "-√3"
                case 135:
                    trig_res_num = "-1"
                case 150:
                    trig_res_num = "-1/√3"
                case 180:
                    trig_res_num = "0"
                case _:
                    trig_res_num = "How are you even here"

        # Hotfix: Change cos 210 -> 240 to negative, and sin 300 -> 240 to positive
        if (trig_strvar.get() != "Cos") and not (210 <= angle <= 240 or 300 <= angle <= 360):
            if not trig_res_num == "Undetermined" and duplicate is True:
                trig_result += "-"  # Add the sign if the angle is negative (double negative sign will be removed later)

        trig_result += trig_res_num
        trig_result = trig_result.replace("--", "").replace("-0", "0")  # Remove double negative sign and negative zero

        trig_result_label.config(text=trig_result)

    def stay_ontop_table():
        global table_ontop_var
        if table_ontop_var is False:
            table_root.attributes("-topmost", True)
            ontop_table_button.config(relief=SUNKEN)
            table_ontop_var = True
        else:
            table_root.attributes("-topmost", False)
            ontop_table_button.config(relief=RAISED)
            table_ontop_var = False

    trig_strvar = StringVar(table_root)
    trig_strvar.set("Sin")  # default value

    trig_func_option = OptionMenu(table_root, trig_strvar, "Sin", "Cos", "Tan")

    num_strvar = StringVar(table_root)
    num_strvar.set("0")  # default value

    option_number = OptionMenu(table_root, num_strvar, "0", "30", "45", "60", "90", "120", "135", "150", "180", "210",
                               "225", "240", "270", "300", "315", "330", "360")

    button_calculate = Button(table_root, text="Calculate", command=calculate)

    trig_result_label = Label(table_root, text="", font=("Consolas", 10))

    ontop_table_button = Button(table_root, text="On Top", command=stay_ontop_table)

    # Pack the widgets
    trig_func_option.place(x=125, y=15)
    option_number.place(x=225, y=15)
    button_calculate.place(x=175, y=70)

    trig_result_label.pack(side=BOTTOM, pady=7)
    ontop_table_button.place(x=7, y=90)


def questions():
    class Question:
        def __init__(self, nomor, x_start, y_start, once):
            self.question_num = nomor
            self.x_start = x_start
            self.y_start = y_start
            self.false_button = self.true_button = None
            self.local_strvar = StringVar()
            self.local_strvar.set("False")  # Biar kosong
            self.question = None
            self.trig_type = None
            self.trig_num = None
            self.once = once

        def generate_question(self, trig_type, trig_num, answer, correct_bool, answer_list):
            self.trig_type = trig_type
            self.trig_num = trig_num

            if self.question_num > questions_amount:
                return None  # If we got more questions than needed

            if self.once == 1:
                self.once += 1
            elif self.once == 2:
                return None
            else:
                pass

            self.question = Label(soal_root, text=f"{self.question_num}.{trig_type}({trig_num}) equals to {answer}",
                                  font=("Consolas", 13))
            self.question.place(x=self.x_start, y=self.y_start)

            # Make 2 checkboxes for the answers
            self.true_button = Checkbutton(soal_root, text="True", variable=self.local_strvar, onvalue=True,
                                           offvalue=False, font=("Consolas", 13))
            self.false_button = Checkbutton(soal_root, text="False", variable=self.local_strvar, onvalue=False,
                                            offvalue=True, font=("Consolas", 13))
            self.true_button.place(x=self.x_start + 400, y=self.y_start)
            self.false_button.place(x=self.x_start + 500, y=self.y_start)
            # Append it to the answer list
            correct_bool.append(answer_list)

        def check_result(self, correct_bool):
            # Check if the answer is correct
            correct_bool = [1 if x is True else 0 for x in correct_bool]  # if True, change to 1, else 0

            if int(self.local_strvar.get()) == correct_bool[self.question_num - 1]:
                return True
            else:
                return False

        def right_answer(self):
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

        def wrong_answer(self):
            self.question.config(fg="red")

            # Sin
            if self.trig_type == "Sin":
                sin_dict = {0: "0",
                            30: "1/2",
                            45: "1/√2",
                            60: "√3/2",
                            90: "1",
                            120: "√3/2",
                            135: "1/√2",
                            150: "1/2",
                            180: "0",
                            210: "-1/2",
                            225: "-1/√2",
                            240: "-√3/2",
                            270: "-1",
                            300: "-√3/2",
                            315: "-1/√2",
                            330: "-1/2",
                            360: "0"}
                # find the right answer
                for key, value in sin_dict.items():
                    if key == self.trig_num:
                        Label(soal_root, text=f"The correct answer is {value}",
                              font=("Consolas", 10)).place(x=self.x_start + 175, y=self.y_start + 30)

            # Cos
            elif self.trig_type == "Cos":
                cos_dict = {0: "1",
                            30: "√3/2",
                            45: "1/√2",
                            60: "1/2",
                            90: "0",
                            120: "-1/2",
                            135: "-1/√2",
                            150: "-√3/2",
                            180: "-1",
                            210: "-√3/2",
                            225: "-1/√2",
                            240: "-1/2",
                            270: "0",
                            300: "1/2",
                            315: "1/√2",
                            330: "√3/2",
                            360: "1"}
                # find the right answer
                for key, value in cos_dict.items():
                    if key == self.trig_num:
                        Label(soal_root, text=f"The correct answer is {value}",
                              font=("Consolas", 10)).place(x=self.x_start + 175, y=self.y_start + 30)

            # Tan
            else:
                tan_dict = {0: "0",
                            30: "1/√3",
                            45: "1",
                            60: "√3",
                            90: "Undetermined",
                            120: "-√3",
                            135: "-1",
                            150: "-1/√3",
                            180: "0",
                            210: "1/√3",
                            225: "1",
                            240: "√3",
                            270: "Undetermined",
                            300: "-√3",
                            315: "-1",
                            330: "-1/√3",
                            360: "0"}
                # find the right answer
                for key, value in tan_dict.items():
                    if key == self.trig_num:
                        Label(soal_root, text=f"The correct answer is {value}",
                              font=("Consolas", 10)).place(x=self.x_start + 175, y=self.y_start + 30)

    def stay_ontop_questions():
        global question_ontop_var
        if question_ontop_var is False:
            soal_root.attributes("-topmost", True)
            questions_ontop_button.config(relief=SUNKEN)
            question_ontop_var = True
        else:
            soal_root.attributes("-topmost", False)
            questions_ontop_button.config(relief=RAISED)
            question_ontop_var = False

    soal_root = Toplevel()
    soal_root.title("Questions")
    soal_root.geometry("600x420")
    soal_root.resizable(False, False)
    questions_amount = 5

    def generate_question(bucket, index):
        # Pick random trig type and number
        sin_dict = cos_dict = tan_dict = {}  # Create empty dictionaries to stop the warnings
        is_correct = random.choice([True, False])
        trig_question_type = random.randint(1, 3)
        trig_question_num = random.choice([0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240,
                                           270, 300, 315, 330, 360])

        # Sin
        if trig_question_type == 1:
            sin_dict = {0: "0",
                        30: "1/2",
                        45: "1/√2",
                        60: "√3/2",
                        90: "1",
                        120: "√3/2",
                        135: "1/√2",
                        150: "1/2",
                        180: "0",
                        210: "-1/2",
                        225: "-1/√2",
                        240: "-√3/2",
                        270: "-1",
                        300: "-√3/2",
                        315: "-1/√2",
                        330: "-1/2",
                        360: "0"}
            soal_trig_jawaban = sin_dict[trig_question_num]
            tipe_trig = "Sin"

        # Cos
        elif trig_question_type == 2:
            cos_dict = {0: "1",
                        30: "√3/2",
                        45: "1/√2",
                        60: "1/2",
                        90: "0",
                        120: "-1/2",
                        135: "-1/√2",
                        150: "-√3/2",
                        180: "-1",
                        210: "-√3/2",
                        225: "-1/√2",
                        240: "-1/2",
                        270: "0",
                        300: "1/2",
                        315: "1/√2",
                        330: "√3/2",
                        360: "1"}
            soal_trig_jawaban = cos_dict[trig_question_num]
            tipe_trig = "Cos"

        # Tan
        else:
            tan_dict = {0: "0",
                        30: "1/√3",
                        45: "1",
                        60: "√3",
                        90: "Undetermined",
                        120: "-√3",
                        135: "-1",
                        150: "-1/√3",
                        180: "0",
                        210: "1/√3",
                        225: "1",
                        240: "√3",
                        270: "Undetermined",
                        300: "-√3",
                        315: "-1",
                        330: "-1/√3",
                        360: "0"}
            soal_trig_jawaban = tan_dict[trig_question_num]
            tipe_trig = "Tan"

        trig_question = f"{tipe_trig}{trig_question_num}"
        if trig_question in bucket:
            generate_question(bucket, index)
        else:
            bucket.append(trig_question)

        if is_correct is False:
            match trig_question_type:
                case 1:
                    soal_trig_jawaban = random.choice(list(sin_dict.values()))
                case 2:
                    soal_trig_jawaban = random.choice(list(cos_dict.values()))
                case 3:
                    soal_trig_jawaban = random.choice(list(tan_dict.values()))
        q[index].generate_question(tipe_trig, trig_question_num, soal_trig_jawaban, answer_bucket, is_correct)

    def check_res():
        temp_bucket = []  # To check if all the answers are already correct or not
        for ind in range(questions_amount):
            if q[ind].check_result(answer_bucket) is True:
                q[ind].right_answer()
                temp_bucket.append(True)
            else:
                q[ind].wrong_answer()

            if len(temp_bucket) == questions_amount:
                soal_root.destroy()

    q = [_ for _ in range(questions_amount)]
    question_bucket, answer_bucket = [], []
    x_start_outer = y_start_outer = 10
    for i in range(questions_amount):
        q[i] = Question(i + 1, x_start_outer, y_start_outer, 1)
        generate_question(question_bucket, i)
        y_start_outer += 75

    check_answers_button = Button(soal_root, text="Check answers", command=check_res)
    check_answers_button.place(x=250, y=380)
    check_answers_button.configure(font=("Consolas", 10))

    questions_ontop_button = Button(soal_root, text="On Top", command=stay_ontop_questions)
    questions_ontop_button.place(x=10, y=380)


def formula():
    formula_root = Toplevel()
    formula_root.title("Formula")
    formula_root.geometry("600x400")
    formula_root.resizable(False, False)

    # Internal Functions
    def quadrant(num):
        quadrant_root = Toplevel(formula_root)
        quadrant_root.title(f"Kuadran {num}")
        quadrant_root.geometry("650x150")
        quadrant_root.resizable(False, False)

        # Label
        quadrant_label = Label(quadrant_root, text=f"Quadrant {num}'s formula:", font=("Consolas", 15, "bold"))
        quadrant_label.place(x=10, y=10)
        match num:
            case 1:
                quadrant_root.geometry("275x150")
                Label(quadrant_root, text="1.Sin(90-A)° = Cos(A)\n"
                                          "2.Cos(90-A)° = Sin(A)\n"
                                          "3.Tan(90-A)° = Cot(A)", font=("Consolas", 15)).place(x=10, y=40)
            case 2:
                Label(quadrant_root, text="1.Sin(180-A)° = Cos(A)\n"
                                          "2.Cos(180-A)° = -Sin(A)\n"
                                          "3.Cot(180-A)° = -Tan(A)", font=("Consolas", 15)).place(x=10, y=40)
                Label(quadrant_root, text="4.Sin(90+A)° = Cos(A)\n"
                                          "5.Cos(90+A)° = -Sin(A)\n"
                                          "6.Tan(90+A)° = -Cot(A)", font=("Consolas", 15)).place(x=360, y=40)
            case 3:
                Label(quadrant_root, text="1.Sin(180+A)° = -Sin(A)\n"
                                          "2.Cos(180+A)° = -Cos(A)\n"
                                          "3.Tan(180+A)° = Tan(A)", font=("Consolas", 15)).place(x=10, y=40)
                Label(quadrant_root, text="4.Sin(270-A)° = -Cos(A)\n"
                                          "5.Cos(270-A)° = -Sin(A)\n"
                                          "6.Tan(270-A)° = Cot(A)", font=("Consolas", 15)).place(x=360, y=40)
            case 4:
                Label(quadrant_root, text="1.Sin(270+A)° = -Cos(A)\n"
                                          "2.Cos(270+A)° = Sin(A)\n"
                                          "3.Tan(270+A)° = -Cot(A)", font=("Consolas", 15)).place(x=10, y=40)
                Label(quadrant_root, text="4.Sin(360-A)° = -Cos(A)\n"
                                          "5.Cos(360-A)° = Sin(A)\n"
                                          "6.Tan(360-A)° = -Tan(A)", font=("Consolas", 15)).place(x=360, y=40)

        def stay_ontop_quadrant():
            global quadrant_ontop_var
            if quadrant_ontop_var is False:
                quadrant_root.attributes("-topmost", True)
                ontop_kuadran_button.config(relief=SUNKEN)
                quadrant_ontop_var = True
            else:
                quadrant_root.attributes("-topmost", False)
                ontop_kuadran_button.config(relief=RAISED)
                quadrant_ontop_var = False

        ontop_kuadran_button = Button(quadrant_root, text="On Top", command=stay_ontop_quadrant)
        ontop_kuadran_button.place(relx=0.5, rely=0.9, anchor=CENTER)

        quadrant_root.mainloop()

    def sin_graph_func():
        plt.figure("Sine Graph")
        plt.title("Sine Graph")
        x = arange(0, 2 * pi, 0.01)

        for i in x:
            y = sin(i)
            plt.plot(i, y, "bo")
        plt.show()

    def cos_graph_func():
        plt.figure("Cosine Graph")
        plt.title("Cosine Graph")
        x = arange(0, 2 * pi, 0.01)

        for i in x:
            y = cos(i)
            plt.plot(i, y, "ro")
        plt.show()

    def tan_graph_func():
        plt.figure("Tangent Graph")
        plt.title("Tangent Graph")
        x = arange(0, 2 * pi, 0.01)

        for i in x:
            y = tan(i)
            # Filter angka yang ketinggian
            if y > 300:
                pass
            else:
                plt.plot(i, y, "go")
        plt.show()

    def ontop_formula():
        global formula_ontop_var
        if formula_ontop_var is False:
            formula_root.attributes("-topmost", True)
            ontop_formula_button.config(relief=SUNKEN)
            formula_ontop_var = True
        else:
            formula_root.attributes("-topmost", False)
            ontop_formula_button.config(relief=RAISED)
            formula_ontop_var = False

    quadrant1_button = Button(formula_root, text="Quadrant 1", font=("Consolas", 20), command=lambda: quadrant(1))
    quadrant2_button = Button(formula_root, text="Quadrant 2", font=("Consolas", 20), command=lambda: quadrant(2))
    quadrant3_button = Button(formula_root, text="Quadrant 3", font=("Consolas", 20), command=lambda: quadrant(3))
    quadrant4_button = Button(formula_root, text="Quadrant 4", font=("Consolas", 20), command=lambda: quadrant(4))

    sin_graph = Button(formula_root, text="Sine Graph", command=sin_graph_func)
    cos_graph = Button(formula_root, text="Cosine Graph", command=cos_graph_func)
    tan_graph = Button(formula_root, text="Tangent Graph", command=tan_graph_func)

    ontop_formula_button = Button(formula_root, text="On Top", command=ontop_formula)
    ontop_formula_button.place(x=5, y=367)

    # Make a line to seperate the buttons
    Label(formula_root, text="-" * 100).place(rely=0.4, relx=0.5, anchor=CENTER)
    Label(formula_root, text="|\n" * 20).place(rely=0.4, relx=0.5, anchor=CENTER)
    quadrant1_button.place(rely=0.05, relx=0.65)
    quadrant2_button.place(rely=0.05, relx=0.075)
    quadrant3_button.place(rely=0.575, relx=0.075)
    quadrant4_button.place(rely=0.575, relx=0.65)

    # angle tag
    Label(formula_root, text="0°", font=("Consolas", 10)).place(rely=0.37, relx=0.93, anchor=CENTER)
    Label(formula_root, text="360°", font=("Consolas", 10)).place(rely=0.43, relx=0.93, anchor=CENTER)
    Label(formula_root, text="90°", font=("Consolas", 10)).place(rely=0.01, relx=0.505, anchor="n")
    Label(formula_root, text="180°", font=("Consolas", 10)).place(rely=0.40, relx=0.07, anchor=CENTER)
    Label(formula_root, text="270°", font=("Consolas", 10)).place(rely=0.79, relx=0.505, anchor="s")

    # Texts
    Label(formula_root, text="Sin(+) Cos(+), Tan(+)", font=("Consolas", 10)).place(rely=0.27, relx=0.73, anchor="n")
    Label(formula_root, text="Sin(-) Cos(+), Tan(-)", font=("Consolas", 10)).place(rely=0.27, relx=0.27, anchor="n")
    Label(formula_root, text="Sin(-) Cos(-), Tan(+)", font=("Consolas", 10)).place(rely=0.53, relx=0.27, anchor="s")
    Label(formula_root, text="Sin(+) Cos(-), Tan(-)", font=("Consolas", 10)).place(rely=0.53, relx=0.73, anchor="s")

    Label(formula_root, font=("Consolas", 20)).pack(anchor="e",
                                                    side=BOTTOM)  # Indentasi, anchor kiri biar gak kelihatan
    sin_graph.place(rely=0.95, relx=0.3, anchor=CENTER)
    cos_graph.place(rely=0.95, relx=0.55, anchor=CENTER)
    tan_graph.place(rely=0.95, relx=0.8, anchor=CENTER)


def main():
    root = Tk()
    tab = ttk.Notebook(root)

    # Window config
    root.title("Trigonoapp")
    root.geometry("500x375")
    root.resizable(False, False)

    # Frame
    main_tab = Frame(tab)
    about_tab = Frame(tab)
    secret_tab = Frame(tab)

    tab.add(main_tab, text="Main")
    tab.add(about_tab, text="About")
    tab.add(secret_tab, text="Debug")

    # Internal functions
    def time_func():
        # Use recursion to update the time
        local_time = datetime.datetime.today()
        formatted_time = local_time.strftime("%H:%M")
        time_label = Label(main_tab, text=f"Local time = {formatted_time}", font=("Consolas", 10))
        about_tab.after(1000, time_func)
        time_label.place(x=350, y=325)

    def ontop_main_menu():
        global main_menu_ontop_var
        if main_menu_ontop_var is False:
            root.attributes("-topmost", True)
            ontop_main_menu_button.config(relief=SUNKEN)
            main_menu_ontop_var = True
        else:
            root.attributes("-topmost", False)
            ontop_main_menu_button.config(relief=RAISED)
            main_menu_ontop_var = False

    def secret_func():
        # disable the button
        secret_button.config(state=DISABLED, relief=SUNKEN)
        Label(secret_tab, text="I just've told you to not click this ._.", font=("Consolas", 15)).pack(side=TOP)

    # Judul internal menu dan tombol menu utama
    label_title_int = Label(main_tab, text="Trigonoapp", font=("Consolas", 30, "bold"))

    button_table = Button(main_tab, text="Table", font=("Consolas", 25), command=table)
    button_question = Button(main_tab, text="Questions", font=("Consolas", 25), command=questions)
    button_formula = Button(main_tab, text="Formula", font=("Consolas", 25), command=formula)

    about_title_label = Label(about_tab, text="About", font=("Consolas", 30, "bold"))
    about_label = Label(about_tab, font=("Consolas", 10), text="""Trigonoapp was a school math project, made by:
    - Redacted for privacy
    - Redacted for privacy
    
    Special Thanks:
    - Redacted for privacy
    - Redacted for privacy
    - Redacted for privacy""")

    # Secret tab
    secret_button = Button(secret_tab, text="DO NOT CLICK", command=secret_func)

    # Version label
    version_label = Label(about_tab, text="Ver.Beta 1.0", font=("Consolas", 10, "bold"))

    # Ontop button (main menu)
    ontop_main_menu_button = Button(main_tab, text="On Top", command=ontop_main_menu)

    # Pack menu
    tab.pack(expand=True, fill="both")

    label_title_int.pack()
    button_table.pack()
    button_question.pack()
    button_formula.pack()

    about_title_label.pack()
    about_label.pack()
    version_label.pack(side=BOTTOM)
    ontop_main_menu_button.place(x=10, y=320)

    # Pack the button in the middle of the screen
    secret_button.pack(side=BOTTOM, anchor="s", pady=150)

    time_func()

    root.mainloop()


if __name__ == "__main__":
    # init
    main_menu_ontop_var = table_ontop_var = question_ontop_var = formula_ontop_var = quadrant_ontop_var = False
    # main function
    main()
