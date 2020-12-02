import pygame
import random

def mask():
    #초기화 #중요!
    pygame.init() 

    score = 0
    #FPS
    clock = pygame.time.Clock()

    #화면 크기 설정
    screenWidth = 480 #가로크기
    screenHeight = 640 #세로크기

    screen = pygame.display.set_mode((screenWidth,screenHeight))  #가로, 세로

    #배경이미지
    background = pygame.image.load("background.png")

    #캐릭터
    character = pygame.image.load("character.png")
    characterSize = character.get_rect().size  #img크기 불러옴
    characterWidth = characterSize[0]
    characterHeight = characterSize[1]
    characterXpos = (screenWidth / 2) - (characterWidth / 2)
    characterYpos = screenHeight - characterHeight

    #이동할 좌표
    toX = 0
    toY = 0

    #이동속도
    characterSpeed = 0.6

    #난수 생성 - 음식 생성용
    randomNumber = 1
    poSpeed = 8

    #마스크
    enemy = pygame.image.load("enemy.png")
    enemySize = enemy.get_rect().size
    enemyWidth = enemySize[0]
    enemyHeight = enemySize[1]
    enemyXpos = 200
    enemyYpos = 100

    #적
    birus = pygame.image.load("birus.png")
    birusSize= birus.get_rect().size
    birusWidth = birusSize[0]
    birusHeight = birusSize[1]
    birusXpos = 200
    birusYpos = 100

    #Title
    pygame.display.set_caption("마스크 게임")

    #폰트 정의
    game_font = pygame.font.Font(None,40) #폰트, 크기

    #게임 플레이 총 시간
    totalTime = 10
    startTicks = pygame.time.get_ticks()
    #Event
    running = True
    while running:  #실행창
        dt = clock.tick(20)
        #print("fps: " + str(clock.get_fps()))
        
        #캐릭터가 1초 100만큼 이동:
        #10FPs : 1초동안 10번 작동 -> 10만큼~~~ 100
        #20FPs : 1초동안 20번 작동 -> 5만큼~~~ 100
        for event in pygame.event.get(): #어떤 이벤트 발생했는지 판단함
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    toX -= characterSpeed
                if event.key == pygame.K_RIGHT:
                    toX += characterSpeed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    toX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    toY = 0 
        
        #캐릭터 이동 & 프레임맞추기
        characterXpos += toX * dt
        characterYpos += toY * dt
        
        
        #경계 설정-가로
        if characterXpos < 0:
            characterXpos = 0
        elif characterXpos > screenWidth - characterWidth:
            characterXpos = screenWidth - characterWidth
        #경계 설정-세로
        if characterYpos < 0:
            characterYpos = 0
        elif characterYpos > screenHeight - characterHeight:
            characterYpos = screenHeight - characterHeight
        
        
        randomNumber = random.randrange(1,200)
        randomNumber2 = random.randrange(1,440)
        randomNumber3 = random.randrange(1,200)
        randomNumber4 = random.randrange(1,440)
        if enemyYpos > 640:
            enemyYpos = randomNumber
            enemyXpos = randomNumber2
            score += 1
            poSpeed += 2
        
        enemyYpos += poSpeed
        
        if birusYpos > 640:
            birusYpos = randomNumber3
            birusXpos = randomNumber4
            
        birusYpos += poSpeed
            

        #충돌
        characterRect = character.get_rect()
        characterRect.left = characterXpos
        characterRect.top = characterYpos
        
        enemyRect = enemy.get_rect()
        enemyRect.left = enemyXpos
        enemyRect.top = enemyYpos

        birusRect = birus.get_rect()
        birusRect.left = birusXpos
        birusRect.top = birusYpos
        
         
        
        if characterRect.colliderect(enemyRect):
            enemyYpos = 9000000
            print("냠냠")
               
            running = True
        if enemyRect.top >= screen.get_rect().bottom :
            running = False

        if characterRect.colliderect(birusRect):
            birusYpos = 9000000
            running = False

        if birusRect.top >= screen.get_rect().bottom:
            running = True

        #타이머
        elapsedTime = (pygame.time.get_ticks())/1000
        #경과시간이 ms 이므로 초단위로 표시
        if totalTime - elapsedTime > 30:
            print("성공!!!")
            running = False
        timer = game_font.render(str(int(elapsedTime)), True, (255,255,255))
        # 출력할 글자, , 색상
        scoree = game_font.render(str(score), True, (200,200,200))
      

        
        
        #screen.fill((0,0,255))
        screen.blit(background, (0,0)) 
        screen.blit(character, (characterXpos , characterYpos))
        screen.blit(enemy, (enemyXpos , enemyYpos))
        screen.blit(birus, (birusXpos , birusYpos))
        screen.blit(timer, (10,10))
        screen.blit(scoree, (10,30))
        pygame.display.update() #화면 새로고침

    pygame.quit()    #pygame 종료
