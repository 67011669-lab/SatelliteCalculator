import tkinter as tk
from PIL import Image, ImageTk
import math 
import tkinter.messagebox

import hover
import zoomcanva

G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24     # Mass of the Earth (kg)
R_E = 6.371e6    # Radius of the Earth (m)


class first:
    def __init__(self):
        r.withdraw()
        global tki
        tki = tk.Toplevel(r)
        tki.title('Satellite Calculator Program')
        tki.geometry("1000x600")
        tki.minsize(1000, 600)
        tki.maxsize(1000, 600)
        tki.config(cursor="plus")

        # Creating a canvas
        # Scale 
        global scale
        scale = 375 * 4
        self.w = tk.Canvas(tki, width=750, height=550, bg="black")
        global w
        w = self.w
        w.grid(row=0, column=3, columnspan=10, rowspan=20, padx=50, pady=20, sticky="E")
        global earthx1
        earthx1 = (-6371/scale)+375
        global earthy1
        earthy1 = (-6371/scale)+275
        global earthx2
        earthx2 = (6371/scale)+375
        global earthy2
        earthy2 =(6371/scale)+275
        global earth_oval
        earth_oval = w.create_oval(earthx1,earthy1,earthx2,earthy2,fill="Blue")
        #moon orbit
        global moonx1
        moonx1 = (-405400/scale)+375
        global moony1
        moony1 = (-363229/scale)+275
        global moonx2
        moonx2 = (405400/scale)+375
        global moony2
        moony2 = (363229/scale)+275
        global moon_oval
        moon_oval = w.create_oval(moonx1,moony1,moonx2,moony2,outline="Grey")
        global zoomval 
        zoomval = 0
        w.tag_bind(moon_oval,"<ButtonPress-1>",hover.hover_moon)
        w.tag_bind(moon_oval,"<ButtonRelease-1>",hover.hide_hover_moon)
        
        zoomiconp= tk.PhotoImage(file="zoomiconp.png")
        zoombuttonp = tk.Button(tki,image=zoomiconp,width=30,height=30,command=zoomcanva.zoomin,bd=2)
        zoombuttonp.place(x=905,y=520)
        zoomiconn= tk.PhotoImage(file="zoomiconn.png")
        zoombuttonn = tk.Button(tki,image=zoomiconn,width=30,height=30,command=zoomcanva.zoomout,bd=2)
        zoombuttonn.place(x=945,y=520)

    
        value_input = tk.Button(tki, text="Calculation input", width=20, height=2, command=value)
        value_input.grid(column=0, row=0, sticky="W", pady=2, rowspan=1, columnspan=2, padx=5)
        
        global op_var
        op_var = tk.StringVar()
        global ov_var
        ov_var = tk.StringVar()
        global ec_var
        ec_var = tk.StringVar()
        global ev_var
        ev_var = tk.StringVar()

       

        Label = tk.Label(tki, text="Orbital Period On Average (hrs): ")
        Label.grid(column=0, row=1, sticky="W", padx=3, pady=2)
        Label1 = tk.Label(tki, text="Average Orbital Velocity (km/s): ")
        Label1.grid(column=0, row=2, sticky="W", padx=3, pady=2)
        Label2 = tk.Label(tki, text="Eccentricity: ")
        Label2.grid(column=0, row=3, sticky="W", padx=3, pady=2)
        Label3 = tk.Label(tki, text="Average Escspe Velocity (km/s): ")
        Label3.grid(column=0, row=4, sticky="W", padx=3, pady=2)
  


        periodlabel = tk.Label(tki, textvariable=op_var)
        periodlabel.grid(column=1, row=1, sticky="W", pady=2)

        orbitallabel = tk.Label(tki, textvariable=ov_var)
        orbitallabel.grid(column=1, row=2, sticky="W" ,pady=2)

        altitudelabel = tk.Label(tki, textvariable=ec_var)
        altitudelabel.grid(column=1, row=3, sticky="W",pady=2)
        
        escapelabel = tk.Label(tki,textvariable=ev_var)
        escapelabel.grid(column=1,row=4,sticky="W",pady=2)



        tki.protocol("WM_DELETE_WINDOW", r.destroy)

        tki.mainloop()


orbit_check = None    
class value:
    def __init__(self):
        tki1 = tk.Toplevel(r)
        tki1.title("Input Value For Calculations")
        tki1.geometry("500x400")
        tki1.maxsize(500,400)
        
        Label_Long = tk.Label(tki1,text="Longest Radius Of Your Satelite Orbit (APHELION)(km)")
        Label_Long.grid(column=0,row=0)

        Label_Short = tk.Label(tki1,text="Shortest Radius Of Your Satelite Orbit (PERIHELION)(km)")
        Label_Short.grid(column=0,row=2)

        Label_Ratio = tk.Label(tki1,text="Ratio Between Aphelion and Perihelion (Your Can Enter The Lenth -1 to 1)")
        Label_Ratio.grid(column=0,row=4)

        Label_Ratio0 = tk.Label(tki1,text="(Input > 0: Right Side - Input < 0 :Left Side)")
        Label_Ratio0.grid(column=0,row=5)

        Label_Ratio1 = tk.Label(tki1,text="(0: Same Distance From Both Sides)")
        Label_Ratio1.grid(column=0,row=6)
        
        
        global number_long
        number_long = tk.IntVar()
        Entry_Long = tk.Entry(tki1,textvariable = number_long)
        Entry_Long.grid(column=0,row=1,sticky ="W", pady = 2)
        
        global number_short
        number_short = tk.IntVar()
        Entry_Long = tk.Entry(tki1,textvariable = number_short)
        Entry_Long.grid(column=0,row=3,sticky ="W", pady = 2)
 
        global number_ratio
        number_ratio = tk.DoubleVar()
        Entry_Long = tk.Entry(tki1,textvariable = number_ratio)
        Entry_Long.grid(column=0,row=7,sticky ="W", pady = 2)


        Enter = tk.Button(tki1,text="Enter the value",width=15,height=2,command=lambda: [self.get(),tki1.withdraw()])
        Enter.grid(column=0,row=8,sticky ="W", pady = 2)
        
        tki1.mainloop()
        
    def get(self):
        
      if zoomval == 0:
        global orbit_check
        global orbit_oval
        if orbit_check == None:
          pass
        elif orbit_check == 1:
          w.delete(orbit_oval)
          orbit_check = None
          
        radius_long = number_long.get()/scale
        radius_short = number_short.get()/scale
        if radius_long <= 0 or radius_short <= 0:
         tkinter.messagebox.showerror("Error","Radius should not be zero or negative")
        elif radius_long < radius_short:
         tkinter.messagebox.showerror("Error","Apohelion values should more than Perilion values") 
        

        elif -1 <= number_ratio.get() <= 1:
            orbit_check = 1
            global orbitx1
            orbitx1 = -radius_long+(-radius_long*-(number_ratio.get()))+375
            global orbity1 
            orbity1 = (-radius_short)+275
            global orbitx2
            orbitx2 = radius_long+(-radius_long*-(number_ratio.get()))+375
            global orbity2
            orbity2 = (radius_short)+275
            orbit_oval = w.create_oval(orbitx1,orbity1,orbitx2,orbity2,outline="Red")
            w.tag_bind(orbit_oval,"<ButtonPress-1>",hover.hover_orbit)
            w.tag_bind(orbit_oval,"<ButtonRelease-1>",hover.hide_hover_orbit)
          
            try:
              radius_short_m = number_short.get() *1000
              radius_long_m = number_long.get()*1000
              av_radius = (radius_long_m + radius_short_m)/2
              eccentricity = (radius_long_m - radius_short_m) / (radius_long_m + radius_short_m)
              av_orbital_velocity = math.sqrt(G * M / av_radius)/1000
              av_orbital_period = (2 * math.pi * math.sqrt(av_radius ** 3 / (G * M)))/3600 
              av_escape_velocity = math.sqrt(2*G * M / av_radius)/1000
              op_var.set(f"{av_orbital_period:.2f}")
              ov_var.set(f"{av_orbital_velocity:.2f}")
              ec_var.set(f"{eccentricity:.2f}")
              ev_var.set(f"{av_escape_velocity:.2f}")
            except ZeroDivisionError:
              pass
            except UnboundLocalError:
              pass
        
        else:
         tkinter.messagebox.showerror("Error","Ratio only can be input in length from -1 to 1")
         print("pass")
         pass
      else:
          tkinter.messagebox.showerror("Info","Zoomout until minimum first before creating new orbit")

        
r = tk.Tk()
r.geometry("400x400")
r.minsize(400,400)
r.maxsize(400,400)
r.title('Satelite Calculator Program')
imgbirb=ImageTk.PhotoImage(file="image1.png")
birb = tk.Label(image=imgbirb)
birb.place(x=150, y=125)
button_start = tk.Button(r,text="Start", width=20, command=first)
button_exit = tk.Button(r, text='Exit', width=20, command=r.destroy)

button_start.pack(padx=100,pady=75)
button_exit.pack(padx=100,pady=90)

r.mainloop()


        





