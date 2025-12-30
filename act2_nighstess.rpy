
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
    jump act2_after_nighstess



