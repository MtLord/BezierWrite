# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
PI=3.1415
# 矢印（ベクトル）の始点
'''
#3omu test
X = 0,2* -np.sqrt(3)/2,2* np.sqrt(3)/2
Y = 2,2* -1/2,2* -1/2
'''
#3omu cyri
X = 2* 0.866,2* -0.866,2* 0
Y = 2* 0.5,2* 0.5,2* -1

'''
#4omu test
X = 2* 0,2* 1,2* 0,2* -1
Y = 2* -1,2* 0,2* 1,2* 0
'''
'''
#4omu made in B
X=2* 1/np.sqrt(2),2* -1/np.sqrt(2),2* -1/np.sqrt(2),2* 1/np.sqrt(2)
Y=2* 1/np.sqrt(2),2* 1/np.sqrt(2),2* -1/np.sqrt(2),2* -1/np.sqrt(2)
'''
vx=-1
vy=-1
xi=0
omega=0
L=0
'''
U = -vx * np.cos(PI/3+xi),vx * np.cos(xi),-vx * np.cos(PI/3+xi)
V = -vy * np.sin(PI/3+xi),vy * np.sin(xi),vy * np.sin(PI/3+xi)
'''
'''
#3omu test
v1=-vx
v2=0.5*vx-0.866*vy
v3=0.5*vx+0.866*vy
U = -1*v1,0.5*v2,0.5*v3
V = 0*v1,-0.866*v2,0.866*v3
'''
'''
#3omu wada
v1=vx*-np.sin(xi+PI/6)+vy*np.cos(xi+PI/6)+L*omega
v2=vx*-np.sin(xi+PI*5/6)+vy*np.cos(xi+5*PI/6)+L*omega
v3=-vx*-np.sin(xi-PI/2)+vy*np.cos(xi+PI/2)+L*omega
U = -0.5*v1,-0.5*v2,1*v3
V = 0.866*v1,-0.866*v2,0*v3
'''
'''
#3omu cyri
v1=-0.5*vx+0.866*vy
v2=-0.5*vx-0.866*vy
v3=vx
U = -0.5*v1,-0.5*v2,1*v3
V = 0.866*v1,-0.866*v2,0*v3
'''
'''4omu test
v1 = 1*vx+0*vy
v2 = 0*vx+1*vy
v3 = -1*vx+0*vy
v4 = 0*vx-1*vy
U = 1*v1,0*v2,-1*v3,0*v4
V = 0*v1,1*v2,0*v3,-1*v4
'''
'''
#4omu made in B
v1=0.707*vx -1* 0.707*vy
v2=-1* -0.707*vx -1* 0.707*vy
v3=-1* -0.707*vx +1* -0.707*vy
v4=0.707*vx +1* -0.707*vy
U=-0.707*v1,-0.707*v2,0.707*v3,0.707*v4
V=0.707*v1,-0.707*v2,-0.707*v3,0.707*v4
'''
'''
#4omu yyy
v1=-0.707*vx +0.707*vy
v2=-0.707*vx -0.707*vy
v3=0.707*vx -0.707*vy
v4=0.707*vx +0.707*vy
U=-0.707*v1,-0.707*v2,0.707*v3,0.707*v4
V=0.707*v1,-0.707*v2,-0.707*v3,0.707*v4
'''
'''
#4omu yyyy
v1 = -vx*np.sin(xi+PI/4) + vy*np.sin(xi+3*PI/4) + L*omega
v2 = vx*np.sin(xi-PI/4) - vy*np.sin(xi+PI/4) + L*omega
v3 = vx*np.sin(xi+PI/4) + vy*np.sin(xi-PI/4) + L*omega
v4 = vx*np.sin(xi+3*PI/4) + vy*np.sin(xi+PI/4) + L*omega
'''
'''
#4omu made in B re
v1 = vx*np.sin(xi+PI/4) + vy*np.sin(xi+7*PI/4) + L*omega
v2 = vx*np.sin(xi+7*PI/4) - vy*np.sin(xi+PI/4) + L*omega
v3 = vx*np.sin(xi+PI/4) + vy*np.sin(xi+3*PI/4) + L*omega
v4 = vx*np.sin(xi+3*PI/4) + vy*np.sin(xi+PI/4) + L*omega
U=-0.707*v1,-0.707*v2,0.707*v3,0.707*v4
V=0.707*v1,-0.707*v2,-0.707*v3,0.707*v4
'''
fig = plt.figure()
ax = fig.add_subplot(111)
# 中心(0.2,0.2)で半径0.2の円を描画
circle = plt.Circle((0,0),2,ec='#000000', fill=False)
ax.add_patch(circle)

plt.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
# グラフ表示
plt.xlim([-4,4])
plt.ylim([-4,4])
plt.grid()
plt.draw()
plt.show()
