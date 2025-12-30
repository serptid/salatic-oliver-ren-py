# scenes_act1.rpy
# Акт I — Вход в киберспейс
# Линейный, без выборов

label act1_entry:

    scene black
    with fade

    play music "audio/ambient_hospital.ogg" fadein 2.0

    oliver "..."
    oliver "ГДЕ Я !!!"

    oliver "Белые стены?!"
    oliver "Запах лекарств!!?"

    pause 0.5

    scene bg hospital_room
    with dissolve

    oliver "Это реальность?"
    oliver "Знаете"
    oliver "А ТУТ НЕПЛОХОХО!"
    oliver "ЯБ ДАЖЕ СКАЗАЛ УЮТНО"

    pause 0.5

    show nurse at center
    with dissolve

    nurse "Так.. Так.. Так.."
    nurse "Салатик Оливер."
    nurse "С а л а т и к  О л и в е р."
    nurse "Время приёма препарата."

    hide nurse
    oliver "А если я не хочу?"
    nurse "Вы же знаете, что будет лучше."
    
    with dissolve

    pause 0.5

    play sound "audio/injection.ogg"

    "..."
    "Мир дрогнул."

    stop music fadeout 1.5
    play music "audio/ambient_transition.ogg" fadein 1.5

    scene black
    with fade

    "Мысли стали тяжёлыми."
    "А потом — слишком лёгкими."

    scene bg cyberspace_void
    with fade

    pause 0.5
    show hamayumi at left
    voice "audio/Hamayumi/SteosVoice 102006.mp3"
    hamayumi "Не пугайся."

    oliver "Кто это? Хамаюми?"

    voice "audio/Hamayumi/SteosVoice 399984.mp3"
    hamayumi "Я — Хамаюми."

    oliver "Привет Матвей."

    voice "audio/Hamayumi/SteosVoice 689791.mp3"
    hamayumi "Ты всегда слышал меня."

    voice "audio/Hamayumi/SteosVoice 386062.mp3"
    hamayumi "Просто теперь — чётко."

    oliver "Чего?"
    oliver "У тебя новый микрофон чтоле"
    oliver "Я схожу с ума?"

    voice "audio/Hamayumi/SteosVoice 680731.mp3"
    hamayumi "Нет."
    voice "audio/Hamayumi/SteosVoice 803360.mp3"
    hamayumi "Ты теряешь фильтры."
    
    oliver "?"

    pause 0.5
    voice "audio/Hamayumi/SteosVoice 560869.mp3"
    hamayumi "Реальность — это интерфейс."
    voice "audio/Hamayumi/SteosVoice 451442.mp3"
    hamayumi "А интерфейсы иногда дают сбой."

    oliver "Ааа Я кажеться понялоа"
    oliver "Ты типо хочешь стать стримером и купил себе фулл сет!"
    oliver "Мониторы и микрофон."
    play music "audio/ambient_cyberspace.ogg" fadein 2.0


    voice "audio/Hamayumi/SteosVoice 815244.mp3"
    hamayumi "Верно."
    voice "audio/Hamayumi/SteosVoice 307458.mp3"
    hamayumi "Это киберспейс."

    oliver "Полное погружение~"

    hamayumi "Глубже."
    hamayumi "Здесь обрабатываются не данные."
    hamayumi "Здесь обрабатываются состояния."

    oliver "СТОП"
    oliver "Где Здесь?"
    oliver "Киберспейс?"

    pause 0.5

    scene bg cyberspace_city
    with fade

    oliver "Город..."

    oliver "Неоновый город."
    oliver "OMG"
    oliver "Я точно сошло с ума"

    show hamayumi at left
    hamayumi "Он реагирует на тебя."
    hamayumi "Пока ты здесь — ты существуешь."

    oliver "Я хочу домой"
    oliver "Как отсюда выбраться"
    oliver "ЧТо за УЖас тут творитьсяЯ!"

    hamayumi "Этот вопрос ты задашь позже."

    pause 0.5

    hamayumi "Сейчас — запомни главное."

    hamayumi "Киберспейс не держит силой."
    hamayumi "Он ждёт, что ты сделаешь выбор."

    pause 0.5

    hamayumi "Но не сейчас."

    scene black
    with fade

    stop music fadeout 2.0

    jump act2_entry
