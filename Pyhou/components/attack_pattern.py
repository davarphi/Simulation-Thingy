from math import radians, pi, sin, cos
from pygame.math import Vector2
from .enemy_projectile import EnemyProjectile

def get_fan_aim_pattern_bullets(cnt1, cnt2, ang1, ang2, spe1, spe2, pos=Vector2(0,0), rel_with=0):
    new_projectile = []
    for i in range(cnt2):
        speed = spe1 - i*(spe1 - spe2)/(cnt2 - 1)
        for j in range(cnt1):
                angle = rel_with - ang1 + ang2*(-(cnt1-1)/2 + j)
                bullet = EnemyProjectile(pos.x, pos.y, radians(angle), speed)
                new_projectile.append(bullet)

    return new_projectile

if __name__ == "__main__":
    output = get_fan_aim_pattern_bullets(7, 3, 0, 5, 6, 2)

    for i in output:
         print(i)