# Mashina Parsing

This project is not created with the intention of offending, harming, or disrupting the business of others, or engaging
in any malicious activities towards users or consumers. It is intended
for [provide a short description of the project's purpose].

## Installation

### Prerequisites

- Python 3.11
- pip

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - For Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - For Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run and enjoy
    ```bash
   python main.py
    ```

## Configuration

Open the `main.py` file and update the following fields in the `MashinaAPI` class:

```python
class MashinaAPI:
    EVERY = 1
    CHAT_ID = "your_chat_id"
    BOT_TOKEN = "your_bot_token"
    TELEGRAM_PATH = f"https://api.telegram.org/%s/sendPhoto" % BOT_TOKEN
    BASE_API = ("https://www.mashina.kg/search/all/all/?currency=1&price_from=10000&price_to=260000&sort_by=upped_at"
                "+desc&time_created=1&page=1")

```
## Build project

1. To build the project into a standalone executable using PyInstaller, run the following commands::

    ```bash
    pip install pyinstaller
   pyinstaller --onefile main.py
    ```

2. To run the executable, navigate to the dist directory and execute:

    - For Windows:

        ```bash
        ./main.exe
        ```

    - For Unix or MacOS:

        ```bash
        ./main
        ```
