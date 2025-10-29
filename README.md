# Face Detection Bot
This is a readme file of the project on Face Detection. This python code uses haarcascade, opencv and face_detection to tell who the person really is, this code works on the local stored photo's of the individuals and can be increased further.
Author Akshat Srivastava

How does this code works for us:

A window will open showing the live feed from your webcam.
The program will draw green (or blue) rectangles around any faces it detects in real-time.
When a face is detected, the script will send a signal (like the character '1') over the USB port to your Arduino.
The Arduino will then (based on its own code) light up an LED (or blink it) to confirm a face is present.

Some information for the model that i have used for the same:

Pros: It is extremely fast and very lightweight (low CPU usage). It's perfect for simple applications or on low-power devices (like a Raspberry Pi).
Cons: It is an older technology and is not very accurate compared to modern methods. It is well-known for:
False Positives: Detecting faces in random patterns, like wood grain or posters.
False Negatives: Missing faces, especially if they are at an angle, in poor lighting, or partially covered (e.g., by a hand or a mask).
