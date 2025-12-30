# ------------------------------------------------------------
# branch_nighstess.rpy
# Ветка Nighstess (расширенная) — "инженерия принятия"
# Открывает концовку Nighstess только при 3/3 правильных выборах
# ------------------------------------------------------------

label branch_nighstess:

    $ nighstess_score = 0

    # -------------------------
    # Экран 1 — вход
    # -------------------------
    scene bg cyberspace_street
    with fade

    play music "audio/nighstess_theme.ogg" fadein 1.5

    show nighstess at center
    with dissolve
    oliver "О"
    nighstess "Ты всё ещё ищешь выход?"
    nighstess "Здесь никто не держит силой."
    oliver "Найтес!"
    oliver "Братанчик"
    oliver "Зайка)"
    show hamayumi at left
    show nighstess at right
    hamayumi "Он опасен спокойствием."
    hamayumi "С ним не спорят — к нему привыкают."
    oliver "Он чё"
    oliver "Афтаритет тут какойто"
    oliver "Да он реальный Филон"

    menu:
        "Тезис"
        "Это иллюзия.":
            nighstess "И всё же ты здесь."
            oliver "Ну а где?"
            hamayumi "Иллюзии тоже требуют участия."
            hamayumi "Ты платишь вниманием."

        "Тут не хочеться существовать.. это не реальность.":
            hide hamayumi
            nighstess "Я хочу, чтобы ты не притворялся."
            nighstess "Остаться — это слово."
            nighstess "Принять — это действие."
        "А если реальный мир хуже?":
            hide hamayumi
            $ nighstess_score += 1
            nighstess "Вот честный вопрос."
            nighstess "Не о свободе. О сравнении боли."
            oliver "Вот бы тут остаться с тобой..."
            oliver "Навсегда!"


    # -------------------------
    # Экран 2 — пауза/разметка понятий
    # -------------------------
    scene bg cyberspace_pause
    with dissolve
    show nighstess at center
    nighstess "В реальности ты диагноз."
    nighstess "Здесь ты процесс, который может думать."
    oliver "Да Задалбал меня "
    oliver "Кто такое КИБЕРСПЕЙС"
    oliver "Я не понимаю"
    oliver "Без понятия"
    oliver "типа"
    hide nighstess
    show hamayumi at left
    show nighstess at right
    hamayumi "Он подменяет ярлыки функцией."
    hamayumi "Так легче согласиться."

    menu:
        "Ответ"

        "А если бегство — форма выживания?":
            $ nighstess_score += 1
            oliver "Типо неважно где и как быть и существовать"
            oliver "Жизнь она такая филосовская"
            nighstess "Тогда ты понимаешь."
            nighstess "Выживание — не позор."
            nighstess "Позор — делать вид, что это не выбор."

        "Ты оправдываешь бегство.":
            oliver "Нет во всем этом смысла"
            nighstess "Я называю вещи своими именами."
            hamayumi "Имя — это ещё не смысл."
            hamayumi "Смысл — в том, что ты сделаешь дальше."

        "Я ищу Quins.":
            oliver "Верни мне моего фембойчика"
            nighstess "Тогда ты ищешь обещание."
            nighstess "И хочешь, чтобы оно было простым."
            nighstess "Но простое обещание — всегда ловушка."

    # -------------------------
    # Экран 7 — возвращение на крышу: решение (3-й балл)
    # -------------------------
    scene bg cyberspace_street
    with dissolve
    show nighstess at right
    nighstess "Я не переписываю тебя."
    nighstess "Я предлагаю жить здесь осознанно."
    oliver "Да я уже понила что ты сумашедший"
    oliver "Получаетсья будем вместе тусить"
    

    menu:
        "Решение"

        "Я не готов решать.":
            nighstess "Тогда решат за тебя."
            hamayumi "И ты назовёшь это спокойствием."
            hamayumi "Потому что так проще выдержать стыд."

        "Отдай мне автопилот.":
            nighstess "Можно."
            nighstess "Но автопилот любит, когда ты исчезаешь из решения."
            hamayumi "И тогда остаётся только маршрут."
            hamayumi "Без твоего имени."

        "Я хочу остаться и принять это.":
            $ nighstess_score += 1
            nighstess "Тогда у тебя будет режим в ядре."
            nighstess "Не клетка."
            nighstess "Интерфейс ответственности."

    # -------------------------
    # Экран 8 — итог и флаг
    # -------------------------
    scene bg cyberspace_precore
    with fade

    if nighstess_score == 3:
        $ nighstess_done = True
        nighstess "Я отметил твой вектор."
        nighstess "В ядре тебе дадут режим."
        nighstess "Ты не получишь счастье."
        nighstess "Ты получишь честность без боли-шума."
        oliver "Я всё ещё не понимаю"
        oliver "Мы типо соседи по полате"
        oliver "Что с вами всеми сделал киберспек"
        hamayumi "Это откроет её концовку."
        hamayumi "Но помни: режим — это инструмент."
        hamayumi "Инструменты любят становиться привычкой."
    else:
        $ nighstess_done = False
        nighstess "Ты ещё не выбрал."
        nighstess "Ты коллекционируешь слова."
        oliver "Прости найтес но ты мне просто друг"
        hamayumi "Слова без решения — просто шум."
        hamayumi "А шум — идеальная маскировка страха."

    hide nighstess
    with dissolve

    call ambient_reset
    jump act2_after_nighstess
