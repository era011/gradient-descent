import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo


def diffn(x:np.ndarray, func,h=.00001)->np.ndarray:
    x.astype(np.float64)
    x=x[:,np.newaxis]
    x=np.repeat(x,x.shape[0],axis=1).T
    arr=x.copy()
    np.fill_diagonal(arr,np.diag(arr)+h)
    funch=np.apply_along_axis(func,arr=arr,axis=1)
    func1=np.apply_along_axis(func,arr=x,axis=1)
        
    return (funch-func1)/h


def func3(x:np.ndarray):
    return np.sin(x[0])*np.sin(x[1])

def func2(x:np.ndarray):
    return 2*x[0]+3*x[1]

def func1(x:np.ndarray):
    return np.square(x[0]+1)+np.square(x[1]+2)

funcn=func3

x=np.array([1.2,1.3])
dotes=x.copy()
flag=True
while flag:
    grad=diffn(x,funcn)
    nue=np.linalg.norm(grad)
    if nue<=.001:
        flag=False       
    x=x-0.01*nue*grad
    dotes=np.concatenate((dotes,x.copy()),axis=0) 

dotes=dotes.reshape((int(dotes.shape[0]/2),2))
z=np.apply_along_axis(funcn,axis=1,arr=dotes)

x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
x, y = np.meshgrid(x, y)
z1 = funcn(np.array([x,y]))

surface = go.Surface(z=z1, x=x, y=y,opacity=0.7)
scatters=go.Scatter3d(x=dotes[:,0],y=dotes[:,1],z=z,marker=dict(size=2, color='black'))

layout = go.Layout(
    title='3D Surface plot',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    )
)

fig = go.Figure(data=[surface,scatters])
fig.show()
print(f"точка минимума {x}")