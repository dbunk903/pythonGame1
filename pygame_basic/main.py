import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("BUBBLE BUBBLE") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 이동속도
character_speed = 0.6



# 배경 이미지 불러오기
background = pygame.image.load('/Users/jeroz/Library/Mobile Documents/com~apple~CloudDocs/Documents/AllCode/NaDo/pythonGame/pygame_basic/pythonGameBackground.png')

# 캐릭터(Sprite) 불러오기
character = pygame.image.load('/Users/jeroz/Library/Mobile Documents/com~apple~CloudDocs/Documents/AllCode/NaDo/pythonGame/pygame_basic/character.png')
character_size = character.get_rect().size #가로,세로 크기를 (이미지의) 크기를 구해옴옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height # 세로 크기 가장 아래에 

# Enemy 
enemy = pygame.image.load('/Users/jeroz/Library/Mobile Documents/com~apple~CloudDocs/Documents/AllCode/NaDo/pythonGame/pygame_basic/enemy.png')
enemy_size = enemy.get_rect().size #가로,세로 크기를 (이미지의) 크기를 구해옴옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 세로 크기 가장 아래에 

# 이동할 좌표 
to_x = 0
to_y = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 포늩 객체 생성 (폰트, 크기) 

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 가져오기

# 이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    dt = clock.tick(60) # delta , 게임 화면의 초당 프레임 수를 설정 
    # 확인 print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
            running = False # 게임이 진행중 아님...
        '''
        Game 에서의 이동이란 좌표의 이동이다
        to x 
        to y 사용
        '''
        if event.type == pygame.KEYDOWN: # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT: # character goes left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # character goes right
                to_x += character_speed
            elif event.key == pygame.K_UP: # character goes up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # character goes down
                to_y += character_speed
        if event.type == pygame.KEYUP: # 키보드 입력값이 있다가 없는 경우 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        character_x_pos += to_x * dt
        character_y_pos += to_y * dt 
        
        # 가로 경계값 처리 
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        # 세로 경계값 처리
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height -  character_height
        
        # 충돌 처리를 위한 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        enemy_rect = enemy.get_rect()
        enemy_rect.left = enemy_x_pos #enemy는 변화 없어서 쓰일 일이 없다.
        enemy_rect.top = enemy_y_pos
        
        # 충돌 체크
        if character_rect.colliderect(enemy_rect):
            print("충돌했어요")
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos))

    screen.blit(enemy, (enemy_x_pos,enemy_y_pos))

    # screen.fill((0,0,255)) 수동을 채울 수도 있다.

    # 타이머 집어 넣기
    # 경과 시간 계산 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간을 1000으로 나누어서 초 단위 표시 (milisecond 이기 때문에 -> sec)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # => 출력할 글자, 시간, True, 글자 색상
    screen.blit(timer, (10,10))
    
    # 만약 시간이 0 이하라면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False 
    
    pygame.display.update() # 게임 화면을 다시 그리기
# 잠시 대기... 
pygame.time.delay(2000)
# pygame 종료
pygame.quit()