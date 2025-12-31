# ------------------------------------------------------------
# branch_nighstess.rpy
# Ветка Nighstess (расширенная) - "инженерия принятия"
# Открывает концовку Nighstess только при 3/3 правильных выборах
# ------------------------------------------------------------

label branch_nighstess:

    $ nighstess_score = 0

    # -------------------------
    # Экран 1 - вход
    # -------------------------
    scene bg cyberspace_street
    with fade

    play music "audio/music/nightass.mp3" fadein 2.0 loop volume 0.008

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

    voice "audio/Hamayumi/nightass/1.mp3"
    hamayumi "Он опасен спокойствием."
    voice "audio/Hamayumi/nightass/2.mp3"
    hamayumi "С ним не спорят - к нему привыкают."

    oliver "Он чё"
    oliver "Афтаритет тут какойто"
    oliver "Да он реальный Филон"

    menu:
        "Тезис"

        "Это иллюзия.":
            nighstess "И всё же ты здесь."
            oliver "Ну а где?"
            voice "audio/Hamayumi/nightass/3.mp3"
            hamayumi "Иллюзии тоже требуют участия."
            voice "audio/Hamayumi/nightass/4.mp3"
            hamayumi "Ты платишь вниманием."

        "Тут не хочеться существовать.. это не реальность.":
            hide hamayumi
            nighstess "Я хочу, чтобы ты не притворялся."
            nighstess "Остаться - это слово."
            nighstess "Принять - это действие."

        "А если реальный мир хуже?":
            hide hamayumi
            $ nighstess_score += 1
            nighstess "Вот честный вопрос."
            nighstess "Не о свободе. О сравнении боли."
            oliver "Вот бы тут остаться с тобой..."
            oliver "Навсегда!"

    # -------------------------
    # Экран 2 - пауза/разметка понятий
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

    voice "audio/Hamayumi/nightass/5.mp3"
    hamayumi "Он подменяет ярлыки функцией."
    voice "audio/Hamayumi/nightass/6.mp3"
    hamayumi "Так легче согласиться."

    menu:
        "Ответ"

        "А если бегство - форма выживания?":
            $ nighstess_score += 1
            oliver "Типо неважно где и как быть и существовать"
            oliver "Жизнь она такая филосовская"
            nighstess "Тогда ты понимаешь."
            nighstess "Выживание - не позор."
            nighstess "Позор - делать вид, что это не выбор."

        "Ты оправдываешь бегство.":
            oliver "Нет во всем этом смысла"
            nighstess "Я называю вещи своими именами."
            voice "audio/Hamayumi/nightass/7.mp3"
            hamayumi "Имя - это ещё не смысл."
            voice "audio/Hamayumi/nightass/8.mp3"
            hamayumi "Смысл - в том, что ты сделаешь дальше."

        "Я ищу Quins.":
            oliver "Верни мне моего фембойчика"
            nighstess "Тогда ты ищешь обещание."
            nighstess "И хочешь, чтобы оно было простым."
            nighstess "Но простое обещание - всегда ловушка."

    # -------------------------
    # Экран 7 - возвращение на крышу
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
            voice "audio/Hamayumi/nightass/9.mp3"
            hamayumi "Он всегда добовляет эту строчку."
            voice "audio/Hamayumi/nightass/10.mp3"
            hamayumi "Как подпись под контрактом."

        "Отдай мне автопилот.":
            nighstess "Можно."
            nighstess "Но автопилот любит, когда ты исчезаешь из решения."
            voice "audio/Hamayumi/nightass/11.mp3"
            hamayumi "Меняют форму… и называют это зрелостью."
            voice "audio/Hamayumi/nightass/12.mp3"
            hamayumi "И данные обычно используют против тебя."

        "Я хочу остаться и принять это.":
            $ nighstess_score += 1
            nighstess "Тогда у тебя будет режим в ядре."
            nighstess "Не клетка."
            nighstess "Интерфейс ответственности."

    # -------------------------
    # Экран 8 - итог и флаг
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

        voice "audio/Hamayumi/nightass/13.mp3"
        hamayumi "Он поднимает ставку."
        voice "audio/Hamayumi/nightass/14.mp3"
        hamayumi "Не угрозой. Контекстом."
        voice "audio/Hamayumi/nightass/15.mp3"
        hamayumi "И он сейчас попробует купить у тебя это право."
    else:
        $ nighstess_done = False
        nighstess "Ты ещё не выбрал."
        nighstess "Ты коллекционируешь слова."
        oliver "Прости найтес но ты мне просто друг"
        voice "audio/Hamayumi/nightass/33.mp3"
        hamayumi "Слова без решения — просто шум.."
        voice "audio/Hamayumi/nightass/34.mp3"
        hamayumi "А шум — идеальная маскировка страха."

    hide nighstess
    with dissolve

    call ambient_reset
    jump act2_after_nighstess
