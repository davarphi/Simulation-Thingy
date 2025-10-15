class Projectile {
  float x, y, r, vx, vy, startX, startY;
  float speed;
  boolean inMotion;
  
  Projectile(float sx, float sy) {
    startX = sx;
    startY = sy;
    x = startX;
    y = startY;
    speed = 10;
    
    r = 10;
    vx = 0;
    vy = 0;
    inMotion = false;
  }
  
  void update() {
    x += vx;
    y += vy;
    checkBound();
  }
  
  void fire(float newX, float newY) {
    x = newX;
    y = newY;
    
    if (!inMotion) {
      vx = 0;
      vy = -speed;
    }
    
    x += vx;
    y += vy;
    inMotion = true;
  }
  void display() {
    fill(255, 0, 0, 60);
    circle(x, y, r);
  }
  
  void reset() {
    x = startX;
    y = startY;
    
    vx = 0;
    vy = 0;
    
    inMotion = false;
  }
  
  void checkBound() {
    if (y < r/2 || y > height - r/2) {
      reset();
  }
 }
}
