import base64
import hashlib
import os

def generate_state():
    state = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')
    return state

def generate_pkce_pair():
    code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')
    code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode('utf-8')).digest()).decode('utf-8').rstrip('=')
    return code_verifier, code_challenge