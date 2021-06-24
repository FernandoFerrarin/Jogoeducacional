import cx_Freeze
executables = [cx_Freeze.Executable(
    script="game.py", icon="assets/ironIcon.ico")]

cx_Freeze.setup(
    name="Iron Man",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["assets"]
        }},
    executables=executables
)