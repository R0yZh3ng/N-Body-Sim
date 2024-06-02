from vpython import *

def gravity(planet1, planet2):
    G = 10 #large gravitational constant to make it faster
    radius = planet2.pos - planet1.pos
    distance = max(radius.mag, 1)
    force_magnitude = (G * planet1.mass * planet2.mass) / pow(distance, 2) #Newton forumla for gravitational attraction
    force = (force_magnitude / distance) * radius.norm()
    return force

def update_velocity(planets, dt):
    for i in range(len(planets)):
        total_force = vector(0, 0, 0)
        for j in range(len(planets)):
            if i != j:
                force = gravity(planets[i], planets[j])
                total_force += force
                print(f"Force between planets {i} and {j}: {force}")
        if planets[i].mass != 0:
            planets[i].velocity += total_force / planets[i].mass * dt
        else:
            planets[i].velocity = vector(0,0,0)

def update_pos(planets, dt):
    for planet in planets:
        if planet.velocity == vector(0,0,0):
            pass
        else:
            planet.pos += planet.velocity * dt
            
def update_energies(planets, dt):
    for planet in planets:
        if planet.mass != 0:
            planet.KE += 0.5 * planet.mass * planet.velocity.mag2

        for other_planet in planets:
            radius = other_planet.pos - planet.pos
            distance = max(radius.mag, 1)
            planet.PE -= (10 * planet.mass * other_planet.mass)/pow(distance, 2)
            
def update_momentum(planets, dt):
    for planet in planets:
        planet.LM = planet.mass * planet.velocity.mag
        #planet.AM = planet.mass * p angular momentum in the making
    

vplot = graph(title = 'position.x/time graph', scroll = True, xmin = 0, xmax = 100, align = "left", width = 700)

plotRed = gcurve(graph = vplot, color = color.red, label = "red", dot = True, dot_color = color.red)
plotGreen = gcurve(graph = vplot, color = color.green, label = "green", dot = True, dot_color = color.green)
plotBlue = gcurve(graph = vplot, color = color.blue, label = "blue", dot = True, dot_color = color.blue)
plotYellow = gcurve(graph = vplot, color = color.yellow, label = "yellow", dot = True, dot_color = color.yellow)
plotOrange = gcurve(graph = vplot, color = color.orange, label = "orange", dot = True, dot_color = color.orange)
plotCyan = gcurve(graph = vplot, color = color.cyan, label = "cyan", dot = True, dot_color = color.cyan)
plotMagenta = gcurve(graph = vplot, color = color.magenta, label = "magenta", dot = True, dot_color = color.magenta)
plotBlack = gcurve(graph = vplot, color = color.black, label = "white", dot = True, dot_color = color.black)
    
PEplot = graph(title = 'Potential Enegery/time graph', scroll = True, xmin = 0, xmax = 100, align = "right", width = 700)

PEplotRed = gcurve(graph = PEplot, color = color.red, label = "red", dot = True, dot_color = color.red)
PEplotGreen = gcurve(graph = PEplot, color = color.green, label = "green", dot = True, dot_color = color.green)
PEplotBlue = gcurve(graph = PEplot, color = color.blue, label = "blue", dot = True, dot_color = color.blue)
PEplotYellow = gcurve(graph = PEplot, color = color.yellow, label = "yellow", dot = True, dot_color = color.yellow)
PEplotOrange = gcurve(graph = PEplot, color = color.orange, label = "orange", dot = True, dot_color = color.orange)
PEplotCyan = gcurve(graph = PEplot, color = color.cyan, label = "cyan", dot = True, dot_color = color.cyan)
PEplotMagenta = gcurve(graph = PEplot, color = color.magenta, label = "magenta", dot = True, dot_color = color.magenta)
PEplotBlack = gcurve(graph = PEplot, color = color.black, label = "white", dot = True, dot_color = color.black)

KEplot = graph(title = 'Kinetic Enegery/time graph', scroll = True, xmin = 0, xmax = 100, align = "left", width = 700)

KEplotRed = gcurve(graph = KEplot, color = color.red, label = "red", dot = True, dot_color = color.red)
KEplotGreen = gcurve(graph = KEplot, color = color.green, label = "green", dot = True, dot_color = color.green)
KEplotBlue = gcurve(graph = KEplot, color = color.blue, label = "blue", dot = True, dot_color = color.blue)
KEplotYellow = gcurve(graph = KEplot, color = color.yellow, label = "yellow", dot = True, dot_color = color.yellow)
KEplotOrange = gcurve(graph = KEplot, color = color.orange, label = "orange", dot = True, dot_color = color.orange)
KEplotCyan = gcurve(graph = KEplot, color = color.cyan, label = "cyan", dot = True, dot_color = color.cyan)
KEplotMagenta = gcurve(graph = KEplot, color = color.magenta, label = "magenta", dot = True, dot_color = color.magenta)
KEplotBlack = gcurve(graph = KEplot, color = color.black, label = "white", dot = True, dot_color = color.black)

LMplot = graph(title = 'Linear Momentum/time graph', scroll = True, xmin = 0, xmax = 100, align = "right", width = 700)

LMplotRed = gcurve(graph = LMplot, color = color.red, label = "red", dot = True, dot_color = color.red)
LMplotGreen = gcurve(graph = LMplot, color = color.green, label = "green", dot = True, dot_color = color.green)
LMplotBlue = gcurve(graph = LMplot, color = color.blue, label = "blue", dot = True, dot_color = color.blue)
LMplotYellow = gcurve(graph = LMplot, color = color.yellow, label = "yellow", dot = True, dot_color = color.yellow)
LMplotOrange = gcurve(graph = LMplot, color = color.orange, label = "orange", dot = True, dot_color = color.orange)
LMplotCyan = gcurve(graph = LMplot, color = color.cyan, label = "cyan", dot = True, dot_color = color.cyan)
LMplotMagenta = gcurve(graph = LMplot, color = color.magenta, label = "magenta", dot = True, dot_color = color.magenta)
LMplotBlack = gcurve(graph = LMplot, color = color.black, label = "white", dot = True, dot_color = color.black)