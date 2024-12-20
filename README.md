# Caddy Chatbot HealthiAI

This is a FastAPI-based chatbot, inspired by the original [Caddy Chatbot](https://github.com/i-dot-ai/caddy-chatbot), enhanced to use AWS Bedrock and Amazon Titan Embeddings.

---

## Getting Started

### Prerequisites

- **Python 3.12 or higher**
- **AWS CLI** installed and configured
- **Make** utility (optional)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com//caddy-chatbot-healthiai.git
   cd caddy-chatbot-healthiai
2. ** Configure AWS credentials **
   aws configure
3. ** Start the fast API server **
  make run-dev
4. ** Access the API Docs **
Swagger UI: http://localhost:8080/docs
5. ** Changes from the Original **
Model: amazon.titan-embed-text-v2:0
Region: us-east-2


