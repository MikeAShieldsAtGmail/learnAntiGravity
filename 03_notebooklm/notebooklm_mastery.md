# NotebookLM Mastery

In this module, we explore how to leverage **NotebookLM**—Google's AI-powered research assistant—alongside your AntiGravity agent.

## Core Concepts

1.  **Source Grounding**: NotebookLM is grounded in the documents you upload.
2.  **Audio Overview**: It can generate a podcast-style conversation about your sources.
3.  **MCP Integration**: By connecting an MCP server (like the Weather server we built), you can potentially feed live data into your notebook context (depending on the specific integration available in the masterclass).

## Integration Steps

To use the code we generated with NotebookLM:

1.  **Upload Sources**:
    - Go to [NotebookLM](https://notebooklm.google.com/).
    - Create a new notebook.
    - Upload the `03_mcp_masterclass/weather_server.py` file.
    - Upload the `02_gorgeous_website/index.html` file.

2.  **Ask Questions**:
    - "Explain how the weather server uses the FastMCP library."
    - "Suggest improvements for the glassmorphism CSS in the website."

3.  **Generate Audio**:
    - Click "Generate" in the Audio Overview section to hear a discussion about your code architecture.

## Advanced: The MCP Connection

In the masterclass, we discuss how agents can "read" from NotebookLM or "write" to it via APIs/MCP. While NotebookLM is primarily a web interface, using it to *understand* your codebase is a powerful agentic pattern.

*Note: As of now, direct API access to NotebookLM is limited, so this workflow is primarily manual but highly effective for learning.*
