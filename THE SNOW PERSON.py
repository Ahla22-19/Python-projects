from cs1graphics import*

#ICELAND
IL=Canvas(800,600,"sky blue","ICELAND")

#LAND

R=Rectangle(800,100)
R.setFillColor("white")
R.move(400,550)
IL.add(R)

#GROUND CIRCLE

SNOWMAN=Layer()

C=Circle(100,Point(600,499))
C.setFillColor("white")
SNOWMAN.add(C)

#MIDDLE CIRCLE

C2=Circle(60,Point(600,340))
C2.setFillColor("white")
SNOWMAN.add(C2)

#KEYS ON THE MIDDLE CIRCLE

K1=Circle(3,Point(600,332))
K1.setFillColor("black")
SNOWMAN.add(K1)

K2=Circle(3,Point(600,305))
K2.setFillColor("black")
SNOWMAN.add(K2)

K3=Circle(3,Point(600,357))
K3.setFillColor("black")
SNOWMAN.add(K3)

#HANDS

H1=Rectangle(50,10,Point(517,330))
H1.setFillColor("Brown")
SNOWMAN.add(H1)

H2=Rectangle(50,10,Point(683,330))
H2.setFillColor("Brown")
SNOWMAN.add(H2)

#FACE

C3=Circle(30,Point(600,250))
C3.setFillColor("white")
SNOWMAN.add(C3)

#EYES

E1=Circle(2,Point(590,240))
E1.setFillColor("black")
SNOWMAN.add(E1)

E2=Circle(2,Point(610,240))
E2.setFillColor("black")
SNOWMAN.add(E2)

#NOSE

N=Polygon(Point(600,260),Point(610,280),Point(610,260))                           
N.setFillColor("YELLOW")
N.rotate(270)
SNOWMAN.add(N)

#HIS SMILE

S1=Circle(2,Point(598,270))
S1.setFillColor("black")
SNOWMAN.add(S1)

S2=Circle(2,Point(605,270))
S2.setFillColor("black")
SNOWMAN.add(S2)

S3=Circle(2,Point(591,264))
S3.setFillColor("black")
SNOWMAN.add(S3)

S3=Circle(2,Point(612,264))
S3.setFillColor("black")
SNOWMAN.add(S3)

IL.add(SNOWMAN)

for i in range(100):
    SNOWMAN.move(1,0)

for i in range(100):
    SNOWMAN.move(-1,0)
