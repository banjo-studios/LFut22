import pygame, webbrowser, random, math, json
from .threads import loading_screen
from .utils import SceneBase, half_of, draw_rounded_rect, blit_text

font = "./font/bowlby-one.ttf"
arialFont = "./font/Arial.ttf"

class SampleScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))


class TitleScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)

        self.screen = screen
        self.timeLeft = 0
        self.text = ''

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.SwitchToScene(StartScene(self.screen))

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((0, 0, 0))
        if self.timeLeft >= 50:
            self.text = 'Made by'
        else:
            self.text = 'Made'
        self.made_by_text = pygame.font.Font(font, 64).render(self.text, True, (255, 255, 255))
        screen.blit(self.made_by_text, (half_of(screen.get_width()) - 400, half_of(screen.get_height()) - 32))
        self.studio_logo = pygame.image.load("./images/studio_logo.png")
        if self.timeLeft >= 100:
            screen.blit(self.studio_logo, (half_of(screen.get_width()) - 300, half_of(screen.get_height()) - 275))
        else:
            pass

        result = loading_screen(self.timeLeft).start()
        if not result[1]:
            self.timeLeft = result[0]
        else:
            self.SwitchToScene(StartScene(self.screen))

class StartScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))