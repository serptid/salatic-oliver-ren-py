# -------------------------
# Ветка Больницы (5 экранов) — "перепрошивка интерпретации"
# Открывает концовку Hospital только при 3/3 правильных выборах
# -------------------------

label branch_hospital:

    # локальный счётчик правильных выборов
    $ hospital_score = 0

    scene hospital_room
    with fade

    play music "audio/ambient_hospital.ogg" fadein 1.5

    oliver "Белый свет."
    oliver "Слишком реальный."

    hamayumi "Это пробой."
    hamayumi "Если ты примешь его — киберспейс отступит."

    oliver "Если это всё симптом…"
    oliver "Тогда я могу остановить это."

    # --- Кабинет врача ---
    scene hospital_office
    with dissolve

    show doctor at center
    with dissolve

    doctor "Салатик Оливер."
    doctor "Расскажите, что вы видите."

    menu:
        "Ответ врачу"

        "Это фантазии. Просто шум.":
            doctor "Хорошо."
            doctor "Мы назовём это и перестанем подпитывать."
            hamayumi "Иногда название — это клетка."

        "Я видел Quins.":
            doctor "Мы разберём это позже."
            hamayumi "Ты спрятал смысл в имени."

        "Я видел город.":
            doctor "Это реакция на стресс."
            hamayumi "И всё же город реагирует на тебя."

        "Я не уверен. Но это влияет на выбор.":
            $ hospital_score += 1
            doctor "Это честный ответ."
            hamayumi "Честность держит тебя целым."

    hide doctor
    with dissolve

    # --- Палата ---
    scene hospital_room
    with dissolve

    hamayumi "Ты стираешь меня словами."
    hamayumi "Но пока не до конца."

    menu:
        "Что делать?"

        "Позвать врача и закрыть это":
            hamayumi "..."
            "Тишина становится слишком удобной."

        "Остановиться и поверить Хамаюми":
            $ hospital_score += 1
            hamayumi "Тогда ты ещё держишься."

        "Промолчать":
            hamayumi "Понял."
            "Молчание не выбирает сторону."

    # --- Медсестра ---
    scene hospital_room
    with dissolve

    show nurse at center
    with dissolve

    nurse "Сегодня спокойно."
    nurse "Вы меньше говорите о киберспейсе."

    menu:
        "Ответ"

        "Потому что его нет.":
            nurse "Понимаю."
            hamayumi "Слова могут быть выключателем."

        "Потому что я устал.":
            nurse "Отдых важен."
            hamayumi "Усталость — не ответ."

        "Потому что я боюсь ошибиться.":
            $ hospital_score += 1
            nurse "Это нормально."
            hamayumi "Страх ошибки — признак, что ты ещё выбираешь."

    hide nurse
    with dissolve

    # --- Итог ветки ---
    scene hospital_room
    with fade

    if hospital_score == 3:
        $ hospital_done = True
        oliver "Если я перестану давать этому власть — оно ослабнет."
        hamayumi "Тогда в ядре у тебя останется только реальность."
    else:
        $ hospital_done = False
        hamayumi "Ты сомневаешься."
        hamayumi "Значит, связь ещё держится."
        "Но ответа ты так и не оформил."

    call ambient_reset
    jump act2_transition
