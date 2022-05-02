import re

raw = '180.179.174.219 - - [17/May/2015:20:05:14 +0000] "GET /downloads/product_2 HTTP/1.1" 404 333 "-" "Debian APT-HTTP/1.3 (0.9.7.9)'
remote_addr = re.compile(r'(\d{1,}\.){2}\d{1,}\.\d{1,}')
request_datetime = re.compile(r'\d{2}[/]\w{2,}[/]\d{4}[:](\d{2}[:]){2}\d{2}\s[+]\d{4}')
request_type = re.compile(r'[A-Z]{3}')
requested_resource = re.compile(r'\w+[/]\w+[_]\d')
response_code = re.compile(r'\s\d{1,}')

adr = remote_addr.match(raw)[0]
datetime = request_datetime.search(raw)[0]
type = request_type.search(raw)[0]
resource = requested_resource.search(raw)[0]
code_size = response_code.findall(raw)
code = str(code_size[0])[1:]
size = str(code_size[1])[1:]

parsed_raw = (adr, datetime, type, resource, code, size)
print(parsed_raw)
