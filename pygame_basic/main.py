from turtle import width
import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width,screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("BUBBLE BUBBLE") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load('/Users/jeroz/Library/Mobile Documents/com~apple~CloudDocs/Documents/AllCode/NaDo/pythonGame/pygame_basic/pythonGameBackground.png')

# 캐릭터(Sprite) 불러오기
character = pygame.image.load('/Users/jeroz/Library/Mobile Documents/com~apple~CloudDocs/Documents/AllCode/NaDo/pythonGame/pygame_basic/character.png')
character_size = character.get_rect().size #가로,세로 크기를 (이미지의) 크기를 구해옴옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2 # 화면 가로의 절반 크기에 위치
character_y_pos = screen_height - character_height # 세로 크기 가장 아래에 

# 이동할 좌표 
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가? 
while running:

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
                to_x -= 20
            elif event.key == pygame.K_RIGHT: # character goes right
                to_x += 20
            elif event.key == pygame.K_UP: # character goes up
                to_y -= 20
            elif event.key == pygame.K_DOWN: # character goes down
                to_y += 20
        if event.type == pygame.KEYUP: # 키보드 입력값이 있다가 없는 경우 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

        character_x_pos += to_x
        character_y_pos += to_y
        
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
        
                 
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos))
    # screen.fill((0,0,255)) 수동을 채울 수도 있다.
    pygame.display.update() # 게임 화면을 다시 그리기
    

# pygame 종료
pygame.quit()