
# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import random
import os, os.path




print("start")
frames = 100 #animation length
vrange = 0.1 #particle speed


#boundary of box
edges = np.linspace(-1,1,200)
right_edge = np.ones(200)
left_edge = right_edge*-1

#initialisation
t = np.linspace(0,100,frames)
x = np.zeros(frames)
y = np.zeros(frames)
v0 = np.array([random.uniform(-vrange, vrange), random.uniform(-vrange, vrange)])


#velocity flags
last_check_y = 0
last_check_x = 0


#calculating positions and velocities
for i in range(1, frames-1):

    #Stepping through by adding velocity
    x[i] = x[i-1] + v0[0]
    y[i] = y[i-1] + v0[1]

    if np.linalg.norm(x[i]) > 1 and last_check_x >3:
        v0[0] = v0[0]*-1
    if np.linalg.norm(y[i]) > 1 and last_check_y >3:
        v0[1] = v0[1]*-1

    last_check_x += 1
    last_check_y += 1


# %%
#plotting
fig, ax = plt.subplots()
ax.set(xlim=[-2, 2], ylim=[-2, 2], xlabel='x', ylabel='y')
ax.set_aspect("equal")

#object 
particle = ax.plot(x[0],y[0],".")[0]

#boundary
l_border = ax.plot(left_edge,edges,"k")
r_border = ax.plot(right_edge,edges,"k")
u_border = ax.plot(edges,right_edge,"k")
b_border = ax.plot(edges,left_edge,"k")


track = 0
#
def particle_update(frame):

    """
    Updates the particle position.
    
    """

    global track 
    track += 1
    if track %30 == 0:
        print("Animating% :",str((track/frames)*100)[0:4]+"%")
    # for each frame, update the data stored on each artist.
    x_current = x[frame-1:frame]
    y_current = y[frame-1:frame]

    # update position
    particle.set_xdata(x_current)
    particle.set_ydata(y_current)
    
    return (particle)



ani = animation.FuncAnimation(fig=fig, func=particle_update, 
                              frames=frames,
                                interval=1)


#file counter
lst = os.listdir(".\\1particle_gifs") # your directory path
number_files = len(lst)


#saving
ani.save(f"1particle_gifs\\Particle_in_a_box_animation{number_files+1}.gif", fps=30)
print("Saved!")

#plt.show()
