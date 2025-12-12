#12. 똥피하고 사과먹기 게임 pygame_12.py 에 추가 (+ GAME OVER 재시작 버튼)
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기")
clock = pygame.time.Clock()

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))


class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 3

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    if keys[pygame.K_UP]:
      self.rect.y -= self.speed
    if keys[pygame.K_DOWN]:
      self.rect.y += self.speed

    self.rect.clamp_ip(screen.get_rect())


class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = poop_img
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

    self.speed_x = 3
    self.speed_y = 2

  def update(self):
    self.rect.x += self.speed_x
    self.rect.y += self.speed_y

    if self.rect.left < 0 or self.rect.right > WIDTH:
      self.speed_x *= -1
    if self.rect.top < 0 or self.rect.bottom > HEIGHT:
      self.speed_y *= -1


all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

enemy = Enemy(50, 260)
all_sprites.add(enemy)
enemy_group.add(enemy)

apples = [] 

apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30

score = 0
running = True
game_over = False

font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 48)


BUTTON_W, BUTTON_H = 180, 50
restart_button_rect = pygame.Rect(
  (WIDTH - BUTTON_W) // 2,
  (HEIGHT // 2) + 40,
  BUTTON_W,
  BUTTON_H
)

def reset_game():
  global game_over, score, apples, apple_spawn_timer
  game_over = False
  score = 0


  player.rect.center = (WIDTH // 2, HEIGHT // 2)

  enemy.rect.topleft = (50, 260)
  enemy.speed_x = 3
  enemy.speed_y = 2

  apples.clear()
  apple_spawn_timer = 0

def spawn_apple():
  side = random.choice(["left", "right", "top", "bottom"])
  size = 40
  if side == "left":
    x = -size
    y = random.randint(0, HEIGHT - size)
    vx = random.randint(2, 4)
    vy = random.randint(-2, 2)
  elif side == "right":
    x = WIDTH
    y = random.randint(0, HEIGHT - size)
    vx = -random.randint(2, 4)
    vy = random.randint(-2, 2)
  elif side == "top":
    x = random.randint(0, WIDTH - size)
    y = -size
    vx = random.randint(-2, 2)
    vy = random.randint(2, 4)
  else:
    x = random.randint(0, WIDTH - size)
    y = HEIGHT
    vx = random.randint(-2, 2)
    vy = -random.randint(2, 4)

  rect = pygame.Rect(x, y, size, size)
  apples.append({"rect": rect, "vx": vx, "vy": vy})

def draw_restart_button():
  mx, my = pygame.mouse.get_pos()
  hover = restart_button_rect.collidepoint(mx, my)

  btn_color = (240, 240, 240) if not hover else (210, 210, 210)
  border_color = (0, 0, 0)

  pygame.draw.rect(screen, btn_color, restart_button_rect, border_radius=10)
  pygame.draw.rect(screen, border_color, restart_button_rect, 2, border_radius=10)

  label = font.render("RESTART", True, (0, 0, 0))
  lx = restart_button_rect.centerx - label.get_width() // 2
  ly = restart_button_rect.centery - label.get_height() // 2
  screen.blit(label, (lx, ly))


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if restart_button_rect.collidepoint(event.pos):
        reset_game()

  if not game_over:
    all_sprites.update()

    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_apple()

    new_apples = []
    for apple in apples:
      rect = apple["rect"]
      rect.x += apple["vx"]
      rect.y += apple["vy"]

      if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
        continue

      if player.rect.colliderect(rect):
        score += 1
        print("사과 먹음!")
        continue

      new_apples.append(apple)

    apples = new_apples

    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
      print("똥에 닿음! 게임 오버")
      game_over = True


  screen.fill((170, 200, 255))
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

  for apple in apples:
    screen.blit(apple_img, apple["rect"])

  all_sprites.draw(screen)

  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))

  if game_over:

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))

    over_text = big_font.render("GAME OVER", True, (255, 80, 80))
    over_x = (WIDTH - over_text.get_width()) // 2
    over_y = (HEIGHT // 2) - 40
    screen.blit(over_text, (over_x, over_y))

    hint = font.render("Click the button to Restart", True, (255, 255, 255))
    screen.blit(hint, ((WIDTH - hint.get_width()) // 2, over_y + 50))

    draw_restart_button()

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
