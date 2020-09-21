/** 
Title: Dragon cave
Creator:
Description:

 */
//  Game setup
info.setLife(1)
info.setScore(0)
//  player
let dragon = sprites.create(img`
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
`)
//  Player controls
dragon.x = 20
dragon.ay = 150
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    dragon.vy = -60
})
//  Generate Columns
function on_update_interval() {
    let gate_img = image.create(10, scene.screenHeight())
    gate_img.fill(7)
    gate_img.fillRect(0, randint(10, 40), 10, randint(50, 80), 0)
    let gate = sprites.createProjectileFromSide(gate_img, -50, 0)
    gate.setPosition(scene.screenWidth(), scene.screenHeight() / 2)
}

//  point increase
//  Game Loop
game.onUpdate(function on_update() {
    if (dragon.y > scene.screenHeight()) {
        death()
    } else if (dragon.y < 0) {
        dragon.y = 0
    }
    
})
//  player death
function death() {
    info.changeLifeBy(-1)
    if (info.life() != 0) {
        dragon.vy = 0
        dragon.y = scene.screenHeight() / 2
        game.splash("Press A to Start")
    }
    
}

