from vpython import *
from Planet import Planet
from forces import *

scene = canvas(width=850, height=500, resizable=True, align = "left")
scene.autoscale = True
range = scene.range

red = Planet(color=color.red, 
            mass=5, 
            radius=0.75, 
            pos=vector(0, 0, 0), 
            initial_pos=vector(0, 0, 0), 
            make_trail= True, 
            retain = 1000,
            visible = True,
            ambient = color.red)

green = Planet(color=color.green,
            mass=4, 
            radius=0.5, 
            pos=vector(5, 5, 0), 
            initial_pos=vector(5, 5, 0), 
            make_trail= True, 
            retain = 1000,
            visible = True,
            ambient = color.green)

blue = Planet(color=color.blue, 
            mass=6, 
            radius=0.4, 
            pos=vector(5, -5, 0), 
            initial_pos=vector(5, -5, 0), 
            make_trail= True, 
            retain = 1000,
            visible = True,
            ambient = color.blue)

yellow = Planet(color=color.yellow,
                mass=7, 
                radius=0.6, 
                pos=vector(-5, -5, 0), 
                initial_pos=vector(-5, -5, 0), 
                make_trail= True, 
                retain = 1000,
                visible = True,
                ambient = color.yellow)

orange = Planet(color=color.orange, 
                mass=10, 
                radius=0.8, 
                pos=vector(-10, -5, 0),
                initial_pos=vector(-10, -5, 0), 
                make_trail= True,
                retain = 1000, 
                visible = True,
                ambient = color.orange)

cyan = Planet(color=color.cyan, 
            mass=12, 
            radius=0.9, 
            pos=vector(3, -5, 3), 
            initial_pos=vector(3, -5, 3),
            make_trail= True, 
            retain = 1000,
            visible = True,
            ambient = color.cyan)

magenta = Planet(color=color.magenta, 
                mass=2, 
                radius=0.2, 
                pos=vector(0, -5, -3), 
                initial_pos=vector(0, -5, -3), 
                make_trail= True, 
                retain = 1000,
                visible = True,
                ambient = color.magenta)

white= Planet(color=color.white, 
            mass=6, 
            radius=0.25, 
            pos=vector(1, -5, -6), 
            initial_pos=vector(1, -5, -6), 
            make_trail= True, 
            retain = 1000,
            visible = True,
            ambient = color.white)


planets = [red, green, blue, yellow, orange, cyan, magenta, white]

def Run(button):
    global running
    running = not running
    if running: button.text = "Pause"
    else: button.text = "Run"
    
runButton = button(text = "Run", pos = scene.title_anchor, bind=Run)

def Reset():
    for planet in planets:
        planet.pos = planet.initial_pos
        planet.velocity = vector(0, 0, 0)
        planet.clear_trail()  
    
    scene.range = range + 10
    scene.autoscale = True
    scene.center = vector(0,0,0)
    
    
    plotRed.delete()
    plotGreen.delete()
    plotBlue.delete()
    plotYellow.delete()
    plotOrange.delete()
    plotCyan.delete()
    plotMagenta.delete()
    plotBlack .delete()
        
    PEplotRed.delete()
    PEplotGreen.delete()
    PEplotBlue.delete()
    PEplotYellow.delete()
    PEplotOrange.delete()
    PEplotCyan.delete()
    PEplotMagenta.delete()
    PEplotBlack .delete()
        
    KEplotRed.delete()
    KEplotGreen.delete()
    KEplotBlue.delete()
    KEplotYellow.delete()
    KEplotOrange.delete()
    KEplotCyan.delete()
    KEplotMagenta.delete()
    KEplotBlack .delete()
        
    LMplotRed.delete()
    LMplotGreen.delete()
    LMplotBlue.delete()
    LMplotYellow.delete()
    LMplotOrange.delete()
    LMplotCyan.delete()
    LMplotMagenta.delete()
    LMplotBlack .delete()
    
    global time
    time = 0
        
resetButton = button(text = "Reset",pos = scene.title_anchor, bind = Reset)

scene.append_to_caption('   Please select a Planet in the drop down to edit values')

def Speed(num):
    global dt
    dt = num.value/100

scene.append_to_caption('\n\n')
scene.append_to_caption('   Adjust speed')
speed = slider(bind = Speed, min = 1, max = 100, step = 1, value = 30)

def change(option):
    if option.selected == "red":
        view(red)
        
    elif option.selected == "green":
        view(green)

    elif option.selected == "blue":
        view(blue)
        
    elif option.selected == "yellow":
        view(yellow)
        
    elif option.selected == "orange":
        view(orange)
    
    elif option.selected == "cyan":
        view(cyan)
        
    elif option.selected == "magenta":
        view(magenta)
        
    elif option.selected == "white":
        view(white)
        
    
edit_select = menu(bind = change, choices = ['Choose','red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'magenta', 'white'])
gui_elements = []

def view(Planet):
    clear_gui()
    
    if Planet.color == vector(1,0,0):
        current = "red"
    
    elif Planet.color == vector(0,1,0):
        current = "green"
        
    elif Planet.color == vector(0,0,1):
        current = "blue"
        
    elif Planet.color == vector(1,1,0):
        current = "yellow"
        
    elif Planet.color == vector(1,0.6,0):
        current = "orange"
        
    elif Planet.color == vector(0,1,1):
        current = "cyan"
        
    elif Planet.color == vector(1,0,1):
        current = "magenta"
        
    elif Planet.color == vector(1,1,1):
        current = "white"
        
        
    if "speed" not in locals():
        scene.append_to_caption('\n\n')
        scene.append_to_caption('   Adjust speed')
        speed = slider(bind=Speed, min=1, max=100, step=1, value=30)
        gui_elements.append(speed)

    if "edit_select" not in locals():
        edit_select = menu(bind=change, choices=['choose', 'red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'magenta', 'white'])
        gui_elements.append(edit_select)
    
    scene.append_to_caption('\n\n')
    scene.append_to_caption("   Currently editing: " + current)

    def init_pos_x(x):
        Planet.initial_pos.x = x.number
        Planet.pos.x = Planet.initial_pos.x
    scene.append_to_caption('\n\n')
    scene.append_to_caption('   init X: ')
    new = winput( bind=init_pos_x, text = "initial x pos", type = "numeric")
    
    def init_pos_y(y):
        Planet.initial_pos.y = y.number
        Planet.pos.y = Planet.initial_pos.y
    scene.append_to_caption('\n\n')
    scene.append_to_caption('   init Y: ')
    new2 = winput( bind=init_pos_y, text = "initial y pos", type = "numeric")
    
    def init_pos_z(z):
        Planet.initial_pos.z = z.number
        Planet.pos.z = Planet.initial_pos.z
    scene.append_to_caption('\n\n')
    scene.append_to_caption('   init Z: ')
    new3 = winput( bind=init_pos_z, text = "initial z pos", type = "numeric")
    scene.append_to_caption('\n\n')
    
    def Pos_x(x):
        Planet.pos.x = x.value
    scene.append_to_caption('\n\n')
    scene.append_to_caption('   X: ')
    new4 = slider( bind=Pos_x, min=-10, max=10, step=0.001, value=0)
    scene.append_to_caption('\n\n')
    
    def Pos_y(y):
        Planet.pos.y = y.value
    scene.append_to_caption('   Y: ')
    new5 = slider( bind=Pos_y, min=-10, max=10, step=0.001, value=0)
    scene.append_to_caption('\n\n')
    
    def Pos_z(z):
        Planet.pos.z = z.value
    scene.append_to_caption('   Z: ')
    new6 = slider( bind=Pos_z, min=-10, max=10, step=0.001, value=0)
    scene.append_to_caption('\n\n')
    
    def radius(rad):
        Planet.radius = rad.value
    scene.append_to_caption('   Radius:')
    new7 = slider( bind = radius, min= 1, max = 10, step = 1, value = Planet.radius)
    scene.append_to_caption('\n\n')
    
    def mass(mass):
        Planet.mass = mass.value
    scene.append_to_caption('   Mass:')
    new8 = slider( bind = mass, min= 1, max = 100, step = 1, value = Planet.mass)
    scene.append_to_caption('\n\n')
    
    def follow(cam):
        kam = cam.checked
        if kam:
            scene.camera.follow(Planet)
    new9 = checkbox(bind = follow, text = '   Cam follow')
    
    def trail(t):
        Planet.make_trail != t.checked
    new10 = checkbox(bind = trail,text = '   Disable Trail effect')
    
    
    def active(a):
        if a.checked:
            Planet.visible = False
            Planet.mass = 0
            
        else:
            Planet.mass = 1
            Planet.visible = True
        
    new11 = checkbox (bind = active, text = '   Disable planet')
    
    gui_elements.extend([new, new2, new3, new4, new5, new6, new7, new8, new9, new10, new11])
    
    
def clear_gui():
    global gui_elements
    element_stay = [speed, edit_select]

    for element in gui_elements:
        if element not in element_stay:
            element.delete()
        

    gui_elements = []
    scene.caption = ""
    


running = False

dt = 0.01 
time = 0
while True:
    if running:
        update_velocity(planets, dt)
        update_pos(planets, dt)
        print(red.pos, 
            green.pos, 
            blue.pos,
            yellow.pos,
            orange.pos,
            cyan.pos,
            magenta.pos,
            white.pos,)
        
        update_energies(planets, dt)
        update_momentum(planets, dt)
        
        plotRed.plot(time,red.pos.x)
        plotGreen.plot(time, green.pos.x)
        plotBlue.plot(time, blue.pos.x)
        plotYellow.plot(time, yellow.pos.x)
        plotOrange.plot(time, orange.pos.x)
        plotCyan.plot(time, cyan.pos.x)
        plotMagenta.plot(time, magenta.pos.x)
        plotBlack .plot(time, white.pos.x)
        
        PEplotRed.plot(time,red.PE)
        PEplotGreen.plot(time, green.PE)
        PEplotBlue.plot(time, blue.PE)
        PEplotYellow.plot(time, yellow.PE)
        PEplotOrange.plot(time, orange.PE)
        PEplotCyan.plot(time, cyan.PE)
        PEplotMagenta.plot(time, magenta.PE)
        PEplotBlack .plot(time, white.PE)
        
        KEplotRed.plot(time,red.KE)
        KEplotGreen.plot(time, green.KE)
        KEplotBlue.plot(time, blue.KE)
        KEplotYellow.plot(time, yellow.KE)
        KEplotOrange.plot(time, orange.KE)
        KEplotCyan.plot(time, cyan.KE)
        KEplotMagenta.plot(time, magenta.KE)
        KEplotBlack .plot(time, white.KE)
        
        LMplotRed.plot(time,red.LM)
        LMplotGreen.plot(time, green.LM)
        LMplotBlue.plot(time, blue.LM)
        LMplotYellow.plot(time, yellow.LM)
        LMplotOrange.plot(time, orange.LM)
        LMplotCyan.plot(time, cyan.LM)
        LMplotMagenta.plot(time, magenta.LM)
        LMplotBlack .plot(time, white.LM)
        
        time += 0.01    
        rate(speed.value)
