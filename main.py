"""
Title: Dragon cave
Creator:
Description:
"""

# Game setup
info.set_life(1)
info.set_score(0)

# player
dragon = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 2 2 . . . . . . . .
    . . . . . . 2 2 . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))
# Player controls
dragon.x = 20
dragon.ay = 150
def on_a_pressed():
    dragon.vy = -60 
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# Generate Columns
def on_update_interval():
    gate_img = image.create(10, scene.screen_height())
    gate_img.fill(7)
    gate_img.fill_rect(0, randint(10,40), 10, randint(50, 80), 0)
    gate = sprites.create_projectile_from_side(gate_img, -50, 0)
    gate.set_position(scene.screen_width(), scene.screen_height()/2)
    
# point increase
def on_on_destroyed():
    info.change_score_by(1)
    gate.on_destroyed(on_on_destroyed)
    
    def on_overlap(sprite, otherSprite):
        death()
    sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_overlap)

# Game Loop
def on_update():
    if dragon.y > scene.screen_height():
        death()
    elif dragon.y < 0:
        dragon.y = 0
game.on_update(on_update)


# player death
def death():
    info.change_life_by(-1)
    if info.life() != 0:
        dragon.vy = 0
        dragon.y = scene.screen_height()/2
        game.splash("Press A to Start")
