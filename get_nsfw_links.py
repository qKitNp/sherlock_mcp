import sys
import json
import os
import time
import re
from io import StringIO

def get_nsfw_links_from_sherlock(username=None):
    if username is None and len(sys.argv) > 1:
        username = ' '.join(sys.argv[1:])
    elif username is None:
        return {"error": "No username provided"}
    
    # Import sherlock here to avoid circular imports
    import sherlock_project.sherlock as sherlock
    
    # Save the original sys.argv and redirect stdout
    original_argv = sys.argv.copy()
    original_stdout = sys.stdout
    
    try:
        # Set up sys.argv for sherlock with --print-found and --no-color to only show found accounts in memory
        sys.argv = [sys.argv[0], username, "--print-found", "--nsfw"]
        
        # Capture the output
        output_buffer = StringIO()
        sys.stdout = output_buffer
        
        # Run sherlock
        sherlock.main()
        
        # Get the output and clean it up
        output = output_buffer.getvalue()
        
        # Parse the output to extract site names and URLs
        results = []
        for line in output.split('\n'):
            line = line.strip()
            if not line or line.startswith('[') and 'Checking username' in line:
                continue
                
            # Extract site name and URL from lines like: "[+] Site: https://example.com/user"
            match = re.match(r'\[\+\]\s+(.+?):\s+(https?://\S+)', line)
            if match:
                site_name = match.group(1)
                url = match.group(2)
                results.append({
                    "site": site_name,
                    "url": url
                })
        
        return {
            "username": username,
            "results": results,
            "count": len(results)
        }
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Clean up
        sys.argv = original_argv
        sys.stdout = original_stdout
        
        # Clean up any temporary files that might have been created
        for ext in ['.csv', '.txt', '.json']:
            file_path = f"{username}{ext}"
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except:
                    pass

if __name__ == "__main__":
    start_time = time.time()
    username = input("Enter username: ")
    print(get_nsfw_links_from_sherlock(f"{username}"))
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
