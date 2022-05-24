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