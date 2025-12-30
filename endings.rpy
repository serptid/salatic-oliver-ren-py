label finale_gate:
    if f_virus:
        jump end_virus

    menu:
        "Финал: Выход (Quins)" if f_quins:
            jump end_quins
        "Финал: Принятие (Nighstess)" if f_nighstess:
            jump end_nighstess
        "Финал: Нейтральный (Песок)" if f_sand or avoid_count >= 2:
            jump end_sand
        "Финал: Плохой (Больница)" if f_hospital:
            jump end_hospital
        "...":
            jump end_default

label end_virus:
    "END: VIRUS"
    return
