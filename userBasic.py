class UserBasic(object):
    def __init__(self, first_name, last_name, mid_name):
        self.first_name = first_name
        self.last_name = last_name
        self.mid_name = mid_name

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.mid_name}'


inst = UserBasic("Taras", "Shmilyk", "Johnny")

print(inst.full_name())
