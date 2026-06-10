# Jarvis Voice Assistant

A Python-based voice assistant that can open websites, play music, and read the latest news using voice commands.

## Features

* Voice activation using the keyword **"Jarvis"**
* Open popular websites:

  * YouTube
  * Google
  * Facebook
  * Twitter
  * Instagram
  * GitHub
  * WhatsApp
* Play songs from a custom music library
* Fetch and read the latest news headlines
* Text-to-speech responses
* Voice command recognition

## Technologies Used

* Python
* SpeechRecognition
* Pyttsx3
* Requests
* PyAudio
* NewsAPI

## Project Structure

```text
Jarvis/
│
├── main.py
├── musicLib.py
├── requirements.txt
├── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your NewsAPI key:

```python
newsapi = "YOUR_API_KEY"
```

## Usage

Run the application:

```bash
python main.py
```

Say:

```text
Jarvis
```

Then use commands such as:

```text
Open YouTube
Open Google
Play Duro
News
Exit
```

## List of songs

*Dekh
*Agar
*Sajni
*Tinak
*Duro

## Requirements

* Python 3.10+
* Working microphone
* Internet connection

## Future Improvements

* Weather updates
* AI-powered conversations
* System control commands
* Application launching
* Reminder and alarm support

## License

This project is open-source and available under the MIT License.
