
# -------------------------
# Рынок патчей (вирус / контракты)
# -------------------------

label patch_market:

    scene cyberspace_market
    with dissolve

    play music "audio/ambient_market.ogg" fadein 1.0

    $ patch_mark = True

    oliver "Здесь продают… состояния."

    hamayumi "И долги."
    hamayumi "Плати собой — и тебя перепишут."

    show zombi at center
    with dissolve

    zombi "Салатик Оливер."
    zombi "Хочешь апдейт без боли?"

    hamayumi "Нет."

    menu:
        "Рынок патчей — выбор"

        "Спросить, что он делает":
            $ virus_risk += 1
            $ virus_debt += 1
            zombi "Я упрощаю."
            zombi "Убираю лишнее."
            zombi "Сомнения — лишнее."
            hamayumi "Не продолжай."

        "Согласиться на пробник":
            $ virus_risk += 2
            $ virus_debt += 2
            $ virus_voice += 1
            $ identity_integrity -= 1
            $ virus_active = True
            zombi "Установка началась."
            play sound "audio/install_tick.ogg"
            hamayumi "..."

        "Поторговаться: \"дать меньше\"":
            $ virus_debt += 1
            $ identity_integrity -= 1
            zombi "Ты уже понял механику."
            zombi "Меньше боли — меньше тебя."
            hamayumi "Мы уходим."

        "Уйти молча":
            $ avoid_counter += 1
            $ virus_debt += 1
            zombi "Увидимся, когда устанешь быть собой."

    hide zombi
    with dissolve

    call ambient_reset
    jump act2_transition

