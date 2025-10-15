class Player {
  PVector pos = new PVector();
  float w, h;
  PVector vel = new PVector();
  float DEF_SPEED;
  
  Player() {
    DEF_SPEED = 4;
    pos.x = width/2;
    pos.y = height/2;
    
    w = 8;
    h = 8;
    vel.x = 0;
    vel.y = 0;
  }
  
  void update() {
    if(LEFT) {
      vel.x = -1;
    } else if (RIGHT) {
      vel.x = 1;
    } else if (!LEFT && !RIGHT) {
      vel.x = 0;
    }
       
    if(UP) {
      vel.y = -1;
    } else if (DOWN) {
      vel.y = 1;
    } else if (!UP && !DOWN) {
      vel.y = 0;
    }
    
    //if ((LEFT || RIGHT) && (UP || DOWN)) {
      
    //}
    float speed = DEF_SPEED;
    if (SLOW) {
      speed /= 2; 
    }
    pos.add(vel.normalize().mult(speed));
    
    if(pos.x < w/2) {
      pos.x = w/2;
      //vx = 0;
    } else if ( pos.x > width - w/2) {
      pos.x = width - w/2;
      //vx = 0;
    }
    
    if(pos.y < h/2) {
      pos.y = h/2;
      //vy = 0;
    } else if ( pos.y > height - h/2) {
      pos.y = height - h/2;
      //vy = 0;
    }
  }
  
  void display() {
    fill(255, 0, 0);
    rectMode(CENTER);
    rect(pos.x, pos.y, w, h);
  }
}
