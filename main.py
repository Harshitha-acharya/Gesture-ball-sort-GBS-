from camera import Camera
from hand import HandTracker
from gesture import Gesture
import cv2
import pygame
from constant import *
from game import Game

pygame.init()

camera = Camera()
tracker = HandTracker()
gesture = Gesture()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Sort Puzzle")

clock = pygame.time.Clock()

game = Game()

selected = None
pinch_active = False

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game.reset()
                selected = None

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            tube = (mx - START_X) // GAP

            if 0 <= tube < len(game.tubes):
                if selected is None:
                    game.pick(tube)
                    selected = tube
                else:
                    game.drop(tube)
                    selected = None

    frame = camera.get_frame()

    if frame is not None:

        frame, points = tracker.findHands(frame)
        finger = tracker.getFingerPosition(points)

        if finger is not None:

            fx, fy = finger
            fx = int(fx * WIDTH / 640)
            fy = int(fy * HEIGHT / 480)
            
            game.held_x = fx
            game.held_y = fy
            if game.held_ball is not None:
             game.held_ball.x = fx
             game.held_ball.y = fy

            camera_h, camera_w = frame.shape[:2]

            draw_x = int(fx * camera_w / WIDTH)
            draw_y = int(fy * camera_h / HEIGHT)

            cv2.circle(frame, (draw_x, draw_y), 10, (255, 0, 0), -1)

            tube = -1

            for i, t in enumerate(game.tubes):
                if t.rect.collidepoint(fx, fy):
                    tube = i
                    break

            is_pinch = gesture.pinch(points)

            if is_pinch:
                cv2.putText(
                    frame,
                    "PINCH",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if not pinch_active:

                    if 0 <= tube < len(game.tubes):

                        if selected is None:
                            game.pick(tube)
                            selected = tube
                        else:
                            game.drop(tube)
                            selected = None

                    pinch_active = True

            else:
                pinch_active = False

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        surface = pygame.surfarray.make_surface(
            frame.swapaxes(0, 1)
        )
        screen.blit(surface, (0, 0))

    game.draw(screen)
    pygame.display.update()

camera.release()
pygame.quit()