from cmu_graphics import *
import math
app.background = gradient("white","lightblue","black",start="center")
app.stepsPerSecond = 100
app.stuned = False
app.stunTime = 0
###variablar
object = Group()
objectPos = []
app.attX = 0
app.attY = 0
KeyX = randrange(0,400)
KeyY = randrange(0,400)
GoalX = randrange(0,400)
GoalY= randrange(0,400)

###Poäng
value = 0
Label("Points:", 30, 15, fill='white',size= 20)    
Point = Label(value, 80, 15, fill='white',size = 18)
#Label("BOSS HEALTH",150,15,fill="cyan",size= 15)

###
app.paused = True
instroctions = Group(Rect(50,50,300,300,fill = "white"), 
                    Label("instructions",200, 75, size = 30),
                    Label("move with WASD and if your close enough", 200,100),
                    Label("to the enemy you can stun him with E", 200, 125),
                    Label("Goal",200,200, size = 30),
                    Label("the goal is to get to the door", 200,225),
                    Label("But to unlock the door you first need to get the key", 200, 250),
                    Label("press any key to start", 200, 325))

###Timer
value = 0
Label("Time:", 355, 15, fill='white')    
time = Label(value, 385, 15, fill='white')
time.count = 0

###defe
defe = Group()
def spawndef():
    defen = Image("https://cdn.discordapp.com/attachments/768055067756068886/950697062138277888/fish_background.png", randrange(100,300), randrange(100,300))
    defen.height = defen.height/5
    defen.width = defen.width/5
    defe.speed = 2
    defe.add(defen)
spawndef()
    

###BOSS
def spawnBoss():
    background.toFront()
    defe.clear()
    object.clear()
    player.toFront()
    boss.opacity = 100
    boss.toFront()
    background.opacity = 100
    defe.toFront()
    player.centerY = 300

### player
player = Image("https://cdn.discordapp.com/attachments/768055067756068886/950694999413104671/Small_background.png", 50, 50)
player.height = player.height/2
player.width = player.width/2
player.speed = 2
player.key = False


def spawno():
    for i in range(20):
    
        x1 = randrange(10,391)
        y1 = randrange(10,391)
        
        r = randrange(8, 20)
        
        farg1 = randrange (0,255)
        farg2 = randrange (0,255)
        farg3 = randrange (0,255)
        
        for X,Y in objectPos:
            dis = distance(X,Y,x1,y1)
            while  dis < 100:
                dis = distance(X,Y,x1,y1)
                x1 = randrange(10,391)
                y1 = randrange(10,391)
        
        objectPos.append((x1,y1))
        o = Circle(x1, y1, r, fill = rgb(farg1,farg2,farg3),border="white")
        object.add(o)
spawno()

boss = Image("https://cdn.discordapp.com/attachments/768055067756068886/950697062138277888/fish_background.png", 100, 50, opacity= 0)
boss.counter = 0

key = Group(Circle(KeyX,KeyY,6,fill= None,borderWidth = 4,border="yellow"),Rect(KeyX+5,KeyY-4,15,5,fill="yellow"),Rect(KeyX+10,KeyY+1,5,5,fill="yellow"))



goal = Group(Rect(GoalX,GoalY,30,30, fill = "Yellow",border="black"), 
        Circle(GoalX+15, GoalY+10, 8,fill="grey"),
        Star(GoalX+15, GoalY+20, 7, 3,fill="grey")
         )

background = Rect(0,0,400,400, opacity = 0)


def onKeyHold(keys): 
    
    ###colision
    for objec in object.children:
        if player.hitsShape(objec) and "w"in keys and player.centerY > objec.centerY + 5:
            player.centerY += player.speed
        if player.hitsShape(objec) and "s"in keys and player.centerY < objec.centerY - 5:
            player.centerY -= player.speed
        if player.hitsShape(objec) and "a"in keys and player.centerX > objec.centerX + 5:
            player.centerX += player.speed
        if player.hitsShape(objec) and "d"in keys and player.centerX < objec.centerX - 5:
            player.centerX -= player.speed
    
    
        
    
    ### move player
    if('w' in keys and 'd' in keys and player.right < 400 and player.top > 0):
        player.centerY -= player.speed/math.sqrt(2)
        player.centerX += player.speed/math.sqrt(2)
        
    elif('a' in keys and 's' in keys and player.left > 0 and player.bottom < 400):
        player.centerY += player.speed/math.sqrt(2)
        player.centerX -= player.speed/math.sqrt(2)
        
    elif('a' in keys and 'w' in keys and player.left > 0 and player.top > 0):
        player.centerY -= player.speed/math.sqrt(2)
        player.centerX -= player.speed/math.sqrt(2)
        
    elif('d' in keys and 's' in keys and player.right < 400  and player.bottom < 400):
        player.centerY += player.speed/math.sqrt(2)
        player.centerX += player.speed/math.sqrt(2)
    
    elif('d' in keys and 'a' in keys):
        player.centerX += 0
    elif('w' in keys and 's' in keys):
        player.centerY += 0
    elif('a' in keys and player.left > 0):
        player.centerX -= player.speed
    elif('d' in keys and player.right < 400):
        player.centerX += player.speed
    elif('s' in keys and player.bottom < 400):
        player.centerY += player.speed
    elif('w' in keys and player.top > 0):
        player.centerY -= player.speed
        
if app.stuned == True:
    Point.value +=  100

###party timer
attTime = Arc(app.attX, app.attY, 20, 20, 1, 1, border='Green')



def onKeyPress(keys):
    dir = distance(player.centerX, player.centerY, defe.centerX, defe.centerY)
    if attTime.sweepAngle == 360 and dir <= 100:
        if keys == "e":
            app.stuned = True
    
    app.paused = False
    instroctions.clear()
    
  #  if attTime.sweepAngle == 360 and dir <=100:
        #if keys =="e":
        #    app.stuned = True
        #    boss.counter += 1
            
    

def onStep():
    app.stunTime -= 1
    
    dir = distance(player.centerX, player.centerY, key.centerX, key.centerY)
    if dir <= 50:
       player.key = True
    
    for o in object.children:
        if key.hitsShape(o):
            keyX = randrange(0,400)
            keyY = randrange(0,400)
        if goal.hitsShape(o):
            goal.centerX = randrange(0,400)
            goal.centerY = randrange(0,400)
    
    if app.stunTime < 0:
        defe.speed = 1
    
    
    
    if(defe.hitsShape(player)):
        Label("You Lose", 200, 200, size= 20, font='arial', bold=True, italic=True, fill='Black', border='Red', borderWidth=2, opacity=100)
        app.stop()
    
    time.count += 1
    if time.count > 75:
        time.count = 0
        time.value += 1
    
    if app.stuned == True:
        defe.speed = 0
        attTime.sweepAngle = 1
        app.stunTime = 100
        app.stuned = False
        Point.value += 100
    
    if player.key == True:
       key.centerX = player.centerX
       key.centerY = player.centerY - 20
    
    if(attTime.sweepAngle<360):
        attTime.sweepAngle += 1
        attTime.fill = None
    elif(attTime.sweepAngle==360):
        attTime.fill = 'Green'
        
        

    if player.hitsShape(goal) and player.key == True:
       player.key = False
       Point.value += 500
       key.centerX = randrange(0,400)
       key.centerY = randrange(0,400)
       goal.centerX = randrange(0,400)
       goal.centerY= randrange(0,400)
       object.clear()
       spawno()
    
    ###Boss
    #if Point.value >= 1000:
    #    spawnBoss()
    
        

        
        
        
    ###move defeder
    for defen in defe.children:
        angleToPlayer = angleTo(defen.centerX, defen.centerY, player.centerX, player.centerY)
        defen.centerX += dsin(angleToPlayer) * defe.speed
        defen.centerY += -dcos(angleToPlayer) * defe.speed
        
        attTime.centerX = defen.centerX
        attTime.centerY = defen.centerY+20

instroctions.toFront()



cmu_graphics.run()
