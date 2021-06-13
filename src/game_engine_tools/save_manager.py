import json as js
import os
from time import gmtime, strftime


class SaveManager:
    def __init__(self):
        self.active_save = None
        self.sm_data = None
        self.saves_list = []
        self.happiness_threshold = 3
        self.load_save_manager_data()

    @staticmethod
    def generate_save_manager_data_to(sm_data_file_path):
        sm_data = dict()
        sm_data['active_save'] = None
        sm_data['max_saves_amount'] = 500
        sm_data['max_save_id'] = 0
        sm_data['free_save_id_list'] = []
        with open(sm_data_file_path, 'w') as new_sm_data_file:
            js.dump(sm_data, new_sm_data_file)

    def load_save_manager_data(self):
        sm_data_file_path = os.path.join(
            'SaveFiles', 'save_manager_data.json')

        if not os.path.isfile(sm_data_file_path):
            self.generate_save_manager_data_to(sm_data_file_path)

        with open(sm_data_file_path, 'r') as sm_data:
            self.sm_data = js.load(sm_data)

    def save_save_manager_data(self):
        sm_data_file_path = os.path.join(
            'SaveFiles', 'save_manager_data.json')

        with open(sm_data_file_path, 'w') as sm_data:
            js.dump(self.sm_data, sm_data)

    def has_active_save(self):
        return self.sm_data['active_save'] is not None

    def create_save(self, name):
        free_save_id = self.sm_data['free_save_id_list']
        save_id = self.sm_data['max_save_id'] + 1
        if len(free_save_id) > 0:
            save_id = free_save_id.pop()

        if self.sm_data['max_save_id'] + 1 >= self.sm_data['max_saves_amount'] and len(free_save_id) == 0:
            return 'You have reached your save limit'
        else:
            self.sm_data['max_save_id'] = max(
                save_id, self.sm_data['max_save_id'])
            self.active_save = (save_id, name, {
                'created': strftime("%Y-%m-%d %H:%M:%S", gmtime())
            })  # generate base save presets in dict
            self.save()
            self.set_active_save()
            return 'Save ' + name + ' created successfully'

    def set_active_save(self):
        if self.sm_data['max_save_id'] == 0:
            self.sm_data['active_save'] = None
        else:
            ind = 1
            while ind in self.sm_data['free_save_id_list']:
                ind += 1
            self.activate_save(ind)

    def activate_save(self, save_id):
        self.sm_data['active_save'] = save_id
        self.save_save_manager_data()

    def delete_save(self):
        save_id = self.sm_data['active_save']

        max_save_id = self.sm_data['max_save_id']
        free_save_id = [int(id) for id in self.sm_data['free_save_id_list']]
        free_save_id.append(save_id)
        while max_save_id in free_save_id:
            max_save_id -= 1
        free_save_id = [id for id in free_save_id if id < max_save_id]
        self.sm_data['max_save_id'] = max_save_id
        self.sm_data['free_save_id_list'] = free_save_id
        del self.sm_data[str(save_id)]
        path = os.path.join('SaveFiles', 'save' + str(save_id) + '.json')
        os.remove(path)
        self.set_active_save()
        self.save_save_manager_data()

    def load_save(self):
        save_id = self.sm_data['active_save']
        save_path = os.path.join(
            'SaveFiles', 'save' + str(save_id) + '.json')
        save_name = self.sm_data[str(save_id)]
        with open(save_path, 'r') as save_file:
            save_data = js.load(save_file)
        self.active_save = (save_id, save_name, save_data)

    def save(self, game_save_data=None):
        if game_save_data is None:
            game_save_data = {}
            
        save_id, save_name, save_data = self.active_save
        save_data['last_saved'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        save_data['game_state'] = game_save_data
        self.sm_data[str(save_id)] = save_name
        self.save_save_manager_data()
        save_path = os.path.join(
            'SaveFiles', 'save' + str(save_id) + '.json')
        with open(save_path, 'w') as save_file:
            js.dump(save_data, save_file)

    def list_saves(self):
        list_of_saves = []
        free_save_id = [int(id) for id in self.sm_data['free_save_id_list']]
        save_ids = [str(id) for id in range(
            1, self.sm_data['max_save_id'] + 1) if id not in free_save_id]
        for key in save_ids:
            list_of_saves.append(
                ('[ ' + self.sm_data[key] + ' ] id: ' + str(key), key))
        return list_of_saves

    def get_gameplay_data(self):
        return self.active_save[2].get('game_state', {})
