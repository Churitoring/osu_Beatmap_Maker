from cx_Freeze import setup, Executable

setup(
    name="osu! Beatmap Maker",
    version="0.0.1",
    description="osu! Beatmap Maker Made By Churitoring",
    executables=[Executable("obmc.py", icon="osu beatmap maker.ico")]
)
