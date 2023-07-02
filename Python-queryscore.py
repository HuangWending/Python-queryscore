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

def on_confirm():
    name = name_entry.get()
    number = number_entry.get()
    display_scores(name, number)

# 创建窗口
window = tk.Tk()
window.title("考试科目分数查询程序")
window.geometry("400x400")

# 创建输入框和标签
name_label = tk.Label(window, text="考生姓名")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

number_label = tk.Label(window, text="考生号码")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()

# 创建确定按钮
confirm_button = tk.Button(window, text="确定", command=on_confirm)
confirm_button.pack()

# 显示版权信息
copyright_label = tk.Label(
    window, text="©黄文定政府教育部考试成绩查询系统-Ⓥ黄文定-2009-2023", anchor="center")
copyright_label.pack()

# 运行程序
window.mainloop()
