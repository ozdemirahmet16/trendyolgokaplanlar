import pygame
import random

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Oyun Ekranı Boyutları
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Karakter Boyutları
CHAR_SIZE = 32

# Ücretlendirme
SINGLE_PACKAGE_FEE = 24
MULTIPLE_PACKAGE_FEE = 15.5

# Pygame Başlat
pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kaplan Kurye Oyunu")

# Emojileri karakter yerine kullanmak için metin oluşturma fonksiyonu
def draw_text(text, x, y):
    label = font.render(text, True, BLACK)
    screen.blit(label, (x, y))

# Başlangıç Değerleri
kaplan_x, kaplan_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
order_x, order_y = random.randint(0, SCREEN_WIDTH - CHAR_SIZE), random.randint(0, SCREEN_HEIGHT - CHAR_SIZE)
has_order = False
total_earnings = 0

# Oyun Döngüsü
running = True
while running:
    screen.fill(WHITE)

    # Kazanç Bilgisi Göster
    draw_text(f"Kazanç: {total_earnings} TL", 10, 10)

    # Kaplan ve Sipariş Durumu Çiz
    draw_text("🐅", kaplan_x, kaplan_y)
    if not has_order:
        draw_text("🛖", order_x, order_y)
    else:
        delivery_x, delivery_y = random.randint(0, SCREEN_WIDTH - CHAR_SIZE), random.randint(0, SCREEN_HEIGHT - CHAR_SIZE)
        draw_text("🙋‍♂️", delivery_x, delivery_y)

    # Tuş Kontrolleri
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        kaplan_x -= 5
    if keys[pygame.K_RIGHT]:
        kaplan_x += 5
    if keys[pygame.K_UP]:
        kaplan_y -= 5
    if keys[pygame.K_DOWN]:
        kaplan_y += 5

    # Sipariş Alımı Kontrolü
    if not has_order and abs(kaplan_x - order_x) < CHAR_SIZE and abs(kaplan_y - order_y) < CHAR_SIZE:
        has_order = True
        total_earnings += SINGLE_PACKAGE_FEE

    # Teslimat Kontrolü
    if has_order and abs(kaplan_x - delivery_x) < CHAR_SIZE and abs(kaplan_y - delivery_y) < CHAR_SIZE:
        total_earnings += MULTIPLE_PACKAGE_FEE
        has_order = False
        order_x, order_y = random.randint(0, SCREEN_WIDTH - CHAR_SIZE), random.randint(0, SCREEN_HEIGHT - CHAR_SIZE)

    # Çıkış Kontrolü
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
