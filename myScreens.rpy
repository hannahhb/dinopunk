label myScreens:

screen mapScreen:
    add "melb.png"

    imagebutton:
        xpos 35
        ypos 120
        idle "blank"
        hover "melb_1"
        action Jump("west")

    imagebutton:
        xpos 490
        ypos 355
        idle "blank"
        hover "melb_3"
        action Jump("cbd")


    imagebutton:
        xpos 999
        ypos 441   
        idle "blank"
        hover "melb_2"
        action Jump("east")

    imagebutton:
        xpos 530
        ypos 320
        idle "dot"
        hover "dot"
        action Jump("home")

