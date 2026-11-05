import sys
import time

def mandelbrot():
    # Настройки размера поля
    WIDTH, HEIGHT = 80, 40
    # Символы для отображения плотности фрактала
    CHARS = " .:-=+*#%@"
    
    # Смещение по осям для центрирования фрактала
    X_START, X_END = -2.0, 0.5
    Y_START, Y_END = -1.2, 1.2
    
    MAX_ITER = 30  # Чем больше, тем детализированнее фрактал

    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            # Превращаем координаты экрана в комплексные числа
            cr = X_START + (x / WIDTH) * (X_END - X_START)
            ci = Y_START + (y / HEIGHT) * (Y_END - Y_START)
            c = complex(cr, ci)
            z = 0j
            
            i = 0
            while abs(z) <= 2 and i < MAX_ITER:
                z = z**2 + c
                i += 1
            
            # Подбираем символ в зависимости от скорости "ухода" в бесконечность
            char_index = int((i / MAX_ITER) * (len(CHARS) - 1))
            line += CHARS[char_index]
        
        print(line)
        time.sleep(0.02)  # Плавный эффект рисования строк

if __name__ == "__main__":
    mandelbrot()