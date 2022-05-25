class Slayer:
    hp = 100
    ammo = 0
    x = 0
    y = 0
    z = 0
    shoot = true

    def getHealth():
        return hp
    
    def setHealth(int h):
        hp = h
        return hp
    
    def getAmmo():
         return ammo

     def setAmmo(int a):
         ammo = a
         return a

     def shoot():
         ammo = ammo - 1;
         if (crosshairs over demon):
             demonHealth = demonHealth - 20
             if (demonHealth = 0 or demonHealth <0):
                 remove demon entity

     def
    
    '''
    class Demon2:

 def __init__(self, health, speed, damage):
    self.demon = Entity(model='rectangle', color=color.white, texture = 'deamon', scale = (2, 4, 2), position = (2, 10, 20), collider = 'rectangle')
    self.health = health
    self.speed = speed
    self.damage = damage

    def aggro(self):
        if player.x > self.demon.x and distance(self.demon.position, player.position) > 2:
            self.demon.x += .05
        if player.x < self.demon.x and distance(self.demon.position, player.position) > 2:
            self.demon.x -= .05
        if player.z > self.demon.z and distance(self.demon.position, player.position) > 2:
            self.demon.z += .05
        if player.z < self.demon.z and distance(self.demon.position, player.position) > 2:
            self.demon.z -= .05

    def notice(self):
        if distance(self.demon.position, player.position) >= 30:
            self.aggro()

    def attack(self):
        count = 0

        if distance(self.demon.position, player.position) <= 10:
            while count < 15:
                if (player.x > self.demon.x and distance(self.demon.position, player.position) > 2:
                    self.fireBall.x += .05
                    count+=1
                if player.x < self.demon.x and distance(self.demon.position, player.position) > 2:
                    self.fireBall.x -= .05
                    count+=1

        if player.x = fireBall.x:
            #player.setHealth(player.getHealth() - self.damage)
        
        elif distance(self.demon.position, player.position) <= 1:
            #player.setHealth(player.getHealth() - self.damage)
                pass

    def die(self):
        destroy(self.demon)
    '''
