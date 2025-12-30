# scenes_act2.rpy
# Акт II — Центральный хаб, свободное исследование веток

label act2_entry:

    scene cyberspace_city
    with fade

    play music "audio/ambient_cyberspace.ogg" fadein 2.0

    oliver "Город из данных."
    oliver "Он не спит."

    hamayumi "Это хаб."
    hamayumi "Отсюда ты можешь идти куда угодно."

    hamayumi "Но помни."
    hamayumi "Здесь легко потерять себя, если ты перестанешь выбирать."

    $ hub_visits += 1

    jump hub_main


label act2_exit:

    scene cyberspace_void
    with fade

    hamayumi "Хаб закрывается."
    hamayumi "Дальше — узел, где придётся определиться."

    oliver "Это точка невозврата?"

    hamayumi "Почти."
    hamayumi "Сначала — конфликт."

    stop music fadeout 2.0

    jump act3_entry
