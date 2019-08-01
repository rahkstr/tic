def setup():
    global player1Turn, gameOver, spot, winner

    # set up window & background
    size(300, 300)
    background(200)
    fill(200)
    
    # draw grid
    line(100, 0, 100, 300)
    line(200, 0, 200, 300)
    line(0, 100, 300, 100)
    line(0, 200, 300, 200)

    # initialize game
    player1Turn = True
    gameOver = False
    spot = [[None] * 3, [None] * 3, [None] * 3]
    winner = None

def draw():
    # we need a draw function to get access to mouseCLicked()
    pass

def mouseClicked():
    global player1Turn, gameOver, spot, winner

    if not gameOver:
        gridX = mouseX / 100
        gridY = mouseY / 100
    
        windowX = gridX * 100
        windowY = gridY * 100
        
        if spot[gridX][gridY] == None:
            # add new move
            if player1Turn:
                spot[gridX][gridY] = "X"
                line(windowX, windowY, windowX+100, windowY+100)
                line(windowX+100, windowY, windowX, windowY+100)
            else:
                spot[gridX][gridY] = "O"
                ellipse(windowX+50, windowY+50, 100, 100)
                
            # check rows
            for x in range(3):
                if spot[x][0] and spot[x][0] == spot[x][1] and spot[x][0] == spot[x][2]:
                    winner = spot[x][0]
            # check columns
            for y in range(3):
                if spot[0][y] and spot[0][y] == spot[1][y] and spot[0][y] == spot[2][y]:
                    winner = spot[0][y]
            # check diagonals
            if spot[0][0] and spot[0][0] == spot[1][1] and spot[0][0] == spot[2][2]:
                    winner = spot[0][0]
            if spot[2][0] and spot[2][0] == spot[1][1] and spot[2][0] == spot[0][2]:
                    winner = spot[2][0]
            
            # update state
            if winner or (all(spot[0]) and all(spot[1]) and all(spot[2])):
                gameOver = True
            else:            
                player1Turn = not player1Turn

    if gameOver:
        background(200)
        fill(0)
        if winner:
            text("Winner is " + winner, 125, 150)
        else:
            text("Womp womp!", 125, 150)
