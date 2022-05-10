from tkinter import *
root = Tk()
root.geometry("700x500")
root.configure(background = 'cyan')
root.title("Profit")


month = ('Janurary', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

profit = (10000, 20000, 50000, 2046385, 65964749, 53947353, 27364, 4638, 77728374293, 1000000, 836596586, 384737 )



#labels

month_label = Label(root, text = str(month))
month_label.place(relx = 0.5, rely = 0.2, anchor = CENTER)

profit_label = Label(root, text = str(profit))
profit_label.place(relx = 0.5, rely = 0.3, anchor = CENTER)

label_max_profit = Label(root)
label_max_profit.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label_min_profit = Label(root)
label_min_profit.place(relx = 0.5, rely = 0.7, anchor = CENTER)


def max_profit():
    max_profit = max(profit)
    max_profit_index = profit.index(max_profit)
    print(max_profit_index)

    max_month = month[max_profit_index]
    print("The Maximum Profit of " + str(max_profit) + " Was Recorded in the Month of " + max_month)
    
    label_max_profit["text"] = "The Maximum Profit of " + str(max_profit) + " Was Recorded in the Month of " + max_month


def min_profit():
    min_profit = min(profit)
    min_profit_index = profit.index(min_profit)
    print(min_profit_index)

    min_month = month[min_profit_index]
    print("The Minimum Profit of " + str(min_profit) + " Was Recorded in the Month of " + min_month)
    label_min_profit["text"] = "The Minimum Profit of " + str(min_profit) + " Was Recorded in the Month of " + min_month
    
btn1 = Button(root, text = "Show Max Profitable Month", command = max_profit, bg = 'gold')
btn1.place(relx = 0.5, rely = 0.4 , anchor = CENTER)
btn2 = Button(root, text = "Show Min Profitable Month", command = min_profit, bg = 'gold')
btn2.place(relx = 0.5, rely = 0.6 , anchor = CENTER)



root.mainloop()