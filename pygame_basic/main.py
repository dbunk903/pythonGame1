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
# 이벤트 루프
running = True # 게임이 진행중인가? 
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 
            running = False # 게임이 진행중 아님...
    screen.blit(background, (0,0)) # 배경 그리기
    
    screen.blit(character, (character_x_pos,character_y_pos))
    # screen.fill((0,0,255)) 수동을 채울 수도 있다.
    pygame.display.update() # 게임 화면을 다시 그리기
    

# pygame 종료
pygame.quit()