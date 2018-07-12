xCoordinate = 50
yCoordinate = 50
speed = 1
ySpeed = 2
ellipseSize = 30
y = 50
x = 100

def setup():
    size(500, 500)
    
def brick(x, y, w, h):
    fill(random(255), random(255), random(255))
    rect(x, y, w, h)
    
def draw():
    background(0)
    global xCoordinate, speed, ySpeed, ellipseSize, yCoordinate, brick
    topBoundary = ellipseSize / 2
    bottomBoundary = 500 - ellipseSize / 2
    leftBoundary = ellipseSize / 2
    rightBoundary = ellipseSize / 2
    y = 50 + ellipseSize / 2 
    if xCoordinate >= bottomBoundary or xCoordinate <= topBoundary:
        speed = -speed
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        ySpeed = -ySpeed
    if yCoordinate <= y:
        ySpeed = -ySpeed
    yCoordinate += ySpeed
    xCoordinate += speed
    fill(255, 25, 100)
    ellipse( xCoordinate + 100, yCoordinate + 100, ellipseSize, ellipseSize)
    rect(0, 0, x, y)
    rect(100, 0, x, y)
    rect(200, 0, x, y)
    rect(300, 0, x, y)
    rect(400, 0, x, y)
    
