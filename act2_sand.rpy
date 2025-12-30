
# -------------------------
# Ветка Песка (5 экранов) — "архив состояний"
# -------------------------

label branch_sand:

    if not sand_started:
        $ sand_started = True

        scene cyberspace_edge
        with fade

        play music "audio/sand_theme.ogg" fadein 1.5

        hamayumi "Край."
        hamayumi "Тут система перестаёт объяснять."

        show sand at center
        with dissolve

        sand "Добро пожаловать туда, где никто не спорит о смысле."

    else:
        scene cyberspace_edge
        with dissolve
        show sand at center
        with dissolve

        if virus_active:
            sand "Когда мир упрощают, он становится похож на песок."
            sand "Только песок честнее."

    menu:
        "Песок — ощущение"

        "Это похоже на покой.":
            $ sand_keys += 1
            $ drift_sand += 1
            sand "Покой — это отсутствие требования."

        "Это пустота.":
            $ avoid_counter += 1
            $ drift_sand += 1
            sand "Пустота — это честность."

        "Это архив.":
            $ sand_keys += 1
            $ identity_integrity += 1
            sand "Да."
            sand "Здесь лежат решения, которые так и не стали выбором."

    scene cyberspace_desert
    with dissolve

    sand "Здесь не зовут остаться."
    sand "И не тянут выйти."

    # Отголоски (делают место "живым")
    if drift_sand >= 2:
        "Голос" "Я почти выбрал."
        "Голос" "Я отложил навсегда."

    menu:
        "Позиция"

        "Остановка — честно.":
            $ sand_keys += 1
            $ drift_sand += 1
            sand "Да."

        "Я не хочу так закончить.":
            $ avoid_counter += 1
            $ identity_integrity += 1
            sand "Тогда ты всё ещё ищешь форму."

        "Это ловушка.":
            sand "Ловушка — когда от тебя что-то хотят."
            sand "Я ничего не хочу."

    scene cyberspace_desert
    with dissolve

    sand "Те следы — не люди."
    sand "Это состояния, которые перестали требовать будущего."

    menu:
        "Ещё шаг"

        "Взять зерно (артефакт)":
            $ sand_keys += 1
            $ sand_trace += 1
            $ identity_integrity += 1
            sand "Это напоминание."
            sand "О цене тишины."

        "Остаться здесь, ничего не решая.":
            $ sand_keys += 1
            $ drift_sand += 1
            $ identity_integrity -= 1
            sand "Тогда система перестанет замечать тебя."

        "Вернуться и выбрать сторону.":
            $ avoid_counter += 1
            $ identity_integrity += 1
            sand "Тогда ты снова войдёшь в спор."

    scene cyberspace_edge
    with dissolve

    sand "Даже ядро не любит неопределённость."
    sand "Но оно терпит, пока ты тихий."

    scene cyberspace_edge
    with fade

    if sand_keys >= 3 and not virus_active:
        $ sand_done = True
        $ core_access_level += 1
        $ drift_sand += 1
        sand "Если ты дойдёшь до ядра — тебе оставят нейтральный выход."
        hamayumi "Это мир из песка."
    else:
        $ avoid_counter += 1
        sand "Ты ещё дергаешься."
        sand "Значит, пауза не твоя."
        if virus_active:
            sand "Или пауза стала чужим инструментом."

    hide sand
    with dissolve

    call ambient_reset
    jump act2_after_sand
