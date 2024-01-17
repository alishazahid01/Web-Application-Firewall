Web Application Firewall using Flask Documentation
Introduction

The "Web Application Firewall using Flask" is a Python script that implements a basic web application firewall (WAF) to protect a Flask-based web application from common security threats such as SQL injection and cross-site scripting (XSS) attacks. This documentation provides an overview of the code structure, usage, and functionality of the WAF.
Getting Started

To use the "Web Application Firewall using Flask" script, follow these steps:

    Install Flask and any other dependencies by running the following command:

    bash

pip install Flask

Clone or download this repository to your local machine.

Open the Python script in your preferred code editor or integrated development environment (IDE).

Execute the script using the following command:


    python waf.py

    The Flask web server will start, and the WAF will be active. It will protect the defined routes from SQL injection and XSS attacks.

Code Structure

The "Web Application Firewall using Flask" script consists of the following components:
1. check_sql_injections Function


# Check SQL injections
def check_sql_injections(sql_injection_patterns):
     # Check for SQL injection
    for pattern in sql_injection_patterns:
        try:
            if re.search(pattern, request.path, re.IGNORECASE) or re.search(pattern, str(request.data), re.IGNORECASE):
              return True  
        
        except:
            return False

This function checks for SQL injection patterns in the request path and data. It returns True if any SQL injection pattern is found; otherwise, it returns False.
2. check_xss_pattern Function


# Check XSS pattern
def check_xss_pattern(xss_pattern):
     # Check for XSS pattern
    for pattern in sql_injection_patterns:
        try:
            if re.search(xss_pattern, str(request.data), re.IGNORECASE):
              return True
        except:
            return False

This function checks for XSS patterns in the request data. It returns True if any XSS pattern is found; otherwise, it returns False.
3. firewall Function


# Creating Firewall
@app.before_request
def firewall(sql_injections_patterns, xss_pattern):
    sql_injection = check_sql_injections(sql_injection_patterns)
    xss = check_xss_pattern(xss_pattern)

    if sql_injection or xss:
        # Reject the request with HTTP 403 Forbidden status code
        abort(403)
    else:
        print("HURRAY.... No signatures found :)")

This function serves as the main WAF logic. It runs before each incoming request and checks for SQL injection and XSS patterns using the previously defined functions. If any pattern is found, it aborts the request with a 403 Forbidden status code.
4. Example Route


# Example route
@app.route('/example', methods=['POST'])
def example_route():
    # Handle the request
    return 'Success'

This is an example Flask route protected by the WAF. Requests to this route will be checked for security threats by the WAF before being processed.
5. Main Execution Block

if __name__ == "__main__":
    # SQL injection patterns 
    sql_injection_patterns = [
        r'\bSELECT\b.*\bFROM\b',
        r'\bINSERT\b.*\bINTO\b',
        r'\bUPDATE\b.*\bSET\b',
        r'\bDELETE\b.*\bFROM\b']
    
    # XSS pattern
    xss_pattern = r'<script>|<\/script>|<script\s*>|<\/script\s*>|<script\s+type=["\']text\/javascript["\']>|<\/script\s*>|<\s*img\s+src=["\'][^"\']+["\']\s*\/?>|<\s*input\s+type=["\']hidden["\']\s+name=["\'][^"\']+["\']\s+value=["\'][^"\']+["\']\s*\/?>|<\s*a\s+href=["\'][^"\']+["\']\s*>|<\s*iframe\s+src=["\'][^"\']+["\']\s*\/?>|<\s*body\s+onload=["\'].*["\']\s*>'
    
    app.run(debug=True)

The main execution block defines the SQL injection patterns and XSS pattern to be checked by the WAF. It also starts the Flask web server in debug mode.
Usage

    Run the Python script as described in the "Getting Started" section.

    The Flask web server will start, and the WAF will be active.

    Access the protected routes of your Flask application (e.g., /example) through a web browser or API requests.

    The WAF will automatically check incoming requests for SQL injection and XSS patterns.

    If a request contains security threats, it will be rejected with a 403 Forbidden status code.

    Review the console output for information on detected threats or successful requests.

Conclusion

The "Web Application Firewall using Flask" script provides basic security protection for a Flask-based web application by identifying and blocking common security threats. By implementing this WAF, you can enhance the security of your web application and protect it from malicious attacks
