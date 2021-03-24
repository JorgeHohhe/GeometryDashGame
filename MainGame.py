import pygame
from source.graphics.misc.font import *
from source.gameplay.utils.constants import *
from source.gameplay.components.platforms.block import *
from source.gameplay.essentials.environment import Environment


def draw_game(win, player, portals, background, components, base):
    background.draw(win)

    player.draw(win)

    for comp in components.values():
        for i in range(0, len(comp)):
            comp[i].draw(win)

    base.draw(win)

    for portal in portals.values():
        for i in range(0, len(portal)):
            portal[i].draw(win)

    pygame.display.update()


def main():
    """ =-=-=-=-=-=-= MAP SETUP =-=-=-=-=-=-= """
    env = Environment()

    # SET WINDOW
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    """ =-=-=-=-=-=-= GAME START =-=-=-=-=-=-= """
    timer = pygame.time.Clock()
    pressed = False
    flag = True
    while flag:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False
                pygame.quit()
                quit()

        # TEST SPACE-BAR FOR THE DIFFERENT GAMEMODES
        state = pygame.key.get_pressed()
        if state[pygame.K_SPACE]:
            if env.gamemode == "cube":
                if env.player.could_jump(env.blocks):
                    env.player.jump()
            elif env.gamemode == "dragon":
                env.player.up()

            if not pressed:
                pressed = True
                if env.gamemode == "laser":
                    env.player.up()
                elif env.gamemode == "orb":
                    if env.player.could_switch(env.blocks):
                        env.player.switch()
                elif env.gamemode == "cyclops":
                    if env.player.could_switch(env.blocks):
                        env.player.switch()
        else:
            pressed = False
            if env.gamemode == "laser":
                env.player.down()

        # MOVE THE PLAYER
        env.player.move()
        env.player.blocks_interaction(env.blocks)

        # MOVE THE MAP
        env.background.move()
        env.base.move()
        for portal in env.portals.values():
            for i in range(0, len(portal)):
                portal[i].move()

        remove_spikes = list()  # LOOK IF IS NECESSARY
        remove_blocks = list()  # LOOK IF IS NECESSARY
        # SPIKES
        for spike in env.components["all_comp"]:
            # SPIKE COLLISION TEST
            if spike.collision(env.player):
                # restart the game
                main()

            if spike.x + spike.img.get_width() < 0:
                remove_spikes.append(spike)

            spike.move()
        # BLOCKS
        for block in env.components["blocks"]:
            # BLOCK COLLISION TEST
            if block.collision(env.player):
                # restart the game
                main()
            # BLOCK COLLISION TEST

            if block.x + block.img.get_width() < 0:
                remove_blocks.append(block)

            block.move()

        # PORTALS TEST
        env.portals_test()

        # REMOVE OBJECTS THAT ALREADY PASSED
        for r in remove_spikes:
            env.components["all_comp"].remove(r)
        for r in remove_blocks:
            env.components["blocks"].remove(r)

        draw_game(win, env.player, env.portals, env.background, env.components, env.base)


if __name__ == '__main__':
    main()
