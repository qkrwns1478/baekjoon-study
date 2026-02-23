import base64
code = "YXJyID0gbGlzdChtYXAoaW50LCBpbnB1dCgpLnNwbGl0KCkpKQphcnIuc29ydCgpCnByaW50KGFyclsxXSk="
exec(base64.b64decode(code.encode('ascii')).decode('UTF-8'))