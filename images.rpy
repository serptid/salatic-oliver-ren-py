init python:
    SW = config.screen_width
    SH = config.screen_height
#Фоны
image bg hospital_room = Transform("gui/images/bg/hospital.png", xysize=(SW, SH))
image bg cyberspace_city = Transform("gui/images/bg/cyberspace_city.png", xysize=(SW, SH))
image bg cyberspace_void = Transform("gui/images/bg/cyberspace_void.png", xysize=(SW, SH))
image bg hospital_office = Transform("images/hospital_office.png", xysize=(SW, SH))
image bg cyberspace_church = Transform("gui/images/bg/cyberspace_church.png", xysize=(SW, SH))
image bg cyberspace_tunnel = Transform("gui/images/bg/cyberspace_tunnel.png", xysize=(SW, SH))
image bg cyberspace_market = Transform("gui/images/bg/cyberspace_market.png", xysize=(SW, SH))
image bg cyberspace_street = Transform("gui/images/bg/cyberspace_street.png", xysize=(SW, SH))
image bg cyberspace_pause = Transform("gui/images/bg/cyberspace_pause.png", xysize=(SW, SH))
image bg cyberspace_precore = Transform("gui/images/bg/cyberspace_precore.png", xysize=(SW, SH))
image bg cyberspace_edge = Transform("gui/images/bg/cyberspace_edge.png", xysize=(SW, SH))
image bg hospital = Transform("gui/images/bg/hospital.png", xysize=(SW, SH))
image bg cyberspace_core = Transform("gui/images/bg/cyberspace_core.png", xysize=(SW, SH))
image bg cyberspace_core_ui = Transform("gui/images/bg/cyberspace_core_ui.png", xysize=(SW, SH))


#Персонажи
image nurse = Transform(
    "gui/images/ch/nurse.png",
    ysize=int(config.screen_height * 0.9)
)
image hamayumi = Transform(
    "gui/images/ch/Hamayumi/norm.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image quins = Transform(
    "gui/images/ch/quins/quins.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image zombi = Transform(
    "gui/images/ch/zombi/norm.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image nighstess = Transform(
    "gui/images/ch/nighstess/norm.png",
    xysize=(int(config.screen_width * 0.25), int(config.screen_height * 0.45)),
    yalign=500
)
image sand = Transform(
    "gui/images/ch/sand/norm.png",
    xysize=(int(config.screen_width * 0.3), int(config.screen_height * 0.6)),
    yalign=500
)

image doctor = Transform(
    "gui/images/ch/doctor/norm.png",
    xysize=(int(config.screen_width * 0.3), int(config.screen_height * 0.6)),
    yalign=500
)
image artemka = Transform(
    "gui/images/ch/artemka/norm.png",
    xysize=(int(config.screen_width * 0.3), int(config.screen_height * 0.6)),
    yalign=500
)