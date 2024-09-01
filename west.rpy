label west: 

    # scene bg wasteland
    show bg west with dissolve
    play audio horror_effect
    pause 2.0
    "Welcome to the Brood"
    $ renpy.movie_cutscene("videos/outro.webm")

    # $ renpy.movie_cutscene("videos/dino_cut_scene.mp4")
    # call screen backButton