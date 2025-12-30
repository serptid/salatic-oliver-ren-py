# -------------------------
# Ветка Nighstess (5 экранов) — "инженерия принятия"
# Открывает концовку Nighstess только при 3/3 правильных выборах
# -------------------------

label branch_nighstess:

    $ nighstess_score = 0

    scene cyberspace_rooftop
    with fade

    play music "audio/nighstess_theme.ogg" fadein 1.5

    show nighstess at center
    with dissolve

    nighstess "Ты всё ещё ищешь выход?"
    nighstess "Здесь никто не держит силой."

    hamayumi "Он опасен спокойствием."

    menu:
        "Nighstess — тезис"

        "А если реальный мир хуже?":
            $ nighstess_score += 1
            nighstess "Вот честный вопрос."

        "Это иллюзия.":
            nighstess "И всё же ты здесь."
            hamayumi "Иллюзии тоже требуют участия."

        "Ты хочешь, чтобы я остался?":
            nighstess "Я хочу, чтобы ты не притворялся."

    scene cyberspace_pause
    with dissolve

    nighstess "В реальности ты диагноз."
    nighstess "Здесь ты процесс, который может думать."

    menu:
        "Ответ"

        "А если бегство — форма выживания?":
            $ nighstess_score += 1
            nighstess "Тогда ты понимаешь."

        "Ты оправдываешь бегство.":
            nighstess "Я называю вещи своими именами."
            hamayumi "Имя — это ещё не смысл."

        "Я ищу Quins.":
            nighstess "Тогда ты ищешь обещание."
            nighstess "И хочешь, чтобы оно было простым."

    scene cyberspace_simroom
    with dissolve

    nighstess "Я показываю варианты."
    nighstess "Не заставляю."

    menu:
        "Оценка Nighstess"

        "Ты адаптировался.":
            nighstess "Наконец."
            nighstess "Адаптация — не сдача."

        "Ты сломался.":
            nighstess "Ломаются те, кто выходит."
            nighstess "Здесь просто меняют форму."

        "Ты боишься выйти снова.":
            nighstess "Страх — не аргумент."
            nighstess "Это данные."

    scene cyberspace_rooftop
    with dissolve

    nighstess "Я не переписываю тебя."
    nighstess "Я предлагаю жить здесь осознанно."

    menu:
        "Решение"

        "Я хочу остаться и принять это.":
            $ nighstess_score += 1
            nighstess "Тогда у тебя будет режим в ядре."

        "Я не готов решать.":
            nighstess "Тогда решат за тебя."
            hamayumi "И ты назовёшь это спокойствием."

        "Отдай мне автопилот.":
            nighstess "Можно."
            nighstess "Но автопилот любит, когда ты исчезаешь из решения."
            hamayumi "И тогда остаётся только маршрут."

    scene cyberspace_city
    with fade

    if nighstess_score == 3:
        $ nighstess_done = True
        nighstess "Я отметил твой вектор."
        nighstess "В ядре тебе дадут режим."
        hamayumi "Это откроет её концовку."
    else:
        $ nighstess_done = False
        nighstess "Ты ещё не выбрал."
        nighstess "Ты коллекционируешь слова."
        hamayumi "Слова без решения — просто шум."

    hide nighstess
    with dissolve

    call ambient_reset
    jump act2_after_nighstess
