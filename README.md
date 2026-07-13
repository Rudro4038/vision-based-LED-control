# Vision-Based LED Control Using Hand Gesture Recognition

A real-time computer vision project that detects the number of fingers shown to a laptop webcam and controls an Arduino to illuminate the corresponding number of LEDs.

---

## 📌 Project Overview

This project combines **Computer Vision** and **Embedded Systems** to create a gesture-controlled LED system. Using **OpenCV** and **MediaPipe**, the system recognizes the number of fingers (0–5) displayed in front of the webcam. The detected finger count is sent via serial communication to an **Arduino Uno**, which lights up the corresponding number of LEDs.

For example:

| Fingers Detected | LEDs ON                   |
| ---------------- | ------------------------- |
| 0                | None                      |
| 1                | LED1                      |
| 2                | LED1 + LED2               |
| 3                | LED1 + LED2 + LED3        |
| 4                | LED1 + LED2 + LED3 + LED4 |
| 5                | All LEDs                  |

---

# Features

* Real-time hand tracking
* Finger counting using MediaPipe
* USB Serial communication
* Arduino-controlled LEDs
* Supports left and right hands
* Lightweight and fast
* Easy to extend for IoT and home automation

---

# Project Structure

```
Vision-Based-LED-Control/
│
├── finger_counter.py          # OpenCV + MediaPipe application
├── arduino/
│   └── led_controller.ino     # Arduino code
│
├── requirements.txt
├── README.md
└── images/
    ├── setup.jpg
    └── demo.gif
```

---

# Hardware Requirements

* Laptop
* Webcam (built-in or USB)
* Arduino Uno/Nano
* Breadboard
* 5 LEDs
* 5 × 220Ω Resistors
* Jumper wires
* USB Cable

---

# Software Requirements

* Python 3.11+
* Arduino IDE
* OpenCV
* MediaPipe
* PySerial

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/vision-led-control.git
```

Enter the project

```bash
cd vision-led-control
```

Create virtual environment

```bash
python3.11 -m venv .venv
```

Activate

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Circuit Diagram

Arduino Connections

| Arduino Pin | Component     |
| ----------- | ------------- |
| D2          | LED1          |
| D3          | LED2          |
| D4          | LED3          |
| D5          | LED4          |
| D6          | LED5          |
| GND         | Common Ground |

Each LED must be connected through a **220Ω resistor**.

---

# How It Works

1. The webcam captures live video.
2. OpenCV reads each frame.
3. MediaPipe detects the hand landmarks.
4. The software counts the number of raised fingers.
5. The finger count (0–5) is sent to the Arduino through USB Serial.
6. The Arduino lights the corresponding LEDs.

---

# Running the Project

## Upload Arduino Code

Open

```
arduino/led_controller.ino
```

Upload it to the Arduino.

---

## Find the Arduino Port

### Windows

```
COM3
```

or

```
COM4
```

### macOS

```
/dev/cu.usbmodem1101
```

or

```
/dev/cu.usbserial-xxxx
```

Update the serial port inside `finger_counter.py`.

Example:

```python
arduino = serial.Serial("/dev/cu.usbmodem1101", 9600)
```

---

## Run

```bash
python finger_counter.py
```

Press **Q** to quit.

---

# Example Output

```
Detected Fingers: 3

Arduino receives:

3

LED Status:

LED1 ON
LED2 ON
LED3 ON
LED4 OFF
LED5 OFF
```

---

# Arduino Logic

```
Receive finger count

↓

Turn ON first N LEDs

↓

Turn OFF remaining LEDs
```

---

# Future Improvements

* ESP32 Wi-Fi Control
* Bluetooth Communication
* RGB LED Strip
* OLED Display
* Relay Module for Home Automation
* Gesture Recognition (Thumbs Up, Fist, Peace Sign)
* Voice + Gesture Hybrid Control
* Mobile App Integration

---

# Technologies Used

* Python
* OpenCV
* MediaPipe
* Arduino
* C/C++
* PySerial

---

# Authors

**Robin Dey**

Department of Computer Science and Engineering

---

# License

This project is licensed under the **MIT License**.
