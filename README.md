# EZ_Assignment
File system heirarachy
   app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── db.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── file.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── file.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── ops.py
│   │   └── client.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   └── dependencies.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── encryption.py
│   │   ├── file_utils.py
│   │   └── hash.py
│   │
│   ├── email_utils/
│   │   ├── __init__.py
│   │   └── smtp.py
│   │
│   └── db_init.py       
│
├── tests/
│   ├── test_ops.py
│   └── test_client.py
│
├── uploads/              
├── .env                 
├── .gitignore
├── requirements.txt


TEST CASES -
1-
Test Case 1: Client User Signup

Test Case	- Signup with valid email and password
Endpoint	POST /client/signup
Request Body	

json

{
  "email": "client1@example.com",
  "password": "client123"
}
| Expected Result | Status 200 OK, message "Verification email sent" |
| Test Type | Positive |

2-
Test Case 2- Client Email Verification
Test Case	- Verify email using the encrypted token
URL Format	- GET /client/verify-email?token=<ENCRYPTED_TOKEN>
Steps	- Get token from email or logs and visit in browser
Expected Result	- Status 200 OK, message "Email verified successfully!"
Test Type	- Positive

3-
Test Case 3: Client Login Before Verification

Test Case	- Login before email is verified
Endpoint	- POST /client/login
Request Body	

json
Copy
Edit
{
  "email": "client1@example.com",
  "password": "client123"
}
| Expected Result | Status 403 Forbidden, message "Email not verified" |
| Test Type | Negative |

4-

Test Case 4: Upload Invalid File Format

Test Case	- Upload .pdf or .exe file
Endpoint	- POST /ops/upload
Expected Result	- Status 400 Bad Request, message "Only pptx, docx, xlsx allowed"
Test Type	- Negative

5-
Test Case 5: Download Using Encrypted URL

Test Case	- Access encrypted download URL as client user
URL Format	- GET /client/secure-download/<token>
Expected Result -	File downloads successfully
Test Type	- Positive


Deployment plan-
Secure File Sharing System – Deployment Guide
This project provides a secure file-sharing platform built with FastAPI, PostgreSQL, and JWT authentication, supporting two user roles: Operation and Client.

Features
JWT Auth with role-based access

Email verification for Client users

Upload (pptx/docx/xlsx) by Operation users

Secure encrypted download links for Client users

REST API architecture

Deployable with Docker + Gunicorn + Uvicorn

# Environment Variables
Create a .env file in the root:

env
Copy
Edit
DATABASE_URL=postgresql://username:password@host:port/dbname
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_password
FERNET_SECRET=generated_fernet_key
BASE_URL=http://localhost:8000

# Docker Build & Run
1. Build the Docker image:
docker build -t secure-api .
2. Run the container:
docker run -d -p 8000:8000 --env-file .env secure-api

# Cloud Deployment (Render / Railway / VPS)
Push this repo to GitHub

Use platforms like Render.com or Railway.app to:

Connect repo

Add environment variables

Use Dockerfile for image

Expose port 8000


# Optional: Email Testing
Use services like:

Mailtrap.io (for testing)

Gmail SMTP (real email)

SendGrid (recommended for production)
