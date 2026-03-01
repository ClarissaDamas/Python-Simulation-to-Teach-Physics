from vpython import *
g = 9.8
altura = 0.1
vbola = vector(5,30,0)
bola = sphere(pos=vector(0,altura,0), radius=1, texture="https://s3.amazonaws.com/glowscript/textures/flower_texture.jpg")
chao = box(pos=vector(0,-9,0), size=vector(200,0.01,200), texture="https://s3.amazonaws.com/glowscript/textures/earth_texture.jpg")
deltat = 0.01
tempo = 0
while bola.pos.y > 0:
    rate(150)
    aceleracao = vector(0,-g,0)
    #velocidade
    vbola = vbola + aceleracao*deltat
    bola.pos = bola.pos + vbola*deltat
    tempo = tempo + deltat
print(vbola)
print("fim")
