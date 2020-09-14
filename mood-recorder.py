# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:23:28 2020

@author: divya
"""
'''
This is a simple mood recorder based on Python Tkinter for GUI and popular libraries including pandas and matplotlib, to generate simple bar charts and  pie charts to track one's 'mood'. 
I created this tool to aid my therapy sessions which required me to log my mood everyday, and report it to my therapist.
'''

import tkinter
import csv
import pandas as pd
import matplotlib.pyplot as plt
import datetime 


# record moood data into a csv file
def record_mood():
    out_label = tkinter.Label(window, text='')
    print('success')
    df = pd.read_csv('moods.csv')
    if df.empty:
         out_label = tkinter.Label(window, text='Add a new day!')

    with open('moods.csv', 'a', newline='') as file:
        writer = csv.writer(file)                   
        writer.writerow([input_widget.get().lower()])
        out_label = tkinter.Label(window, text='Mood recorded!')
        out_label.pack()

    file.close()
        
# keeps data for only 1 day, deletes previous data        
def new_day():     
    file = open('moods.csv', 'w')
    file.truncate()
    writer = csv.DictWriter(file, fieldnames=['Mood'])
    writer.writeheader()   
    file.close()
        
# retrieve data and plot pie     
def generate_pie():    
    
    # pie chart name 
    fname = datetime.datetime.now().strftime('%b %d, %Y')    
    filename = '\{}.png'.format(fname)
    
    # generate pie chart
    df = pd.read_csv('moods.csv')
    labels = df['Mood'].unique()
    plt.pie(df['Mood'].value_counts(), autopct='%1.1f%%')
    plt.title('Mood chart for ' + str(fname) + ' with ' + str(len(df.index)) + ' Entries')
    plt.legend(labels, loc='best')
    plt.axis('equal')
    plt.tight_layout()
    
    # pie chart save directory    
    save_results_to = r'\Users\Divya Rustagi\Desktop\Jobs and Internships\mood-recorder\mood-recorder\generated-pie-charts'  
           
    # save pie chart       
    plt.savefig(save_results_to + filename, dpi=300)
    plt.show()
        
def generate_bar():    
    
    # bar chart name 
    fname = datetime.datetime.now().strftime('%b %d, %Y')    
    filename = '\{} Bars.png'.format(fname)
    
    # generate bar chart
    df = pd.read_csv('moods.csv')
    
        
    df['Mood'].value_counts().plot(kind='barh')
    plt.ylabel('Moods')
    plt.xlabel('Percentage')
    plt.title('Mood chart for ' + str(fname) + ' with ' + str(len(df.index)) + ' Entries')
       
    # bar chart save directory    
    save_results_to = r'\Users\Divya Rustagi\Desktop\Jobs and Internships\mood-recorder\mood-recorder\generated-bar-charts'  
           
    # save bar chart       
    plt.savefig(save_results_to + filename, dpi=300)
    plt.show()
        
    
# GUI elements    
window = tkinter.Tk()
window.title("Mood Recorder")

# pack is used to show the object in the window
label = tkinter.Label(window, text = "Hi, Divya. How are you feeling today?")
record_widget = tkinter.Button(window,text="Record", command=record_mood)
newDay_widget = tkinter.Button(window,text="New Day", command=new_day)
pie_widget = tkinter.Button(window, text='Generate Pie', command=generate_pie)
bar_widget = tkinter.Button(window, text='Generate Bars', command=generate_bar)
input_widget = tkinter.Entry(window)


# interface layout
label.pack()
input_widget.pack()
record_widget.pack(padx=5, pady=10, side=tkinter.LEFT)
pie_widget.pack(padx=5, pady=20, side=tkinter.LEFT)
bar_widget.pack(padx=5, pady=20, side=tkinter.LEFT)
newDay_widget.pack(padx=5, pady=20, side=tkinter.LEFT)

window.mainloop()


