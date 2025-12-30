# scenes_hub.rpy
# Акт II — Хаб + ветки персонажей + вирус (усиленная версия с зависимостями)

# NOTE:
# Все `default` переменные должны быть объявлены в state.rpy (один раз).
# Этот файл ТОЛЬКО использует/обновляет их.
#
# Ожидаемые переменные (примерно):
# hub_visits, avoid_counter, virus_risk, virus_active
# branch_visits_quins, branch_visits_nighstess, branch_visits_sand, branch_visits_hospital, branch_visits_patch
# quins_started, nighstess_started, sand_started, hospital_started
# quins_done, nighstess_done, sand_done, hospital_done
# quins_keys, nighstess_keys, sand_keys, hospital_keys
#
# Новые зависимости (добавь в state.rpy):
# trust_hamayumi, trust_quins, trust_nighstess
# drift_sand, reality_pull, identity_integrity
# virus_debt, virus_voice, patch_mark
# quins_nighstess_conflict, hospital_trace, sand_trace
# core_access_level

label hub_main:

    scene cyberspace_city
    with dissolve

    call hub_update_state

    # Если активен вирус-голос — иногда меняем тон меню/комментов
    if virus_voice >= 2:
        hamayumi "Слова стали короче."
        hamayumi "Это не облегчение. Это вычитание."

    # Если игрок уже закрыл хотя бы одну ветку — предупреждение о конфликте путей.
    if quins_done or nighstess_done or sand_done or hospital_done:
        hamayumi "Один путь уже оформился."
        hamayumi "Если продолжишь — начнётся конфликт смыслов."
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

    # Динамические вставки хаба — чтобы чувствовалось, что мир реагирует
    call hub_dynamic_inserts

    menu:
        "Куда идти?"

        "Статус хаба (диагностика)":
            call hub_status
            jump hub_main

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

        # Вирус может предлагать "удобную" паузу — это ловушка комфорта.
        "Сделать паузу (комфортно)" if virus_voice >= 2:
            $ avoid_counter += 1
            $ virus_debt += 1
            $ identity_integrity -= 1
            oliver "..."
            hamayumi "Так удобно, что страшно."
            jump hub_main

        "Ничего не делать":
            $ avoid_counter += 1
            oliver "..."
            hamayumi "Это тоже выбор."
            jump hub_main


# -------------------------
# Глобальные вставки / состояние
# -------------------------

label hub_update_state:

    $ hub_visits += 1

    # Нормализация целостности (на всякий)
    if identity_integrity < 0:
        $ identity_integrity = 0
    if identity_integrity > 10:
        $ identity_integrity = 10

    # Ранние подсказки
    if hub_visits == 2:
        hamayumi "Выбирай направление."
        hamayumi "Но не пытайся удержать все ответы сразу."

    # Круги по хабу — не просто штраф: это переводит тебя в режим "удобных решений"
    if hub_visits >= 6 and not (quins_done or nighstess_done or sand_done or hospital_done):
        hamayumi "Ты слишком долго ходишь кругами."
        hamayumi "Система это заметит."
        $ avoid_counter += 1
        $ virus_risk += 1

    # Долг вирусу растёт от избеганий (меньше, чем от патчей)
    if avoid_counter >= 3:
        $ virus_risk += 1
        $ virus_debt += 1

    # Целостность — главный индикатор: если падает, вирусу проще "говорить"
    if identity_integrity <= 3:
        $ virus_voice += 1

    # Метка рынка ускоряет
    if patch_mark and avoid_counter >= 2:
        $ virus_risk += 1

    # След песка делает "паузу" более вероятной (дрейф в тишину)
    if sand_trace >= 1 and hub_visits % 2 == 0:
        $ drift_sand += 1

    # След больницы влияет на "реальность" и на Хамаюми
    if hospital_trace >= 1 and hub_visits % 2 == 1:
        $ reality_pull += 1
        $ trust_hamayumi -= 1

    # Условие активации вируса — комбинация факторов
    if virus_risk >= 3 or virus_debt >= 4 or (patch_mark and identity_integrity <= 2):
        $ virus_active = True

    if virus_active:
        call zombi_whisper

    return


label hub_dynamic_inserts:

    # Вставки перед меню, чтобы хаб был "живым"
    if virus_active and virus_voice >= 2:
        hamayumi "Здесь стало слишком гладко."
        hamayumi "Как будто тебе заранее упростили выбор."

    if patch_mark and hub_visits >= 3:
        hamayumi "Рынок оставляет метки."
        hamayumi "Они не на коже — в привычках."

    if quins_done and nighstess_done:
        hamayumi "Две траектории спорят прямо в тебе."
        $ quins_nighstess_conflict += 1

    if drift_sand >= 3:
        hamayumi "Тишина начинает звучать как обещание."
        hamayumi "Не верь обещаниям без цены."

    if reality_pull >= 4:
        hamayumi "Слова 'нормально' становятся слишком удобными."
        hamayumi "Иногда это просто другое название для капитуляции."

    return


label ambient_reset:
    stop music fadeout 1.0
    play music "audio/ambient_cyberspace.ogg" fadein 1.0
    return


label hub_status:
    python:
        renpy.say(None,
            "Статус хаба:\n"
            "посещений: {}\n"
            "избегал: {}\n"
            "риск вируса: {}\n"
            "вирус активен: {}\n"
            "долг вирусу: {}\n"
            "голос вируса: {}\n"
            "метка патчей: {}\n"
            "целостность: {}\n"
            "доверие Хамаюми: {}\n"
            "доверие Quins: {}\n"
            "доверие Nighstess: {}\n"
            "дрейф песка: {}\n"
            "тяга к реальности: {}\n"
            "доступ ядра: {}\n".format(
                hub_visits, avoid_counter, virus_risk, virus_active,
                virus_debt, virus_voice, patch_mark,
                identity_integrity,
                trust_hamayumi, trust_quins, trust_nighstess,
                drift_sand, reality_pull,
                core_access_level
            )
        )

    menu:
        "Назад":
            return


label zombi_whisper:

    play sound "audio/glitch_short.ogg"

    # Чем сильнее голос вируса — тем менее "свой" Хамаюми
    if virus_voice >= 3:
        hamayumi "Слышишь?"
        hamayumi "Тут есть кто-то третий."
        hamayumi "И он экономит на тебе."
    else:
        hamayumi "Слышишь?"
        hamayumi "Тут есть кто-то третий."

    oliver "Что это?"

    if trust_hamayumi <= -2:
        hamayumi "..."
        hamayumi "Не отвечай."
    else:
        hamayumi "Не отвечай."
        hamayumi "Не соглашайся."

    return


# -------------------------
# Рынок патчей (вирус / контракты)
# -------------------------

label patch_market:

    scene cyberspace_market
    with dissolve

    play music "audio/ambient_market.ogg" fadein 1.0

    $ patch_mark = True

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
            $ virus_debt += 1
            zombi "Я упрощаю."
            zombi "Убираю лишнее."
            zombi "Сомнения — лишнее."
            hamayumi "Не продолжай."

        "Согласиться на пробник":
            $ virus_risk += 2
            $ virus_debt += 2
            $ virus_voice += 1
            $ identity_integrity -= 1
            $ virus_active = True
            zombi "Установка началась."
            play sound "audio/install_tick.ogg"
            hamayumi "..."

        "Поторговаться: \"дать меньше\"":
            $ virus_debt += 1
            $ identity_integrity -= 1
            zombi "Ты уже понял механику."
            zombi "Меньше боли — меньше тебя."
            hamayumi "Мы уходим."

        "Уйти молча":
            $ avoid_counter += 1
            $ virus_debt += 1
            zombi "Увидимся, когда устанешь быть собой."

    hide zombi
    with dissolve

    call ambient_reset
    return


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

    return


# -------------------------
# Ветка Quins (5 экранов) — "честная цена"
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

        # Перекрестная реакция Quins на Nighstess/Hospital
        if trust_nighstess >= 2:
            quins "Ты принёс с крыши чужую ясность."
            quins "Она удобная. И потому опасная."
        if hospital_trace >= 1:
            quins "На тебе чужой протокол."
            quins "Его цель — назвать тебя и успокоиться."

    menu:
        "Quins — первый шаг"

        "Мне нужен выход.":
            $ quins_keys += 1
            $ trust_quins += 1
            $ identity_integrity += 1
            quins "Тогда слушай внимательно."
            hamayumi "Ей можно верить."

        "Ты реальная или программа?":
            quins "Разницы нет, если выбор твой."
            $ identity_integrity += 1

        "Я хочу стать сильнее всех.":
            $ virus_risk += 1
            $ virus_debt += 1
            quins "Сила без цели — удобная клетка."
            $ identity_integrity -= 1

    scene cyberspace_tunnel
    with dissolve

    quins "Контракт на личность выглядит как кнопка."
    quins "Но цена — всегда память."

    menu:
        "Что отдать двери?"

        "Тёплое воспоминание":
            $ quins_keys += 1
            $ identity_integrity += 1
            quins "Дорого. Значит честно."

        "Страшное воспоминание":
            $ avoid_counter += 1
            $ virus_debt += 1
            quins "Если выбросить страх, он найдёт другой вход."
            $ identity_integrity -= 1

        "Пустышку":
            $ virus_debt += 1
            $ identity_integrity -= 1
            quins "Ты хочешь обмануть систему."
            quins "Она терпелива, но не глупа."

    scene cyberspace_market
    with dissolve

    show zombi at center
    with dissolve

    zombi "О, вы вдвоём."
    if patch_mark:
        zombi "Ты уже отмечен."
        zombi "Значит, торг тебе знаком."
    zombi "Хочешь быстро?"

    hamayumi "Не отвечай."

    menu:
        "Ответ на соблазн"

        "Молчать и уйти":
            $ quins_keys += 1
            $ identity_integrity += 1
            quins "Хорошо."
            zombi "Ладно. Пока."

        "Спросить про апдейт":
            $ virus_risk += 1
            $ virus_debt += 1
            zombi "Я упрощаю тебя."
            quins "Мы уходим."
            $ identity_integrity -= 1

        "Согласиться на пробник":
            $ virus_risk += 2
            $ virus_debt += 2
            $ virus_voice += 1
            $ identity_integrity -= 1
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

        "Я хочу уйти, даже если там будет тяжело":
            $ quins_keys += 1
            $ trust_quins += 1
            $ identity_integrity += 1
            quins "Тогда шанс есть."

        "Я хочу уйти, потому что тут скучно":
            $ avoid_counter += 1
            $ virus_debt += 1
            quins "Тогда ты просто меняешь декорации."
            $ identity_integrity -= 1

        "Я хочу остаться, но чтобы ты была рядом":
            quins "Я не якорь."
            quins "Я — проводник."

    scene cyberspace_church
    with fade

    # Итог Quins: даёт высокий доступ к ядру, если ты не ушёл в вирус
    if quins_keys >= 3 and not virus_active and virus_debt <= 2:
        $ quins_done = True
        $ core_access_level += 2
        $ trust_quins += 1
        $ identity_integrity += 1
        quins "Я запомнила твою траекторию."
        quins "В ядре у тебя будет вариант — без упрощения."
        hamayumi "Это открывает лучший выход."
    else:
        $ avoid_counter += 1
        quins "Ты ещё не готов."
        quins "Или уже начал платить не туда."
        if virus_debt >= 3:
            quins "У долга будет момент взыскания."
        $ identity_integrity -= 1

    hide quins
    with dissolve

    call ambient_reset
    return


# -------------------------
# Ветка Nighstess (5 экранов) — "инженерия принятия"
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

        if trust_quins >= 2:
            nighstess "Quins продаёт боль как смысл."
            nighstess "Иногда это просто красивое название для страха."
            $ quins_nighstess_conflict += 1

    menu:
        "Nighstess — тезис"

        "А если реальный мир хуже?":
            $ nighstess_keys += 1
            $ trust_nighstess += 1
            $ identity_integrity += 1
            nighstess "Вот честный вопрос."

        "Это иллюзия.":
            $ avoid_counter += 1
            $ virus_debt += 1
            nighstess "И всё же ты здесь."
            $ identity_integrity -= 1

        "Ты хочешь, чтобы я остался?":
            nighstess "Я хочу, чтобы ты не притворялся."
            $ identity_integrity += 1

    scene cyberspace_pause
    with dissolve

    nighstess "В реальности ты диагноз."
    nighstess "Здесь ты процесс, который может думать."

    menu:
        "Ответ"

        "А если бегство — форма выживания?":
            $ nighstess_keys += 1
            $ identity_integrity += 1
            nighstess "Тогда ты понимаешь."

        "Ты оправдываешь бегство.":
            $ avoid_counter += 1
            $ virus_debt += 1
            nighstess "Я называю вещи своими именами."
            $ identity_integrity -= 1

        "Я ищу Quins.":
            nighstess "Тогда ты ищешь обещание."
            $ quins_nighstess_conflict += 1

    scene cyberspace_simroom
    with dissolve

    nighstess "Я показываю варианты."
    nighstess "Не заставляю."

    menu:
        "Оценка Nighstess"

        "Ты адаптировался.":
            $ nighstess_keys += 1
            $ trust_nighstess += 1
            $ identity_integrity += 1
            nighstess "Наконец."

        "Ты сломался.":
            $ avoid_counter += 1
            $ virus_debt += 1
            nighstess "Ломаются те, кто выходит."
            $ identity_integrity -= 1

        "Ты боишься выйти снова.":
            nighstess "Страх — не аргумент. Это данные."
            $ identity_integrity += 1

    scene cyberspace_rooftop
    with dissolve

    nighstess "Я не переписываю тебя."
    nighstess "Я предлагаю жить здесь осознанно."

    menu:
        "Решение"

        "Я хочу остаться и принять это.":
            $ nighstess_keys += 1
            $ trust_nighstess += 1
            $ identity_integrity += 1
            nighstess "Тогда у тебя будет режим в ядре."

        "Я не готов решать.":
            $ avoid_counter += 1
            $ virus_debt += 1
            nighstess "Тогда решат за тебя."
            $ identity_integrity -= 1

        "Отдай мне автопилот.":
            # Опасный выбор: спокойствие ценой голоса вируса
            $ virus_debt += 2
            $ virus_voice += 1
            $ identity_integrity -= 1
            nighstess "Можно."
            nighstess "Но автопилот любит, когда ты исчезаешь из решения."

    scene cyberspace_city
    with fade

    if nighstess_keys >= 3 and not virus_active and virus_debt <= 3:
        $ nighstess_done = True
        $ core_access_level += 2
        $ trust_nighstess += 1
        nighstess "Я отметил твой вектор."
        nighstess "В ядре тебе дадут режим."
        hamayumi "Это откроет хорошую концовку."
    else:
        $ avoid_counter += 1
        nighstess "Ты ещё не выбрал."
        nighstess "Ты коллекционируешь слова."
        if virus_voice >= 2:
            nighstess "И кто-то уже выбирает формулировки за тебя."

    hide nighstess
    with dissolve

    call ambient_reset
    return


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
    return


# -------------------------
# Ветка Больницы (5 экранов) — "перепрошивка интерпретации"
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

    # Безопасная формулировка: не про самоповреждение, а про "остановить власть симптома"
    oliver "Если это всё симптом…"
    oliver "Тогда я могу остановить это."

    scene hospital_office
    with dissolve

    show doctor at center
    with dissolve

    doctor "Салатик Оливер."
    doctor "Расскажите, что вы видите."

    if patch_mark:
        doctor "И не спешите упрощать ответ."
        doctor "Я слышу в ваших словах знакомый сценарий."

    menu:
        "Ответ врачу"

        "Это фантазии. Просто шум.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ hospital_trace += 1
            doctor "Хорошо."
            doctor "Мы назовём это и перестанем подпитывать."
            $ identity_integrity -= 1

        "Я видел Quins.":
            $ avoid_counter += 1
            $ hospital_trace += 1
            doctor "Мы разберём это позже."
            $ trust_hamayumi -= 1

        "Я видел город.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ hospital_trace += 1
            doctor "Это реакция на стресс."
            $ identity_integrity -= 1

        "Я не уверен. Но это влияет на выбор.":
            $ hospital_keys += 1
            $ identity_integrity += 1
            $ hospital_trace += 1
            doctor "Это честный ответ."

    hide doctor
    with dissolve

    scene hospital_room
    with dissolve

    if trust_hamayumi <= -2:
        hamayumi "..."
        hamayumi "Ты называешь меня — и я становлюсь меньше."
    else:
        hamayumi "Ты стираешь меня словами."

    menu:
        "Что делать?"

        "Позвать врача и закрыть это":
            $ hospital_keys += 1
            $ reality_pull += 2
            $ trust_hamayumi -= 1
            $ identity_integrity -= 1
            hamayumi "..."

        "Остановиться и поверить Хамаюми":
            $ avoid_counter += 1
            $ trust_hamayumi += 1
            $ identity_integrity += 1
            hamayumi "Тогда ты ещё держишься."

        "Промолчать":
            $ hospital_keys += 1
            $ virus_debt += 1
            $ identity_integrity -= 1
            hamayumi "Понял."

    scene hospital_room
    with dissolve

    show nurse at center
    with dissolve

    nurse "Сегодня спокойно."
    if sand_trace >= 1:
        nurse "Вы стали слишком тихим."
    nurse "Вы меньше говорите о киберспейсе."

    menu:
        "Ответ"

        "Потому что его нет.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ identity_integrity -= 1

        "Потому что я устал.":
            $ avoid_counter += 1
            $ identity_integrity += 1

        "Потому что я боюсь ошибиться.":
            $ avoid_counter += 1
            $ identity_integrity += 1

    hide nurse
    with dissolve

    scene hospital_room
    with fade

    if hospital_keys >= 3:
        $ hospital_done = True
        $ core_access_level += 1
        $ reality_pull += 2
        $ hospital_trace += 1
        oliver "Если я перестану давать этому власть — оно ослабнет."
        hamayumi "Тогда в ядре у тебя останется только реальность."
        # Цена: реальность может "съесть" внутренний голос
        $ trust_hamayumi -= 1
    else:
        $ avoid_counter += 1
        hamayumi "Ты сомневаешься."
        hamayumi "Значит, связь ещё держится."
        $ identity_integrity += 1

    call ambient_reset
    return


# -------------------------
# Выход из Акта II
# -------------------------

# NOTE: `act2_exit` is defined in scenes_act2.rpy. The duplicate definition
# that previously lived here has been removed to avoid label conflicts.


# -------------------------
# Точка входа Акта III (label должен существовать)
# -------------------------

# NOTE: `act3_entry` is defined in scenes_act3.rpy. The placeholder here
# has been removed to prevent duplicate label definitions.
