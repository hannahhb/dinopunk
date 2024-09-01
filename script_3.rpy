# # Define characters
# define n = Character("Narrator")
# define r = Character("Reporter")
# define elivanth = Character("Elivanth")
# define trebble = Character("Trebble")

# # Define images and video
# image bg black = "#000"
# image bg melbournex_ruins = im.Scale("images/wilderness_city.webp", 1920, 1080)
# image bg wilderness = im.Scale("images/wilderness.png", 1920, 1080)
# image bg nest_with_eggs = im.Scale("images/wilderness_eggs.png", 1920, 1080)

# # image bg nest_with_eggs = "images/nest_with_eggs.jpg"
# image bg room = "images/room.jpg"
# image bg map = im.Scale("images/map.png", 1920, 1080)

# # image narrator = "images/science_officer.webp"
# # image trevor concerned = "images/trevor_concerned.webp"
# image khopesh_sword = "images/khopesh_sword.png"
# image megalania = "images/megalania.png"
# image khopesh_strike_megalania = "images/khopesh_strike_megalania.png"
# image red_flash = "#f00"
# image nest_burning = im.Scale("images/wilderness_fire.png", 1920, 1080)
# image egg_by_side = "images/egg_by_side.jpg"
# image cracked_egg_open = "images/cracked_egg_open.jpg"

# # Define variables for coins and weapons
# default coins = 0
# default weapons = 0
# default has_khopesh = False
# default has_gun = False
# default has_flamethrower = False

# # Define video
# $ renpy.movie_cutscene("videos/intro_dinopunk.webm")

# transform trebble_left_large:
#     xpos 0.1
#     ypos 0.5
#     zoom 1.5

# # Define audio
# define audio.bg_music = "audio/dinopunk.mp3"

# # Define the swirling transformation
# transform swirl_move:
#     xpos 0.5 ypos 0.5  # Starting position (center of the screen)
#     zoom 1.0
#     rotate 0  # Start without rotation

#     # First movement: Rotate and move towards the dino
#     linear 0.5 rotate 360 xpos 0.5 ypos 0.1 zoom 1.5

#     # Second movement: Shrink and fade out after hitting
#     linear 0.2 zoom 0.1 alpha 0


# transform fire:
#     linear 0.1 alpha 0.8
#     linear 0.1 alpha 1.0
#     repeat

# # Define a transformation for a larger image size and positioning
# # transform trebble_left:
# #     xpos 0.1
# #     ypos 0.1
# #     zoom 1.5

# screen progress_bar_screen():
#     # Coin Progress Bar
#     hbox:
#         text "Coins: [coins]" xpos 0.05 ypos 0.05
#         bar value coins range 100 xpos 0.2 ypos 0.05 xmaximum 300 ymaximum 20

# screen weapon_hud():
#     hbox:
#         xpos 0.75
#         ypos 0.05
#         spacing 50  # Space between the icons
        
#         # Background bar for the weapons
#         frame:
#             background "#333"  # Dark gray color for the bar
#             xmaximum 400  # Width of the bar
#             ymaximum 130  # Height of the bar

#             hbox:
#                 spacing 20  # Space between the icons and labels
#                 # padding (10, 10)  # Padding inside the frame

#                 # Khopesh sword icon with label
#                 if has_khopesh:
#                     vbox:
#                         add "images/khopesh_sword.png" size (80, 80)  # Adjust the size as needed
#                         text "Khopesh \nSword" size 20 align (0.5, 0.5)  # Label for the weapon

#                 # Gun icon with label
#                 if has_gun:
#                     vbox:
#                         add "images/gun.png" size (160, 80)  # Replace with the correct image for the gun
#                         text "Gun" size 20 align (0.5, 0.5)  # Label for the weapon

#                 # Flamethrower icon with label
#                 if has_flamethrower:
#                     vbox:
#                         add "images/flamethrower.png" size (80, 80)  # Replace with the correct image for the flamethrower
#                         text "Flamethrower" size 20 align (0.5, 0.5)  # Label for the weapon
                

# label start:
#     # Start playing background music
#     play music bg_music fadein 2.0

#     scene bg black
#     with fade

#     $ renpy.movie_cutscene("videos/intro_dinopunk.webm")

#     scene bg black
#     with fade

#     n "50 years ago, Melbourne, once known as the world's most liveable city, faced an unimaginable catastrophe..."

#     # n "In the aftermath, it evolved into what we now call Melbournex."

#     # n "That was the last broadcast from any major news network in Australia."

#     # n "In the decades that followed, nature reclaimed Melbournex and its surroundings. Humanity was pushed to the brink of extinction."

#     n "Now, only small communities remain in what was once called Victoria, struggling to survive in a world that no longer belongs to us."

#     scene bg melbournex_ruins
#     with fade

#     n "This is where your story begins, in the ruins of Melbournex..."

#     # Ask for the player's name
#     $ player_name = renpy.input("What is your name, survivor of Melbournex?")
#     show trebble rest at trebble_left_large

#     trebble "Welcome to the new world, [player_name]. Your journey in the remains of Melbournex starts now."
#     show screen progress_bar_screen
#     show screen weapon_hud

#     # Continue with the Elivanth scene
#     scene bg wilderness with fade

#     trebble "[player_name], Get back on your feet ya dog!"
#     show screen progress_bar_screen
#     trebble "We got a bit of a pickle mate a nest of Megalania has appeared on our east border! Come with us to wipe them out of our home"
#     show trebble crazy
#     trebble "You feeling right mate? Ya look like you’ve seen a Bunyip." 
#     trebble "(chuckles)"
#     trebble "Ah that's the spirit!"

#     # Show the HUD with the Khopesh sword

#     # Switch to new background showing the nest
#     scene bg nest_with_eggs with dissolve

#     voice "Destroy them- now!"

#     # Show the Megalania
#     show megalania rest at top with vpunch
#     play sound "audio/roar_effect.mp3"
#     $ has_khopesh = True

#     pause 1.5
#     # Player choices
#     menu:
#         "1. Strike with khopesh":
#             $ result = "strike"
#         "2. Call for help (risk losing population)":
#             $ result = "call_help"
#         "3. Run (reduce influence)":
#             $ result = "run"

#     if result == "strike":
#         $ combat_result = "won"
#         "You draw your khopesh and prepare to strike."
#         play sound "audio/sword_effect.mp3"

#         # Show the khopesh swirling toward the Megalania and disappearing
#         show khopesh_sword at swirl_move

#         "The khopesh strikes the Megalania, sinking deep into its neck."

#         show red_flash
#         "Megalania falls to the ground, strikes YOU then scurries away."
#         trebble "It’s gone! Destroy the nest before it comes back."
        
#     # Burn the nest
#     show nest_burning
#     trebble "You realize we don’t always have to fight with our hands?"

#     show trebble gun 
#     trebble "(pulls out the glock) This would do a better job!"

#     $ has_gun = True

#     # Show egg and player feels compelled to take it
#     # show egg_by_side 
#     "Suddenly, you feel a pull towards the egg and pocket it."
#     trebble "Quite the trinket, eh? Just don’t want it hatching on you! Wouldn’t mind one myself."

#     # Player choices for bargaining
#     menu:
#         "1. Bargain (weapons, worn coins (10))":
#             $ result = "bargain"
#         "2. Refuse":
#             $ result = "refuse"

#     if result == "bargain":
#         $ coins += 10  # Add 10 coins
#         "[player_name] received 10 coins!"

#     "Turning away, you join the others and trudge back to the colony."
#     scene bg room with dissolve
#     "You enter your room, a simple bed. A framed photo of a smiling man on the bedside table."

#     # Show the map and egg interaction
#     scene bg map 
#     # show cracked_egg_open with dissolve
#     "Opening the cracked egg, a leathery parchment falls out. A ripped map."
#     "On one side, ‘Stralis’, on the other, a red and green heart."

#     # Transition to the next part of the game or story
#     return
