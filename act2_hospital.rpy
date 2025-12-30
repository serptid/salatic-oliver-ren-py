
# -------------------------
# Ветка Больницы (5 экранов) — "перепрошивка интерпретации"
# -------------------------

label branch_hospital:

    if not hospital_started:
        $ hospital_started = True

        scene hospital_room
        with fade

        play music "audio/ambient_hospital.ogg" fadein 1.5

        oliver "Белый свет."
        oliver "Слишком реальный."

        hamayumi "Это пробой."
        hamayumi "Если ты примешь его — киберспейс отступит."

    else:
        scene hospital_room
        with dissolve

    # Безопасная формулировка: не про самоповреждение, а про "остановить власть симптома"
    oliver "Если это всё симптом…"
    oliver "Тогда я могу остановить это."

    scene hospital_office
    with dissolve

    show doctor at center
    with dissolve

    doctor "Салатик Оливер."
    doctor "Расскажите, что вы видите."

    if patch_mark:
        doctor "И не спешите упрощать ответ."
        doctor "Я слышу в ваших словах знакомый сценарий."

    menu:
        "Ответ врачу"

        "Это фантазии. Просто шум.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ hospital_trace += 1
            doctor "Хорошо."
            doctor "Мы назовём это и перестанем подпитывать."
            $ identity_integrity -= 1

        "Я видел Quins.":
            $ avoid_counter += 1
            $ hospital_trace += 1
            doctor "Мы разберём это позже."
            $ trust_hamayumi -= 1

        "Я видел город.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ hospital_trace += 1
            doctor "Это реакция на стресс."
            $ identity_integrity -= 1

        "Я не уверен. Но это влияет на выбор.":
            $ hospital_keys += 1
            $ identity_integrity += 1
            $ hospital_trace += 1
            doctor "Это честный ответ."

    hide doctor
    with dissolve

    scene hospital_room
    with dissolve

    if trust_hamayumi <= -2:
        hamayumi "..."
        hamayumi "Ты называешь меня — и я становлюсь меньше."
    else:
        hamayumi "Ты стираешь меня словами."

    menu:
        "Что делать?"

        "Позвать врача и закрыть это":
            $ hospital_keys += 1
            $ reality_pull += 2
            $ trust_hamayumi -= 1
            $ identity_integrity -= 1
            hamayumi "..."

        "Остановиться и поверить Хамаюми":
            $ avoid_counter += 1
            $ trust_hamayumi += 1
            $ identity_integrity += 1
            hamayumi "Тогда ты ещё держишься."

        "Промолчать":
            $ hospital_keys += 1
            $ virus_debt += 1
            $ identity_integrity -= 1
            hamayumi "Понял."

    scene hospital_room
    with dissolve

    show nurse at center
    with dissolve

    nurse "Сегодня спокойно."
    if sand_trace >= 1:
        nurse "Вы стали слишком тихим."
    nurse "Вы меньше говорите о киберспейсе."

    menu:
        "Ответ"

        "Потому что его нет.":
            $ hospital_keys += 1
            $ reality_pull += 1
            $ identity_integrity -= 1

        "Потому что я устал.":
            $ avoid_counter += 1
            $ identity_integrity += 1

        "Потому что я боюсь ошибиться.":
            $ avoid_counter += 1
            $ identity_integrity += 1

    hide nurse
    with dissolve

    scene hospital_room
    with fade

    if hospital_keys >= 3:
        $ hospital_done = True
        $ core_access_level += 1
        $ reality_pull += 2
        $ hospital_trace += 1
        oliver "Если я перестану давать этому власть — оно ослабнет."
        hamayumi "Тогда в ядре у тебя останется только реальность."
        # Цена: реальность может "съесть" внутренний голос
        $ trust_hamayumi -= 1
    else:
        $ avoid_counter += 1
        hamayumi "Ты сомневаешься."
        hamayumi "Значит, связь ещё держится."
        $ identity_integrity += 1

    call ambient_reset
    jump act2_transition
