import turtle
t = turtle.Pen()
t.left(90)
t.color('red')
t.right(305)             
t.forward(80)
for x in range(180):
    t.forward(1)
    t.right(1)
t.right(180) # forma-se a metade do coração lado esquerdo
t.forward(1)
#t = turtle.Pen()
t.left(15)
t.right(1)
#metade do coração lado direito
t = turtle.Pen()
t.left(-90)
t.color('red')
t.right(-305)
t.forward(-80)
for x in range(180):
    t.forward(-1)
    t.right(-1)
t.right(180)
t.forward(1)
t.left(-15)
t.right(-1)
#fim novo cod do lado do coração direito

