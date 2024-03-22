import pygame
c = 1

while c == 1:
    pygame.init()
    pygame.font.init()
    display = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Sokoban deserving of an A")
    clock = pygame.time.Clock()

    myfont = pygame.font.SysFont('Comic Sans Ms', 50)
    player_sprite = pygame.image.load("sokoban/Mover.png")
    box_sprite = pygame.image.load("sokoban/Crate.png")
    wall_sprite = pygame.image.load("sokoban/Wall.png")
    checkpoint_sprite = pygame.image.load("sokoban/Checkpoint.png")

    class player:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.up = False
            self.down = False
            self.left = False
            self.right = False
            self.playerRect = 0
            self.ox = x
            self.oy = y

        def move(self, x, y):
            self.ox = x
            self.oy = y

            vX = 0
            vY = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        vX += 25
                    if event.key == pygame.K_a:
                        vX -= 25
                    if event.key == pygame.K_w:
                        vY -= 25
                    if event.key == pygame.K_s:
                        vY += 25

            self.x += vX
            self.y += vY

        def draw(self, display):
            display.blit(pygame.transform.scale(player_sprite, (25, 25)), (self.x, self.y))

        def main(self):
            self.move(self.x, self.y)
            self.draw(display)


    class box:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self, display):
            display.blit(pygame.transform.scale(box_sprite, (25, 25)), (self.x, self.y))

        def main(self):
            self.draw(display)


    class wall:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self, display):
            display.blit(pygame.transform.scale(wall_sprite, (25, 25)), (self.x, self.y))

        def main(self):
            self.draw(display)


    class checkpoint:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def draw(self, display):
            display.blit(pygame.transform.scale(checkpoint_sprite, (25, 25)), (self.x, self.y))

        def main(self):
            self.draw(display)

    Player = player(325, 325)
    Boxes = [box(75, 275), box(200, 325), box(75, 225)]
    Walls = [wall(375, 375),wall(375,350),wall(375,325),wall(375,300),wall(375,275),wall(375,250),wall(375,225),wall(375,200),wall(375,175),wall(375,150),wall(375,125),wall(375,100),wall(375,75),wall(375,50),wall(375,25),wall(375,0),wall(350,0),wall(325,0),wall(300,0),wall(275,0),wall(250,0),wall(225,0),wall(200,0),wall(175,0),wall(150,0),wall(125,0),wall(100,0),wall(75,0),wall(50,0),wall(25,0),wall(0,0),wall(0,25),wall(0,50),wall(0,75),wall(0,100),wall(0,125),wall(0,150),wall(0,175),wall(0,200),wall(0,225),wall(0,250),wall(0,275),wall(0,300),wall(0,325),wall(0,350),wall(0,375),wall(25,375),wall(50,375),wall(75,375),wall(100,375),wall(125,375),wall(150,375),wall(175,375),wall(200,375),wall(225,375),wall(250,375),wall(275,375),wall(300,375),wall(325,375),wall(350,375),wall(275,250),wall(300,250),wall(325,250),wall(350,250),wall(300,225),wall(300,275),wall(75,25),wall(75,50),wall(75,75),wall(75,100),wall(75,125),wall(75,150),wall(75,175),wall(75,200),wall(50,125),wall(100,175),wall(125,175),wall(225,25),wall(225,50),wall(225,75),wall(225,100),wall(225,125),wall(225,150),wall(225,175),wall(225,225),wall(175,175),wall(200,175),wall(250,150),wall(275,150),wall(300,150),wall(300,125),wall(300,100),wall(350,100),wall(350,75),wall(50,250),wall(75,250),wall(100,250),wall(125,250),wall(50,325),wall(75,325),wall(100,375),wall(125,325),wall(150,325),wall(125,300),wall(150,300),wall(125,275),wall(150,275),wall(175,275),wall(225,275),wall(225,300),wall(225,325)]
    Checkpoints = [checkpoint(250, 125), checkpoint(200, 25), checkpoint(25, 25)]

    def main():
        boxesleft = 3
        while True:
            display.fill((105, 105, 105))

            Player.main()

            for point in Checkpoints:
                point.main()

                for box in Boxes:
                    if point.x == box.x and point.y == box.y:
                        Boxes.remove(box)
                        Checkpoints.remove(point)
                        boxesleft -= 1

        
            for wall in Walls:
                if Player.x == wall.x and Player.y == wall.y:
                    if Player.ox >= wall.x and Player.oy == wall.y:
                        Player.x += 25
                    elif Player.ox <= wall.x and Player.oy == wall.y:
                        Player.x -= 25
                    elif Player.oy >= wall.y and Player.ox == wall.x:
                        Player.y += 25
                    elif Player.oy <= wall.y and Player.ox == wall.x:
                        Player.y -= 25

                            

            for box in Boxes:
                box.main()

                # collisions
                for wall in Walls:
                    if int(Player.x) == int(box.x) and int(Player.y) == int(box.y):
                        if int(Player.ox) >= int(box.x) and int(Player.oy) == int(box.y):
                            if box.x - 25 != wall.x and box.y != wall.y:
                                obx = box.x
                                oby = box.y
                                box.x -= 25
                        elif int(Player.ox) <= int(box.x) and int(Player.oy) == int(box.y):
                            if box.x + 25 != wall.x and box.y != wall.y:
                                obx = box.x
                                oby = box.y
                                box.x += 25
                        elif int(Player.oy) >= int(box.y) and int(Player.ox) == int(box.x):
                            if box.x != wall.x and box.y - 25 != wall.y:
                                obx = box.x
                                oby = box.y
                                box.y -= 25
                        elif int(Player.oy) <= int(box.y) and int(Player.ox) == int(box.x):
                            if box.x != wall.x and box.y + 25 != wall.y:
                                obx = box.x
                                oby = box.y
                                box.y += 25
                    if box.x == wall.x and box.y == wall.y:
                        box.x = obx
                        box.y = oby
                        Player.x = Player.ox
                        Player.y = Player.oy

            for wall in Walls:
                wall.main()
            

            if boxesleft == 0:
                textsurface = myfont.render("You Won!", False, (0,255,255))
                display.blit(textsurface, (50,250))
                


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        quit()
                    if event.key == pygame.K_r:
                        return False



            clock.tick(24)
            pygame.display.update()


    main()

