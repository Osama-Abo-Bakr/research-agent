# Research Agent with LangChain and Groq

## Overview

This project demonstrates how to create a research agent using LangChain and Groq. The agent is designed to answer complex research questions by leveraging the Semantic Scholar tool for academic research and the Groq API for language model capabilities. The agent is initialized with a prompt template and can execute queries to provide detailed explanations on various topics.

## Project Structure

The project is organized into the following files and folders:

```
research-agent/
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

### Files

- **`.env.example`**: A template for the `.env` file where you can add your `GROQ_API_KEY`.
- **`main.py`**: The main script that initializes the research agent, sets up the tools, and executes the agent to answer research questions.
- **`requirements.txt`**: Lists the Python dependencies required to run the project.
- **`README.md`**: This file, providing an overview and instructions for the project.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/research-agent.git
   cd research-agent
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the environment variables**:
   - Rename `.env.example` to `.env`.
   - Add your `GROQ_API_KEY` to the `.env` file.

## Usage

To run the research agent, execute the `main.py` script:

```bash
python main.py
```

The agent will process the input query and provide a detailed explanation based on the available tools and the Groq language model.

## Example Query

The agent is pre-configured to answer the following query:

```plaintext
Explain me what the multi head attention in transformer
```

The agent will retrieve relevant information from Semantic Scholar and use the Groq language model to generate a detailed response.

## Dependencies

- **semanticscholar**: Provides access to the Semantic Scholar API for academic research.
- **python-dotenv**: Used for managing environment variables.
- **langchain**: The core framework for creating and managing agents.
- **langchain_groq**: Integration with the Groq API for language model capabilities.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- **LangChain**: For providing the framework to create and manage agents.
- **Groq**: For providing the language model capabilities.
- **Semantic Scholar**: For providing access to academic research papers.

---