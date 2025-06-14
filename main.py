from fastmcp import FastMCP
from get_links import get_links_from_sherlock
from get_nsfw_links import get_nsfw_links_from_sherlock

mcp = FastMCP("Sherlock MCP")

@mcp.tool   
def get_links(username: str) -> dict:
    """Search for a username across multiple social media platforms using Sherlock.
    
    Args:
        username (str): The username to search for across social media platforms.
        
    Returns:
        str: A JSON string containing a list of dictionaries with 'site' and 'url' keys
             for each platform where the username was found.
             Returns an error message if no username is provided.
             
    Example:
        >>> get_links("testuser")
        '[{"site": "GitHub", "url": "https://github.com/testuser"}, ...]'
    """
    return get_links_from_sherlock(username)

@mcp.tool

def get_nsfw_links(username: str) -> dict:
    """Search for a username across multiple social media platforms using Sherlock.
    
    Args:
        username (str): The username to search for across social media platforms including NSFW platforms.
        
    Returns:
        str: A JSON string containing a list of dictionaries with 'site' and 'url' keys
             for each platform where the username was found.
             Returns an error message if no username is provided.
             
    Example:
        >>> get_nsfw_links("testuser")
        '[{"site": "GitHub", "url": "https://github.com/testuser"}, ...]'
    """
    return get_nsfw_links_from_sherlock(username)

if __name__ == "__main__":
    mcp.run()
