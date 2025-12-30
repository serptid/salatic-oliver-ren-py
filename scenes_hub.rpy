label act2_hub:
    $ act = 2

    menu:
        "Осмотреться дальше (ничего не решать)":
            $ avoid_count += 1
            $ virus_risk += 1
            jump act2_hub

        "Quins" if not act2_quins_done:
            $ act2_quins_done = True
            $ f_quins = True
            jump act2_hub

        "Nighstess" if not act2_nighstess_done:
            $ act2_nighstess_done = True
            $ f_nighstess = True
            jump act2_hub

        "Песок" if not act2_sand_done:
            $ act2_sand_done = True
            $ f_sand = True
            jump act2_hub

        "Больница" if not act2_hospital_done:
            $ act2_hospital_done = True
            $ f_hospital = True
            jump act2_hub

        "Дальше" if (act2_quins_done or act2_nighstess_done or act2_sand_done or act2_hospital_done) or avoid_count >= 2:
            jump act3_entry
