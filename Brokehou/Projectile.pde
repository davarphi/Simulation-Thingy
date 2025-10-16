class Projectile {
  PVector pos, vel, start;
  float r;
  float speed;
  float attackDeg;
  boolean inMotion;
  
  Projectile(float sx, float sy) {
    start = new PVector(sx, sy);
    pos = start.copy();
    speed = 10;
    
    r = 10;
    vel = new PVector(0, 0);
    inMotion = false;
  }
  
  void update() {
    pos.add(vel);
    checkBound();
  }
  
  void fire(float newX, float newY, int flag) {
    if (SLOW) {
      attackDeg = radians(2);
      println("Firing focus...");
    } else {
      attackDeg = radians(5);
    }
    
    pos.set(newX, newY);
    
    if (!inMotion) {
      switch (flag) {
      case 0:
      vel.set(cos(HALF_PI + attackDeg), -sin(HALF_PI + attackDeg)).mult(speed);
      break;
      case 1:
      vel.set(0, -speed);
      break;
      case 2:
      vel.set(cos(HALF_PI - attackDeg), -sin(HALF_PI - attackDeg)).mult(speed);
      break;
      }
    }
    
    pos.add(vel);
    inMotion = true;
  }
  void display() {
    fill(255, 0, 0, 60);
    circle(pos.x, pos.y, r);
  }
  
  void reset() {
    pos.set(start);
    vel.set(0, 0);
    inMotion = false;
  }
  
  void checkBound() {
    if (pos.y < r/2 || pos.y > height - r/2) {
      reset();
  }
 }
}
