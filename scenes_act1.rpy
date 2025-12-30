# scenes_act1.rpy
# Акт I — Вход в киберспейс
# Линейный, без выборов

label act1_entry:

    scene black
    with fade

    play music "audio/ambient_hospital.ogg" fadein 2.0

    oliver "..."

    oliver "Белые стены."
    oliver "Запах лекарств."
    oliver "Они говорят — это реальность."

    pause 0.5

    oliver "Но если это так — почему она кажется такой хрупкой?"

    scene hospital_room
    with dissolve

    oliver "Я здесь не первый раз."
    oliver "Каждый день одинаковый."
    oliver "Только мысли становятся громче."

    pause 0.5

    show nurse at center
    with dissolve

    nurse "Салатик Оливер."
    nurse "Время приёма препарата."

    oliver "А если я не хочу?"

    nurse "Вы же знаете, что будет лучше."

    hide nurse
    with dissolve

    pause 0.5

    play sound "audio/injection.ogg"

    oliver "..."

    scene hospital_room
    with vpunch

    oliver "Мир дрогнул."

    stop music fadeout 1.5
    play music "audio/ambient_transition.ogg" fadein 1.5

    scene black
    with fade

    oliver "Мысли стали тяжёлыми."
    oliver "А потом — слишком лёгкими."

    pause 0.5

    hamayumi "Не пугайся."

    oliver "Кто это?"

    hamayumi "Я — Хамаюми."
    hamayumi "Ты всегда слышал меня."
    hamayumi "Просто теперь — чётко."

    oliver "Я схожу с ума?"

    hamayumi "Нет."
    hamayumi "Ты теряешь фильтры."

    pause 0.5

    hamayumi "Реальность — это интерфейс."
    hamayumi "А интерфейсы иногда дают сбой."

    scene cyberspace_void
    with dissolve

    play music "audio/ambient_cyberspace.ogg" fadein 2.0

    oliver "Где я?"

    oliver "Это не сон."

    hamayumi "Верно."
    hamayumi "Это киберспейс."

    oliver "Интернет?"

    hamayumi "Глубже."
    hamayumi "Здесь обрабатываются не данные."
    hamayumi "Здесь обрабатываются состояния."

    pause 0.5

    scene cyberspace_city
    with fade

    oliver "Город..."

    oliver "Он живой."

    hamayumi "Он реагирует на тебя."
    hamayumi "Пока ты здесь — ты существуешь."

    oliver "А если я выйду?"

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
