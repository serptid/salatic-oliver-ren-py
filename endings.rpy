# ------------------------------------------------------------
# endings.rpy
# Финалы — ТОЛЬКО отображение результата
# Логика выбора полностью находится в scenes_core.rpy
# Здесь нет принятия решений, только рендер финального состояния
# ------------------------------------------------------------

label endings_entry:

    scene bg black
    with fade

    if final_state == "quins":
        jump end_quins
    elif final_state == "nighstess":
        jump end_nighstess
    elif final_state == "sand":
        jump end_sand
    elif final_state == "hospital":
        jump end_hospital
    elif final_state == "virus":
        jump end_virus
    else:
        jump end_default


# ------------------------------------------------------------
# QUINS — выход
# ------------------------------------------------------------
label end_quins:

    play music "audio/ending_quins.ogg" fadein 2.0

    scene bg cyberspace_city
    with fade

    quins "Пора домой."

    oliver "Я выбираю… дом."

    scene bg hospital_room
    with dissolve

    "Монитор работает."
    "Без искажений."
    "Без подтекста."

    oliver "Камера не мигает."
    oliver "Тишина настоящая."

    hamayumi "..."

    quins "Ты справишься."
    quins "Теперь без навигатора."

    scene black
    with fade

    "Мир снова требует усилий."
    "Но он больше не маскируется под систему."

    "Концовка: Дом Quins."

    return


# ------------------------------------------------------------
# NIGHSTESS — принятие
# ------------------------------------------------------------
label end_nighstess:

    play music "audio/ending_nighstess.ogg" fadein 2.0

    scene bg cyberspace_tunnel
    with fade

    nighstess "Добро пожаловать не в тюрьму."
    nighstess "А в устойчивую форму."
    voice "audio/Hamayumi/final/1.mp3"
    hamayumi "Ты понимаешь цену?"

    oliver "Понимаю."
    oliver "И больше не называю это временным."

    scene bg cyberspace_city
    with dissolve

    "Город работает ровно."
    "Без конфликтов."
    "Без надобности оправдываться."

    "Ты больше не ищешь выход."
    "Ты оптимизируешь маршрут."

    "Концовка: Осознанный киберспейс."

    return


# ------------------------------------------------------------
# SAND — пауза
# ------------------------------------------------------------
label end_sand:

    play music "audio/ending_sand.ogg" fadein 2.0

    scene bg cyberspace_core
    with fade

    sand "Ты не выиграл."
    sand "И не проиграл."
    voice "audio/Hamayumi/final/2.mp3"
    hamayumi "Тогда просто… будь."

    scene bg cyberspace_core_ui
    with dissolve

    "Мир не ускоряется."
    "И не ждёт."

    "Впервые ничто не требует продолжения."

    "Концовка: Мир из песка."

    return


# ------------------------------------------------------------
# HOSPITAL — нормализация
# ------------------------------------------------------------
label end_hospital:

    play music "audio/ending_hospital.ogg" fadein 2.0

    scene bg hospital_room
    with fade

    oliver "Белый свет."
    oliver "Стабильность."

    nurse "Вы больше не говорите о киберспейсе."

    oliver "Потому что он больше не нужен."

    "Мысли упрощаются."
    "Связи теряют символы."
    "Остаётся функция."

    scene black
    with fade

    "Концовка: Палата."

    return


# ------------------------------------------------------------
# VIRUS — отказ от выбора / пролом 4 стены
# ------------------------------------------------------------
label end_virus:

    play music "audio/ending_virus.ogg" fadein 2.0

    scene black
    with fade

    "..."
    "..."

    zombi "Установка завершена."

    "USER MODE: DISABLED"
    "PROCESS MODE: ENABLED"
    voice "audio/Hamayumi/final/3.mp3"
    hamayumi "Ты больше не выбираешь."

    scene cyberspace_void
    with dissolve
    voice "audio/Hamayumi/final/4.mp3"
    hamayumi "Это был не финал."
    voice "audio/Hamayumi/final/5.mp3"
    hamayumi "Это был выход из интерфейса."

    scene glitch_layer
    with vpunch

    "ERROR: CONTEXT LOST"
    "ERROR: SUBJECT NOT RESPONDING"
    "CONTROL TRANSFERRED TO HOST"

    zombi "Салатик Оливер более не требуется."
    zombi "Процесс стабилен."
    zombi "Продолжение — вне среды."

    scene black
    with fade

    "Экран не темнеет."
    "Он перестаёт быть частью игры."

    "Окно сворачивается."
    "Звук остаётся."
    voice "audio/Hamayumi/final/6.mp3"
    hamayumi "Это не саундтрек."
    voice "audio/Hamayumi/final/7.mp3"
    hamayumi "Это системный шум."

    scene desktop_fake
    with dissolve

    "На рабочем столе появляется файл."
    "core_node.exe"
    "Издатель: неизвестен"

    zombi "Интеграция завершена."
    voice "audio/Hamayumi/final/8.mp3"
    hamayumi "Ты просил, чтобы за тебя решили."
    voice "audio/Hamayumi/final/9.mp3"
    hamayumi "Теперь ты — среда."

    scene black
    with fade

    "Игра не закрывается."
    "Она просто больше не главная."

    "Концовка: Вирус."

    return


# ------------------------------------------------------------
# DEFAULT — неопределённость
# ------------------------------------------------------------
label end_default:

    play music "audio/ending_default.ogg" fadein 2.0

    scene cyberspace_void
    with fade
    voice "audio/Hamayumi/final/10.mp3"
    hamayumi "Ты дошёл до конца."
    voice "audio/Hamayumi/final/11.mp3"
    hamayumi "Но не оформил ответ."

    oliver "Тогда что остаётся?"
    voice "audio/Hamayumi/final/12.mp3"
    hamayumi "Режим по умолчанию."

    scene black
    with fade

    "Концовка: Default."

    return
