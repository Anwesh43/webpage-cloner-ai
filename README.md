# Webpage Cloner AI

A Python project to clone and analyze web pages using AI-powered tools. The core functionality is implemented in the `webpage_cloner_ai` directory.

## 📁 Project Structure
```
.
├── amazon-dark-clone.html
├── educative-light.html
├── leet.png
├── neetcode-light.html
├── neetcode.png
├── poetry.lock
├── pyproject.toml
├── README.md
├── test.html
├── tests/
└── webpage_cloner_ai/
    ├── agents/
    ├── prompts/
    ├── services/
    ├── tools/
    └── tests/
```

## 🔧 Key Components

### 1. Core Logic (`webpage_cloner_ai`)
- **Agents**: Contains the main logic for webpage cloning
  - `webpage_agent.py` - Main agent implementation
- **Prompts**: AI prompt templates
  - `system_prompt.py` - System prompt definitions
- **Services**: Functional components
  - `ollama_vision_service.py` - AI-powered vision analysis
  - `save_html_service.py` - HTML saving functionality
  - `screenshot_service.py` - Screenshot capture
- **Tools**: Utility functions
  - `webpage_tools.py` - Helper utilities

### 2. Example Templates
- Dark mode clone of Amazon UI
- Light mode clone of Educative UI
- Logo files for LeetCode and NeetCode

### 3. Setup
Install dependencies using:
```bash
poetry install
```

### 4. Testing
Run tests with:
```bash
poetry run pytest tests/
```

## 📝 Notes
- The project uses Ollama for AI vision analysis
- HTML files are saved using the save_html_service
- Screenshot functionality is implemented in screenshot_service.py
- All AI prompts are defined in the prompts directory