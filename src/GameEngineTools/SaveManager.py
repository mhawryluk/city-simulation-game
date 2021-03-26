import os
import json as js
from time import gmtime, strftime


class SaveManager:
    def __init__(self):
        self.active_save = None
        self.settings = None
        self.saves_list = []
        self.load_settings()

    def generate_base_settings(self, settings_file):
        settings = dict()
        settings['active_save'] = None
        settings['max_saves_amount'] = 500
        settings['max_save_id'] = 0
        settings['free_save_id_list'] = []
        with open(settings_file, 'w') as new_settings_file:
            js.dump(settings, new_settings_file)

    def get_game_save(self):
        pass

    def load_settings(self):
        settings_file = os.path.join('SaveFiles', 'settings.json')

        if not os.path.isfile(settings_file):
            self.generate_base_settings(settings_file)

        with open(settings_file, 'r') as settings:
            self.settings = js.load(settings)

    def save_settings(self):
        settings_file = os.path.join('SaveFiles', 'settings.json')

        with open(settings_file, 'w') as settings:
            js.dump(self.settings, settings)

    def has_active_save(self):
        return self.settings['active_save'] != None

    def create_save(self, name):
        free_save_id = self.settings['free_save_id_list']
        save_id = self.settings['max_save_id'] + 1
        if len(free_save_id) > 0:
            save_id = free_save_id.pop()

        if self.settings['max_save_id'] + 1 >= self.settings['max_saves_amount'] and len(free_save_id) == 0:
            return 'You have reached your save limit'
        else: 
            self.settings['max_save_id'] = max(save_id, self.settings['max_save_id'])
            self.active_save = (save_id, name, {
                'created' : strftime("%Y-%m-%d %H:%M:%S", gmtime())
            }) #generate base save presets in dict
            self.save()
            return 'Save ' + name + ' created successfully'

    def delete_save(self, save_id):
        max_save_id = self.settings['max_save_id']
        free_save_id = [int(id) for id in self.settings['free_save_id_list']]
        if save_id > max_save_id or save_id in free_save_id:
            return 'Error! No such save exists!'
        else:
            free_save_id.append(save_id)
            while max_save_id in free_save_id:
                max_save_id -= 1
            print(free_save_id)
            free_save_id = [id for id in free_save_id if id < max_save_id]
            self.settings['max_save_id'] = max_save_id
            self.settings['free_save_id_list'] = free_save_id
            del self.settings[str(save_id)]
            path = os.path.join('SaveFiles', 'save' + str(save_id) + '.json')
            os.remove(path)
            self.save_settings()
            return 'Save deleted successfully'

    def activate_save(self, save_id):
        self.settings['active_save'] = save_id

    def load_save(self, save_id):
        try:
            pass
        except:
            pass

    def save(self):
        save_id, save_name, save_data = self.active_save
        save_data['last_saved'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.settings[str(save_id)] = save_name
        self.save_settings()
        save_path = os.path.join('SaveFiles', 'save' + str(save_id) + '.json')
        with open(save_path, 'w') as save_file:
            js.dump(save_data, save_file)
