# scenes_core.rpy
# CORE NODE — финальный выбор
# Правка: если игрок НЕ выбирает ни одну концовку (уходит в отмены/петлю),
# ядро через лимит отмен отправляет в virus.
# Если не открыто ничего — тоже virus.

label core_entry:

    $ core_cancel_count = 0

label core_select:

    scene bg cyberspace_void
    with fade

    play music "audio/core_node.ogg" fadein 1.5
    show hamayumi at center
    hamayumi "Дальше — ядро."
    hamayumi "Здесь не торгуются."
    hamayumi "Здесь фиксируют."

    scene bg cyberspace_core
    with dissolve

    show artemka at center
    with dissolve

    artemka "Переменная обнаружена."
    artemka "Салатик Оливер."
    artemka "Статус: нестабильный."

    oliver "Ты MR_artemka."

    artemka "Я администратор."
    artemka "Я закрываю неопределённость."
    artemka "Не лечу."
    artemka "Компилирую."
    hide artemka
    show hamayumi at right
    show artemka at left
    hamayumi "Он даст интерфейс."
    hamayumi "Но доступные варианты зависят от того, что ты оформил."
    hamayumi "В ядре нельзя 'попробовать'."

    scene bg cyberspace_core_ui
    with dissolve

    artemka "SELECT FINAL STATE."
    artemka "Выбор необратим."
    artemka "Подтверждение потребуется."

    # Если нет ни одной открытой человеческой концовки — сразу вирус
    if not (quins_done or nighstess_done or sand_done or hospital_done):
        artemka "Доступных состояний: 0."
        artemka "Назначение: FALLBACK."
        $ final_state = "virus"
        jump endings_entry

    # Если игрок слишком много раз отменяет — ядро закрывает неопределённость вирусом
    if core_cancel_count >= 3:
        artemka "Обнаружена рекурсивная отмена."
        artemka "Неопределённость превышает лимит."
        artemka "Назначение: FALLBACK."
        $ final_state = "virus"
        jump endings_entry

    menu:
        "SELECT FINAL STATE"

        "Стабилизация: выход из киберспейса" if quins_done:
            artemka "Параметры: разрыв связи. Возврат в физический контур."
            hamayumi "Цена: потеря удобной формы."
            hamayumi "И риск, что реальность окажется без сюжета."
            menu:
                "CONFIRM: EXIT?"
                "Подтвердить выход.":
                    $ final_state = "quins"
                    artemka "Принято."
                    jump endings_entry
                "Отмена.":
                    $ core_cancel_count += 1
                    artemka "Отмена принята."
                    jump core_select

        "Стабилизация: непрерывное существование" if nighstess_done:
            artemka "Параметры: закрепление в среде. Режим ядра."
            hamayumi "Цена: ты перестанешь называть это временным."
            hamayumi "Привычка станет законом."
            menu:
                "CONFIRM: CONTINUOUS?"
                "Подтвердить непрерывность.":
                    $ final_state = "nighstess"
                    artemka "Принято."
                    jump endings_entry
                "Отмена.":
                    $ core_cancel_count += 1
                    artemka "Отмена принята."
                    jump core_select

        "Стабилизация: пауза без выбора" if sand_done:
            artemka "Параметры: нейтральный контур. Снижение требований."
            hamayumi "Цена: будущее перестанет стучать."
            hamayumi "И ты можешь полюбить это слишком сильно."
            menu:
                "CONFIRM: PAUSE?"
                "Подтвердить паузу.":
                    $ final_state = "sand"
                    artemka "Принято."
                    jump endings_entry
                "Отмена.":
                    $ core_cancel_count += 1
                    artemka "Отмена принята."
                    jump core_select

        "Стабилизация: нормализация реальности" if hospital_done:
            artemka "Параметры: приоритет физического объяснения. Снижение символов."
            hamayumi "Цена: часть смысла станет 'лишним'."
            hamayumi "И это будет ощущаться как облегчение."
            menu:
                "CONFIRM: NORMALIZE?"
                "Подтвердить нормализацию.":
                    $ final_state = "hospital"
                    artemka "Принято."
                    jump endings_entry
                "Отмена.":
                    $ core_cancel_count += 1
                    artemka "Отмена принята."
                    jump core_select
