
# -------------------------
# Камео
# -------------------------

label cameo_vanya:

    scene cyberspace_rooftop
    with dissolve

    show vanya at center
    with dissolve

    vanya "Я думал, это сон."
    vanya "А оказалось — привычка."

    oliver "Ты хочешь выйти?"

    vanya "Я уже вышел."
    vanya "Просто тело забыли забрать."

    hide vanya
    with dissolve

    $ avoid_counter += 1

    # Камео слегка повышает целостность (свидетель "живого факта"), но усиливает конфликт
    $ identity_integrity += 1
    if quins_done and nighstess_done:
        $ quins_nighstess_conflict += 1

    call ambient_reset
    jump act2_transition
