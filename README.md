# 📬 Serverless Feedback Collection System using AWS

## 📌 Project Overview

This project is a mini cloud-based feedback system built using **AWS services** including **S3, API Gateway, Lambda**, and **DynamoDB**. Users can fill out a feedback form hosted on a static website, and the data is processed and stored without any backend server setup — using fully **serverless architecture**.

---

## 🚀 Features

- 📄 HTML form hosted via **Amazon S3**
- 🔗 Submits data through **API Gateway**
- ⚙️ Feedback processed by **AWS Lambda**
- 💾 Data saved in **DynamoDB**
- 📋 Logs managed by **CloudWatch**
- 📧 *(Future Scope)*: Email notifications using **AWS SES**

---

## 🧱 Tech Stack

| Component     | Service/Tech               |
|---------------|----------------------------|
| Frontend UI   | HTML, CSS, JavaScript      |
| Hosting       | Amazon S3 (static website) |
| API           | AWS API Gateway            |
| Backend Logic | AWS Lambda (Python)        |
| Database      | Amazon DynamoDB            |
| Logging       | CloudWatch                 |
| IAM Roles     | For permissions setup      |

---

## ⚙️ How It Works

1. User fills the form → `index.html`
2. `fetch()` sends POST request to API Gateway
3. API Gateway routes request to Lambda
4. Lambda parses and stores data into DynamoDB
5. (Future) Lambda can also send email via AWS SES

---

## 💻 Setup Guide with AWS Console/CLI

### 1. 🧾 Create DynamoDB Table

- Table name: `Feedback`
- Partition key: `id` (String)

OR using CLI:

```bash
aws dynamodb create-table \
  --table-name Feedback \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
