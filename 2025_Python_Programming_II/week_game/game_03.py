# 똥피하고 사과먹기 : py_game12.py 를 기반으로 수정했습니다!
# 기존의 빨간 사과를 먹으면 점수가 1점 상승하지만,
# 10초마다 생성되는 새로운 객체 '황금사과'를 '덕새'가 먹으면 점수가 5점 상승하도록 추가적으로 구현해 두었습니다.
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기")
clock = pygame.time.Clock()

# 이미지 로드
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

poop_img = pygame.image.load("poop.png")
poop_img = pygame.transform.scale(poop_img, (40, 40))

gold_img = pygame.image.load("goldenApple.png")          
gold_img = pygame.transform.scale(gold_img, (40, 40))    


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
enemy = Enemy(50, 260)

all_sprites.add(player)
all_sprites.add(enemy)
enemy_group.add(enemy)

apples = []
golden_apples = []  # 황금사과 리스트 생성

apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 30

gold_spawn_timer = 0
GOLD_SPAWN_INTERVAL = 60 * 10
# 스폰 타이머에 황금사과 추가, 10초마다 하나씩 생성

score = 0
final_score = 0
running = True
game_over = False

font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 48)
mid_font = pygame.font.SysFont(None, 30)

BUTTON_W, BUTTON_H = 180, 50
restart_button_rect = pygame.Rect(
  (WIDTH - BUTTON_W) // 2,
  (HEIGHT // 2) + 70,
  BUTTON_W,
  BUTTON_H
)

def reset_game():
  global game_over, score, final_score
  global apples, golden_apples
  global apple_spawn_timer, gold_spawn_timer

  game_over = False
  score = 0
  final_score = 0

  player.rect.center = (WIDTH // 2, HEIGHT // 2)

  enemy.rect.topleft = (50, 260)
  enemy.speed_x = 3
  enemy.speed_y = 2

  apples.clear()
  golden_apples.clear()
  apple_spawn_timer = 0
  gold_spawn_timer = 0

# 황금사과 / 일반사과 생성되는 방식은 같으므로 묶어서 함수 만들기
def spawn_moving_apple(target_list, size=40, speed_min=2, speed_max=4):
  side = random.choice(["left", "right", "top", "bottom"])

  if side == "left":
    x = -size
    y = random.randint(0, HEIGHT - size)
    vx = random.randint(speed_min, speed_max)
    vy = random.randint(-2, 2)
  elif side == "right":
    x = WIDTH
    y = random.randint(0, HEIGHT - size)
    vx = -random.randint(speed_min, speed_max)
    vy = random.randint(-2, 2)
  elif side == "top":
    x = random.randint(0, WIDTH - size)
    y = -size
    vx = random.randint(-2, 2)
    vy = random.randint(speed_min, speed_max)
  else:
    x = random.randint(0, WIDTH - size)
    y = HEIGHT
    vx = random.randint(-2, 2)
    vy = -random.randint(speed_min, speed_max)

  rect = pygame.Rect(x, y, size, size)
  target_list.append({"rect": rect, "vx": vx, "vy": vy})


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


def update_flying_items(item_list, eat_score):
  global score
  new_list = []

  for item in item_list:
    rect = item["rect"]
    rect.x += item["vx"]
    rect.y += item["vy"]

    if rect.right < 0 or rect.left > WIDTH or rect.bottom < 0 or rect.top > HEIGHT:
      continue

    if player.rect.colliderect(rect):
      score += eat_score
      continue

    new_list.append(item)

  return new_list


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if game_over and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if restart_button_rect.collidepoint(event.pos):
        reset_game()

    if event.type == pygame.KEYDOWN:
      if game_over and event.key == pygame.K_RETURN:
        reset_game()

  if not game_over:
    all_sprites.update()

    apple_spawn_timer += 1
    if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
      apple_spawn_timer = 0
      spawn_moving_apple(apples)

    gold_spawn_timer += 1
    if gold_spawn_timer >= GOLD_SPAWN_INTERVAL:
      gold_spawn_timer = 0
      spawn_moving_apple(golden_apples)

    apples = update_flying_items(apples, eat_score=1)
    golden_apples = update_flying_items(golden_apples, eat_score=5)

    hits = pygame.sprite.spritecollide(player, enemy_group, False)
    if hits:
      final_score = score
      game_over = True


  screen.fill((170, 200, 255))
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

  for apple in apples:
    screen.blit(apple_img, apple["rect"])

  for g in golden_apples:
    screen.blit(gold_img, g["rect"])

  all_sprites.draw(screen)


  text = font.render(f"Score: {score:03d}", True, (0, 0, 0))
  screen.blit(text, (10, 10))

  if game_over:
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))
    screen.blit(overlay, (0, 0))

    over_text = big_font.render("GAME OVER", True, (255, 80, 80))
    over_x = (WIDTH - over_text.get_width()) // 2
    over_y = (HEIGHT // 2) - 80
    screen.blit(over_text, (over_x, over_y))

    score_line = mid_font.render(f"Total Score: {final_score:03d}", True, (255, 255, 255))
    sx = (WIDTH - score_line.get_width()) // 2
    sy = over_y + 55
    screen.blit(score_line, (sx, sy))

    hint = font.render("Click the button or Press Enter", True, (255, 255, 255))
    screen.blit(hint, ((WIDTH - hint.get_width()) // 2, sy + 35))

    draw_restart_button()

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
