label interactionmenu(approach, observe, leave):

    menu:
        "Approach":
            call expression approach

        "Observe":
            jump expression observe

        "Leave":
            jump expression leave