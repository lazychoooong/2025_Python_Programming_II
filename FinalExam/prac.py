#4. 이벤트 처리(Event Handling)
import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 4")

running = True

while running:
  # 4. 이벤트 처리
  for event in pygame.event.get():
    if event.type == pygame.QUIT:      # 창 닫기 버튼
      running = False
    if event.type == pygame.KEYDOWN:   # 키 눌림
      print("KEYDOWN:", event.key)
    if event.type == pygame.KEYUP:     # 키에서 손 뗌
      print("KEYUP:", event.key)
    if event.type == pygame.MOUSEBUTTONDOWN:   # 마우스 클릭
      print("Mouse Click:", event.pos)

  # (업데이트 로직이 들어갈 자리)

  # (그리기 로직)
  screen.fill((200, 200, 200))
  pygame.display.flip()

pygame.quit()

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