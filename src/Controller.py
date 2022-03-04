import pygame

class Controller:

    def __init__(self):
        pygame.init()
        
        #Get and store the monitor's resolution. Decrease WINDOW_HEIGHT to account for taskbar
        screenInfo = pygame.display.Info()
        self.WINDOW_WIDTH = screenInfo.current_w
        self.WINDOW_HEIGHT = screenInfo.current_h * 0.9

        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH,self.WINDOW_HEIGHT),pygame.RESIZABLE)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((255,255,255))
        self.font = pygame.font.Font("freesansbold.ttf",30)

    def startScreen(self):
        startImg = pygame.transform.scale(pygame.image.load("assets/startscreen.jpeg"),(self.WINDOW_WIDTH,self.WINDOW_HEIGHT))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.runTetris()
            self.screen.blit(self.background,(0,0))
            self.screen.blit(startImg,(0,0))
            pygame.display.flip()
            
                


    def runTetris(self):
        pass

    def endScreen(self):
        pass