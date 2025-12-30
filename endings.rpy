# endings.rpy
# Финалы. Игрок не выбирает концовку напрямую.
label endings_entry:

    scene black
    with fade

    # Вирус — только если не открыта ни одна человеческая концовка
    if not (quins_done or nighstess_done or hospital_done or sand_done):
        jump end_virus

    # Переходим только в те финалы, которые реально открыты
    if final_state == "quins" and quins_done:
        jump end_quins
    elif final_state == "nighstess" and nighstess_done:
        jump end_nighstess
    elif final_state == "hospital" and hospital_done:
        jump end_hospital
    elif final_state == "sand" and sand_done:
        jump end_sand
    else:
        jump end_default




label end_quins:

    play music "audio/ending_quins.ogg" fadein 2.0

    scene cyberspace_shaft
    with fade

    quins "Пора домой."
    oliver "Я выбираю… дом."

    scene hospital_room
    with dissolve

    oliver "Камера не мигает."
    oliver "Тишина настоящая."

    hamayumi "..."
    oliver "Ты ушёл?"

    quins "Нет."
    quins "Просто теперь ты справишься без навигатора."

    scene black
    with fade

    "Концовка: Дом Quins."

    return


label end_nighstess:

    play music "audio/ending_nighstess.ogg" fadein 2.0

    scene cyberspace_rooftop
    with fade

    nighstess "Добро пожаловать не в тюрьму."
    nighstess "А в убежище."

    hamayumi "Ты понимаешь цену?"

    oliver "Понимаю."
    oliver "И всё равно остаюсь."

    scene cyberspace_city
    with dissolve

    "Концовка: Осознанный киберспейс."

    return


label end_sand:

    play music "audio/ending_sand.ogg" fadein 2.0

    scene cyberspace_desert
    with fade

    sand "Ты не выиграл."
    sand "И не проиграл."

    hamayumi "Тогда просто… будь."

    scene cyberspace_desert
    with dissolve

    "Концовка: Мир из песка."

    return


label end_hospital:

    play music "audio/ending_hospital.ogg" fadein 2.0

    scene hospital_room
    with fade

    oliver "Белый свет."
    oliver "Стабильность."

    nurse "Вы больше не говорите о киберспейсе."
    oliver "Потому что его нет."

    scene black
    with fade

    "Концовка: Палата."

    return


label end_virus:

    play music "audio/ending_virus.ogg" fadein 2.0

    scene black
    with fade

    zombi "Установка завершена."

    "USER MODE: DISABLED"
    "PROCESS MODE: ENABLED"

    hamayumi "Ты больше не выбираешь."

    scene black
    with fade

    "Концовка: Вирус."

    return


label end_default:

    play music "audio/ending_default.ogg" fadein 2.0

    scene cyberspace_void
    with fade

    hamayumi "Ты дошёл до конца."
    hamayumi "Но не оформил ответ."

    oliver "Тогда что остаётся?"

    hamayumi "То, что система выдаёт по умолчанию."

    scene black
    with fade

    "Концовка: Default."

    return
