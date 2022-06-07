import numpy as np

def Lorenzkey(x0,y0,z0,num_steps):
  dt=0.01

  xs = np.empty(num_steps + 1)
  ys = np.empty(num_steps + 1)
  zs = np.empty(num_steps + 1)

  #Set initial values
  xs[0],ys[0],zs[0] = (x0,y0,z0)

  s=10
  r=28
  b=2.667
  for i in range(num_steps):
    xs[i+1] = xs[i] + (s*(ys[i]- xs[i])*dt)
    ys[i+1] = ys[i] + ((xs[i] * (r-zs[i])- ys[i])*dt)
    zs[i+1] = zs[i] + ((xs[i] * ys[i]- b * zs[i])*dt)

  return xs,ys,zs