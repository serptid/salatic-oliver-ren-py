# scenes_core.rpy
# CORE NODE - финальный выбор
# Правка: если игрок НЕ выбирает ни одну концовку (уходит в отмены/петлю),
# ядро через лимит отмен отправляет в virus.
# Если не открыто ничего - тоже virus.

label core_entry:

    $ core_cancel_count = 0

label core_select:

    scene bg cyberspace_void
    with fade

    play music "audio/music/mrartem.mp3" fadein 2.0 loop volume 0.008

    show hamayumi at center
    hamayumi "Край."
    voice "audio/Hamayumi/scen_core/1.mp3"
    hide hamayumi
    show hamayumi_up at center
    hamayumi "Дальше - ядро."
    voice "audio/Hamayumi/scen_core/2.mp3"
    hide hamayumi_up
    show hamayumi_T at center
    hamayumi "Здесь не торгуются."
    voice "audio/Hamayumi/scen_core/3.mp3"
    hide hamayumi_T
    show hamayumi_forw at center
    hamayumi "Здесь фиксируют."

    scene bg cyberspace_core
    with dissolve

    show artemka at center
    with dissolve

    oliver "Ты MR_artemka."
    oliver "Тёма"
    oliver "Что такое этот ваш киберспек"
    oliver "..."

    artemka "Переменная обнаружена."
    artemka "Салатик Оливер."
    artemka "Статус: нестабильный."

    artemka "Я администратор."
    artemka "Я закрываю неопределённость."
    artemka "Не лечу."
    artemka "Компилирую."

    hide artemka
    show artemka at left

    show hamayumi at right
    voice "audio/Hamayumi/scen_core/4.mp3"
    hamayumi "Он даст интерфейс."

    voice "audio/Hamayumi/scen_core/5.mp3"
    hide hamayumi
    show hamayumi_cry at right
    hamayumi "Но доступные варианты зависят от того, что ты оформил."

    voice "audio/Hamayumi/scen_core/6.mp3"
    hide hamayumi_cry
    show hamayumi_you at right
    hamayumi "В ядре нельзя 'попробовать'."

    scene bg cyberspace_core_ui
    with dissolve

    artemka "SELECT FINAL STATE."
    artemka "Выбор необратим."
    artemka "Подтверждение потребуется."
    oliver "Вы с серёгой чё вообще ебу дали"
    oliver "Хватит мне уже голову марочить"
    oliver "Что такое киберсейс ваш А А"

    # Если нет ни одной открытой человеческой концовки - сразу вирус
    if not (quins_done or nighstess_done or sand_done or hospital_done):
        artemka "Доступных состояний: 0."
        artemka "Назначение: FALLBACK."
        $ final_state = "virus"
        jump endings_entry

    # Если игрок слишком много раз отменяет - ядро закрывает неопределённость вирусом
    if core_cancel_count >= 3:
        artemka "Обнаружена рекурсивная отмена."
        artemka "Неопределённость превышает лимит."
        artemka "Назначение: FALLBACK."
        $ final_state = "virus"
        jump endings_entry

    menu:
        "SELECT FINAL STATE"

        "Стабилизация: выход из киберспейса с любовью" if quins_done:
            artemka "Параметры: разрыв связи. Возврат в физический контур."

            voice "audio/Hamayumi/scen_core/7.mp3"
            hide hamayumi_you
            show hamayumi at right
            hamayumi "Цена: потеря удобной формы."

            voice "audio/Hamayumi/scen_core/8.mp3"
            hide hamayumi
            show hamayumi_up at right
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
                    jump end_virus

        "Стабилизация: непрерывное существование с другом" if nighstess_done:
            artemka "Параметры: закрепление в среде. Режим ядра."

            voice "audio/Hamayumi/scen_core/9.mp3"
            hide hamayumi_up
            show hamayumi_T at right
            hamayumi "Цена: ты перестанешь называть это временным."

            voice "audio/Hamayumi/scen_core/10.mp3"
            hide hamayumi_T
            show hamayumi_forw at right
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
                    jump end_virus

        "Стабилизация: пауза без выбора с мечтой" if sand_done:
            artemka "Параметры: нейтральный контур. Снижение требований."

            voice "audio/Hamayumi/scen_core/11.mp3"
            hide hamayumi_forw
            show hamayumi_you at right
            hamayumi "Цена: будущее перестанет стучать."

            voice "audio/Hamayumi/scen_core/12.mp3"
            hide hamayumi_you
            show hamayumi_cry at right
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
                    jump end_virus

        "Стабилизация: нормализация реальности с самим собой" if hospital_done:

            artemka "Параметры: приоритет физического объяснения. Снижение символов."
            voice "audio/Hamayumi/scen_core/13.mp3"
            hide hamayumi_cry
            show hamayumi_you at right
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
                    jump end_virus
