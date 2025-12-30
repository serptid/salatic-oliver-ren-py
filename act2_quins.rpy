# -------------------------
# Ветка Quins (5 экранов) — "честная цена"
# Открывает концовку Quins только при 3/3 правильных выборах
# -------------------------

label branch_quins:

    # локальный счётчик правильных выборов в этой ветке
    $ quins_score = 0

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

    menu:
        "Quins — первый шаг"

        "Мне нужен выход.":
            $ quins_score += 1
            quins "Тогда слушай внимательно."
            hamayumi "Ей можно верить."

        "Ты реальная или программа?":
            quins "Разницы нет, если выбор твой."

        "Я хочу стать сильнее всех.":
            quins "Сила без цели — удобная клетка."

    scene cyberspace_tunnel
    with dissolve

    quins "Контракт на личность выглядит как кнопка."
    quins "Но цена — всегда память."

    menu:
        "Что отдать двери?"

        "Тёплое воспоминание":
            $ quins_score += 1
            quins "Дорого. Значит честно."

        "Страшное воспоминание":
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
            $ quins_score += 1
            quins "Хорошо."
            zombi "Ладно. Пока."

        "Спросить про апдейт":
            zombi "Я упрощаю тебя."
            quins "Мы уходим."

        "Согласиться на пробник":
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
            quins "Тогда шанс есть."

        "Я хочу уйти, потому что тут скучно":
            quins "Тогда ты просто меняешь декорации."

        "Я хочу остаться, но чтобы ты была рядом":
            quins "Я не якорь."
            quins "Я — проводник."

    scene cyberspace_church
    with fade

    # открытие концовки Quins: только если 3/3 правильных выбора
    if quins_score == 3:
        $ quins_done = True
        quins "Я запомнила твою траекторию."
        quins "В ядре у тебя будет вариант — без упрощения."
        hamayumi "Это открывает выход."
    else:
        $ quins_done = False
        quins "Ты ещё не готов."
        quins "Или платишь не тем, что нужно."

    hide quins
    with dissolve

    call ambient_reset
    jump act2_after_quins
