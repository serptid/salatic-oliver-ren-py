# -------------------------
# Камео — просто сцена
# Отсылка: Иван Золо / трек «БАОБАБ»
# -------------------------

label cameo_vanya:

    scene cyberspace_rooftop
    with dissolve

    play music "audio/baobab_echo.ogg" fadein 1.0

    show vanya at center
    with dissolve

    vanya "Я думал, это сон."
    vanya "А оказалось — привычка."
    vanya "Знаешь, как трек, который сначала раздражает."
    vanya "А потом ловишь себя на том, что напеваешь."

    oliver "Ты хочешь выйти?"

    vanya "Я уже вышел."
    vanya "Просто тело забыли забрать."
    vanya "Оно там, по инерции, живёт расписанием."

    oliver "И что ты здесь делаешь?"

    vanya "Слушаю эхо."
    vanya "В одном мире я говорил слишком много."
    vanya "В другом — понял, что слова тоже форма шума."

    vanya "БАОБАБ крутился по кругу."
    vanya "Глупо. Навязчиво."
    vanya "Но идеально, чтобы не думать."

    vanya "Вот и я стал таким треком."
    vanya "Фоном."

    oliver "Тебя это устраивает?"

    vanya "Не знаю."
    vanya "Но привычка — сильнее желания."
    vanya "Это я усвоил раньше всех."

    hide vanya
    with dissolve

    stop music fadeout 1.0

    call ambient_reset
    jump act2_transition
