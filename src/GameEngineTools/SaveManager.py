import os
import json as js
from time import gmtime, strftime


class SaveManager:
    def __init__(self):
        self.active_save = None
        self.sm_data = None
        self.saves_list = []
        self.load_save_manager_data()

    def generate_save_manager_data_to(self, sm_data_file_path):
        sm_data = dict()
        sm_data['active_save'] = None
        sm_data['max_saves_amount'] = 500
        sm_data['max_save_id'] = 0
        sm_data['free_save_id_list'] = []
        with open(sm_data_file_path, 'w') as new_sm_data_file:
            js.dump(sm_data, new_sm_data_file)

    def get_game_save(self):
        pass

    def load_save_manager_data(self):
        sm_data_file_path = os.path.join('SaveFiles', 'save_manager_data.json')

        if not os.path.isfile(sm_data_file_path):
            self.generate_save_manager_data_to(sm_data_file_path)

        with open(sm_data_file_path, 'r') as sm_data:
            self.sm_data = js.load(sm_data)

    def save_save_manager_data(self):
        sm_data_file_path = os.path.join('SaveFiles', 'save_manager_data.json')

        with open(sm_data_file_path, 'w') as sm_data:
            js.dump(self.sm_data, sm_data)

    def has_active_save(self):
        return self.sm_data['active_save'] != None

    def create_save(self, name):
        free_save_id = self.sm_data['free_save_id_list']
        save_id = self.sm_data['max_save_id'] + 1
        if len(free_save_id) > 0:
            save_id = free_save_id.pop()

        if self.sm_data['max_save_id'] + 1 >= self.sm_data['max_saves_amount'] and len(free_save_id) == 0:
            return 'You have reached your save limit'
        else: 
            self.sm_data['max_save_id'] = max(save_id, self.sm_data['max_save_id'])
            self.active_save = (save_id, name, {
                'created' : strftime("%Y-%m-%d %H:%M:%S", gmtime())
            }) #generate base save presets in dict
            self.save()
            return 'Save ' + name + ' created successfully'

    def delete_save(self, save_id):
        max_save_id = self.sm_data['max_save_id']
        free_save_id = [int(id) for id in self.sm_data['free_save_id_list']]
        if save_id > max_save_id or save_id in free_save_id:
            return 'Error! No such save exists!'
        else:
            free_save_id.append(save_id)
            while max_save_id in free_save_id:
                max_save_id -= 1
            print(free_save_id)
            free_save_id = [id for id in free_save_id if id < max_save_id]
            self.sm_data['max_save_id'] = max_save_id
            self.sm_data['free_save_id_list'] = free_save_id
            del self.sm_data[str(save_id)]
            path = os.path.join('SaveFiles', 'save' + str(save_id) + '.json')
            os.remove(path)
            self.save_save_manager_data()
            return 'Save deleted successfully'

    def activate_save(self, save_id):
        self.sm_data['active_save'] = save_id

    def load_save(self, save_id):
        try:
            pass
        except:
            pass

    def save(self):
        save_id, save_name, save_data = self.active_save
        save_data['last_saved'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.sm_data[str(save_id)] = save_name
        self.save_save_manager_data()
        save_path = os.path.join('SaveFiles', 'save' + str(save_id) + '.json')
        with open(save_path, 'w') as save_file:
            js.dump(save_data, save_file)
