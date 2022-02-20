import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기 
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("BUBBLE BUBBLE") # 게임 이름

