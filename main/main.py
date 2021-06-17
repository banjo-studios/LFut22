import pygame, sys, json, os
from scene import scene
from setup import main_setup

main_setup()

if int(sys.version[0]) < 3:
    print("Error detected. Wrong python version.")

nameOfGame = "LFut22"
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(nameOfGame, nameOfGame)
#pygame.display.set_icon(pygame.image.load('./images/logo.png'))
settings_data = json.load(open("../player/settings.json", "r+"))

if settings_data['load_starting_screen']:
    active_scene = scene.TitleScene(screen)
else:
    active_scene = scene.StartScene(screen)

while active_scene is not None:
    pressed_keys = pygame.key.get_pressed()

    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_F4 and alt_pressed:
                quit_attempt = True

        if quit_attempt:
            active_scene.Terminate()
        else:
            filtered_events.append(event)

    active_scene.ProcessInput(filtered_events, pressed_keys)
    active_scene.Update()
    active_scene.Render(screen)
    active_scene = active_scene.next

    pygame.display.flip()