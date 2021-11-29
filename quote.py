from tkinter import*
Root =Tk()
Root.geometry = ("400×400")
# Root.maxsize(1500,1200)
Root.title("Motivational Quotes For Women")
Label1= Label(text="Beauty is not about a pretty face, it's about a pretty mind and pretty soul."
,font="comicsansms 18 bold", bg= "red" , fg="white", padx= 9, pady= 9)
Label2= Label(text="You are who you are, and nothing can change that. You're beautiful just as you are."
,font="comicsansms 18 bold", bg= "purple" , fg="white", padx= 9, pady= 9)
Label3= Label(text="Don't be afraid. Be focused. Be determined. Be hopeful. Be empowered."
,font="comicsansms 18 bold", bg= "yellow" , fg="black", padx= 9, pady= 9)
Label4= Label(text="There is no limit to what we, as women, can accomplish."
,font="comicsansms 18 bold" , bg= "cyan" , fg="white", padx= 9, pady= 9)
Label5= Label(text="Never apologize for being a powerful woman."
,font="comicsansms 18 bold", bg= "red" , fg="white", padx= 9, pady= 9)
Label6= Label(text="Each time a woman stands up for herself, she stands up for all women."
,font="comicsansms 18 bold", bg= "purple" , fg="white", padx= 9, pady= 9)
Label7= Label(text="A woman is the full circle. Within her is the power to create, nurture and transform."
,font="comicsansms 18 bold", bg= "yellow" , fg="black", padx= 9, pady= 9)
Label8= Label(text="She was powerful not because she wasn’t scared but because she went on so strongly, despite the fear."
,font="comicsansms 18 bold" , bg= "cyan" , fg="white", padx= 9, pady= 9)
Label9= Label(text="One of the most courageous things you can do is identify yourself, know who you are, what you believe in and where you want to go."
,font="comicsansms 18 bold", bg= "red" , fg="white", padx= 9, pady= 9)
Label10= Label(text="Once you figure out what respect tastes like, it tastes better than attention."
,font="comicsansms 18 bold", bg= "purple" , fg="white", padx= 9, pady= 9)
Label11= Label(text="You have to have confidence in your ability, and then be tough enough to follow through."
,font="comicsansms 18 bold", bg= "yellow" , fg="black", padx= 9, pady= 9)
Label12= Label(text="There is no limit to what we, as women, can accomplish."
,font="comicsansms 18 bold" , bg= "cyan" , fg="white", padx= 9, pady= 9)


photo = PhotoImage(file="beauty.png")
photo_label = Label(image=photo , height=500 , width=500 )
photo_label.pack(side = "bottom",anchor="s")

Label1.pack()
Label2.pack()
Label3.pack()
Label4.pack()
Label5.pack()
Label6.pack()
Label7.pack()
Label8.pack()
Label9.pack()
Label10.pack()
Label11.pack()
Label12.pack()

Root.mainloop()