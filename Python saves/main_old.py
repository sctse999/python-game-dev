import pygame
from random import *
pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

score = 0
bird_surf = pygame.image.load('graphics/bird.png')
bird_rect = bird_surf.get_rect(center = (60, 300))
score_text = pygame.font.Font(None, 100)
score_surf = score_text.render(str(score), True, "Black")
score_rect = score_surf.get_rect(center = (400, 50))
normal_text = pygame.font.Font(None, 50)
start_surf = normal_text.render("Press [Space] to Start!", True, "Blue")
start_rect = start_surf.get_rect(center = (400, 250))
bird_posy = 300
bird_vel = -10.0
bird_acc = 0.5
gameActive = False
isGameOver = False
pipeTimer = 90
gap_width = 250
pipes = []

def randomGap():
    return random() * 300 + 150

class pipe_data():
    posx = 800
    scored = False
    upper_surf = pygame.Rect(posx, 0, 60, 400)
    lower_surf = pygame.Rect(posx, 0, 60, 400)
    upper_rect = None
    lower_rect = ModuleNotFoundError
    gap = 0
    
    def __init__(self):
        self.gap = randomGap()
        self.lower_surf = pygame.image.load('graphics/pipe.png')
        self.upper_surf = pygame.transform.flip(pygame.image.load('graphics/pipe.png'), False, True)
        self.upper_rect = self.upper_surf.get_rect(bottomleft = (800, self.gap - gap_width / 2))
        self.lower_rect = self.lower_surf.get_rect(topleft = (800, self.gap + gap_width / 2))
        
        
    def draw(self):
        screen.blit(self.upper_surf, self.upper_rect)
        screen.blit(self.lower_surf, self.lower_rect)

screen.fill((192,192,255))
screen.blit(bird_surf, bird_rect)
screen.blit(start_surf, start_rect)
pygame.display.update()

def gameOver():
    global bird_vel, isGameOver, normal_text, lost_rect, lost_surf, scoreShow_rect, scoreShow_surf
    bird_vel = -10
    isGameOver = True
    lost_surf = normal_text.render("Game Over...", True, "Red")
    lost_rect = lost_surf.get_rect(center = (400, 280))
    scoreShow_surf = normal_text.render(f"Your Score: {score}", True, "Red")
    scoreShow_rect = scoreShow_surf.get_rect(center = (400, 320))

# Keep the game running and update the screen, end the program when the close button is pressed
while True:
    for event in pygame.event.get(): # Loop through events
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if gameActive:
            currentTime = pygame.time.get_ticks() - startTime
            
            if event.type == pygame.KEYDOWN and not isGameOver:
                if event.key == pygame.K_SPACE:
                    bird_vel = -10
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameActive = True
                startTime = pygame.time.get_ticks()
                
    if gameActive:
           
        # Bird Physics
        bird_vel += bird_acc
        bird_posy += bird_vel
        
        if bird_posy < 0:
            bird_vel = bird_posy = 0
        bird_rect.y = bird_posy
                
        screen.fill((192,192,255))
        screen.blit(bird_surf, bird_rect)
        for current in pipes:
            current.draw()
        
        if not isGameOver:
            for current in pipes:
                current.posx -= 3
                current.upper_rect.x = current.lower_rect.x = current.posx
                if not current.scored and current.posx < 60:
                    score += 1
                    current.scored = True
                
                if current.posx < -60:
                    pipes.remove(current)
                    
                if current.upper_rect.colliderect(bird_rect) or current.lower_rect.colliderect(bird_rect):
                    gameOver()
        
            pipeTimer -= 1
            if pipeTimer == 0:
                pipeTimer = 90
                pipes.append(pipe_data())
        
            if bird_posy > 550:
                gameOver()
            
        else:
            screen.blit(lost_surf, lost_rect)
            screen.blit(scoreShow_surf, scoreShow_rect)
               
    score_surf = score_text.render(str(score), 100, "Black")
    score_rect = score_surf.get_rect(center = (400, 50))   
    screen.blit(score_surf, score_rect)
        
    pygame.display.update() # Update the screen
    clock.tick(60) # Set the FPS to 60