
import pygame
import random
pygame.init()

# create window and set display
window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))

# set the title of window
pygame.display.set_caption("My Game")

# set frame rate
clock = pygame.time.Clock()
FPS =  60

# create background surface
bg_color = (135, 206, 235)
bg_width = window_width
bg_height = max(0, window_height - 145)  # ensure the height is at least 0
bg_surface = pygame.Surface((bg_width, bg_height))
bg_surface.fill(bg_color)

score = 0
balance = 0
score_font = pygame.font.SysFont(None, 30)



class Coin(pygame.sprite.Sprite):
    def __init__(self, x , y):
        super().__init__()
        self.image = pygame.image.load("BIG_0000_Capa-1.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 2, self.image.get_height() // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spawn_coin():
        coin = Coin(random.randint(0, window_width), random.randint(0, window_height))
        coins.add(coin)
            
def show_coins():
        balance_text = score_font.render("Balance: " + str(balance), True, (255, 255, 255))
        win.blit(balance_text, (window_width - 800,10))

        pygame.display.update()
        
        
coins = pygame.sprite.Group()
coins.add(Coin(80,199))
coins.add(Coin(287,145))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x,  y):
        super().__init__()
        self.image = pygame.image.load("platform.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 20, self.image.get_height() // 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
# create a group for platforms
platforms = pygame.sprite.Group()

# create some platforms and add them to the group
platforms.add(Platform(40,250))
platforms.add(Platform(247,200))
platforms.add(Platform(435,250))
platforms.add(Platform(630,200))

pygame.display.update()

attack_sprites = pygame.sprite.Group()

# load Sprites
player_img = pygame.image.load('Player_Sprite_R.png')
run_ani_R = [pygame.image.load("Player_Sprite_R.png"), pygame.image.load("Player_Sprite2_R.png"),
             pygame.image.load("Player_Sprite3_R.png"), pygame.image.load("Player_Sprite4_R.png"),
             pygame.image.load("Player_Sprite5_R.png"), pygame.image.load("Player_Sprite6_R.png"),]
run_ani_L = [pygame.transform.flip(run_ani_R[i], True, False) for i in range(len(run_ani_R))]

# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load("Player_Attack_R.png"),
                pygame.image.load("Player_Attack2_R.png"),pygame.image.load("Player_Attack2_R.png"),
                pygame.image.load("Player_Attack3_R.png"),pygame.image.load("Player_Attack3_R.png"),
                pygame.image.load("Player_Attack4_R.png"),pygame.image.load("Player_Attack4_R.png"),
                pygame.image.load("Player_Attack5_R.png"),pygame.image.load("Player_Attack5_R.png"),
                pygame.image.load("Player_Sprite_R.png")]

for attack_frame in attack_ani_R:
    attack_sprite = pygame.sprite.Sprite()
    attack_sprite.image = attack_frame
    attack_sprite.rect = attack_sprite.image.get_rect()
    attack_sprites.add(attack_sprite)
 
# Attack animation for the LEFT
attack_ani_L = [pygame.transform.flip(attack_ani_R[i], True, False) for i in range(len(attack_ani_R))]

for attack_frame in attack_ani_L:
    attack_sprite = pygame.sprite.Sprite()
    attack_sprite.image = attack_frame
    attack_sprite.rect = attack_sprite.image.get_rect()
    attack_sprites.add(attack_sprite)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, name, health, damage, defense):
        super().__init__()
        self.font = pygame.font.SysFont(None, 20)
        self.name = name
        self.health = health
        self.max_health = health
        self.current_health = health
        self.damage = damage
        self.defense = defense
        self.image = pygame.image.load("sprite_rotmg_enemy0.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 2
        self.direction = "right"

    def take_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        elif self.current_health > self.max_health:
            self.current_health = self.max_health
        
    def move(self, dx, dy):
        self.rect.center = (self.rect.centerx + dx, self.rect.centery + dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    # Update direction based on movement
        if dx > 0:
            self.direction = "right"
        elif dx < 0:
            self.direction = "left"

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                elif dx < 0:
                    self.rect.left = platform.rect.right
                elif dy > 0:
                    self.rect.bottom = platform.rect.top
                elif dy < 0:
                    self.rect.top = platform.rect.bottom

                # Update direction based on collision
                if dx != 0:
                    self.direction = "left" if dx > 0 else "right"   
                    
    def respawn(self):
        self.current_health = self.max_health
        self.rect.center = (random.randint(1, window_width), window_height // 1 - 175)
        
    def update(self):
        if self.direction == "right":
            self.rect.x += self.vel
            if self.rect.right > window_width:
                self.direction = "left"
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "left":
            self.rect.x -= self.vel
            if self.rect.left < 0:
                self.direction = "right"
                self.image = pygame.transform.flip(self.image, True, False)

        # Check if the enemy collides with the player's attack animation
        for attack_sprite in attack_sprites:
            if self.rect.colliderect(attack_sprite.rect):
                # Enemy takes damage
                self.take_damage(10)
                if self.current_health == 0:
                    global score 
                    score += 10
                    self.respawn()
            
    def check_collision(self, dx, dy):
        for platform in platforms:
            if self.rect.move(dx, dy).colliderect(platform.rect):
                return True
        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        name_text = self.font.render(self.name, True, (255, 255, 255))
        damage_text = self.font.render(f"Damage: {self.damage}", True, (255, 255, 255))
        defense_text = self.font.render(f"Defense: {self.defense}", True, (255, 255, 255))
        health_text = self.font.render(f"Health: {self.current_health}/{self.max_health}", True, (255, 255, 255))
        win.blit(name_text, (self.rect.x + self.rect.width // 2 - name_text.get_width() // 2, self.rect.y - 20))
        win.blit(damage_text, (self.rect.x + self.rect.width // 2 - damage_text.get_width() // 2, self.rect.y + self.rect.height + 5))
        win.blit(defense_text, (self.rect.x + self.rect.width // 2 - defense_text.get_width() // 2, self.rect.y + self.rect.height + 25))
        win.blit(health_text, (self.rect.x + self.rect.width // 2 - health_text.get_width() // 2, self.rect.y + self.rect.height + 45))


enemies = pygame.sprite.Group()
enemies.add(Enemy(300, 390, "Ghost", 50, 10, 5))

def show_score():
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    win.blit(score_text, (window_width - 450, 10))
    
    pygame.display.update()
    
    
# set player attributes
player_size = 64
player_speed =5
player_rect = player_img.get_rect()
player_rect.center = (window_width // 2, window_height // 1 - 50)  # make the player start higher up
direction = 1  # 1 = right, -1 = left
animation_count = 0
is_idle = True
# jumping
jump_count = 10
is_jumping = False
enemy = Enemy(100, 100, "Goblin", 50, 10, 5)

# load background image
bg = pygame.image.load('ORS97Z0.jpg').convert()
bg = pygame.transform.scale(bg, (window_width, window_height))

# create function for drawing the window
player_attack_rect = pygame.Rect(0, 0, 64, 64)
attack_sprite = pygame.sprite.Sprite()
attack_sprite.rect = player_attack_rect
attack_sprite.image = pygame.Surface((64, 64), pygame.SRCALPHA)

def redraw_window():
    attack_sprite.rect.center = (player_rect.centerx + (direction * 50), player_rect.centery - 10)
    # draw background
    win.blit(bg, (0, 0))

    # draw player
    if direction == 1:
        if is_idle:
            win.blit(player_img, player_rect)
        else:
            win.blit(run_ani_R[animation_count // 10], player_rect)
    elif direction == -1:
        if is_idle:
            win.blit(pygame.transform.flip(player_img, True, False), player_rect)
        else:
            win.blit(run_ani_L[animation_count // 10], player_rect)
            
            
    # check for collision between the player and coins
    for coin in coins:
        if player_rect.colliderect(coin.rect):
            coin.kill()
            global balance
            balance += 20
            coin = Coin(random.randint(1, window_width), window_height // 1 - 175)
            coins.add(coin)
            
            
    platforms.draw(win)
    enemies.draw(win)
    coins.draw(win)
    show_score()
    show_coins()
    pygame.display.update()
    

# create function for drawing the main menu
def draw_main_menu():
    # draw background
    win.fill((0, 0, 0))
    win.blit(pygame.transform.scale(bg, (window_width, window_height)), (0, 0))
    

    # draw title
    font = pygame.font.SysFont('comicsans', 80)
    text = font.render('My game', 1, (255, 255, 255))
    win.blit(text, (window_width // 2 - text.get_width() // 2, 100))

    # draw menu options
    font = pygame.font.SysFont('comicsans', 50)
    text = font.render('Press ESC to start', 1, (255, 255, 255))
    win.blit(text, (window_width // 2 - text.get_width() // 2, 300))

    pygame.display.update()

# main game loop
run = True
in_main_menu = True  # add flag for main menu
attacking = False 
attack_frame = 0
facing_right = direction == 0

attack_sprites = pygame.sprite.Group()
attack_sprites.add(attack_sprite)
while run:
    # set frame rate
    clock.tick(FPS)

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if in_main_menu:  # show main menu
        draw_main_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            in_main_menu = False  # exit main menu
    else:

    # movement
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0
        if keys[pygame.K_LEFT]:
            move_x = -player_speed
            direction = -1
            is_idle = False
        elif keys[pygame.K_RIGHT]:
            move_x = player_speed
            direction = 1
            is_idle = False
        else:
            is_idle = True

        if player_rect.bottom >= window_height - 145:  # make the ground higher up
            if keys[pygame.K_SPACE]:
                if not is_jumping:
                    is_jumping = True
                    jump_count = 18
            else:
                is_jumping = False

        if is_jumping:
            move_y = -jump_count
            jump_count -= 0.75
            if move_y < 0:
                move_y += 1

    # add gravity to y movement
        move_y += 1
    # check for collision with left and right edges of the window
        if player_rect.right + move_x > window_width:
            move_x = window_width - player_rect.right
        elif player_rect.left + move_x < 0:
            move_x = -player_rect.left

    # check for collision with top and bottom edges of the window
        if player_rect.bottom + move_y > window_height:
            move_y = window_height - player_rect.bottom
        elif player_rect.top + move_y < 0:
            move_y = -player_rect.top

    # update player position and detect collision with ground
        player_rect.move_ip(move_x, move_y)
        if player_rect.bottom >= window_height - 145:  # make the ground higher up
            player_rect.bottom = window_height - 145
            move_y = 0

    # animation
        if not is_idle:
            animation_count += player_speed
            if animation_count >= 60:
                animation_count = 0
                
    # update player attack rect position
        player_attack_rect.center = player_rect.center

    # attacking 
        if keys[pygame.K_x]:
            attacking = True
            direction = 1 if facing_right else -1

        if attacking:
            if direction == 1:
                if attack_frame < len(attack_ani_R):
                    player_img = attack_ani_R[attack_frame]
                    attack_frame += 1
                else:
                    attack_frame = 0
                    attacking = False
                    player_img = run_ani_R[0]
            elif direction == -1:
                if attack_frame < len(attack_ani_L):
                    player_img = attack_ani_L[attack_frame]
                    attack_frame += 1
                else:
                    attack_frame = 0
                    attacking = False
                    player_img = run_ani_L[0]
                    
        # Check if the enemy collides with the player's attack animation
        for attack_sprite in attack_sprites:
            if pygame.sprite.collide_rect(attack_sprite, enemy):
                enemy.take_damage(10)

        # check if the player is touching a platform
        touching_platform = False
        for platform in platforms:
            if player_rect.colliderect(platform.rect):
                touching_platform = True
                if move_y > 0:  # check if the player is falling
                    player_rect.bottom = platform.rect.top
                    is_jumping = False
                    move_y = 0

        # check if player is on a platform
        on_platform = False
        for platform in platforms:
            if player_rect.colliderect(platform.rect):
                on_platform = True
                if keys[pygame.K_SPACE]:
                    jump_count = 10
                    is_jumping = True

        if not on_platform:
            player_rect.y += 2
            
         # check for collisions between enemy and attack sprites
        if pygame.sprite.spritecollide(enemy, attack_sprites, False):
            enemy.respawn()
            
        coins.update()
        # update enemy sprites
        enemies.update()

        # update platforms
        platforms.update()
        
        # redraw window
        redraw_window() 
        
        

pygame.quit()       
