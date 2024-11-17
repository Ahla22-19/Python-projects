from cs1graphics import*
G=Canvas(900,700,"light blue","GARDEN")

#BEE

bee=Layer()

B=Ellipse(220,100)
B.setFillColor("yellow")
B.move(150,300)
B.setDepth(6)
bee.add(B)

H1=Rectangle(20,94,Point(113,300))
H1.setFillColor("black")
H1.setDepth(4)
bee.add(H1)

H2=Rectangle(20,98,Point(150,300))
H2.setFillColor("black")
H2.setDepth(4)
bee.add(H2)

H3=Rectangle(20,94,Point(188,300))
H3.setFillColor("black")
H3.setDepth(4)
bee.add(H3)

#EYES
E1=Circle(16,Point(252,279))
E1.setFillColor("white")
E1.setDepth(4)
bee.add(E1)

E2=Circle(16,Point(252,310))
E2.setFillColor("white")
E2.setDepth(4)
bee.add(E2)

E3=Circle(7,Point(252,279))
E3.setFillColor("black")
E3.setDepth(3)
bee.add(E3)

E4=Circle(7,Point(252,310))
E4.setFillColor("black")
E4.setDepth(3)


bee.add(E4)

#WINGS

W1=Ellipse(120,50)
W1.setFillColor("white")
W1.move(150,350)
W1.rotate(75)
W1.setDepth(7)
bee.add(W1)

W2=W1.clone()
W2.move(0,-100)
W2.rotate(50)
bee.add(W2)
bee.move(0,50)
G.add(bee)

#################################
#FLOWER
S=Layer()
F=Square(150,Point(700,345))
F.setFillColor("red")
F.setBorderColor("red")
F.setDepth(200)
S.add(F)

F2=F.clone()
F2.rotate(22.5)
S.add(F2)

F3=F.clone()
F3.rotate(65)
S.add(F3)

F4=F.clone()
F4.rotate(-48.25)
S.add(F4)


F1=Circle(80,Point(700,345))
F1.setFillColor("red")
F1.setBorderColor("red")
F1.setDepth(100)
S.add(F1)

F5=Circle(40,Point(700,345))
F5.setFillColor("yellow")
F5.setBorderColor("yellow")
F5.setDepth(90)
S.add(F5)
S.setDepth(500)
G.add(S)

#FLOWER STEM AND LEAVES

l=Rectangle(15,330,Point(700,600))
l.setFillColor("green")
l.setBorderColor("green")
l.setDepth(1000)
G.add(l)

L1=Ellipse(40,150,Point(650,533))
L1.setFillColor("green")
L1.setBorderColor("green")
L1.rotate(-45)
G.add(L1)

L2=Ellipse(40,150,Point(750,533))
L2.setFillColor("green")
L2.setBorderColor("green")
L2.rotate(45)
G.add(L2)

for i in range (550):
    bee.move(1,0)

for i in range (550):
   bee.move(-1,0)
