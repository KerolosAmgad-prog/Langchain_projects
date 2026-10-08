# Langchain Search Agent

This project demonstrates a simple and effective AI Agent built using **LangChain** and **Tavily**. The agent acts as an automated researcher capable of searching the web for real-time information and reasoning over the results using an OpenAI Language Model.

## 🚀 Features

- **Tavily Search Integration:** Leverages the Tavily Search API as a custom LangChain tool to perform internet searches quickly and accurately.
- **OpenAI Powered:** Uses `ChatOpenAI` as the reasoning engine to decide when to search and how to compile the final answer based on the user's prompt.
- **Environment Management:** Uses `python-dotenv` for secure loading of API keys.

## 🛠️ Prerequisites

To run this project, you will need the following API keys:
1. **OpenAI API Key:** For the language model. Get it from [OpenAI](https://platform.openai.com/).
2. **Tavily API Key:** For the search tool. Get it from [Tavily](https://tavily.com/).

## 💻 Setup Instructions

1. **Clone or download the project** to your local machine.
2. **Install dependencies:** Make sure you have the required Python packages installed. You can install them using pip:
   ```bash
   pip install langchain langchain-openai langchain-core python-dotenv tavily-python
   ```
3. **Configure Environment Variables:** 
   Ensure you have a `.env` file in the root directory (same level as `main.py`) and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

## 🏃‍♂️ How to Run

Execute the `main.py` file from your terminal:

```bash
python main.py
```

By default, the script asks the agent to find 3 job postings for an AI engineer using LangChain in the Bay Area on LinkedIn. It will print the search logs and then output the agent's final synthesized response.

## 📁 Project Structure

- [`main.py`](main.py): The main execution script containing the tool definition and agent setup.
- `.env`: Holds your secret API keys (do not commit this file to version control).
