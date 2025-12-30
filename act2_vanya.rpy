# -------------------------
# Камео — просто сцена
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

    call ambient_reset
    jump act2_transition
