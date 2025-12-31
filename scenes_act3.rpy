# scenes_act3.rpy
# Акт III — Конфликт (укорочен)
# Теперь: короткий "файт" аргументов -> прямой переход к финалу (core_entry)

label act3_entry:

    scene bg cyberspace_city
    with fade

    play music "audio/act3_conflict.ogg" fadein 1.0

    oliver "Город дрожит."
    oliver "Как будто ему больно."
    voice "audio/Hamayumi/act_3/1.mp3"
    hamayumi "Схождение."
    voice "audio/Hamayumi/act_3/2.mp3"
    hamayumi "Не людей."
    voice "audio/Hamayumi/act_3/3.mp3"
    hamayumi "Аргументов."

    scene bg cyberspace_city
    with vpunch

    "Вывески перегорают."
    "Шумы складываются в ритм."
    "Ритм — в давление."

    oliver "Это… бой?"
    voice "audio/Hamayumi/act_3/4.mp3"
    hamayumi "Да."
    voice "audio/Hamayumi/act_3/5.mp3"
    hamayumi "Но без ударов."
    voice "audio/Hamayumi/act_3/6.mp3"
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
        hamayumi "Пусто."
        voice "audio/Hamayumi/act_3/8.mp3"
        hamayumi "Значит, бой будет проще."
        voice "audio/Hamayumi/act_3/9.mp3"
        hamayumi "Тебя будут брать не смыслом — усталостью."

    # --- Перелом: город пытается выбрать за героя ---
    scene bg cyberspace_city
    with vpunch

    "Город сжимается."
    "Улицы становятся коридорами."
    "Коридоры — стрелками."
    "Стрелки — одним направлением."

    oliver "Меня ведут."
    voice "audio/Hamayumi/act_3/10.mp3"
    hamayumi "Потому что ядро не ждёт."
    voice "audio/Hamayumi/act_3/11.mp3"
    hamayumi "Оно собирает то, что ты оставил."

    # --- Финальный 'файт'-вывод в 2–3 реплики ---
    voice "audio/Hamayumi/act_3/12.mp3"
    hamayumi "Смотри:"
    voice "audio/Hamayumi/act_3/13.mp3"
    hamayumi "Выход, принятие, пауза, нормализация."
    voice "audio/Hamayumi/act_3/14.mp3"
    hamayumi "Это не персонажи. Это кнопки на тебе."

    stop music fadeout 1.5

    scene bg cyberspace_core_gate
    with fade

    "Впереди — CORE NODE."
    "Дверь без ручки."
    "Только интерфейс."
    voice "audio/Hamayumi/act_3/15.mp3"
    hamayumi "Идём."
    voice "audio/Hamayumi/act_3/16.mp3"
    hamayumi "Конец — это не сцена."
    voice "audio/Hamayumi/act_3/17.mp3"
    hamayumi "Это выбранное состояние."

    jump core_entry
