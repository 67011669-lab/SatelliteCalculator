import tkinter as tk
import math


def hover_moon(event):
   from mymain import r,w,scale,zoomval
   global temp_window
   temp_window = tk.Toplevel(r)
   temp_window.geometry(f"375x50+{event.x+200}+{event.y+100}")  
   temp_window.wm_overrideredirect(True)  
   frame = tk.Frame(temp_window, highlightbackground="blue", highlightthickness=2)
   frame.pack(padx=2, pady=2)
   a=(event.x-375)*scale 
   b=(event.y-275)*scale
   if zoomval > 0:
       a=(event.x-375)*scale / (zoomval*2)
       b=(event.y-275)*scale / (zoomval*2)
   radius_moon = math.sqrt((a**2 + b ** 2))
   label_app = tk.Label(temp_window,text="Approximate distance for center of the Earth to the Moon orbit")
   label_app.pack()
   label_r = tk.Label(temp_window, text=f"{radius_moon:.1f} KM")
   label_r.pack()
   #from center the earth
   global line
   line = w.create_line(event.x,event.y,375,275,fill="Grey")


   

def hide_hover_moon(event):

    from mymain import r,w,scale
    if temp_window:
        temp_window.destroy()
        w.delete(line)


def hover_orbit(event):
   from mymain import r,w,scale,zoomval,orbitx1,orbitx2,orbity1,orbity2
   global temp_window
   temp_window = tk.Toplevel(r)
   temp_window.geometry(f"375x50+{event.x+200}+{event.y+100}")  
   temp_window.wm_overrideredirect(True)  
   frame = tk.Frame(temp_window, highlightbackground="blue", highlightthickness=2)
   frame.pack(padx=2, pady=2)
   a=(event.x-375)*scale 
   b=(event.y-275)*scale
#    if zoomval > 0:
#        a=(event.x-375)*scale / (zoomval*2)
#        b=(event.y-275)*scale / (zoomval*2)
   radius_orb = math.sqrt((a** 2 + b ** 2))
   if 3 > zoomval > 0:
       radius_orb = (math.sqrt((a** 2 + b ** 2)))/(zoomval * 2.0)
   elif zoomval >= 3:
       radius_orb = (math.sqrt((a** 2 + b ** 2)))/(zoomval * 2.0 * 1.32)  
   label_app = tk.Label(temp_window,text="Approximate distance for center of the Earth to the Satelite orbit")
   label_app.pack()
   label_r = tk.Label(temp_window, text=f"{radius_orb:.1f} KM")
   label_r.pack()
   #from center the earth
   global line1
   line1 = w.create_line(event.x,event.y,375,275,fill="Red")

def hide_hover_orbit(event):

    from mymain import r,w,scale
    if temp_window:
        temp_window.destroy()
        w.delete(line1)
     
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
       