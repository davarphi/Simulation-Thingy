boolean UP, DOWN, LEFT, RIGHT;
boolean SLOW;
boolean SHOOT;
Projectile[] projs;
int nextProjectile;
Timer firingTimer;

Player p;
Enemy e;

void setup() {
  //size(960, 720); //DEFAULT SIZE
  size(576, 672);
  UP = false;
  DOWN = false;
  LEFT = false;
  RIGHT = false;
  SHOOT = false;
  SLOW = false;
  
  p = new Player();
  e = new Enemy();
  projs = new Projectile[60];
  for (int i = 0; i < projs.length; i++) {
    projs[i] = new Projectile(-3, -3);
  }
  
  nextProjectile = 0;
  firingTimer = new Timer(100);
  firingTimer.start();
  println("Success!");
}

void draw() {
  background(128);
  if (SHOOT) {
    if (firingTimer.complete()) {
      projs[nextProjectile].fire(p.pos.x, p.pos.y);
      nextProjectile = (nextProjectile + 1) % projs.length;
      firingTimer.start();
    }
  }
  
  for (int j = 0; j < projs.length; j++) {
    projs[j].update();
    projs[j].display();
    if (isProjIntersect(projs[j], e)) {
      e.takeDamage();
      projs[j].reset();
    }
  }
  
  p.update();
  p.display();
  e.display();
}

void keyPressed() {
  switch (keyCode) {
    case 37:
    LEFT  = true;
    break;
    case 38:
    UP  = true;
    break;
    case 39:
    RIGHT  = true;
    break;
    case 40:
    DOWN  = true;
    break;
    case 16:
    SLOW  = true;
    break;
    case 90:
    SHOOT  = true;
    break;
  }
}

void keyReleased() {
    switch (keyCode) {
    case 37:
    LEFT  = false;
    break;
    case 38:
    UP  = false;
    break;
    case 39:
    RIGHT  = false;
    break;
    case 40:
    DOWN  = false;
    break;
    case 16:
    SLOW  = false;
    break;
    case 90:
    SHOOT  = false;
    break;
  }
}
boolean isPlayerIntersect(Player p, Enemy e){
  return true;
}
boolean isProjIntersect(Projectile p, Enemy e){
  float e_left = e.x - e.w/2;
  float e_right = e.x + e.w/2;
  float e_up = e.y - e.h/2;
  float e_down = e.y + e.h/2;
  
  float closest_x = max(e_left, min(p.x, e_right));
  float closest_y = max(e_up, min(p.y, e_down));
  
  float distance_x = p.x - closest_x;
  float distance_y = p.y - closest_y;
  
  double distance_squared = Math.pow(distance_x, 2) + Math.pow(distance_y, 2);
  
  return distance_squared <= Math.pow(p.r, 2);
}
