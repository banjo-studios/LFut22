import pygame, webbrowser, random, math, json
from .threads import loading_screen
from .utils import SceneBase, half_of, draw_rounded_rect, blit_text
from pygame import mixer


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
        self.buttons_interact = None
        self.init()

    def init(self):
        self.buttons = []
        self.start_bg = pygame.image.load("./images/game_menu.png")
        # social buttons
        self.socialbutton1 = pygame.rect.Rect(self.screen.get_width() - 80, 10, 70, 70)
        self.socialbutton2 = pygame.rect.Rect(self.screen.get_width() - 160, 10, 70, 70)
        self.socialbutton3 = pygame.rect.Rect(self.screen.get_width() - 240, 10, 70, 70)
        self.github_image = pygame.image.load("./images/rsz_github.png")
        self.discord_image = pygame.image.load("./images/rsz_discord.png")
        self.twitter_image = pygame.image.load("./images/rsz_twitter.png")
        self.buttons.append(self.socialbutton1)
        self.buttons.append(self.socialbutton2)
        self.buttons.append(self.socialbutton3)

        # the quit button
        self.quit_button = pygame.rect.Rect(265, self.screen.get_height() - 200, 269, 80)
        self.buttons.append(self.quit_button)
        self.quit_button_text = pygame.font.Font(font, 38).render("Quit game", True, (0, 0, 0))

        self.play_button = pygame.rect.Rect(525, self.screen.get_height() - 885, 120, 60)
        self.buttons.append(self.play_button)
        self.play_button_text = pygame.font.Font(font,38).render("Play", True, (0, 0, 0))

        # Background Sound
        mixer.music.load('Stadium_Noises.mp3')
        mixer.music.play(-1)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                for button in self.buttons:
                    if button.collidepoint(mouse_pos):
                        self.buttons_interact = button
                        break
                    else:
                        self.buttons_interact = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.play_button.collidepoint(mouse_pos):
                    self.SwitchToScene(OnlineScene(self.screen))

                if self.quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
                if self.socialbutton1.collidepoint(mouse_pos):
                    webbrowser.open("https://github.com/banjo-studios/project-skate")
                    exit()
                if self.socialbutton2.collidepoint(mouse_pos):
                    webbrowser.open("https://discord.gg/6v4GR23cqs")
                    exit()
                if self.socialbutton3.collidepoint(mouse_pos):
                    webbrowser.open("https://twitter.com/thebanjostudios")
                    exit()

    def Update(self):
        pass

    def Render(self, screen):
        self.init()
        screen.blit(self.start_bg, (0, 0))

        for button in self.buttons:
            if button == self.buttons_interact:
                draw_rounded_rect(screen, button, (136, 136, 136), 18)
            else:
                draw_rounded_rect(screen, button, (255, 255, 255), 18)


            screen.blit(self.github_image, (self.screen.get_width() - 75, 15))
            screen.blit(self.discord_image, (self.screen.get_width() - 152.5, 17.5))
            screen.blit(self.twitter_image, (self.screen.get_width() - 237, 14))
            screen.blit(self.quit_button_text, (288, self.screen.get_height() - 187))
            screen.blit(self.play_button_text, (535, self.screen.get_height() - 885))


class OnlineScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen
        self.interacting_button = None

    def init(self):
        self.buttons = []
        self.back_button = pygame.rect.Rect(265, self.screen.get_height() - 200, 269, 80)
        self.buttons.append(self.back_button)
        self.back_button_text = pygame.font.Font(font, 38).render("Back", True, (0, 0, 0))


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if self.back_button.collidepoint(mouse_pos):
                self.SwitchToScene(StartScene(self.screen))

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))

        for button in self.buttons:
            if button == self.interacting_button:
                draw_rounded_rect(screen, button, (136, 136, 136), 18)
            else:
                draw_rounded_rect(screen, button, (255, 255, 255), 18)

            screen.blit(self.back_button_text, (288, self.screen.get_height() - 187))

