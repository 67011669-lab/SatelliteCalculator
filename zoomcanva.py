import tkinter as tk
import tkinter.messagebox


def zoomin():
    import mymain as m
    if m.orbit_check != None:
     if m.zoomval < 5:
        m.zoomval += 1
        print(m.zoomval)
        # Update coordinates
        
        orbitxc = (m.orbitx1 +m.orbitx2)/2
        orbityc =(m.orbity1 + m.orbity2)/2
        orbitxw = m.orbitx2 - m.orbitx1
        orbityh = m.orbity2 - m.orbity1
        orbitxz = 2 * orbitxw 
        orbityz = 2 * orbityh
        m.orbitx1 = orbitxc - orbitxz/2
        m.orbitx2 = orbitxc + orbitxz/2
        m.orbity1 = orbityc - orbityz/2
        m.orbity2 = orbityc + orbityz/2

        moonxc = (m.moonx1 + m.moonx2)/2 
        moonyc = (m.moony1 + m.moony2)/2
        moonxw = m.moonx2 - m.moonx1 
        moonyh = m.moony2 - m.moony1
        moonxz = 2 * moonxw
        moonyz = 2 * moonyh
        m.moonx1 = moonxc - moonxz/2
        m.moonx2 = moonxc + moonxz/2
        m.moony1 = moonyc - moonyz/2
        m.moony2 = moonyc + moonyz/2
        earthxc = (m.earthx1 + m.earthx2)/2
        earthyc = (m.earthy1 + m.earthy2)/2
        earthxw = m.earthx2 - m.earthx1
        earthyh = m.earthy2 - m.earthy1
        earthxz = 2 * earthxw
        earthyz = 2 * earthyh
        m.earthx1 = earthxc - earthxz/2
        m.earthx2 = earthxc + earthxz/2
        m.earthy1 = earthyc - earthyz/2
        m.earthy2 = earthyc + earthyz/2
        m.w.coords(m.earth_oval,m.earthx1,m.earthy1,m.earthx2,m.earthy2)
        m.w.coords(m.moon_oval,m.moonx1,m.moony1,m.moonx2,m.moony2)
        m.w.coords(m.orbit_oval,m.orbitx1,m.orbity1,m.orbitx2,m.orbity2)
     else:
        tkinter.messagebox.showinfo("Info", "Maximum zoom reached")
    else: 
        tkinter.messagebox.showerror("Error", "Input your satelite value first")


def zoomout():
    import mymain as m
    if m.orbit_check != None:
        if m.zoomval > 0:
            m.zoomval -= 1
            print(m.zoomval)
            # Update coordinates
            orbitxc = (m.orbitx1 +m.orbitx2)/2
            orbityc =(m.orbity1 + m.orbity2)/2
            orbitxw = m.orbitx2 - m.orbitx1
            orbityh = m.orbity2 - m.orbity1
            orbitxz = 0.5 * orbitxw 
            orbityz = 0.5 * orbityh
            m.orbitx1 = orbitxc - orbitxz/2
            m.orbitx2 = orbitxc + orbitxz/2
            m.orbity1 = orbityc - orbityz/2
            m.orbity2 = orbityc + orbityz/2

            moonxc = (m.moonx1 + m.moonx2)/2 
            moonyc = (m.moony1 + m.moony2)/2
            moonxw = m.moonx2 - m.moonx1 
            moonyh = m.moony2 - m.moony1
            moonxz = 0.5 * moonxw
            moonyz = 0.5 * moonyh
            m.moonx1 = moonxc - moonxz/2
            m.moonx2 = moonxc + moonxz/2
            m.moony1 = moonyc - moonyz/2
            m.moony2 = moonyc + moonyz/2
            earthxc = (m.earthx1 + m.earthx2)/2
            earthyc = (m.earthy1 + m.earthy2)/2
            earthxw = m.earthx2 - m.earthx1
            earthyh = m.earthy2 - m.earthy1
            earthxz = 0.5 * earthxw
            earthyz = 0.5 * earthyh
            m.earthx1 = earthxc - earthxz/2
            m.earthx2 = earthxc + earthxz/2
            m.earthy1 = earthyc - earthyz/2
            m.earthy2 = earthyc + earthyz/2
            m.w.coords(m.earth_oval,m.earthx1,m.earthy1,m.earthx2,m.earthy2)
            m.w.coords(m.moon_oval,m.moonx1,m.moony1,m.moonx2,m.moony2)
            m.w.coords(m.orbit_oval,m.orbitx1,m.orbity1,m.orbitx2,m.orbity2)
        else:
                tkinter.messagebox.showinfo("Info", "Minimum zoom reached")
    else: 
        tkinter.messagebox.showerror("Error", "Input your satelite value first")