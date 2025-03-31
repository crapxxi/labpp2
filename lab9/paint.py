import pygame
import math
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    shapes = []
    circles = []
    rhombs = []
    triangles = []
    equis = []
    squares = []

    drawing = False
    start_pos = None
    drawing_rect = False
    drawing_circle = False
    drawing_rhombus = False
    drawing_triangle = False
    drawing_equi = False
    drawing_square = False
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:   #mc
                    mode = 'eraser'
                elif event.key == pygame.K_s:
                    mode = 'rectangle'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'triangle'
                elif event.key == pygame.K_y:
                    mode = 'equi'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'
                elif event.key == pygame.K_q:
                    mode = 'square'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'rectangle':    #mc
                    start_pos = event.pos
                    drawing_rect = True
                elif mode == 'circle':
                    start_pos = event.pos
                    drawing_circle = True
                elif mode == 'rhombus':
                    start_pos = event.pos
                    drawing_rhombus = True
                elif mode == 'triangle':
                    start_pos = event.pos
                    drawing_triangle = True
                elif mode == 'equi':
                    start_pos = event.pos
                    drawing_equi = True
                elif mode == 'square':
                    start_pos = event.pos
                    drawing_square = True
                else:
                    drawing = True
                    points.append(((None,None),mode))
                points.append(((None,None), mode))
            elif event.type == pygame.MOUSEBUTTONUP:
                if drawing_rect and start_pos:      #mc
                    end_pos = event.pos
                    shapes.append((start_pos, end_pos, mode))  # Сохраняем прямоугольник
                    drawing_rect = False
                elif drawing_circle and start_pos:
                    end_pos = event.pos
                    circles.append((start_pos, end_pos, mode))  # Сохраняем круг
                    drawing_circle = False
                elif drawing_rhombus and start_pos:
                    end_pos = event.pos
                    rhombs.append((start_pos, end_pos, mode))  # Сохраняем круг
                    drawing_rhombus = False
                elif drawing_triangle and start_pos:
                    end_pos = event.pos
                    triangles.append((start_pos, end_pos, mode))  # Сохраняем круг
                    drawing_triangle = False
                elif drawing_equi and start_pos:
                    end_pos = event.pos
                    equis.append((start_pos, end_pos, mode))  # Сохраняем круг
                    drawing_equi = False
                elif drawing_square and start_pos:
                    end_pos = event.pos
                    squares.append((start_pos, end_pos, mode))  # Сохраняем круг
                    drawing_square = False
                drawing = False
            
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1: # left click grows radius
            #         radius = min(200, radius + 1)
            #     elif event.button == 3: # right click shrinks radius
            #         radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION and drawing:
                # if mouse moved, add point to list
                position = event.pos
                points.append((position, mode))
                
        screen.fill((0, 0, 0))
        for rect in shapes:
            start, end, rect_mode = rect
            drawRectangle(screen, start, end, rect_mode)
        
        for circle in circles:
            start, end, circle_mode = circle
            drawCircle(screen, start, end, circle_mode)

        for rhombus in rhombs:
            start, end, rhomb_mode = rhombus
            drawRhomb(screen, start, end, rhomb_mode)
        
        for triangle in triangles:
            start, end, tri_mode = triangle
            drawTriangle(screen, start, end, tri_mode)
        for equi in equis:
            start, end, equi_mode = equi
            drawEqui(screen, start, end, equi_mode)
        for square in squares:
            start, end, square_mode = square
            drawSquare(screen, start, end, square_mode)
        # draw all points
        i = 0
        while i < len(points) - 1:
            if points[i][0] != (None,None) and points[i+1][0] != (None,None):
                drawLineBetween(screen, i, points[i], points[i + 1], radius, points[i][1])
            i += 1

        if drawing_rect and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawRectangle(screen, start_pos, end_pos, mode)
        
        if drawing_circle and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawCircle(screen, start_pos, end_pos, mode)
        
        if drawing_rhombus and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawRhomb(screen, start_pos, end_pos, mode)
        if drawing_triangle and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawTriangle(screen, start_pos, end_pos, mode)
        if drawing_equi and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawEqui(screen, start_pos, end_pos, mode)
        if drawing_square and start_pos:
            end_pos = pygame.mouse.get_pos()
            drawSquare(screen, start_pos, end_pos, mode)
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, point1, point2, width, color_mode):
    start, color_mode = point1
    end, _ = point2
    # c1 = max(0, min(255, 2 * index - 256))
    # c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    elif color_mode == 'eraser':
        color = (0,0,0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию

    rect_x = min(start[0], end[0])
    rect_y = min(start[1], end[1])
    rect_width = abs(start[0] - end[0])
    rect_height = abs(start[1] - end[1])

    pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height), 3)
def drawCircle(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию

    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    radius = max(abs(start[0] - end[0]) // 2, abs(start[1] - end[1]) // 2)

    pygame.draw.circle(screen, color, (center_x, center_y), radius, 3)
def drawRhomb(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    points = [(center_x, center_y - dy), (center_x + dx, center_y), (center_x, center_y + dy), (center_x - dx, center_y)]
    pygame.draw.polygon(screen, color, points, 3)
def drawTriangle(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию
    pygame.draw.polygon(screen, color, [start, end, (start[0], end[1])], 3)
def drawEqui(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию
    height = abs(end[1] - start[1])
    base = height * math.sqrt(3)
    pygame.draw.polygon(screen, color, [(start[0], start[1]), (start[0] + base, start[1]), (start[0] + base / 2, start[1] - height)], 3)
def drawSquare(screen, start, end, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    else:
        color = (255, 255, 255)  # Цвет по умолчанию
    side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, color, (start[0], start[1], side, side), 3)
main()
