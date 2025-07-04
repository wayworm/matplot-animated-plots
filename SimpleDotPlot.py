
# %%
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import os

frames = 800


#Creating data
t = np.linspace(0,2*np.pi,frames)
x = np.cos(t)
y = np.sin(t)
start_x = x[0]
start_y = y[0]


##plotting
fig, ax = plt.subplots()
ax.set(xlim=[-2, 2], ylim=[-2, 2], xlabel='x', ylabel='y')


#initial position / frame 0
circle = ax.plot(x[0],[0],".")[0]

track = 0

#FrameUpdater
def FrameUpdater_dot(frame):
    """ for each frame, update the positon of the dot along it's path.

        FrameUpdater is made to be passed to the animation.FuncAnimation() 

    
    """
    global track 
    track += 1
    if track %30 == 0:
        print("Animating% :",str((track/frames)*100)[0:4]+"%")



    # update the plot
    circle.set_xdata(x[frame-1:frame])
    circle.set_ydata(y[frame-1:frame])
    return (circle)


ani = animation.FuncAnimation(fig=fig, func=FrameUpdater_dot, frames=frames, interval=15)



lst = os.listdir(".\\dot_gifs") # your directory path
number_files = len(lst)
print ("files:",number_files)

ani.save(f"dot_gifs\\Dot_animation{number_files+1}.gif", fps=30)
print("Saved!")
# %%
