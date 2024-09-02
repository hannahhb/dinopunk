label west: 

    # scene bg wasteland
    show bg west with dissolve
    
    "Welcome to the Brood"
    trebble "One of the worst areas in this godforsaken country."
   
    $ renpy.movie_cutscene("videos/west_cut_scene.webm")
    trebble "If the Dinos don’t kill you, the people will, everyone out for each others blood trying to gain an advantage"
    trebble ", make sure your stocked up on resources before coming here."
    $ renpy.movie_cutscene("videos/outro.webm")

    # $ renpy.movie_cutscene("videos/dino_cut_scene.mp4")
    # call screen backButton