import pygame

# Initialize the game
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Initialize game variables
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [2, 2]  # Velocity of the ball
paddle_width = 20
paddle_height = 100

# Initialize paddles' positions
paddle1_pos = screen_height // 2 - paddle_height // 2
paddle2_pos = screen_height // 2 - paddle_height // 2

# Initialize scores
score1 = 0
score2 = 0

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the frame rate
fps = 60
clock = pygame.time.Clock()

# Function to draw the game objects
def draw_objects():
    screen.fill(black)  # Clear the screen with a black color
    pygame.draw.circle(screen, white, ball_pos, 10)  # Draw the ball
    pygame.draw.rect(screen, white, (10, paddle1_pos, paddle_width, paddle_height))  # Draw paddle 1
    pygame.draw.rect(screen, white, (screen_width - 30, paddle2_pos, paddle_width, paddle_height))  # Draw paddle 2
    pygame.display.flip()  # Update the screen

# Function to move the ball
def move_ball():
    global ball_pos, ball_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check for collision with top and bottom walls
    if ball_pos[1] <= 0 or ball_pos[1] >= screen_height:
        ball_vel[1] = -ball_vel[1]
    
    # Check for collision with paddles
    if ball_pos[0] <= paddle_width + 10 and paddle1_pos <= ball_pos[1] <= paddle1_pos + paddle_height:
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] >= screen_width - paddle_width - 30 and paddle2_pos <= ball_pos[1] <= paddle2_pos + paddle_height:
        ball_vel[0] = -ball_vel[0]
    
    # Check for scoring
    if ball_pos[0] < 0:
        score2 += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_vel = [-ball_vel[0], ball_vel[1]]
    elif ball_pos[0] > screen_width:
        score1 += 1
        ball_pos = [screen_width // 2, screen_height // 2]
        ball_vel = [-ball_vel[0], ball_vel[1]]

# Function to move the paddles
def move_paddles(keys):
    global paddle1_pos, paddle2_pos
    if keys[pygame.K_w]:
        paddle1_pos -= 5
    if keys[pygame.K_s]:
        paddle1_pos += 5
    if keys[pygame.K_UP]:
        paddle2_pos -= 5
    if keys[pygame.K_DOWN]:
        paddle2_pos += 5

    # Ensure paddles stay within the screen bounds
    paddle1_pos = max(min(paddle1_pos, screen_height - paddle_height), 0)
    paddle2_pos = max(min(paddle2_pos, screen_height - paddle_height), 0)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the paddles
    move_paddles(keys)

    # Move the ball
    move_ball()

    # Draw game objects
    draw_objects()
    
    # Cap the frame rate
    clock.tick(fps)

# End the game
pygame.quit()
