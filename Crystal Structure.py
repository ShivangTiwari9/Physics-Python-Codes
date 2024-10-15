from vpython import sphere,vector,color
L=5
R=.3
for i in range(0,L+1,2):
    for j in range(0,L+1,2):
        for k in range(0,L+1,2):
            sphere(pos=vector(i,j,k),radius=R,color=color.red)
for i in range(1,L+1,2):
    for j in range(1,L+1,2):
        for k in range(0,L+1,2):
            sphere(pos=vector(i,j,k),radius=0.1,color=color.blue)
for i in range(1,L+1,2):
    for j in range(0,L+1,2):
        for k in range(1,L+1,2):
            sphere(pos=vector(i,j,k),radius=0.1,color=color.green)
for i in range(0,L+1,2):
    for j in range(1,L+1,2):
        for k in range(1,L+1,2):
            sphere(pos=vector(i,j,k),radius=0.1,color=color.white)
