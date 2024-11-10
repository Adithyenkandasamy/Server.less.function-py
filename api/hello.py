# api/hello.py

def handler(request):
    # Get the 'name' query parameter, or default to 'World' if not provided
    name = request.get("query", {}).get("name", "World")
    
    return {
        "statusCode": 200,
        "body": f"Hello, {name}!"
    }
