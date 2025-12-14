import os
import random
import pygame


WIDTH, HEIGHT = 900, 520
FPS = 60

GROUND_Y = HEIGHT - 85
GRAVITY = 0.9
JUMP_VELOCITY = -20

AIR_Y = GROUND_Y - 90

BASE_LIVES = 3
MAX_LIVES = 5

LEVEL_COUNT = 3
LEVEL_DURATION_SEC = 35

# 3단계에서 30초 후 복단이 등장 -> 복단, 덕새 만나야 클리어
BOKDAN_SPAWN_SEC = 30

LEVEL_SPEED = [6, 8, 10]

SPAWN_INTERVAL_MS = 950  # 아이템/위험/하트 등 장애물 스폰

SPAWN_WEIGHTS = {"score": 35, "damage": 60, "heart": 5}

SCORE_ITEMS = [
    ("greek_yogurt", 2),
    ("bagel", 2),
    ("chapssal_donut", 3),
    ("bubble_tea", 4),
]

DAMAGE_ITEMS = [
    ("car", 1),
    ("bus", 1),
    ("subway", 1),
    ("trash1", 1),
    ("trash2", 1),
]


ASSET_DIR = os.path.dirname(os.path.abspath(__file__))


def asset_path(filename: str) -> str:
    return os.path.join(ASSET_DIR, filename)

# 한글이 깨질 것 고려한 장치! 시스템 한글 폰트 후보 중 괜찮은 것으로 돌리기
def get_korean_font_name() -> str:
    candidates = ["Malgun Gothic", "맑은 고딕", "AppleGothic", "NanumGothic", "Noto Sans CJK KR"]
    for name in candidates:
        try:
            pygame.font.SysFont(name, 14)
            return name
        except Exception:
            pass
    return ""


def load_image_or_placeholder(filename: str, size: tuple[int, int], label: str) -> pygame.Surface:
    path = asset_path(filename)
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, size)

    # 혹시 이미지 파일이 없거나 인식 안 되는 것 대비 -> 사각형으로 대체
    # 중간에 이유를 모르겠는데 이미지가 자꾸 인식이 안 돼서 따로 알아보고 추가했습니다..
    surf = pygame.Surface(size, pygame.SRCALPHA)
    surf.fill((255, 255, 255, 180))
    pygame.draw.rect(surf, (30, 30, 30), surf.get_rect(), 2)

    font = pygame.font.SysFont(get_korean_font_name(), 16)
    txt = font.render(label, True, (10, 10, 10))
    surf.blit(txt, txt.get_rect(center=(size[0] // 2, size[1] // 2)))
    return surf


def load_background_scaled(filename: str, size: tuple[int, int]) -> pygame.Surface | None:
    path = asset_path(filename)
    if not os.path.exists(path):
        return None
    img = pygame.image.load(path).convert()
    return pygame.transform.smoothscale(img, size)


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def wrap_text(font: pygame.font.Font, text: str, max_width: int) -> list[str]:
    lines = []
    for paragraph in text.split("\n"):
        if paragraph.strip() == "":
            lines.append("")
            continue

        words = paragraph.split(" ")
        current = words[0]
        for w in words[1:]:
            trial = current + " " + w
            if font.size(trial)[0] <= max_width:
                current = trial
            else:
                lines.append(current)
                current = w
        lines.append(current)
    return lines


# 덕새 (기본/점프할 때 다르게)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_img = load_image_or_placeholder("duksae_run.png", (82, 82), "DUKSAE_RUN")
        self.jump_img = load_image_or_placeholder("duksae_jump.png", (82, 82), "DUKSAE_JUMP")
        self.image = self.run_img
        self.rect = self.image.get_rect(midbottom=(140, GROUND_Y))

        self.vel_y = 0.0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.vel_y = JUMP_VELOCITY
            self.on_ground = False

    def update(self, keys):
        speed_x = 6
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed_x
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed_x
        self.rect.x = clamp(self.rect.x, 10, WIDTH - self.rect.width - 10)

        self.vel_y += GRAVITY
        self.rect.y += int(self.vel_y)

        self.on_ground = False
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

        self.image = self.run_img if self.on_ground else self.jump_img


class Obstacle(pygame.sprite.Sprite):
    SCALE_MULT = 1.35

    def __init__(self, spec: dict, x, y, speed):
        super().__init__()
        self.spec = spec
        self.speed = speed

        base_size = (52, 52) if spec["kind"] != "heart" else (44, 44)
        size = (int(base_size[0] * self.SCALE_MULT), int(base_size[1] * self.SCALE_MULT))

        filename = f"{spec['name']}.png"
        label = spec["name"].upper()

        self.image = load_image_or_placeholder(filename, size, label)
        self.rect = self.image.get_rect(midbottom=(x, y))

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < -10:
            self.kill()

# 복단 (덕새랑 만나면 최종 클리어)
class Bokdan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image_or_placeholder("bokdan.png", (105, 105), "BOKDAN")
        self.rect = self.image.get_rect(midbottom=(WIDTH - 60, GROUND_Y))

# 게임 화면에서 요소들 출력
def draw_hud(screen, hud_font, level, score, lives, time_left_sec):
    text = f"레벨 {level}  |  점수: {score}  |  목숨: {lives}  |  남은 시간: {time_left_sec:02d}s"
    screen.blit(hud_font.render(text, True, (20, 20, 20)), (18, 14))


def draw_center_message(screen, big_font, small_font, title, subtitle=None):
    t = big_font.render(title, True, (20, 20, 20))
    screen.blit(t, t.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20)))
    if subtitle:
        s = small_font.render(subtitle, True, (40, 40, 40))
        screen.blit(s, s.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25)))


def draw_button(screen, font, rect: pygame.Rect, label: str, hovered: bool):
    bg = (230, 230, 230) if not hovered else (210, 210, 210)
    pygame.draw.rect(screen, bg, rect, border_radius=10)
    pygame.draw.rect(screen, (60, 60, 60), rect, 2, border_radius=10)
    txt = font.render(label, True, (20, 20, 20))
    screen.blit(txt, txt.get_rect(center=rect.center))


def draw_story_box(screen, story_font, story_text, box: pygame.Rect):
    pygame.draw.rect(screen, (255, 255, 255), box, border_radius=12)
    pygame.draw.rect(screen, (70, 70, 70), box, 2, border_radius=12)

    padding_x, padding_y = 22, 18
    inner_x = box.x + padding_x
    inner_y = box.y + padding_y
    max_w = box.width - padding_x * 2
    max_h = box.height - padding_y * 2

    lines = []
    for para in story_text.split("\n"):
        if para.strip() == "":
            lines.append("")
        else:
            lines.extend(wrap_text(story_font, para, max_w))

    line_h = 24
    y = inner_y
    bottom_limit = inner_y + max_h

    for line in lines:
        if line == "":
            y += 14
            if y + line_h > bottom_limit:
                break
            continue
        if y + line_h > bottom_limit:
            break
        screen.blit(story_font.render(line, True, (30, 30, 30)), (inner_x, y))
        y += line_h



def choose_obstacle_spec() -> dict:
    bucket = random.choices(
        population=["score", "damage", "heart"],
        weights=[SPAWN_WEIGHTS["score"], SPAWN_WEIGHTS["damage"], SPAWN_WEIGHTS["heart"]],
        k=1,
    )[0]

    if bucket == "score":
        name, pts = random.choice(SCORE_ITEMS)
        return {"kind": "score", "name": name, "value": pts}

    if bucket == "damage":
        name, dmg = random.choice(DAMAGE_ITEMS)
        return {"kind": "damage", "name": name, "value": dmg}

    return {"kind": "heart", "name": "heart", "value": 1}


def choose_spawn_y(spec: dict) -> int:
    if spec["kind"] == "heart":
        return AIR_Y if random.random() < 0.75 else GROUND_Y
    else:
        return AIR_Y if random.random() < 0.35 else GROUND_Y


def spawn_obstacle(obstacles: pygame.sprite.Group, speed: int):
    spec = choose_obstacle_spec()
    x = WIDTH + 60
    y = choose_spawn_y(spec)
    obstacles.add(Obstacle(spec, x, y, speed))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("덕새의 복단이를 찾아서")
    clock = pygame.time.Clock()

    font_name = get_korean_font_name()

    story_font = pygame.font.SysFont(font_name, 18)
    hud_font = pygame.font.SysFont(font_name, 22)
    small_font = pygame.font.SysFont(font_name, 18)
    big_font = pygame.font.SysFont(font_name, 34)

    bg_img = load_background_scaled("background.png", (WIDTH, HEIGHT))

    story_text = (
        "덕새의 단짝친구 복단이는 학기 중과 방학을 가리지 않고\n"
        "열심히 공부하는 모범생이다.\n\n"
        "오늘도 학교에 있는 복단이와 같이 과제를 하러,\n"
        "덕새는 둥지를 떠나 학교로 등교하는 여정을 시작하는데...\n\n"
        "맛있는 음식은 먹으면 점수가 올라간다!\n"
        "자동차나 버스나 지하철, 그리고 쓰레기는 먹으면 안 돼!\n"
        "복단이가 학교에서 기다리고 있을 거야.. 얼른 가자!"
    )

    state = "STORY" 

    level = 1
    score = 0
    lives = BASE_LIVES
    reached_level = 1

    game_started_ms = pygame.time.get_ticks()
    total_play_time_sec = 0
    level_start_ms = pygame.time.get_ticks()

    player = Player()
    obstacles = pygame.sprite.Group()
    last_spawn_ms = 0

    # 복단이 관련
    bokdan = None
    bokdan_spawned = False

    start_btn = pygame.Rect(WIDTH // 2 - 120, HEIGHT - 110, 240, 56)

    def reset_game(now_ms: int):
        nonlocal level, score, lives, reached_level
        nonlocal game_started_ms, total_play_time_sec, level_start_ms, last_spawn_ms
        nonlocal bokdan, bokdan_spawned

        level = 1
        score = 0
        lives = BASE_LIVES
        reached_level = 1

        obstacles.empty()
        player.rect.midbottom = (140, GROUND_Y)
        player.vel_y = 0

        last_spawn_ms = now_ms
        level_start_ms = now_ms

        game_started_ms = now_ms
        total_play_time_sec = 0

        bokdan = None
        bokdan_spawned = False

    while True:
        clock.tick(FPS)
        now_ms = pygame.time.get_ticks()

        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

            if state == "STORY":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    reset_game(now_ms)
                    state = "PLAY"

            elif state == "PLAY":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.jump()

            elif state == "LEVEL_CLEAR":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if level < LEVEL_COUNT:
                        level += 1
                        reached_level = level

                        obstacles.empty()
                        player.rect.midbottom = (140, GROUND_Y)
                        player.vel_y = 0

                        last_spawn_ms = now_ms
                        level_start_ms = now_ms

                        bokdan = None
                        bokdan_spawned = False

                        state = "PLAY"
                    else:
                        state = "PLAY"  # 3레벨은 복단이 만나야 클리어

            elif state in ("GAME_OVER", "GAME_CLEAR"):
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    state = "STORY"

        if state == "STORY":
            if mouse_clicked and start_btn.collidepoint(mouse_pos):
                reset_game(now_ms)
                state = "PLAY"

        if state == "PLAY":
            total_play_time_sec = (now_ms - game_started_ms) // 1000
            speed = LEVEL_SPEED[level - 1]

            keys = pygame.key.get_pressed()
            player.update(keys)

            elapsed_sec = (now_ms - level_start_ms) // 1000

            if now_ms - last_spawn_ms >= SPAWN_INTERVAL_MS:
                # 복단이 등장 후 장애물 스폰 멈추기
                if not (level == 3 and bokdan_spawned):
                    spawn_obstacle(obstacles, speed)
                last_spawn_ms = now_ms

            obstacles.update()

            # 3레벨 30초 이후 복단이 등장
            if level == 3 and (not bokdan_spawned) and elapsed_sec >= BOKDAN_SPAWN_SEC:
                bokdan = Bokdan()
                bokdan_spawned = True

            # 장애물 충돌
            hits = pygame.sprite.spritecollide(player, obstacles, True)
            for ob in hits:
                spec = ob.spec
                if spec["kind"] == "score":
                    score += spec["value"]
                elif spec["kind"] == "heart":
                    lives = min(MAX_LIVES, lives + spec["value"])
                elif spec["kind"] == "damage":
                    lives -= spec["value"]

            if lives <= 0:
                state = "GAME_OVER"

            # 복단이와 충돌하면 게임 클리어
            if bokdan_spawned and bokdan is not None:
                if player.rect.colliderect(bokdan.rect):
                    state = "GAME_CLEAR"

            # 레벨 시간 종료 처리
            if level < 3 and elapsed_sec >= LEVEL_DURATION_SEC and state == "PLAY":
                state = "LEVEL_CLEAR"

        if state == "STORY":
            screen.fill((135, 206, 235))

            title = big_font.render("덕새의 복단이를 찾아서", True, (20, 20, 20))
            screen.blit(title, title.get_rect(center=(WIDTH // 2, 70)))

            hint_text = "Enter로 시작 / 방향키 ← → 로 이동 / Space로 점프"
            hint_surf = small_font.render(hint_text, True, (60, 60, 60))

            hint_y = start_btn.y - 30
            box_top = 120
            box_bottom = hint_y - 18
            box_h = max(200, box_bottom - box_top)
            box = pygame.Rect(80, box_top, WIDTH - 160, box_h)

            draw_story_box(screen, story_font, story_text, box)
            screen.blit(hint_surf, hint_surf.get_rect(center=(WIDTH // 2, hint_y)))

            hovered = start_btn.collidepoint(mouse_pos)
            draw_button(screen, big_font, start_btn, "START", hovered)

        else:
            if bg_img is not None:
                screen.blit(bg_img, (0, 0))
            else:
                screen.fill((135, 206, 235))

            pygame.draw.rect(screen, (220, 220, 220), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
            pygame.draw.line(screen, (140, 140, 140), (0, GROUND_Y), (WIDTH, GROUND_Y), 2)

            obstacles.draw(screen)
            screen.blit(player.image, player.rect)

            if bokdan_spawned and bokdan is not None:
                screen.blit(bokdan.image, bokdan.rect)

            if state == "PLAY":
                elapsed_sec = (pygame.time.get_ticks() - level_start_ms) // 1000
                time_left = max(0, LEVEL_DURATION_SEC - elapsed_sec) if level < 3 else 0
                draw_hud(screen, hud_font, level, score, lives, time_left)

                if level == 3 and not bokdan_spawned:
                    remain = max(0, BOKDAN_SPAWN_SEC - elapsed_sec)
                    msg = small_font.render(f"복단이가 {remain}초 뒤에 나타나요!", True, (40, 40, 40))
                    screen.blit(msg, (WIDTH - msg.get_width() - 18, 44))
                elif level == 3 and bokdan_spawned:
                    msg = small_font.render("복단이를 찾아가서 만나세요! →", True, (40, 40, 40))
                    screen.blit(msg, (WIDTH - msg.get_width() - 18, 44))

            if state == "LEVEL_CLEAR":
                draw_center_message(screen, big_font, small_font, f"{level}단계 클리어! ", "Enter로 다음 단계")

            elif state == "GAME_OVER":
                draw_center_message(screen, big_font, small_font, "GAME OVER...", "Enter로 스토리 화면으로")
                info = small_font.render(f"도달 레벨: {reached_level}  |  점수: {score}", True, (60, 60, 60))
                screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75)))

            elif state == "GAME_CLEAR":
                draw_center_message(screen, big_font, small_font, "축하합니다! 모든 단계 클리어!", "Thanks for playing!")
                info = small_font.render(f"최종 점수: {score}  |  플레이시간: {total_play_time_sec}s", True, (60, 60, 60))
                screen.blit(info, info.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 85)))
                hint = small_font.render("Enter로 스토리 화면으로", True, (60, 60, 60))
                screen.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 115)))

        pygame.display.flip()


if __name__ == "__main__":
    main()
