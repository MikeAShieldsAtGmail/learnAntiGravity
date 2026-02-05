from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("weather")

# Define a tool that the agent can use
@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city.
    
    Args:
        city: The name of the city to get weather for.
    """
    # In a real app, you would call an external API here (e.g., OpenWeatherMap)
    # For this masterclass demo, we return mock data.
    return f"The weather in {city} is currently sunny and 72°F with specific humidity of 45%."

@mcp.tool()
def get_forecast(days: int = 3) -> str:
    """Get the forecast for the next few days."""
    return f"Forecast for the next {days} days: Sunny, Cloudy, Sunny."

if __name__ == "__main__":
    # This runs the server over stdio for the agent to connect to
    mcp.run()
