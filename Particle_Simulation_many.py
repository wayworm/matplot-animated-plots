
# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import random
import os

frames = 1000
N = 5000
vrange = 0.1


#Boundaries
edges = np.linspace(-1,1,200)
right_edge = np.ones(200)
left_edge = right_edge*-1

t = np.linspace(0,100,frames)
x = np.zeros(frames)
y = np.zeros(frames)


positions = np.zeros([N,frames,2])
v0s = np.ones((N,2))
for i in range(0,N):
    v0s[i] = np.array([random.uniform(-vrange, vrange), random.uniform(-vrange, vrange)])


#print(positions[0][0]) # first particle, first frame
#print(positions[0][0][0]) # first particle, first frame, x component

last_check_y = np.zeros(N)
last_check_x = np.zeros(N)



for j in range(0, N):
    for i in range(1, frames-1):

        positions[j][i][0] = positions[j][i-1][0] + v0s[j][0]
        positions[j][i][1] = positions[j][i-1][1] + v0s[j][1]

        #Reflect at boundary
        if abs(positions[j][i][0]) > 1 and last_check_x[j] >3:
            v0s[j][0] *= -1

        if abs(positions[j][i][1]) > 1 and last_check_y[j] >3:
            v0s[j][1] *= -1



        last_check_x[j] += 1
        last_check_y[j] += 1


start_x = x[0]
start_y = y[0]

fig, ax = plt.subplots()
ax.set(xlim=[-2, 2], ylim=[-2, 2], xlabel='x', ylabel='y')
ax.set_aspect("equal")


(particles) = list()
for i in range(0,N):
    (particles).append(ax.plot(positions[i][0][0],positions[i][0][1],".")[0])

# %%
l_border = ax.plot(left_edge,edges,"k")
r_border = ax.plot(right_edge,edges,"k")
u_border = ax.plot(edges,right_edge,"k")
b_border = ax.plot(edges,left_edge,"k")


track = 0

def many_particles_update(frame):
    
    # for each frame, update the data stored on each artist.

    """ Updates all particle positions."""
    global track
    track += 1
    if track % 30 == 0:
        print("Animating% :",str((track/frames)*100)[0:4]+"%")


    for i in range(0,N):
        current_particle = (particles)[i]
        #current_particle.set_xdata(positions[i][frame-1:frame][0])
        #current_particle.set_ydata(positions[i][frame-1:frame][1])

        #print("Xpos:",positions[i][frame-1:frame])

        #arr_arr
        val_x = float(positions[i][frame][0])
        arr_x = [val_x]
        arr_arr_x = [arr_x]

        val_y = float(positions[i][frame][1])
        arr_y = [val_y]
        arr_arr_y = [arr_y]



        # circles[i].set_xdata(positions[i][frame-1])
        # current_particle.set_ydata(positions[i][frame-1])
        (particles)[i].set_xdata(arr_arr_x)
        current_particle.set_ydata(arr_arr_y)
    


    return ((particles))


#Removes axes in plot
ax.axes.set_axis_off()

ani = animation.FuncAnimation(fig=fig, func=many_particles_update, frames=frames, interval=15)



#file counter
lst = os.listdir(".\\ManyParticle_gifs") # your directory path
number_files = len(lst)

#saving
ani.save(f"ManyParticle_gifs\\Particles_in_a_box_animation{number_files+1}.gif", fps=30)
print("Saved!")
