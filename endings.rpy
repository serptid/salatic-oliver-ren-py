# ------------------------------------------------------------
# endings.rpy
# Финалы - ТОЛЬКО отображение результата
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
# QUINS - выход
# ------------------------------------------------------------
label end_quins:

    play music "audio/music/best_End.mp3" fadein 2.0 loop volume 0.008

    scene bg cyberspace_city
    with fade

    quins "Пора домой."

    oliver "Я выбираю... тебя."

    scene bg hospital_room
    with dissolve

    "Монитор работает."
    "Без искажений."
    "Без подтекста."

    oliver "Камера не мигает."
    oliver "Тишина настоящая."

    quins "Ты справишься."
    quins "Теперь без навигатора."
    quins "Матвея больше нет"
    quins "Теперь я за него..."
    quins "Любовь моя"

    scene black
    with fade

    "Мир снова требует усилий."
    "Но он больше не маскируется под систему."

    "Концовка: Моя любовь с Quins."

    return


# ------------------------------------------------------------
# NIGHSTESS - принятие
# ------------------------------------------------------------
label end_nighstess:

    play music "audio/music/nightass_End.mp3" fadein 2.0 loop volume 0.008

    scene bg cyberspace_tunnel
    with fade

    nighstess "Добро пожаловать не в тюрьму."
    nighstess "А в устойчивую форму."
    voice "audio/Hamayumi/final/1.mp3"
    hamayumi "Ты понимаешь цену?"

    oliver "Понимаю."
    oliver "И больше не называю это временным."
    oliver "Теперь киберспейс это моя жизнь"


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
# SAND - пауза
# ------------------------------------------------------------
label end_sand:

    play music "audio/music/sand_End.mp3" fadein 2.0 loop volume 0.008

    scene bg cyberspace_core
    with fade

    sand "Ты не выиграл."
    sand "И не проиграл."
    voice "audio/Hamayumi/final/2.mp3"
    hamayumi "Тогда просто... будь."
    oliver "Я теперь просто писко..."
    oliver "Буду копать..."
    

    scene bg cyberspace_core_ui
    with dissolve

    "Мир не ускоряется."
    "И не ждёт."

    "Впервые ничто не требует продолжения."

    "Концовка: Мир из песка."

    return


# ------------------------------------------------------------
# HOSPITAL - нормализация
# ------------------------------------------------------------
label end_hospital:

    play music "audio/music/durka_End.mp3" fadein 2.0 loop volume 0.008

    scene bg hospital_room
    with fade

    oliver "Белый свет."
    oliver "Стабильность."

    nurse "Вы больше не говорите о киберспейсе."

    oliver "Потому что он больше не нужен."
    oliver "Теперь я буду играть в геншин!"

    "Мысли упрощаются."
    "Связи теряют символы."
    "Остаётся функция."

    scene black
    with fade

    "Концовка: Палата. без киберспейса"

    return


# ------------------------------------------------------------
# VIRUS - отказ от выбора / пролом 4 стены
# ------------------------------------------------------------
label end_virus:

    play music "audio/music/zombi_End.mp3" fadein 2.0 loop volume 0.008

    scene bg virus
    with fade
    show zombi at right
    "..."
    "..."

    
    zombi "Установка завершена."
    zombi "Ты нажала не на тот exeшник"
    zombi "Я ставлю троян на твой пк"
    zombi "Ты совсем рамки перепутала"
    zombi "Прошла мою игру но не запала не на одного мальчика"
    zombi "Выбрала не те ответы в диалогах?"
    zombi "Получай концовку которую заслужила"
    zombi "Перепроходи теперь всё"
    zombi "Только сначала купи себе новый компьютер"
    zombi "Этот теперь мой..."
    zombi "АХАХАХАХ"
    zombi "ЭЭЭЭ"
    zombi "Линукс линукс!!!"

    "WINDOWS: DISABLED"
    "LINUX: ENABLED"
    voice "audio/Hamayumi/final/3.mp3"
    hamayumi "Ты больше не выбираешь."
    zombi "Спасибо за помощь матвей"
    oliver "Нет.."
    oliver "Как ты смеешь?"

    voice "audio/Hamayumi/final/4.mp3"
    hamayumi "Это был не финал."
    voice "audio/Hamayumi/final/5.mp3"
    hamayumi "Это был выход из интерфейса."

    "ERROR: CONTEXT LOST"
    "ERROR: SUBJECT NOT RESPONDING"
    "CONTROL TRANSFERRED TO HOST"

    zombi "Нейросети теперь сделайют всё за меня"
    zombi "Салатик Оливер более не требуется."
    zombi "Процесс стабилен."
    zombi "Продолжение - вне среды."
    hide zombi

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

    scene bg desktop_fake
    with dissolve

    "На рабочем столе появляется файл."
    "SalaticOliver.exe"
    "Издатель: неизвестен"
    "Защитник виндовс в шоке"
    "Пк не отвечает"

    zombi "Интеграция завершена."
    zombi "Кароче"
    zombi "Матвей"
    zombi "идём посмотрим что у неё в папке - мопсы.folder "
    zombi "ООООО"
    zombi "как так..."
    zombi "Блять.. фу..."
    zombi "ужас.."
    zombi "Матвей?"
    zombi "как мне теперь это развидеть 0_0"
    zombi "ТУТ НЕ МОПСЫ... ТУТ! □□□□□"


    voice "audio/Hamayumi/final/8.mp3"
    hamayumi "Ты просил, чтобы за тебя решили."
    voice "audio/Hamayumi/final/9.mp3"
    hamayumi "Теперь ты - среда."

    scene black
    with fade

    "Игра не закрывается."
    "Она просто больше не реагирует на тебя"

    "Ты никогда не сможешь узнать что такое Киберспейс"
    "Серёжа установил тебе ubuntu lts 24.04"
    "Посколько номер фиксиков уже давно был утерян"
    "ты не знаешь как тебе установить windows"
    "Ведь всё что ты знаешь о командной строке линукс"
    "Это то что это опасность"
    "..."
    "Ты никогда не узнаешь что такое Киберспейс на самом деле"
    "Благодоря серёге ты узнала что все твои путешествия по дурке"
    "Майнкрафту"
    "Киберспейсу"
    "Это меньшая из проблем"
    "Киберспейс это - пиздец"
    "Спасибо Серёга"
    "Концовка: Вирус."
    "winint"

    return


