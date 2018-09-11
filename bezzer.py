import numpy as np
import matplotlib.pyplot as plt

def comb(n, k):
    m = 1
    if n < 2 * k:
        k = n - k
    for i in xrange(1, k + 1):
        m = m * (n - i + 1) / i
    return m
def bernstein(n, i, t):
    return comb(n, i) * t**i * (1 - t)**(n-i)
def bezier(n, t, q):
    p = np.zeros(2)
    for i in range(n + 1):
        p += bernstein(n, i, t) * q[i]
        print(bernstein(n, i, t))
    return p

q = np.array([[900, 1500], [-500, 1800], [500, 3000],[1700,2100],[900,2100]], dtype=np.float)
#r = np.array([[300,300],[300,1000],[900,700],[900,1500]], dtype=np.float)
r = np.array([[0,0],[230,890],[994,600],[994,2000]], dtype=np.float)
#////
a = np.array([[600,600],[1238,600]], dtype=np.float)
b = np.array([[0,0],[0,2490]], dtype=np.float)
c = np.array([[0,2490],[1238,2490]], dtype=np.float)
d = np.array([[1238,2490],[1238,600]], dtype=np.float)
ee = np.array([[0,0],[1238,0]], dtype=np.float)
ff = np.array([[600,1900],[1238,1900]], dtype=np.float)
gg = np.array([[0,1300],[600,1300]], dtype=np.float)
#////

list = []
lists = []
for t in np.linspace(0, 1, 100):
    list.append(bezier(4, t, q))
    lists.append(bezier(3,t, r))

    #integral
#I = I +
    #////////
P = np.array(list)
R = np.array(lists)

plt.plot(R.T[0], R.T[1])
#plt.plot(P.T[0], P.T[1])
plt.plot(r.T[0], r.T[1], '--o')
#plt.plot(q.T[0], q.T[1], '--o')

plt.plot(a.T[0], a.T[1], '--x')
plt.plot(b.T[0], b.T[1], '--x')
plt.plot(c.T[0], c.T[1], '--x')
plt.plot(d.T[0], d.T[1], '--x')
plt.plot(ee.T[0], ee.T[1], '--x')
plt.plot(ff.T[0], ff.T[1], '--x')
plt.plot(gg.T[0], gg.T[1], '--x')

plt.show()
