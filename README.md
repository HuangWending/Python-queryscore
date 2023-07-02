# Python-queryscore
Python考生考试成绩查询程序
import tkinter as tk
from tkinter import messagebox

scoreDict = {
    "yangkao1": {
        "数学": 0, "语文": 0, "英语": 0, "政治": 0, "物理": 0,
        "化学": 0, "生物": 0, "地理": 0, "历史": 0
    },
    "huangkao1": {
        "数学": 95, "语文": 80, "英语": 100, "政治": 69, "物理": 90,
        "化学": 100, "生物": 100, "地理": 100, "历史": 50
    }
}
导入Tkinter库，并导入messagebox模块。

创建一个字典scoreDict，包含两个考生的姓名和对应的科目分数
def display_scores(name, number):
    if number in scoreDict:
        scores = scoreDict[number]
        total_score = sum(scores.values())
        score_text = f"考生姓名: {name}\n考生号码: {number}\n\n科目成绩表格:\n"
        score_text += "-------------------------\n"
        for subject, score in scores.items():
            score_text += f"{subject}: {score}\n"
        score_text += "-------------------------\n"
        score_text += f"总分数: {total_score}\n\n"
        score_text += f"版权信息: ©黄文定政府教育部考试成绩查询系统-考生{name}-Ⓥ黄文定2009-2023"
        messagebox.showinfo("成绩查询结果", score_text)
    else:
        messagebox.showwarning("错误", "未找到对应考生信息")
定义一个函数display_scores，接受考生的姓名和号码作为参数。

如果输入的号码存在于scoreDict中，获取对应的科目分数，并计算总分。然后构建一个字符串score_text，显示考生的姓名、号码以及科目分数表格。

如果输入的号码不存在于scoreDict中，弹出一个警告对话框，显示未找到对应考生信息的错误提示。
def on_confirm():
    name = name_entry.get()
    number = number_entry.get()
    display_scores(name, number)
定义一个函数on_confirm，在用户点击确认按钮时调用。

从姓名输入框和号码输入框中获取对应的文本值，并调用display_scores函数显示分数。
window = tk.Tk()
window.title("考试科目分数查询程序")
window.geometry("400x400")
创建一个窗口对象window，设置窗口的标题为"考试科目分数查询程序"，大小为400x400。
name_label = tk.Label(window, text="考生姓名")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

number_label = tk.Label(window, text="考生号码")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()
创建两个标签和两个输入框，分别用于显示和输入考生的姓名和号码。

将标签和输入框打包，并显示在窗口中。
confirm_button = tk.Button(window, text="确定", command=on_confirm)
confirm_button.pack()
创建一个确认按钮，文本为"确定"，点击按钮时调用on_confirm函数。

将按钮打包，并显示在窗口中。
copyright_label = tk.Label(
    window, text="©黄文定政府教育部考试成绩查询系统-Ⓥ黄文定-2009-2023", anchor="center")
copyright_label.pack()
创建一个版权信息的标签，显示版权相关的文本。

将标签打包，并显示在窗口中。
window.mainloop()
进入窗口的主循环，等待用户交互。
