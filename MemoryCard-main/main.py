from PyQt5.QtCore import*
from PyQt5.QtWidgets import*



app=QApplication([])

from main_window import*
from menu_window import*
from random import shuffle

text_wrong='Неправильно'
text_correct='Правильно'


from_qs='Ябдуко'
from_r='apple'
from_wrong1='application'
from_wrong2='building'
from_wrong3='caterpillar'

rbtn_list=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]
shuffle(rbtn_list)
answer=rbtn_list[0]

wrong_answer1,wrong_answer2,wrong_answer3=rbtn_list[1],rbtn_list[2],rbtn_list[3]

def show_data():
    lb_Question.setText(from_qs)
    lb_Correct.setText(from_r)
    answer.setText(from_r)
    wrong_answer1.setText(from_wrong1)
    wrong_answer2.setText(from_wrong2)
    wrong_answer3.setText(from_wrong3)

def check_result():
    correct=answer.isChecked()
    if correct:
        lb_Result.setText(text_correct)
        show_result()
    else:
        incorrect=wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
    if incorrect:
        lb_Result.setText(text_wrong)
        show_result()
def click_OK():
    if btn_OK.text()!=' наступне питання':
        ckeck_result()


btn_OK.clicked.connect(click_OK)

show_data()
show_question()

app.exec_()