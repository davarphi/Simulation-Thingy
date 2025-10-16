class Enemy {
  PVector pos, vel;
  float w, h;
  float health = 100;
  
  
  Enemy() {
    pos = new PVector(width/2, 40);
    
    w = 16;
    h = 32;
    vel = new PVector(0,0);
  }
  void display() {
    fill(255, 255, 0);
    rectMode(CENTER);
    rect(pos.x, pos.y, w, h);
  }
 
 void takeDamage() {
   health -= 1;
   if (health < 0) {
     health = 0;
   }
   println(health);
   
 }
}
