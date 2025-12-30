# scenes_core.rpy
# CORE NODE — выбор финального состояния только из открытых концовок

label core_entry:

    scene cyberspace_void
    with fade

    play music "audio/core_node.ogg" fadein 2.0

    hamayumi "Дальше — ядро."
    hamayumi "Здесь не торгуются."

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

    hamayumi "Он даст интерфейс."
    hamayumi "Но доступные варианты зависят от того, что ты оформил."

    scene cyberspace_core_ui
    with dissolve

    artemka "Выбери финальное состояние."
    artemka "Не конец."
    artemka "Форму."

    # Если нет ни одной открытой человеческой концовки — отправляем в вирус через endings_entry
    if not (quins_done or nighstess_done or sand_done or hospital_done):
        $ final_state = "virus"
        jump endings_entry

    # Иначе показываем только открытые
    menu:
        "SELECT FINAL STATE"

        "Стабилизация: выход из киберспейса" if quins_done:
            $ final_state = "quins"
            artemka "Принято."
            jump endings_entry

        "Стабилизация: непрерывное существование" if nighstess_done:
            $ final_state = "nighstess"
            artemka "Принято."
            jump endings_entry

        "Стабилизация: пауза без выбора" if sand_done:
            $ final_state = "sand"
            artemka "Принято."
            jump endings_entry

        "Стабилизация: нормализация реальности" if hospital_done:
            $ final_state = "hospital"
            artemka "Принято."
            jump endings_entry
