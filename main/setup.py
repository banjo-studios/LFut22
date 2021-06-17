import os, json


def main_setup():
    try:
        settings_data = json.load(open("./player/settings.json", "r+"))
        # if settings_data['load_player_folder'] = False:
        #    return
        # if setting is true
    except FileNotFoundError:
        pass

    os.chdir("..")

    if not os.path.isdir('./player/'):
        os.mkdir("./player/")
        os.mkdir("./player/data")

    try:
        open("./player/settings.json", "x").write("{ }")
        settings_data = json.load(open("./player/settings.json", "r+"))
        settings_data['load_starting_screen'] = True
        settings_data['skip_preload'] = False

        # add more settings
        json.dump(settings_data, open("./player/settings.json", "w"), indent=4)
    except FileExistsError:
        pass

    os.chdir('./main')
