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
    voice "audio/Hamayumi/act_1/1.mp3"
    hamayumi "Не пугайся."

    oliver "Кто это? Хамаюми?"

    voice "audio/Hamayumi/act_1/2.mp3"
    hamayumi "Я — Хамаюми."

    oliver "Привет Матвей."

    voice "audio/Hamayumi/act_1/3.mp3"
    hamayumi "Ты всегда слышал меня."

    voice "audio/Hamayumi/act_1/4.mp3"
    hamayumi "Просто теперь — чётко."

    oliver "Чего?"
    oliver "У тебя новый микрофон чтоле"
    oliver "Я схожу с ума?"

    voice "audio/Hamayumi/act_1/5.mp3"
    hamayumi "Нет."
    voice "audio/Hamayumi/act_1/6.mp3"
    hamayumi "Ты теряешь фильтры."
    
    oliver "?"

    pause 0.5
    voice "audio/Hamayumi/act_1/7.mp3"
    hamayumi "Реальность — это интерфейс."
    voice "audio/Hamayumi/act_1/8.mp3"
    hamayumi "А интерфейсы иногда дают сбой."

    oliver "Ааа Я кажеться понялоа"
    oliver "Ты типо хочешь стать стримером и купил себе фулл сет!"
    oliver "Мониторы и микрофон."
    play music "audio/ambient_cyberspace.ogg" fadein 2.0


    voice "audio/Hamayumi/act_1/9.mp3"
    hamayumi "Верно."
    voice "audio/Hamayumi/act_1/10.mp3"
    hamayumi "Это киберспейс."

    oliver "Полное погружение~"
    voice "audio/Hamayumi/act_1/11.mp3"
    hamayumi "Глубже."
    voice "audio/Hamayumi/act_1/12.mp3"
    hamayumi "Здесь обрабатываются не данные."
    voice "audio/Hamayumi/act_1/13.mp3"
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
    voice "audio/Hamayumi/act_1/14.mp3"
    hamayumi "Он реагирует на тебя."
    voice "audio/Hamayumi/act_1/15.mp3"
    hamayumi "Пока ты здесь — ты существуешь."

    oliver "Я хочу домой"
    oliver "Как отсюда выбраться"
    oliver "ЧТо за УЖас тут творитьсяЯ!"
    voice "audio/Hamayumi/act_1/16.mp3"
    hamayumi "Этот вопрос ты задашь позже."

    pause 0.5
    voice "audio/Hamayumi/act_1/17.mp3"
    hamayumi "Сейчас — запомни главное."
    voice "audio/Hamayumi/act_1/18.mp3"
    hamayumi "Киберспейс не держит силой."
    voice "audio/Hamayumi/act_1/19.mp3"
    hamayumi "Он ждёт, что ты сделаешь выбор."

    pause 0.5
    voice "audio/Hamayumi/act_1/20.mp3"
    hamayumi "Но не сейчас."

    scene black
    with fade

    stop music fadeout 2.0

    jump act2_entry
