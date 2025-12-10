# 시험문제는 세 문제 이상 (3 or 5문제 중 고민 중 /
# 5문제 출제 시 상속+다형성, Tkinter, 파이게임 세 문제
# + 나머지 두 문제는 아마 점수 주기용인 쉬운 문제일 듯)

# 파이게임은 주어진 9번 예제를 바탕으로 조금씩 develop (추가 변형)하는 것
# 예시 : 
# - “GAME OVER” 텍스트 띄우면서, 재시작(버튼 만들어도 됨)
# - 점수 계산 기능 추가
# - 아이디어 아무거나 추가 (주석달기)
# - 플레이어 혹은 객체가 여러개 생성되게끔
# - 그리고 그 객체가 움직일 수 있게 (랜덤, 좌우, 위아래)
# - 사운드추가 (액션)
# - 객체가 부딪혔을 때, 변수가 변경되도록
# 등등...

#1. pygame 초기화 & 종료
#2. 화면(디스플레이) 만들기
#3. 게임 루프(Game Loop)의 구조
#4. 이벤트 처리(Event Handling)
#5. 실시간 키 입력(get_pressed)
#6. Surface와 Rect
#6-1. Surface와 Rect(이미지적용버전)
#7. 그리기(Drawing)
#8. 프레임 속도(FPS) 제어
#9. Sprite 클래스 & 그룹 (중급 기본기)

# 파이게임 9번 : 움직임 구현
# 10번 : 충돌 구현 - 게임오버, 점수
# 11번 : 이미지 적용 + 사과 움직임 + 리스타트 구현
# 12번 : 사과 여러 개 관리, 사과 바깥 쪽에서 스폰해오기


#---------------------------------------------------------------
# 파이게임 디벨롭 예시 1 : 목숨 시스템 추가

# lives = 3 (예: 3번까지 똥에 닿을 수 있음)
# 똥에 닿으면:
# lives -= 1
# 플레이어/적 위치 초기화
# lives == 0이면 game_over = True
# 화면에 Lives: 3 같이 표시
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하고 사과먹기 - 목숨 시스템")

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

# 여러 개 사과는 귀찮으면 생략하고, 여기선 단일 사과만 두어도 됨
apples = []
apple_spawn_timer = 0
APPLE_SPAWN_INTERVAL = 60

def spawn_apple():
    size = 40
    rect = pygame.Rect(
        random.randint(0, WIDTH - size),
        random.randint(0, HEIGHT - size),
        size, size
    )
    apples.append(rect)

score = 0
lives = 3          # ★ 목숨 개수
running = True
game_over = False

font = pygame.font.SysFont(None, 24)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_RETURN:
                # 게임 전체 리셋
                game_over = False
                score = 0
                lives = 3
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                enemy.rect.topleft = (50, 260)
                enemy.speed_x, enemy.speed_y = 3, 2
                apples.clear()
                apple_spawn_timer = 0

    if not game_over:
        all_sprites.update()

        # 사과 스폰
        apple_spawn_timer += 1
        if apple_spawn_timer >= APPLE_SPAWN_INTERVAL:
            apple_spawn_timer = 0
            spawn_apple()

        # 사과 충돌 처리
        new_apples = []
        for rect in apples:
            if player.rect.colliderect(rect):
                score += 1
                print("사과 먹음!")
                # 먹힌 사과는 삭제 (다시 리스트에 안 넣음)
            else:
                new_apples.append(rect)
        apples = new_apples

        # ★ 똥 충돌 처리: 목숨 감소 + 리스폰
        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            lives -= 1
            print(f"똥에 닿음! 남은 목숨: {lives}")

            if lives <= 0:
                print("목숨 0! 게임 오버")
                game_over = True
            else:
                # 플레이어/적 위치만 리셋 후 계속 플레이
                player.rect.center = (WIDTH // 2, HEIGHT // 2)
                enemy.rect.topleft = (50, 260)
                enemy.speed_x, enemy.speed_y = 3, 2

    # ----------- 그리기 -----------
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    for rect in apples:
        screen.blit(apple_img, rect)

    all_sprites.draw(screen)

    # 점수 / 목숨 출력
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 30))

    if game_over:
        over_text = font.render("GAME OVER (Press Enter)", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
 

# --------------------------------------------

# 2. 적(Enemy) 여러 개 추가 예제
# Enemy 클래스는 그대로.
# for문이나 리스트를 이용해서 여러 개 생성.
# enemy_group에 전부 넣기 → Sprite 충돌은 같은 코드 재사용.
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("똥피하기 - 여러 적")

clock = pygame.time.Clock()

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
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.image = poop_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

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

# ★ 여러 적 생성 (랜덤 위치, 랜덤 속도)
for _ in range(5):  # 적 5마리
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    speed_x = random.choice([-3, -2, 2, 3])
    speed_y = random.choice([-3, -2, 2, 3])
    enemy = Enemy(x, y, speed_x, speed_y)
    all_sprites.add(enemy)
    enemy_group.add(enemy)

running = True
game_over = False
font = pygame.font.SysFont(None, 24)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_RETURN:
                # 간단히: 프로그램 다시 실행한다고 가정하거나,
                # 여기에서 위치/스피드 재설정하면 됨 (구현 생략 가능)
                game_over = False
                player.rect.center = (WIDTH // 2, HEIGHT // 2)

    if not game_over:
        all_sprites.update()
        # ★ 여러 적과 한 번에 충돌 체크
        hits = pygame.sprite.spritecollide(player, enemy_group, False)
        if hits:
            print("적들과 충돌! 게임 오버")
            game_over = True

    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    all_sprites.draw(screen)

    if game_over:
        over_text = font.render("GAME OVER (Press Enter)", True, (255, 0, 0))
        over_x = (WIDTH - over_text.get_width()) // 2
        over_y = (HEIGHT - over_text.get_height()) // 2
        screen.blit(over_text, (over_x, over_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
