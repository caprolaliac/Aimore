# AI Movie Reccomendation system

## Overview

This Streamlit-based application leverages artificial intelligence to provide personalized movie recommendations. It uses the { Mistral/phi3 } language model via Ollama for generating recommendations and integrates with The Movie Database (TMDb) API for fetching additional movie metadata*. 

## Features

- **AI-Driven Recommendations**: Utilizes the Mistral language model through Ollama to generate contextual movie suggestions.
- **Multi-Criteria Selection**: Users can filter recommendations by genre, year range, and mood.
- **TMDb Integration**: Fetches additional movie details from The Movie Database API*.
- **Interactive UI**: Built with Streamlit for a responsive and user-friendly interface.

***Issue**: 'Streamlit: TMDb movie link not opening in new tab'

## Installation

1. Clone the repository:
    ```bash
      git clone https://github.com/caprolaliac/Aimore

2. Install dependencies:
    ```bash
      pip install -r requirements.txt

3. Install and set up Ollama:
    ```bash
      chmod +x install_ollama.sh
    ```
    ```bash
      sudo ./install_ollama.sh
    ```
    ```bash
      ollama serve &
    ```
    ```bash
      ollama pull mistral / ollama pull phi3
    ```

4. Set up your TMDb API key in the script.

5. run streamlit app

   ```bash
      python -m streamlit run app.py
   ```

  ## Usage

1. Select movie genres, year ranges, and moods from the provided options.
2. (Optional) Add any additional preferences in the text area.
3. Click "Get Recommendation" to receive an AI-generated movie suggestion.
4. Use the "Get More Details from TMDb" button to fetch and display additional movie information.

## Results


### Ollama Logs:

```bash

time=2024-06-22T18:44:50.440Z level=INFO source=server.go:590 msg="llama runner started in 13.56 seconds"

[GIN] 2024/06/22 - 18:46:46 | 200 |         2m10s |       127.0.0.1 | POST     "/api/chat"

[GIN] 2024/06/22 - 18:52:26 | 200 |         1m11s |       127.0.0.1 | POST     "/api/chat"
```

These logs indicate:

1. Ollama server started successfully (first line).
2. Successful POST requests to the `/api/chat` endpoint (subsequent lines).
3. HTTP status 200 means the requests were processed successfully.
4. The time taken for each request (e.g., 2m10s, 1m11s) shows processing duration.

Long processing times (over 1 minute) are normal for complex tasks like generating movie recommendations
