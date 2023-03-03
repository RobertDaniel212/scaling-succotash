import pygame
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

class Platform(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.image = pygame.image.load("platform.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 20, self.image.get_height() // 20))
        self.rect = self.image.get_rect()
        self.rect.x = window_width
        self.rect.y = window_height

        

# create a group for platforms
platforms = pygame.sprite.Group()

# create some platforms and add them to the group
platforms.add(Platform(40,250))
platforms.add(Platform(247,200))
platforms.add(Platform(435,250))
platforms.add(Platform(630,200))

pygame.display.update()

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
 
# Attack animation for the LEFT
attack_ani_L = [pygame.transform.flip(attack_ani_R[i], True, False) for i in range(len(attack_ani_R))]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprite_rotmg_enemy0.png")
        self.image = pygame.transform.scale(self.image, (64, 64))  # optional, adjust size if needed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 2  # adjust velocity if needed
        self.direction = "right"
        self.rect.center = (window_width // 2.5, window_height // 1 - 175)  # make the player start higher up
    
    def move(self, dx, dy):
        self.move_single_axis(dx, dy)
    
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                    self.direction = "left"
                if dx < 0:
                    self.rect.left = platform.rect.right
                    self.direction = "right"
                if dy > 0:
                    self.rect.bottom = platform.rect.top
                if dy < 0:
                    self.rect.top = platform.rect.bottom

    def update(self):
        if self.direction == "right":
            self.rect.x += self.vel
            if self.rect.right > window_width:
                self.direction = "left"
        elif self.direction == "left":
            self.rect.x -= self.vel
            if self.rect.left < 0:
                self.direction = "right"

    def draw(self, surface):
        surface.blit(self.image, self.rect)


enemies = pygame.sprite.Group()
enemies.add(Enemy(300, 390))


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



# load background image
bg = pygame.image.load('ORS97Z0.jpg').convert()
bg = pygame.transform.scale(bg, (window_width, window_height))



# create function for drawing the window
def redraw_window():
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

    platforms.draw(win)
    enemies.draw(win)

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
    text = font.render('Press SPACE to start', 1, (255, 255, 255))
    win.blit(text, (window_width // 2 - text.get_width() // 2, 300))

    pygame.display.update()


# main game loop
run = True
in_main_menu = True  # add flag for main menu
attacking = False 
attack_frame = 0
facing_right = direction == 0
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
        if keys[pygame.K_SPACE]:
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

        enemies.update()
        # redraw window
        
        redraw_window()
       
pygame.quit()       
