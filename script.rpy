# Define characters
define n = Character("Narrator")

define trebble = Character("Trebble")

# Define images and video
image bg black = "#000"
# image bg wasteland = im.scale
image bg melbournex_ruins = im.Scale("images/wilderness_city.webp", 1920, 1080)
image bg wilderness = im.Scale("images/wilderness.png", 1920, 1080)
image bg nest_with_eggs = im.Scale("images/wilderness_eggs.png", 1920, 1080)

# image bg nest_with_eggs = "images/nest_with_eggs.jpg"
image bg room = "images/room.jpg"
image bg map = "images/melb.png"

# image narrator = "images/science_officer.webp"
# image trevor concerned = "images/trevor_concerned.webp"
image khopesh_sword = "images/khopesh_sword.png"
image megalania = "images/megalania.png"
image khopesh_strike_megalania = "images/khopesh_strike_megalania.png"
image red_flash = "#f00"
image nest_burning = im.Scale("images/wilderness_fire.png", 1920, 1080)
image map_icon =  im.Scale("images/melb.png", 150, 100)  # Replace with the correct path to your icon image
image egg_by_side = "images/egg_by_side.jpg"
image cracked_egg_open = "images/cracked_egg_open.jpg"
image fire = "images/flamethrower_weapon.png"
# Define variables for coins and weapons
default population = 50
default coins = 0
default weapons = 0
default has_khopesh = False
default has_gun = False
default has_flamethrower = False

# Define video
$ renpy.movie_cutscene("videos/intro_dinopunk.webm")
$ renpy.movie_cutscene("videos/dino_cut_scene.mp4")
transform trebble_left_large:
    xpos 50
    ypos 150
    zoom 1.5

# Define audio
define audio.bg_music = "audio/dinopunk_song1.mp3"

# Define the swirling transformation
transform swirl_move:
    xpos 0.5 ypos 0.5  # Starting position (center of the screen)
    zoom 1.0
    rotate 0  # Start without rotation

    # First movement: Rotate and move towards the dino
    linear 0.5 rotate 360 xpos 0.5 ypos 0.1 zoom 1.5

    # Second movement: Shrink and fade out after hitting
    linear 0.2 zoom 0.1 alpha 0


# transform fire:
#     linear 0.1 alpha 0.8
#     linear 0.1 alpha 1.0
#     repeat

# Define a transformation for a larger image size and positioning
# transform trebble_left:
#     xpos 0.1
#     ypos 0.1
#     zoom 1.5

screen progress_bar_screen():
    # Coin Progress Bar
    hbox:
        text "Coins: [coins]" xpos 0.05 ypos 0.05
        bar value coins range 100 xpos 0.2 ypos 0.05 xmaximum 300 ymaximum 20
    # Population
        text "Population: [population]" xpos 0.55 ypos 0.05
        bar value population range 50 xpos 0.7 ypos 0.05 xmaximum 300 ymaximum 20
  
screen weapon_hud():
    hbox:
        xpos 0.75
        ypos 0.05
        spacing 50  # Space between the icons
        
        # Background bar for the weapons
        frame:
            background "#333"  # Dark gray color for the bar
            xmaximum 400  # Width of the bar
            ymaximum 130  # Height of the bar

            hbox:
                spacing 20  # Space between the icons and labels
                # padding (10, 10)  # Padding inside the frame

                # Khopesh sword icon with label
                if has_khopesh:
                    vbox:
                        add "images/khopesh_sword.png" size (80, 80)  # Adjust the size as needed
                        text "Khopesh \nSword" size 20 align (0.5, 0.5)  # Label for the weapon

                # Gun icon with label
                if has_gun:
                    vbox:
                        add "images/gun.png" size (160, 80)  # Replace with the correct image for the gun
                        text "Gun" size 20 align (0.5, 0.5)  # Label for the weapon

                # Flamethrower icon with label
                if has_flamethrower:
                    vbox:
                        add "images/flamethrower_weapon.png" size (160, 80)  # Replace with the correct image for the flamethrower
                        text "Flame\nthrow" size 20 align (0.5, 0.5)  # Label for the weapon
                
image fire_animation:
    "images/fire_gif/fire_1.png"
    0.1
    "images/fire_gif/fire_2.png"
    0.1
    "images/fire_gif/fire_3.png"
    0.1
    "images/fire_gif/fire_4.png"
    0.1
    "images/fire_gif/fire_5.png"
    0.1
    # Continue for all frames
    repeat

image dying_a:
    "images/dying_gif/dying_1.png"
    0.1
    "images/dying_gif/dying_2.png"
    0.1
    "images/dying_gif/dying_3.png"
    0.1
    "images/dying_gif/dying_4.png"
    0.1
    "images/dying_gif/dying_5.png"
    0.1
    "images/dying_gif/dying_6.png"
    0.1
    "images/dying_gif/dying_7.png"
    0.1
    "images/dying_gif/dying_8.png"
    0.1
    "images/dying_gif/dying_9.png"
    0.1
    "images/dying_gif/dying_10.png"
    0.1
    # Continue for all frames
    repeat

# Screen to show the map icon
screen map_icon_screen():
    if show_map_icon:
        # Display the map icon
        imagebutton:
            idle "map_icon"  # Image to display
            hover "map_icon"  # Image when hovered
            xpos 0.6  # Position of the icon on the screen
            ypos 0.05
            action ShowMenu("mapScreen") 


default show_map_icon = False


label start:
    # Start playing background music
    play music bg_music fadein 2.0

    scene bg black
    with fade

    $ renpy.movie_cutscene("videos/intro_dinopunk.webm")

    scene bg black
    with fade

    n "50 years ago, Melbourne, once known as the world's most liveable city, faced an unimaginable catastrophe..."

    # n "In the aftermath, it evolved into what we now call Melbourne."

    # n "That was the last broadcast from any major news network in Australia."

    # n "In the decades that followed, nature reclaimed Melbournex and its surroundings. Humanity was pushed to the brink of extinction."

    n "Now, only small communities remain in what was once called Victoria, struggling to survive in a world that no longer belongs to us."

    scene bg melbournex_ruins
    with fade

    n "This is where your story begins, in the ruins of Melbourne..."

    # Ask for the player's name
    $ player_name = renpy.input("What is your name, survivor of Melbourne?")
    show trebble rest at trebble_left_large

    trebble "Welcome to the new world, [player_name]. Your journey in the remains of Melbourne starts now."
    show screen progress_bar_screen
    show screen weapon_hud

    # Continue with the Elivanth scene
    scene bg wilderness with fade
    show trebble rest at trebble_left_large

    trebble "[player_name], Get back on your feet ya dog!"
    show screen progress_bar_screen
    trebble "We got a bit of a pickle mate, a nest of Megalania has appeared on our east border! Come with us to wipe them out of our home"
    # show trebble crazy at trebble_left_large
    trebble "You feeling right mate? Ya look like you’ve seen a Bunyip." 
    trebble "(chuckles)"
    trebble "Ah that's the spirit!"

    # Show the HUD with the Khopesh sword

    # Switch to new background showing the nest
    scene bg nest_with_eggs with dissolve

    voice "Destroy them- now!"

    # Show the Megalania
    show megalania rest at top with vpunch
    play sound "audio/roar_effect.mp3"
    $ has_khopesh = True

    pause 1.5
    # Player choices
    menu:
        "Strike with khopesh":
            $ result = "strike"
        "Call for help (risk losing population)":
            $ result = "call_help"
        "Run (reduce influence)":
            $ result = "run"

    #FIX THIS SCRIPT
    if result == "strike":
        $ combat_result = "won"
        "You draw your khopesh and prepare to strike."
        play sound "audio/sword_effect.mp3"

        # Show the khopesh swirling toward the Megalania and disappearing
        show khopesh_sword at swirl_move

        "The khopesh strikes the Megalania, sinking deep into its neck."
        
        show trebble gun at left
        trebble "You realize you don’t always have to fight with your old ass sword?"

        show red_flash
        "Megalania falls to the ground, strikes YOU then scurries away."
        trebble "It’s gone! Destroy the nest before it comes back."
        # show 
        play sound "audio/fire_effect.mp3"
        #ADD FLATHROWER SOUND EFFECT

        show fire_animation at trebble_left_large
        pause 3
        # Hide the fire image
        hide fire_animation

        show nest_burning
        $ has_flamethrower = True

    if result == "call_help":
        play audio "audio/Uuhhh.oga"
        $ population -= 2
        trebble "Oof that was a battle and a half may those poor souls find some redemption"
        show dying_a at trebble_left_large
        pause 3
        # Hide the fire image
        show dying_a
        trebble "naoiusniuaodnosanbdioa"

    if result == "run":
        trebble "naoiusniuaodnosanbdioa"
    
    


    trebble "(pulls out the glock) This would do a better job!"

    $ has_gun = True
    
    # Show egg and player feels compelled to take it
    # show egg_by_side 
    "Suddenly, you feel a pull towards the egg and pocket it."
    trebble "Quite the trinket, eh? Just don’t want it hatching on you! Wouldn’t mind one myself."

    # Player choices for bargaining
    menu:
        "Bargain (weapons, worn coins (10))":
            $ result = "bargain"
        "Refuse":
            $ result = "refuse"

    if result == "bargain":
        $ coins += 10  # Add 10 coins
        "[player_name] received 10 coins!"
    if result == "refuse":
        trebble "usdnoaun"

    # show screen map_icon_screen

    # $ show_map_icon = True  # Make the map icon visible

    "Turning away, you join the others and trudge back to the colony."
    scene bg room with dissolve
    "You enter your room, a simple bed. Home sweet home."

    # Show the map and interaction
    call screen mapScreen
    # play sound "audio/dinosaur_roar.mp3"
    # player moves outside to overgrown_city
    # 
    
    # show cracked_egg_open with dissolve
    "Opening the cracked egg, a leathery parchment falls out. A ripped map."
    "On one side, ‘Stralis’, on the other, a red and green heart."

    # Transition to the next part of the game or story
    return
