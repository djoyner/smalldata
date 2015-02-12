#define OPTICAL_SWITCH_PIN  14  // A0

#define WHEEL    0
#define NO_WHEEL 1

void setup()
{
  Serial.begin(38400);
  Serial.println("Hello Leia!");
  pinMode(OPTICAL_SWITCH_PIN, INPUT);
}

int lastWheelState = NO_WHEEL;  // Assume no wheel

void loop()
{
  // Read the current wheel state
  int wheelState = digitalRead(OPTICAL_SWITCH_PIN);
  
  // If the wheel wasn't present before but is present now, print a plus sign
  if (lastWheelState == NO_WHEEL && wheelState == WHEEL)
  {
     Serial.println("+");
  }
  
  // Save the wheel state for next time
  lastWheelState = wheelState;
}
