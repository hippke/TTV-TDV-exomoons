"""n-body simulator to derive TDV+TTV diagrams of planet-moon configurations.
Credit for part of the source is given to
https://github.com/akuchling/50-examples/blob/master/gravity.rst
Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
"""

import numpy
import math
import matplotlib.pylab as plt
from modified_turtle import Turtle
from phys_const import *


class Body(Turtle):
    """Subclass of Turtle representing a gravitationally-acting body"""
    name = 'Body'
    vx = vy = 0.0  # velocities in m/s
    px = py = 0.0  # positions in m
    
    def attraction(self, other):
        """(Body): (fx, fy) Returns the force exerted upon this body by the other body"""

        # Distance of the other body
        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox-sx)
        dy = (oy-sy)
        d = math.sqrt(dx**2 + dy**2)

        # Force f and direction to the body
        f = G * self.mass * other.mass / (d**2)  
        theta = math.atan2(dy, dx)  

        # direction of the force
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy

def loop(bodies, orbit_duration):
    """([Body]) Loops and updates the positions of all the provided bodies"""

    # Calculate the duration of our simulation: One full orbit of the outer moon
    seconds_per_day = 24*60*60

    timesteps_per_day = 1000

    timestep = seconds_per_day / timesteps_per_day 
    total_steps = int(orbit_duration / 3600 / 24 * timesteps_per_day)
    #print total_steps, orbit_duration / 24 / 60 / 60

    for body in bodies:
        body.penup()
        body.hideturtle()

    for step in range(total_steps):

        for body in bodies:
            if body.name == 'planet':
                # Add current position and velocity to our list
                tdv_list.append(body.vx)
                ttv_list.append(body.px)
        force = {}
        for body in bodies:
            # Add up all of the forces exerted on 'body'
            total_fx = total_fy = 0.0
            for other in bodies:
                # Don't calculate the body's attraction to itself
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            # Record the total force exerted
            force[body] = (total_fx, total_fy)

        # Update velocities based upon on the force
        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            # Update positions
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            #body.goto(body.px*SCALE, body.py*SCALE)
            #body.dot(3)


def run_sim(R_star, transit_duration, bodies):
    """Run 3-body sim and convert results to TTV + TDV values in [minutes]"""

    # Run 3-body sim for one full orbit of the outermost moon
    loop(bodies, orbit_duration)
    

    # Move resulting data from lists to numpy arrays
    ttv_array = numpy.array([])
    ttv_array = ttv_list
    tdv_array = numpy.array([])
    tdv_array = tdv_list

    # Zeropoint correction
    middle_point =  numpy.amin(ttv_array) + numpy.amax(ttv_array)
    ttv_array = numpy.subtract(ttv_array, 0.5 * middle_point)
    ttv_array = numpy.divide(ttv_array, 1000)  # km/s

    # Compensate for barycenter offset of planet at start of simulation:
    planet.px = 0.5 * (gravity_firstmoon + gravity_secondmoon)
    stretch_factor = 1 / ((planet.px / 1000) / numpy.amax(ttv_array))
    ttv_array = numpy.divide(ttv_array, stretch_factor)

    # Convert to time units, TTV
    ttv_array = numpy.divide(ttv_array, R_star)
    ttv_array = numpy.multiply(ttv_array, transit_duration * 60 * 24)  # minutes

    # Convert to time units, TDV
    oldspeed = (2 * R_star / transit_duration) * 1000 / 24 / 60 / 60  # m/sec
    newspeed = oldspeed - numpy.amax(tdv_array)
    difference = (transit_duration - (transit_duration * newspeed / oldspeed)) * 24 * 60
    conversion_factor = difference / numpy.amax(tdv_array)
    tdv_array = numpy.multiply(tdv_array, conversion_factor)

    return ttv_array, tdv_array



"""Main routine"""

# Set variables and constants. Do not change these!
G = 6.67428e-11  # Gravitational constant G
SCALE = 5e-07  # [px/m] Only needed for plotting during nbody-sim
tdv_list = []
ttv_list = [] 
R_star = 6.96 * 10**5 # [km], solar radius
transit_duration = (2*pi/sqrt(G*(M_sun+M_jup)/a_jup**3)*R_sun/(pi*a_jup)*sqrt((1+R_jup/R_sun)**2))/60/60/24 # transit duration without a moon, Eq. (C1) Kipping (2009b, MNRAS), for q = 0
print transit_duration

planet = Body()
planet.name = 'planet'
planet.mass = M_jup
#semimajor_axis = 1. * AU #[m]
semimajor_axis = a_jup
stellar_mass = M_sun
radius_hill = semimajor_axis * (planet.mass / (3 * (stellar_mass))) ** (1./3)

# Define parameters
firstmoon = Body()
firstmoon.mass = M_gan
firstmoon.px = a_io

secondmoon = Body()
secondmoon.mass = M_gan
secondmoon.px = a_gan

# Calculate start velocities
firstmoon.vy = math.sqrt(G * planet.mass * (2 / firstmoon.px - 1 / firstmoon.px))
secondmoon.vy = math.sqrt(G * planet.mass * (2 / secondmoon.px - 1 / secondmoon.px))
planet.vy = (-secondmoon.vy * secondmoon.mass - firstmoon.vy * firstmoon.mass) / planet.mass

# Calculate planet displacement. This holds for circular orbits
gravity_firstmoon = (firstmoon.mass / planet.mass) * firstmoon.px
gravity_secondmoon = (secondmoon.mass / planet.mass) * secondmoon.px
planet.px = 0.5 * (gravity_firstmoon + gravity_secondmoon)

# Use the outermost moon to calculate the length of one full orbit duration
orbit_duration = math.sqrt((4 * math.pi**2 *secondmoon.px ** 3) / (G * (secondmoon.mass + planet.mass))) 

# Run simulation. Make sure to add/remove the moons you want to simulate!
ttv_array, tdv_array = run_sim(
    R_star, 
    transit_duration, 
    [planet, firstmoon, secondmoon])


# Output information
print 'TTV amplitude =', numpy.amax(ttv_array), \
    '[min] = ', numpy.amax(ttv_array) * 60, '[sec]'
print 'TDV amplitude =', numpy.amax(tdv_array), \
    '[min] = ', numpy.amax(tdv_array) * 60, '[sec]'

ax = plt.axes()
plt.plot(ttv_array, tdv_array, color = 'k')
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
plt.rc('text', usetex=True)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('transit timing variation [minutes]', fontsize = 16)
plt.ylabel('transit duration variation [minutes]', fontsize = 16)
ax.tick_params(direction='out')
plt.ylim([numpy.amin(tdv_array) * 1.2, numpy.amax(tdv_array) * 1.2])
plt.xlim([numpy.amin(ttv_array) * 1.2, numpy.amax(ttv_array) * 1.2])
plt.plot((0, 0), (numpy.amax(tdv_array) * 10., numpy.amin(tdv_array) * 10.), 'k', linewidth=0.5)
plt.plot((numpy.amin(ttv_array) * 10., numpy.amax(ttv_array) * 10.), (0, 0), 'k', linewidth=0.5)

# Fix axes for comparisons
plt.xlim(-0.2, +0.2)
plt.ylim(-0.5, +0.5)
plt.annotate(r"4:1", xy=(-0.19, +0.42), size=16)


plt.savefig("fig_system_4.eps", bbox_inches = 'tight')

