# scenes_act3.rpy
# Акт III — Конфликт (укорочен)
# Теперь: короткий "файт" аргументов -> прямой переход к финалу (core_entry)

label act3_entry:

    scene cyberspace_city
    with fade

    play music "audio/act3_conflict.ogg" fadein 1.0

    oliver "Город дрожит."
    oliver "Как будто ему больно."

    hamayumi "Схождение."
    hamayumi "Не людей."
    hamayumi "Аргументов."

    scene cyberspace_city
    with vpunch

    "Вывески перегорают."
    "Шумы складываются в ритм."
    "Ритм — в давление."

    oliver "Это… бой?"

    hamayumi "Да."
    hamayumi "Но без ударов."
    hamayumi "Только попытки назвать тебя вместо тебя."

    # --- Микро-файт: аргументы появляются быстро и перебивают друг друга ---
    scene cyberspace_pause
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
        scene hospital_room
        with dissolve
        play sound "audio/hospital_bleep.ogg"
        "Белый свет режет мысль."
        scene cyberspace_pause
        with dissolve

    if not (quins_done or nighstess_done or sand_done or hospital_done):
        hamayumi "Пусто."
        hamayumi "Значит, бой будет проще."
        hamayumi "Тебя будут брать не смыслом — усталостью."

    # --- Перелом: город пытается выбрать за героя ---
    scene cyberspace_city
    with vpunch

    "Город сжимается."
    "Улицы становятся коридорами."
    "Коридоры — стрелками."
    "Стрелки — одним направлением."

    oliver "Меня ведут."

    hamayumi "Потому что ядро не ждёт."
    hamayumi "Оно собирает то, что ты оставил."

    # --- Финальный 'файт'-вывод в 2–3 реплики ---
    hamayumi "Смотри:"
    hamayumi "Выход, принятие, пауза, нормализация."
    hamayumi "Это не персонажи. Это кнопки на тебе."

    stop music fadeout 1.5

    scene cyberspace_core_gate
    with fade

    "Впереди — CORE NODE."
    "Дверь без ручки."
    "Только интерфейс."

    hamayumi "Идём."
    hamayumi "Конец — это не сцена."
    hamayumi "Это выбранное состояние."

    jump core_entry
