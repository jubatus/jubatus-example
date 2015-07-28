import configparser
import random
import jubatus

class Slot:
    def __init__(self, p, ave, std):
        self.p   = p
        self.ave = ave
        self.std = std

    def hit(self):
        if random.random() < self.p:
            return True
        else:
            return False

    def generate_reward(self):
        if self.hit():
            return random.normalvariate(self.ave, self.std)
        else:
            return 0


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 9199
    name = 'bandit'
    player = 'player_A'
    cl = jubatus.Bandit(host, port, name, 0)

    config = configparser.SafeConfigParser()
    config.read('../config/slot.conf')
    slots = {}

    for  slot in config.options('slots'):
        cl.register_arm(slot)
        p, ave, std = [float(x) for x in config.get('slots', slot).split(',')]
        slots[slot] = Slot(p, ave, std)

    cl.reset(player)
    iteration = int(config.get('common', 'iteration'))
    cumulative_reward = 0
    for i in range(iteration):
        arm = cl.select_arm(player)
        reward = float(slots[arm].generate_reward())
        cl.register_reward(player, arm, reward)
        cumulative_reward += reward
    print ('cumulative reward is %.2f' % cumulative_reward)
    arm_info = cl.get_arm_info(player)
    print ('slot frequencies are:')
    print (sorted([(x, arm_info[x].trial_count) for x in arm_info.keys()], key= lambda x: x[1], reverse=True))
    

