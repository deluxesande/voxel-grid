import moderngl as mgl
import pygame as pg
import sys

from cube import Cube
from camera import Camera
from light import Light
from settings import *


class VoxelEngine:
    def __init__(self):
        pg.init()
        self.WINSIZE = WIN_RES
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(
            pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE
        )
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(self.WINSIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context()
        # To see the internal faces
        # self.ctx.front_face = "cw"
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = "auto"

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        self.is_running = True

        # Light
        self.light = Light()
        # Camera
        self.camera = Camera(self)
        # Scene
        self.scene = Cube(self)

    def update(self):
        self.delta_time = self.clock.tick(60)
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f"{self.clock.get_fps() : .0f}")

    def render(self):
        self.ctx.clear(color=BG_COLOR)

        # Render the scene
        self.scene.render()

        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                self.is_running = False
                self.scene.destroy()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.camera.update()
            self.render()

        pg.quit()
        sys.exit()


if __name__ == "__main__":
    app = VoxelEngine()
    app.run()
