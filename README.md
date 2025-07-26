# literalsubtitletranslator
A Gemini tool for translating subtitles from Japanese to English literally, i.e., preserving sentence structure, for learning vocabulary. This is my first ever project. Thank you for checking it out!

## 🔧 Installation
To set up this project locally, follow these steps:

```bash
# Clone the Repository
git clone https://github.com/ppllama/literalsubtitletranslator
cd literalsubtitletranslator

# Create virtual environment
python -m venv venv

# Activate it
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Make a .env file which contains your gemini api key in the following format:
GEMINI_API_KEY="<your api key>"

```
## Usage
```bash
# Run this command from the project root
python main.py "<path to file>" "start=<starting_line_number>" --verbose
# Start defaults to 1
# You can use an optional --verbose flag to get responses at different stages of the subtitle translation
```

## Config Notes
The following defaults can be changed in the config file:

1. NUMBER_OF_LINES_PER_REQUEST = 50
2. STARTING_LINE = 1
3. AI_FAIL_LIMIT = 5 (Number of retries before giving up on the gemini api)
4. SYSTEM_PROMPT
5. SHIFT_TIME = 5 (seconds integer) (Shift subtitle forwards or backwards by seconds)

PS: I have only tried srt files so far. I have not looked into any other formats. The output is in ass format.
