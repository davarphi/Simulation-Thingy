class Enemy {
  float x, y, w, h;
  float vx, vy;
  float health = 100;
  
  
  Enemy() {
    x = width/2;
    y = 40;
    
    w = 16;
    h = 32;
    vx = 0;
    vy = 0;
  }
  void display() {
    fill(255, 255, 0);
    rectMode(CENTER);
    rect(x, y, w, h);
  }
 
 void takeDamage() {
   health -= 1;
   if (health < 0) {
     health = 0;
   }
   println(health);
   
 }
}
