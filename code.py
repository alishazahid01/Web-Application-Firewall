# Web application firewall using Flask
import re 
from flask import request, Flask, abort

app = Flask(__name__)

#  Check SQl injections
def check_sql_injections(sql_injection_patterns):
     # Check for SQL injection
    for pattern in sql_injection_patterns:
        try:
            if re.search(pattern, request.path, re.IGNORECASE) or re.search(pattern, str(request.data), re.IGNORECASE):
              return True  
        
        except:
            return False
    

# Check xss pattern
def check_xss_pattern(xss_pattern):
     # Check for SQL injection
    for pattern in sql_injection_patterns:
        try:
            if re.search(xss_pattern, str(request.data), re.IGNORECASE):
              return True
        except:
            return False
    
# Creating Firewall
@app.before_request
def firewall(sql_injections_patterns,xss_pattern):
    sql_injection = check_sql_injections(sql_injection_patterns)
    xss = check_xss_pattern(xss_pattern)

    if sql_injection or xss:
        # Reject the request with HTTP 403 Forbidden status code
        abort(403)
    else:
        print("HURRAY.... No signatures found :)")

# Example route
@app.route('www.google.com', methods=['POST'])
def example_route():
    # Handle the request
    return 'Success'

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
