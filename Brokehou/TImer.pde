class Timer {
  int startTime;
  int intreval;
  
  Timer(int timeIntreval) {
    intreval = timeIntreval;
  }
  
  void start() {
    startTime = millis();
  }
  
  boolean complete() {
    int elapsedTime = millis() - startTime;
    if (elapsedTime > intreval) {
      return true;
    } else {
      return false;
    }
  }
}
