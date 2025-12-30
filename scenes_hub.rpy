# scenes_hub.rpy
# Хаб Акта II + ветки персонажей + глобальный триггер вируса

label hub_main:

    scene cyberspace_city
    with dissolve

    $ hub_visits += 1

    if hub_visits == 2:
        hamayumi "Выбирай направление."
        hamayumi "Но не пытайся удержать все ответы сразу."

    if hub_visits >= 6 and not (quins_done or nighstess_done or sand_done or hospital_done):
        hamayumi "Ты слишком долго ходишь кругами."
        hamayumi "Система это заметит."
        $ avoid_counter += 1

    if avoid_counter >= 3:
        $ virus_risk += 1

    if virus_risk >= 3:
        $ virus_active = True

    if virus_active:
        call zombi_whisper

    if quins_done or nighstess_done or sand_done or hospital_done:
        hamayumi "Один путь уже оформился."
        hamayumi "Если продолжишь — начнётся конфликт."
        menu:
            "Дальше?"
            "Вернуться в хаб ещё раз":
                jump hub_menu
            "Идти дальше":
                jump act2_exit

    jump hub_menu


label hub_menu:

    scene cyberspace_city
    with dissolve

    menu:
        "Куда идти?"
        "Тихий тоннель (Quins)" if not quins_done:
            $ branch_visits_quins += 1
            call branch_quins
            jump hub_main

        "Крыша мегаблока (Nighstess)" if not nighstess_done:
            $ branch_visits_nighstess += 1
            call branch_nighstess
            jump hub_main

        "Край города (Песок Песочнеков)" if not sand_done:
            $ branch_visits_sand += 1
            call branch_sand
            jump hub_main

        "Белый шум (Больница)" if not hospital_done:
            $ branch_visits_hospital += 1
            call branch_hospital
            jump hub_main

        "Рынок патчей (опасно)":
            $ branch_visits_patch += 1
            call patch_market
            jump hub_main

        "Случайная встреча (ВаняЗолотов)":
            call cameo_vanya
            jump hub_main

        "Ничего не делать":
            $ avoid_counter += 1
            oliver "..."
            hamayumi "Это тоже выбор."
            jump hub_main


# -------------------------
# Глобальные вставки
# -------------------------

label zombi_whisper:

    play sound "audio/glitch_short.ogg"
    hamayumi "Слышишь?"
    hamayumi "Тут есть кто-то третий."

    oliver "Что это?"

    hamayumi "Не отвечай."
    hamayumi "Не соглашайся."
    return


label patch_market:

    scene cyberspace_market
    with dissolve

    play music "audio/ambient_market.ogg" fadein 1.0

    oliver "Здесь продают… состояния."

    hamayumi "И долги."
    hamayumi "Плати собой — и тебя перепишут."

    show zombi at center
    with dissolve

    zombi "Салатик Оливер."
    zombi "Хочешь апдейт без боли?"

    hamayumi "Нет."

    menu:
        "Рынок патчей — выбор"
        "Спросить, что он делает":
            $ virus_risk += 1
            zombi "Я упрощаю."
            zombi "Убираю лишнее."
            zombi "Сомнения — лишнее."
            hamayumi "Не продолжай."

        "Согласиться на пробник":
            $ virus_risk += 3
            $ virus_active = True
            zombi "Установка началась."
            play sound "audio/install_tick.ogg"
            hamayumi "..."

        "Уйти молча":
            $ avoid_counter += 1
            zombi "Увидимся, когда устанешь быть собой."

    hide zombi
    with dissolve

    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0

    return


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
    return


# -------------------------
# Ветка Quins (5 экранов)
# -------------------------

label branch_quins:

    if not quins_started:
        $ quins_started = True

        scene cyberspace_church
        with fade

        play music "audio/quins_theme.ogg" fadein 1.5

        hamayumi "Тут чинят головы."
        hamayumi "Иногда — вместе с человеком."

        show quins at center
        with dissolve

        quins "Ты пришёл не туда, куда хотел."
        quins "Но туда, куда нужно."

        oliver "Ты меня знаешь?"

        quins "Я вижу тех, кто ещё способен сохранить себя."

    else:
        scene cyberspace_church
        with dissolve
        show quins at center
        with dissolve

    menu:
        "Quins — первый шаг"
        "Мне нужен выход.":
            $ quins_keys += 1
            quins "Тогда слушай внимательно."
            hamayumi "Ей можно верить."
        "Ты реальная или программа?":
            quins "Разницы нет, если выбор твой."
        "Я хочу стать сильнее всех.":
            $ virus_risk += 1
            quins "Сила без цели — удобная клетка."

    scene cyberspace_tunnel
    with dissolve

    quins "Контракт на личность выглядит как кнопка."
    quins "Но цена — всегда память."

    menu:
        "Что отдать двери?"
        "Тёплое воспоминание":
            $ quins_keys += 1
            quins "Дорого. Значит честно."
        "Страшное воспоминание":
            $ avoid_counter += 1
            quins "Если выбросить страх, он найдёт другой вход."
        "Пустышку":
            quins "Ты хочешь обмануть систему."
            quins "Она терпелива, но не глупа."

    scene cyberspace_market
    with dissolve

    show zombi at center
    with dissolve

    zombi "О, вы вдвоём."
    zombi "Хочешь быстро?"

    hamayumi "Не отвечай."

    menu:
        "Ответ на соблазн"
        "Молчать и уйти":
            $ quins_keys += 1
            quins "Хорошо."
            zombi "Ладно. Пока."
        "Спросить про апдейт":
            $ virus_risk += 1
            zombi "Я упрощаю тебя."
            quins "Мы уходим."
        "Согласиться на пробник":
            $ virus_risk += 3
            $ virus_active = True
            zombi "Установка началась."
            hamayumi "..."
            quins "Поздно."

    hide zombi
    with dissolve

    scene cyberspace_shaft
    with dissolve

    quins "Выход — не дверь."
    quins "Это готовность не прятаться."

    menu:
        "Ответ Quins"
        "Я хочу уйти, даже если там будет больно":
            $ quins_keys += 1
            quins "Тогда шанс есть."
        "Я хочу уйти, потому что тут скучно":
            $ avoid_counter += 1
            quins "Тогда ты просто меняешь декорации."
        "Я хочу остаться, но чтобы ты была рядом":
            quins "Я не якорь."
            quins "Я — проводник."

    scene cyberspace_church
    with fade

    if quins_keys >= 3 and not virus_active:
        $ quins_done = True
        quins "Я запомнила твою траекторию."
        quins "Если дойдёшь до ядра — у тебя будет вариант."
        hamayumi "Это открывает лучший выход."
    else:
        $ avoid_counter += 1
        quins "Ты ещё не готов."
        quins "Не обманывай себя."

    hide quins
    with dissolve

    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0

    return


# -------------------------
# Ветка Nighstess (5 экранов)
# -------------------------

label branch_nighstess:

    if not nighstess_started:
        $ nighstess_started = True

        scene cyberspace_rooftop
        with fade

        play music "audio/nighstess_theme.ogg" fadein 1.5

        show nighstess at center
        with dissolve

        nighstess "Ты всё ещё ищешь выход?"
        nighstess "Здесь никто не держит силой."

        hamayumi "Он опасен спокойствием."

    else:
        scene cyberspace_rooftop
        with dissolve
        show nighstess at center
        with dissolve

    menu:
        "Nighstess — тезис"
        "А если реальный мир хуже?":
            $ nighstess_keys += 1
            nighstess "Вот честный вопрос."
        "Это иллюзия.":
            $ avoid_counter += 1
            nighstess "И всё же ты здесь."
        "Ты хочешь, чтобы я остался?":
            nighstess "Я хочу, чтобы ты не притворялся."

    scene cyberspace_pause
    with dissolve

    nighstess "В реальности ты диагноз."
    nighstess "Здесь ты процесс, который может думать."

    menu:
        "Ответ"
        "А если бегство — форма выживания?":
            $ nighstess_keys += 1
            nighstess "Тогда ты понимаешь."
        "Ты оправдываешь бегство.":
            $ avoid_counter += 1
            nighstess "Я называю вещи своими именами."
        "Я ищу Quins.":
            nighstess "Тогда ты ищешь обещание."

    scene cyberspace_simroom
    with dissolve

    nighstess "Я показываю варианты."
    nighstess "Не заставляю."

    menu:
        "Оценка Nighstess"
        "Ты адаптировался.":
            $ nighstess_keys += 1
            nighstess "Наконец."
        "Ты сломался.":
            $ avoid_counter += 1
            nighstess "Ломаются те, кто выходит."
        "Ты боишься выйти снова.":
            nighstess "Страх — не аргумент. Это данные."

    scene cyberspace_rooftop
    with dissolve

    nighstess "Я не переписываю тебя."
    nighstess "Я предлагаю жить здесь осознанно."

    menu:
        "Решение"
        "Я хочу остаться и принять это.":
            $ nighstess_keys += 1
            nighstess "Тогда у тебя будет выбор в ядре."
        "Я не готов решать.":
            $ avoid_counter += 1
            nighstess "Тогда решат за тебя."
        "Я хочу выйти, но боюсь.":
            nighstess "Тогда ты ещё держишься за старый интерфейс."

    scene cyberspace_city
    with fade

    if nighstess_keys >= 3 and not virus_active:
        $ nighstess_done = True
        nighstess "Я отметил твой вектор."
        nighstess "В ядре тебе дадут режим."
        hamayumi "Это откроет хорошую концовку."
    else:
        $ avoid_counter += 1
        nighstess "Ты ещё не выбрал."
        nighstess "Ты коллекционируешь слова."

    hide nighstess
    with dissolve

    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0

    return


# -------------------------
# Ветка Песок Песочнеков (5 экранов)
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

    menu:
        "Песок — ощущение"
        "Это похоже на покой.":
            $ sand_keys += 1
            sand "Покой — это отсутствие требования."
        "Это пустота.":
            $ avoid_counter += 1
            sand "Пустота — это честность."
        "Это смерть.":
            sand "В киберспейсе нет смерти."
            sand "Есть прекращение выбора."

    scene cyberspace_desert
    with dissolve

    sand "Здесь не зовут остаться."
    sand "И не тянут выйти."

    menu:
        "Позиция"
        "Остановка — честно.":
            $ sand_keys += 1
            sand "Да."
        "Я не хочу так закончить.":
            $ avoid_counter += 1
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
        "Остаться здесь, ничего не решая.":
            $ sand_keys += 1
            sand "Тогда система перестанет замечать тебя."
        "Вернуться и выбрать сторону.":
            $ avoid_counter += 1
            sand "Тогда ты снова войдёшь в спор."
        "Закрыть глаза и ждать.":
            $ avoid_counter += 1
            sand "Ждать — тоже выбор."

    scene cyberspace_edge
    with dissolve

    sand "Даже ядро не любит неопределённость."
    sand "Но оно терпит, пока ты тихий."

    scene cyberspace_edge
    with fade

    if sand_keys >= 3 and not virus_active:
        $ sand_done = True
        sand "Если ты дойдёшь до ядра — тебе оставят нейтральный выход."
        hamayumi "Это мир из песка."
    else:
        $ avoid_counter += 1
        sand "Ты ещё дергаешься."
        sand "Значит, пауза не твоя."

    hide sand
    with dissolve

    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0

    return


# -------------------------
# Ветка Больницы (5 экранов)
# -------------------------

label branch_hospital:

    if not hospital_started:
        $ hospital_started = True

        scene hospital_room
        with fade

        play music "audio/ambient_hospital.ogg" fadein 1.5

        oliver "Белый свет."
        oliver "Слишком реальный."

        hamayumi "Это пробой."
        hamayumi "Если ты примешь его — киберспейс отступит."

    else:
        scene hospital_room
        with dissolve

    oliver "Если это всё симптом…"
    oliver "Тогда я могу закончить."

    scene hospital_office
    with dissolve

    show doctor at center
    with dissolve

    doctor "Салатик Оливер."
    doctor "Расскажите, что вы видите."

    menu:
        "Ответ врачу"
        "Это фантазии. Просто шум.":
            $ hospital_keys += 1
            doctor "Хорошо."
        "Я видел Quins.":
            $ avoid_counter += 1
            doctor "Мы разберём это позже."
        "Я видел город.":
            doctor "Это реакция на стресс."

    hide doctor
    with dissolve

    scene hospital_room
    with dissolve

    hamayumi "Ты стираешь меня собой."

    menu:
        "Что делать?"
        "Позвать врача и закрыть это":
            $ hospital_keys += 1
            hamayumi "..."
        "Остановить и поверить Хамаюми":
            $ avoid_counter += 1
            hamayumi "Тогда ты ещё держишься."
        "Промолчать":
            $ hospital_keys += 1
            hamayumi "Понял."

    scene hospital_room
    with dissolve

    show nurse at center
    with dissolve

    nurse "Сегодня спокойно."
    nurse "Вы больше не говорите о киберспейсе."

    menu:
        "Ответ"
        "Потому что его нет.":
            $ hospital_keys += 1
        "Потому что я устал.":
            $ avoid_counter += 1
        "Потому что я боюсь.":
            $ avoid_counter += 1

    hide nurse
    with dissolve

    scene hospital_room
    with fade

    if hospital_keys >= 3:
        $ hospital_done = True
        oliver "Если я перестану верить — всё исчезнет."
        hamayumi "Тогда в ядре у тебя останется только реальность."
    else:
        $ avoid_counter += 1
        hamayumi "Ты сомневаешься."
        hamayumi "Значит, связь ещё держится."

    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0

    return
