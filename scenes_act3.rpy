# scenes_act3.rpy
# Акт III - Конфликт (укорочен)
# Теперь: короткий "файт" аргументов -> прямой переход к финалу (core_entry)

label act3_entry:

    scene bg cyberspace_city
    with fade

    play music "audio/act3_conflict.ogg" fadein 1.0

    oliver "Город дрожит."
    oliver "Как будто ему больно."
    oliver "Я взорву тут всё"

    voice "audio/Hamayumi/act_3/1.mp3"
    show hamayumi at left
    hamayumi "Схождение."
    voice "audio/Hamayumi/act_3/2.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Не людей."
    voice "audio/Hamayumi/act_3/3.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Аргументов."

    scene bg cyberspace_city
    with vpunch

    "Вывески перегорают."
    "Шумы складываются в ритм."
    "Ритм - в давление."

    oliver "Это... бой?"
    oliver "О мой бой"
    voice "audio/Hamayumi/act_3/4.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Да."
    voice "audio/Hamayumi/act_3/5.mp3"
    hide hamayumi_forw
    show hamayumi_you at left
    hamayumi "Но без ударов."
    voice "audio/Hamayumi/act_3/6.mp3"
    hide hamayumi_you
    show hamayumi_cry at left
    hamayumi "Только попытки назвать тебя вместо тебя."

    # --- Микро-файт: аргументы появляются быстро и перебивают друг друга ---
    scene bg cyberspace_pause
    with dissolve

    if quins_done:
        show quins at center
        with dissolve
        quins "Решение. Шаг. Выход."
        hide quins
        with dissolve

    if nighstess_done:
        show nighstess at center
        with dissolve
        nighstess "Принять. Настроить. Жить внутри."
        hide nighstess
        with dissolve

    if sand_done:
        show sand at center
        with dissolve
        sand "Пауза. Тишина. Не требовать."
        hide sand
        with dissolve

    if hospital_done:
        scene bg hospital_room
        with dissolve
        play sound "audio/hospital_bleep.ogg"
        "Белый свет режет мысль."
        scene bg cyberspace_pause
        with dissolve

    if not (quins_done or nighstess_done or sand_done or hospital_done):
        voice "audio/Hamayumi/act_3/7.mp3"
        hide hamayumi_cry
        show hamayumi_you at left
        hamayumi "Пусто."
        voice "audio/Hamayumi/act_3/8.mp3"
        hide hamayumi_you
        show hamayumi at left
        hamayumi "Значит, бой будет проще."
        voice "audio/Hamayumi/act_3/9.mp3"
        hide hamayumi
        show hamayumi_up at left
        hamayumi "Тебя будут брать не смыслом - усталостью."

    # --- Перелом: город пытается выбрать за героя ---
    scene bg cyberspace_city
    with vpunch

    "Город сжимается."
    "Улицы становятся коридорами."
    "Коридоры - стрелками."
    "Стрелки - одним направлением."

    oliver "Матвей. Веди.!.!"
    voice "audio/Hamayumi/act_3/10.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Потому что ядро не ждёт."
    voice "audio/Hamayumi/act_3/11.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Оно собирает то, что ты оставил."

    # --- Финальный 'файт'-вывод в 2–3 реплики ---
    voice "audio/Hamayumi/act_3/12.mp3"
    hide hamayumi_forw
    show hamayumi_you at left
    hamayumi "Смотри:"
    voice "audio/Hamayumi/act_3/13.mp3"
    hide hamayumi_you
    show hamayumi_cry at left
    hamayumi "Выход, принятие, пауза, нормализация."
    voice "audio/Hamayumi/act_3/14.mp3"
    hide hamayumi_cry
    show hamayumi_you at left
    hamayumi "Это не персонажи. Это кнопки на тебе."
    hamayumi ".!."

    stop music fadeout 1.5

    scene  black
    with fade

    "Впереди - CORE NODE."
    "Дверь без ручки."
    "Только интерфейс."
    ".!."
    ":0"
    voice "audio/Hamayumi/act_3/15.mp3"
    hide hamayumi_you
    show hamayumi at left
    hamayumi "Идём."
    voice "audio/Hamayumi/act_3/16.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Конец - это не сцена."
    voice "audio/Hamayumi/act_3/17.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Это выбранное состояние."

    hide hamayumi_T
    jump core_entry
