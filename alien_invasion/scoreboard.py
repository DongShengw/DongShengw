import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""显示得分信息的类"""
	
	def __init__(self,ai_settings, screen, stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		#显示得分信息时使用的字体设置
		self.text_color = (50, 150 ,70 )
		self.font = pygame.font.SysFont(None, 35)
		
		#准备初始得分图像
		self.prep_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		"""将得分转换为一幅渲染的图像"""
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
		
		#将得分放到屏幕的右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 10
		self.score_rect.top = 15
		
	def prep_level(self):
		"""将等级转换为渲染的图像"""
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
		
		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
	
	def prep_ships(self):
		"""显示还剩多少飞船"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number  * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	
	def show_score(self):
		"""在屏幕上显示飞船和得分"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		#绘制飞船
		self.ships.draw(self.screen)
