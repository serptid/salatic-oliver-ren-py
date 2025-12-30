# scenes_act3.rpy
# Акт III — Конфликт, схождение веток (линейный, но учитывает флаги)

label act3_entry:

    scene cyberspace_city
    with fade

    play music "audio/act3_conflict.ogg" fadein 2.0

    oliver "Город дрожит."
    oliver "Как будто ему больно."

    hamayumi "Ты держал слишком много вариантов в голове."
    hamayumi "Система не любит неопределённость."

    if virus_active:
        play sound "audio/glitch_short.ogg"
        hamayumi "И ещё."
        hamayumi "Что-то чужое уже рядом."

    scene cyberspace_city
    with vpunch

    oliver "Что происходит?"

    hamayumi "Схождение."
    hamayumi "Твои ответы начинают конфликтовать."

    scene cyberspace_pause
    with dissolve

    hamayumi "Сейчас появятся они."
    hamayumi "Не как люди."
    hamayumi "Как аргументы."

    # --- Проявление Quins ---
    if quins_started:
        show quins at center
        with dissolve

        quins "Ты затянул."
        quins "Выход не любит колебаний."

        oliver "Я пытался понять."

        quins "Понимание без решения — это петля."
        quins "Если ты хочешь домой — иди до конца."

        hide quins
        with dissolve

    # --- Проявление Nighstess ---
    if nighstess_started:
        show nighstess at center
        with dissolve

        nighstess "Ты называешь это конфликтом."
        nighstess "Я называю это правдой: ты уже выбираешь."

        oliver "Я не выбирал."

        nighstess "Любая пауза — выбор."
        nighstess "Любая надежда — выбор."

        hide nighstess
        with dissolve

    # --- Проявление Песка ---
    if sand_started:
        show sand at center
        with dissolve

        sand "Система шумит, потому что ты требуешь от неё ответа."
        sand "А ответы не обязаны существовать."

        oliver "И что тогда?"

        sand "Тогда останется только пауза."
        sand "Если ты её выдержишь."

        hide sand
        with dissolve

    # --- Проявление Больницы ---
    if hospital_started:
        scene hospital_room
        with dissolve

        play sound "audio/hospital_bleep.ogg"

        oliver "Палата…"
        oliver "Я снова здесь?"

        hamayumi "Это не возврат."
        hamayumi "Это давление."

        scene cyberspace_pause
        with dissolve

    # --- Вирусная инъекция (если активен) ---
    if virus_active:
        show zombi at center
        with dissolve

        zombi "Слишком много голосов."
        zombi "Хочешь тишину?"

        hamayumi "Не отвечай."

        zombi "Тишина — это контроль."
        zombi "Контроль — это свобода, если ты устал."

        hide zombi
        with dissolve

    # --- Ключевой момент: закрытие хаба ---
    scene cyberspace_city
    with fade

    hamayumi "Хаб больше не доступен."
    hamayumi "Дальше только ядро."

    oliver "Ядро?"

    hamayumi "CORE NODE."
    hamayumi "Там тебя заставят оформить состояние."

    if quins_done:
        hamayumi "Quins оставила тебе шанс на выход."
    if nighstess_done:
        hamayumi "Nighstess оставил тебе шанс на принятие."
    if sand_done:
        hamayumi "Песок оставил тебе шанс на паузу."
    if hospital_done:
        hamayumi "Больница оставила тебе шанс на отрицание."

    if virus_active:
        hamayumi "А вирус оставил тебе шанс на пустоту."
        hamayumi "Он заберёт его первым, если сможет."

    scene cyberspace_void
    with fade

    oliver "А кто решает?"

    hamayumi "Администратор."
    hamayumi "MR_artemka."

    oliver "Он бог?"

    hamayumi "Он — правило."
    hamayumi "А правило не спорит."

    stop music fadeout 2.0

    jump core_entry
