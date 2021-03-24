import os
import json as js

class SaveManager:
    def __init__(self):
        self.active_save = None
        self.active_settings = None
        self.saves_list = []
        self.load_settings()

    def generate_base_settings(self, settings_file):
        settings = dict()
        settings['active_save'] = None
        settings['saves_amount'] = 0
        settings['max_saves_amount'] = 500
        with open(settings_file, 'w') as new_settings_file:
            js.dump(settings, new_settings_file)

    def generate_game_save_source(self):
        pass

    def load_settings(self):
        settings_file = os.path.join('SaveFiles', 'settings.json')

        if not os.path.isfile(settings_file):
            self.generate_base_settings(settings_file)

        with open(settings_file, 'r') as settings:
            self.active_settings = js.load(settings)

    def save_settings(self):
        pass

    def has_active_save(self):
        return self.active_settings['active_save'] != None

    def create_save(self, name):
        save_id = settings['saves_amount'] + 1
        if save_id >= settings['max_saves_amount']:
            # error
            pass
        else:
            settings['saves_amount'] = save_id
            self.active_save = {'name': name, 'id': save_id}

            self.save()

    def activate_save(self, save_id):
        self.active_settings['active_save'] = save_id

    def load_save(self, save_id):
        try:
            pass
        except:
            pass

    def save(self):
        save_id = self.activate_save['id']
        self.active_save['last_saved'] = pg.time.get_time()
        save_path = os.path.join('SaveFiles', 'save' + save_id + '.json')
        with open(save_path, 'w') as save_file:
            js.dump(self.activate_save, save_file)
