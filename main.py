import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
	asteroidfield = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return	

		screen.fill((0,0,0))
		
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.detectCollision(player):
				print("Game over!")
				sys.exit()
			
			for shot in shots:
				if asteroid.detectCollision(shot):
					asteroid.split()
					shot.kill()
					
					

		for item in drawable:
			item.draw(screen)
		pygame.display.flip()

		# Limit the game to 60fps
		dt = clock.tick(60) / 1000
		

if __name__ == "__main__":
	main()
