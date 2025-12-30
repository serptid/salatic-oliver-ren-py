# scenes_core.rpy
# CORE NODE — выбор концовки по открытым рутам

label core_entry:

    scene cyberspace_void
    with fade

    play music "audio/core_node.ogg" fadein 2.0

    hamayumi "Дальше — ядро."
    hamayumi "Здесь не торгуются."

    if virus_active:
        play sound "audio/glitch_short.ogg"
        hamayumi "И да."
        hamayumi "Он уже рядом."

    scene cyberspace_core
    with dissolve

    show artemka at center
    with dissolve

    artemka "Переменная обнаружена."
    artemka "Салатик Оливер."
    artemka "Статус: нестабильный."

    oliver "Ты MR_artemka."

    artemka "Я администратор."
    artemka "Я закрываю неопределённость."

    hamayumi "Он даст интерфейс."
    hamayumi "Но кнопки появятся только там, где ты дошёл до конца."

    # Если вирус активен — нет ручного выбора (как у тебя было)
    if virus_active:
        artemka "Обнаружено постороннее вмешательство."
        artemka "Приоритет: безопасность."
        artemka "Завершение будет выполнено автоматически."
        hide artemka
        with dissolve
        stop music fadeout 1.0
        $ final_state = "virus"
        jump endings_entry


    scene cyberspace_core_ui
    with dissolve

    artemka "Выбери финальное состояние."
    artemka "Не конец."
    artemka "Форму."

    # Если не открыт ни один рут — только default
    if not (quins_done or nighstess_done or sand_done or hospital_done):
        artemka "У тебя нет оформленного ответа."
        artemka "Система применит значение по умолчанию."
        $ final_state = "default"
        jump core_finalize

    menu:
        "SELECT ENDING"

        "Quins: выход из киберспейса" if quins_done:
            $ final_state = "quins"
            jump core_finalize

        "Nighstess: остаться осознанно" if nighstess_done:
            $ final_state = "nighstess"
            jump core_finalize

        "Sand: пауза без выбора" if sand_done:
            $ final_state = "sand"
            jump core_finalize

        "Hospital: нормализация реальности" if hospital_done:
            $ final_state = "hospital"
            jump core_finalize


label core_finalize:

    scene cyberspace_core
    with dissolve

    artemka "Фиксация состояния."

    if final_state == "quins":
        artemka "Параметр: выход."
    elif final_state == "nighstess":
        artemka "Параметр: принятие."
    elif final_state == "sand":
        artemka "Параметр: пауза."
    elif final_state == "hospital":
        artemka "Параметр: нормализация."
    elif final_state == "virus":
        artemka "Параметр: вмешательство."
    else:
        artemka "Параметр: default."

    hamayumi "Идём."

    hide artemka
    with dissolve

    stop music fadeout 1.5

    jump endings_entry
