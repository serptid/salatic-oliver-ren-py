# scenes_core.rpy
# Акт IV — CORE NODE (точка невозврата) + переход в финалы

label core_entry:

    scene cyberspace_void
    with fade

    play music "audio/core_node.ogg" fadein 2.0

    hamayumi "Дальше — ядро."
    hamayumi "Здесь не торгуются."

    if virus_active:
        play sound "audio/glitch_short.ogg"
        hamayumi "И да."
        hamayumi "Он уже рядом."

    scene cyberspace_core
    with dissolve

    show artemka at center
    with dissolve

    artemka "Переменная обнаружена."
    artemka "Салатик Оливер."
    artemka "Статус: нестабильный."

    oliver "Ты MR_artemka."

    artemka "Я администратор."
    artemka "Я закрываю неопределённость."

    oliver "Значит, выбора нет."

    artemka "Неверно."
    artemka "Выбор есть всегда."
    artemka "Но не всегда он оформлен."

    hamayumi "Он даст интерфейс."
    hamayumi "Но доступные варианты зависят от того, что ты сделал."

    if virus_active:
        artemka "Обнаружено постороннее вмешательство."
        artemka "Приоритет: безопасность."
        artemka "Завершение будет выполнено автоматически."

        hide artemka
        with dissolve

        stop music fadeout 1.0
        jump endings_entry

    # Системный экран: выбор состояния (не концовки)
    scene cyberspace_core_ui
    with dissolve

    artemka "Выбери финальное состояние."
    artemka "Не конец."
    artemka "Форму."

    # Если доступен хотя бы один "осознанный" путь — даём выбрать форму.
    # Если ничего не оформлено — одна кнопка (default).
    if quins_done or nighstess_done or sand_done or hospital_done:

        menu:
            "SELECT FINAL STATE"

            "Стабилизация: выход из киберспейса" if quins_done:
                $ final_state = "quins"
                artemka "Принято."
                jump core_finalize

            "Стабилизация: непрерывное существование" if nighstess_done:
                $ final_state = "nighstess"
                artemka "Принято."
                jump core_finalize

            "Стабилизация: пауза без выбора" if sand_done:
                $ final_state = "sand"
                artemka "Принято."
                jump core_finalize

            "Стабилизация: нормализация реальности" if hospital_done:
                $ final_state = "hospital"
                artemka "Принято."
                jump core_finalize

    else:

        artemka "У тебя нет оформленного ответа."
        artemka "Система применит значение по умолчанию."

        $ final_state = "default"
        jump core_finalize


label core_finalize:

    scene cyberspace_core
    with dissolve

    artemka "Фиксация состояния."

    if final_state == "quins":
        artemka "Параметр: выход."
    elif final_state == "nighstess":
        artemka "Параметр: принятие."
    elif final_state == "sand":
        artemka "Параметр: пауза."
    elif final_state == "hospital":
        artemka "Параметр: отрицание."
    else:
        artemka "Параметр: default."

    hamayumi "Идём."

    hide artemka
    with dissolve

    stop music fadeout 1.5

    # Переход в файл endings.rpy (там окончательная развязка)
    jump endings_entry
