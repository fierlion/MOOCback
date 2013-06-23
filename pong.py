# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [3,  -1]
vel1 = 0
vel2 = 0
score1 = 0
score2 = 0
pad1_pos = [0, 160]
pad1_bot = [0, pad1_pos[1]+80]
pad2_pos = [600, 160]
pad2_bot = [600, pad2_pos[1]+80]


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, vel # these are vectors stored as lists


# define event handlers

def new_game():
    global pad1_pos, pad2_pos, vel, vel1, vel2, ball_pos  # these are floats
    global score1, score2  # these are ints
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel = [3,  -1]
    vel1 = 0
    vel2 = 0
    score1 = 0
    score2 = 0
    pad1_pos = [0, 160]
    pad2_pos = [600, 160]

def draw(c):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, vel
 
    # update paddle's vertical position, keep paddle on the screen
    pad1_pos[1] += vel1
    pad1_bot[1] += vel1
    pad2_pos[1] += vel2
    pad2_bot[1] += vel2
    
         #update score
    if (ball_pos[0] <= BALL_RADIUS - 40):
        score2 += 1
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [random.randrange(1, 9), -3]
    
    if (ball_pos[0] >= (WIDTH + 40) - BALL_RADIUS):
        score1 += 1
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        vel = [-(random.randrange(1, 9)), -3]
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line(pad1_pos, pad1_bot, PAD_WIDTH+8, "Cyan")
    c.draw_line(pad2_pos, pad2_bot, PAD_WIDTH+8, "Yellow")
     
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
        # lh collide
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
            if (pad1_bot[1] > ball_pos[1] > pad1_pos[1]):
                vel[0] = - vel[0]
                vel[1] += 2
                
        # rh collide
    if (ball_pos[0] >= (WIDTH) - BALL_RADIUS- PAD_WIDTH):
            if (pad2_bot[1] > ball_pos[1] > pad2_pos[1]):
                vel[0] = - vel[0]
                vel[1] += 2
                
    if (ball_pos[1] <= 0 + BALL_RADIUS):
            vel[1] = - vel[1]
            
    if (ball_pos[1] >= HEIGHT - BALL_RADIUS):
            vel[1] = - vel[1]
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Cyan", "Yellow")
    c.draw_text(str(score1), [200, 50], 30, "Cyan")
    c.draw_text(str(score2), [385, 50], 30, "Yellow")
        
def keydown(key):
    global vel1, vel2
    acc = 2
    
    if key==simplegui.KEY_MAP["s"]:
        vel1 += acc
    elif key==simplegui.KEY_MAP["w"]:
        vel1 -= acc
    elif key==simplegui.KEY_MAP["down"]:
        vel2 += acc
    elif key==simplegui.KEY_MAP["up"]:
        vel2 -= acc
   
def keyup(key):
    global vel1, vel2
    if key==simplegui.KEY_MAP["s"]:
        vel1 = 0
    elif key==simplegui.KEY_MAP["w"]:
        vel1 = 0
    if key==simplegui.KEY_MAP["down"]:
        vel2 = 0
    if key==simplegui.KEY_MAP["up"]:
        vel2 = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)


# start frame
frame.start()
