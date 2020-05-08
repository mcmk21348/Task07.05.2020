class Soldier:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

class Gun:
    def __init__(self, name1, reloads, bullets):
        self.name1 = name1
        self.reloads = reloads
        self.bullets = bullets
        self.shooting = 0
    
    def Shoot(self):
        for i in range(self.bullets):
            self.shooting += 1
            self.bullets -= 1
            print('Тыр тыр тыр тыр', self.bullets)
            if self.bullets == 0:
                print('No patron!!!')
                continue
    
    def reload(self, reloads):
        self.reloads = reloads
        print('Soldier done reload')


class Act_if_Shooting(Gun, Soldier):
    def __init__(self, name, rank, name1, reloads, bullets):
        Soldier.__init__(self, name, rank)
        Gun.__init__(self, name1, reloads, bullets)
        print('Soldier will fire from a gun and reload, and fire one more time.')


soldier = Act_if_Shooting('Beka', 'Serjant', 'M416', 'reloads', 70)
soldier.Shoot()
soldier.reload('reloads')








