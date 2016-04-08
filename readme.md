# Predictable patterns in planetary transit timing variations and transit duration variations due to exomoons

*If you make use of this code, please cite this repository in combination with our paper*

*René Heller, Michael Hippke, Ben Placek, Daniel Angerhausen, and Eric Agol*

## Tutorial

### Define parameters
```python
planet.mass = M_jup
semimajor_axis = a_jup
stellar_mass = M_sun

firstmoon = Body()
firstmoon.mass = M_gan
firstmoon.px = a_io

secondmoon = Body()
secondmoon.mass = M_gan
secondmoon.px = a_eur
```

### Calculate initial conditions
```python
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
```

### Run the simulation
```python
ttv_array, tdv_array = run_sim(
    R_star, 
    transit_duration, 
    [planet, firstmoon, secondmoon])
```    

### Show results
````python
print 'TTV amplitude =', numpy.amax(ttv_array), \
    '[min] = ', numpy.amax(ttv_array) * 60, '[sec]'
print 'TDV amplitude =', numpy.amax(tdv_array), \
    '[min] = ', numpy.amax(tdv_array) * 60, '[sec]'
plt.plot(ttv_array, tdv_array, color = 'k')
```
