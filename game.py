import pygame
import random
pygame.init()

#colors  rgb value

#window
width=900
heigth=700
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
exit_button = False
gameWindow=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Snake-Game")





clock=pygame.time.Clock()
font=pygame.font.SysFont(None,50)
def screen_score(text,color,x,y):
    screeen_text=font.render(text,True,color)
    gameWindow.blit(screeen_text,[x,y]) # Window Update

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_button=False
    while not exit_button:
        gameWindow.fill(white)
        screen_score("Swagat h aapka Saanp ki duniya m",black,width/5,heigth/2.5)
        screen_score("Khela Shuru karne k liy Spacebar Dabaiy", black, width / 6, heigth / 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                exit_button = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)


#Game loop
def gameloop():
    # Game variables
    exit_button = False
    game_over = False
    x_cord = 45
    y_cord = 60
    snake_size = 15
    width = 900
    heigth = 700
    fps = 30
    velocity_x = 0  
    velocity_y = 0
    food_x = random.randint(10, width / 2) 
    food_y = random.randint(10, heigth / 2)
    score = 0


    snk_list = []
    snk_length = 1

    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    try:
        f=open("hiscore.txt","x")
        try:
            hiscore=f.read()
        except Exception as e:
            hiscore=30
        f.close()
    except Exception as e:
        f=open("hiscore.txt","r")
        hiscore=f.read()
        f.close()

    while not exit_button:
        if game_over:
            f=open("hiscore.txt","w")
            f.write(str(hiscore))
            gameWindow.fill(white)
            screen_score("Game Over, Press Enter to continue",red,width/5.5,heigth/2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Enable Close Button
                    exit_button = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
                    if event.key==pygame.K_ESCAPE:
                        exit_button=True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # ye fuction kya karega ki jab aap upper close ka button dabay toh vo band ho jaay
                    exit_button = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        exit_button=True
                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0

                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0

                    if event.key==pygame.K_UP:
                        velocity_y=-10 #ye isme posivive y direction neeche hota h
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=+10
                        velocity_x=0

            x_cord=x_cord+velocity_x
            y_cord=y_cord+velocity_y

            if abs(x_cord-food_x)<7 and abs(y_cord-food_y)<7: #ye ab snake exactly to overlap karega ni food pr toh isly absolute value lenge
                score+=10
                food_x = random.randint(10, width / 2)  # /2 s vo thoda center ki taraf rahega
                food_y = random.randint(10, heigth / 2)
                snk_length+=3
                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill(white)  # jab bhi ham esa kuch karte h toh hamko display update karna hota h
            screen_score("Score :"+str(score)+"  Hiscore :"+str(hiscore),red,5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(x_cord)
            head.append(y_cord)
            snk_list.append(head)
            if len(snk_list) >snk_length:
                del snk_list[0]

            if head in snk_list[:-1]: #[:-1] matlab saare elements execpt the last one
                game_over=True

            if x_cord<0 or x_cord>width or y_cord<0 or y_cord>heigth:
                game_over=True
            # ab ham snake banayneg uske liy rectanagle banana h
            # pygame.draw.rect(gameWindow, black, [x_cord, y_cord, snake_size, snake_size]) #iski jagah ham ek fuction banaynge jo ki snake plotkarega or size badayga

            plot_snake(gameWindow,black,snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
    f.close()

welcome()