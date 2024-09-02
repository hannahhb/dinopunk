label east: 
    scene bg east with dissolve
    play audio horror_effect
    pause 2.0
    # scene bg wasteland
    "Welcome to the Yarro Wetlands"
    # $ renpy.movie_cutscene("videos/dino_cut_scene.mp4")
    trebble "Aaah the Yarro Wetlands, make sure you bring your swimmers mate."
    trebble "The water biomes are filled with great resources to improve yourself, but watch out for the creatures of the deep."
    trebble "Once you get too far into the water, you don’t come back. Big risks, big rewards."
    $ renpy.movie_cutscene("videos/outro.webm")

    # call screen backButton