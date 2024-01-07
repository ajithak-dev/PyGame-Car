import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
WHITE = (255, 255, 255)

# Initialize Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Race Car Game")

# Load car image
car_image = pygame.image.load("C:/Users/Admin/Desktop/Game Project Py/assetsf/car.png")  # Provide the path to your car image file
background_image = pygame.image.load("C:/Users/Admin/Desktop/Game Project Py/assetsf/bg.png")

# Load enemy car images
enemy_car_images = []
for i in range(1, 6):  # Assuming you have 5 different enemy car images named "enemy_car1.png", "enemy_car2.png", ...
    enemy_car_images.append(pygame.image.load(f"C:/Users/Admin/Desktop/Game Project Py/assetsf/ecar{i}.png"))

# Set initial car position
car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
car_y = SCREEN_HEIGHT - CAR_HEIGHT - 20

# Set initial number of enemy cars and their attributes
num_enemy_cars = 5  # You can adjust the number of enemy cars
enemy_cars = []

for _ in range(num_enemy_cars):
    enemy_car_width, enemy_car_height = 50, 100
    enemy_car_x = random.randint(1, SCREEN_WIDTH - enemy_car_width)
    enemy_car_y = random.randint(-SCREEN_HEIGHT, 0)
    enemy_car_speed = random.randint(10, 20)
    enemy_car_image = random.choice(enemy_car_images)
    enemy_cars.append({"x": enemy_car_x, "y": enemy_car_y, "speed": enemy_car_speed, "image": enemy_car_image})

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the car based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 10
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
        car_x += 10
    if keys[pygame.K_UP] and car_y > 0:  # Move forward
        car_y -= 10
    if keys[pygame.K_DOWN] and car_y < SCREEN_HEIGHT - CAR_HEIGHT:  # Move backward
        car_y += 10

    # Move and draw enemy cars
    for enemy_car in enemy_cars:
        enemy_car["y"] += enemy_car["speed"]
        # Reset enemy car if it's out of the screen
        if enemy_car["y"] > SCREEN_HEIGHT:
            enemy_car["y"] = random.randint(-SCREEN_HEIGHT, 0)
            enemy_car["x"] = random.randint(1, SCREEN_WIDTH - enemy_car_width)
            enemy_car["speed"] = random.randint(15, 25)
            enemy_car["image"] = random.choice(enemy_car_images)
        screen.blit(enemy_car["image"], (enemy_car["x"], enemy_car["y"]))

        # Collision detection
        if car_x < enemy_car["x"] + enemy_car_width and car_x + CAR_WIDTH > enemy_car["x"] and \
                car_y < enemy_car["y"] + enemy_car_height and car_y + CAR_HEIGHT > enemy_car["y"]:
            print("Game Over!")  # You can customize the game over behavior here
            running = False

    # Draw everything on the screen
    pygame.display.flip()
    screen.blit(background_image, (0, 0))
    screen.blit(car_image, (car_x, car_y))
    

    # Limit frames per second
    clock.tick(30)

pygame.quit()
