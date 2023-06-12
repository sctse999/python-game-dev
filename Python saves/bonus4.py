# Bonus 4 - Glide (+17 Lines)
import pygame
from random import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
normal_text = pygame.font.Font("graphics/comic.ttf", 50) 
start_surf = normal_text.render("Press [Space] to Start!", True, "Blue")
start_rect = start_surf.get_rect(center = (400, 250))
bird_acc = 0.5
pipeDistance = 300
gap_width = 250
running = True
bg_surf = pygame.image.load('graphics/bg.png')

def randomGap():
    return random() * 300 + 150

class pipe_data():
    posx = 800
    scored = False
    special = False
    
    def __init__(self):
        self.gap = randomGap()
        if random() < 0.05:
            self.special = True
            self.lower_surf = pygame.image.load('graphics/pipe_sp.png')
            self.upper_surf = pygame.transform.flip(pygame.image.load('graphics/pipe_sp.png'), False, True)
            self.upper_rect = self.upper_surf.get_rect(bottomleft = (800, self.gap - gap_width / 3))
            self.lower_rect = self.lower_surf.get_rect(topleft = (800, self.gap + gap_width / 3))
        else:
            self.lower_surf = pygame.image.load('graphics/pipe.png')
            self.upper_surf = pygame.transform.flip(pygame.image.load('graphics/pipe.png'), False, True)
            self.upper_rect = self.upper_surf.get_rect(bottomleft = (800, self.gap - gap_width / 2))
            self.lower_rect = self.lower_surf.get_rect(topleft = (800, self.gap + gap_width / 2))
        
        
    def draw(self):
        screen.blit(self.upper_surf, self.upper_rect)
        screen.blit(self.lower_surf, self.lower_rect)

def gameOver():
    global bird_vel, isGameOver, normal_text, lost_rect, lost_surf, scoreShow_rect, scoreShow_surf, glide, bird_surf, restart_rect, restart_surf
    bird_vel = -10
    glide = False
    isGameOver = True
    lost_surf = normal_text.render("Game Over...", True, "Red")
    lost_rect = lost_surf.get_rect(center = (400, 280))
    scoreShow_surf = normal_text.render(f"Your Score: {score}", True, "Red")
    scoreShow_rect = scoreShow_surf.get_rect(center = (400, 320))
    bird_surf = pygame.image.load('graphics/bird_dead.png')
    restart_surf = normal_text.render("Press [R] to Play Again", True, "Blue")
    restart_rect = restart_surf.get_rect(center = (400, 400))
    
def gameReset():
    global gameActive, isGameOver, bird_posy, bird_vel, score, distance, bird_surf, pipes, lastPipe, bird_rect, speed, score_surf, score_rect, score_text, speed_surf, speed_rect, glide
    gameActive = isGameOver = False
    bird_posy = 300
    bird_vel = -10
    score = 0
    score_text = pygame.font.Font("graphics/comic.ttf", 100)
    score_surf = score_text.render(str(score), True, "Black")
    score_rect = score_surf.get_rect(center = (400, 50))
    distance = 0
    pipes = []
    lastPipe = 0
    speed = 3
    speed_surf = normal_text.render(f"{speed:.1f} m/s", True, "Black")
    speed_rect = speed_surf.get_rect(bottomright = (775, 575))
    bird_surf = pygame.image.load('graphics/bird.png')
    bird_rect = bird_surf.get_rect(center = (60, 300))
    glide = False
    
gameReset()

# Keep the game running and update the screen, end the program when the close button is pressed
while running:
    screen.blit(bg_surf, (0, 0))
    screen.blit(bird_surf, bird_rect)
    for event in pygame.event.get(): # Loop through events
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not isGameOver:
            if event.key == pygame.K_SPACE:
                bird_vel = -10
            elif event.key == pygame.K_LSHIFT:
                glide = True
                bird_surf = pygame.image.load('graphics/bird_glide.png')
        if event.type == pygame.KEYUP and not isGameOver:
            if event.key == pygame.K_LSHIFT:
                glide = False
                bird_surf = pygame.image.load('graphics/bird.png')
                speed = 3 + score / 10
                
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            gameReset()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                
    if gameActive:
           
        # Bird Physics
        if glide and bird_vel >= 1:
            bird_vel = 1
        else:
            bird_vel += bird_acc
        bird_posy += bird_vel
        
        if glide:
            speed += 0.05
        
        if bird_posy < 0:
            bird_vel = bird_posy = 0
        bird_rect.y = bird_posy

        for current in pipes:
            current.draw()
        
        if not isGameOver:
            for current in pipes:
                current.posx -= speed
                current.upper_rect.x = current.lower_rect.x = current.posx
                if not current.scored and current.posx < 0:
                    if current.special:
                        score += 5
                        speed += 0.5
                    else:
                        score += 1
                        speed += 0.1
                    current.scored = True
                
                if current.posx < -60:
                    pipes.remove(current)
                    
                if current.upper_rect.colliderect(bird_rect) or current.lower_rect.colliderect(bird_rect):
                    gameOver()
                    
            if distance - lastPipe >= pipeDistance:
                lastPipe = distance
                pipes.append(pipe_data())
                
            distance += speed
        
            if bird_rect.bottom > 600:
                gameOver()
            
        else:
            screen.blit(lost_surf, lost_rect)
            screen.blit(scoreShow_surf, scoreShow_rect)
            screen.blit(restart_surf, restart_rect)
            speed = 0
    else: 
        screen.blit(start_surf, start_rect)
        
    score_surf = score_text.render(str(score), 100, "Black")
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    speed_surf = normal_text.render(f"{speed:.1f} m/s", True, "Black")
    speed_rect = speed_surf.get_rect(bottomright = (775, 575))
    screen.blit(speed_surf, speed_rect)
        
    pygame.display.update() # Update the screen
    clock.tick(60) # Set the FPS to 60

pygame.quit()