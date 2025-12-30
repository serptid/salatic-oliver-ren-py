# scenes_act3.rpy
# Акт III — Конфликт (линейный, без вируса, без started-флагов)

label act3_entry:

    scene cyberspace_city
    with fade

    play music "audio/act3_conflict.ogg" fadein 2.0

    oliver "Город дрожит."
    oliver "Как будто ему больно."

    hamayumi "Ты прошёл через чужие ответы."
    hamayumi "Теперь они требуют формы."

    scene cyberspace_city
    with vpunch

    oliver "Что происходит?"

    hamayumi "Схождение."
    hamayumi "Не людей."
    hamayumi "Аргументов."

    scene cyberspace_pause
    with dissolve

    # Если открыта хотя бы одна человеческая концовка — показываем соответствующие “аргументы”
    if quins_done:
        show quins at center
        with dissolve

        quins "Выход не любит украшений."
        quins "Он любит решение."

        oliver "Я сделал выбор?"

        quins "Ты сделал цену."
        quins "Теперь сделай шаг."

        hide quins
        with dissolve

    if nighstess_done:
        show nighstess at center
        with dissolve

        nighstess "Ты ищешь дверь."
        nighstess "А я предлагаю — жить внутри."

        oliver "Это не бегство?"

        nighstess "Это форма."
        nighstess "Форма честнее слова 'побег'."

        hide nighstess
        with dissolve

    if sand_done:
        show sand at center
        with dissolve

        sand "Система шумит, потому что ты требуешь конца."
        sand "А иногда конец — это пауза."

        oliver "Пауза — это ничего?"

        sand "Пауза — это выдержать."
        sand "И не попросить упрощения."

        hide sand
        with dissolve

    if hospital_done:
        scene hospital_room
        with dissolve

        play sound "audio/hospital_bleep.ogg"

        oliver "Палата…"

        hamayumi "Не возврат."
        hamayumi "Давление словом 'нормально'."

        scene cyberspace_pause
        with dissolve

    # Если не открыта ни одна концовка — атмосфера “пустого ответа”
    if not (quins_done or nighstess_done or sand_done or hospital_done):
        hamayumi "Тишина без формы."
        hamayumi "Ты дошёл, но не оформил ответ."

    scene cyberspace_city
    with fade

    hamayumi "Дальше — ядро."
    hamayumi "CORE NODE."
    hamayumi "Там ты выберешь финальное состояние."

    if quins_done:
        hamayumi "Quins оставила тебе вариант выхода."
    if nighstess_done:
        hamayumi "Nighstess оставил тебе вариант принятия."
    if sand_done:
        hamayumi "Песок оставил тебе вариант паузы."
    if hospital_done:
        hamayumi "Больница оставила тебе вариант нормализации."

    stop music fadeout 2.0

    jump core_entry
