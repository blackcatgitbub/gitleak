# Dummy app with example secrets for testing gitleaks
# this is for testing purposes only

API_KEY = "sk_live_4eXampl3SkrYt3xAmpl3S3cr3tKey"
AWS_ACCESS_KEY_ID = "AKIAEXAMPLEACCESSKEY00"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "SuperSecretPass123!"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example.signature"

def main():
    print("App starting")
    # pretend to use secrets
    print("Using API_KEY:", API_KEY[:6] + "...")
    print("Using DB host with password", DB_PASSWORD[:3] + "...")

if __name__ == "__main__":
    main()