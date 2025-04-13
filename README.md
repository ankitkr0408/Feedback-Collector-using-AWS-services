# Serverless Feedback Collection System using AWS

A lightweight, serverless web application that collects user feedback in real-time using AWS services — without any backend server. Ideal for college mini-projects, feedback systems, and AWS practice.

---

## 📌 Project Overview

This project uses a fully serverless architecture with AWS to accept and store user feedback through a static web form. It eliminates the need for traditional server hosting or complex backend configurations.

---

## 🎯 Objective

Build a feedback collection system using the following AWS services:

- Amazon S3
- API Gateway
- AWS Lambda
- DynamoDB

---

## 🧩 Problem Statement

Traditional feedback systems require managing infrastructure like servers and databases. This adds cost, maintenance, and complexity.

This project simplifies that using serverless services — reducing effort while improving scalability and ease of deployment.

---

## ✅ Key Features

- **100% Serverless** – No servers to manage
- **Cost-Efficient** – Pay only for usage
- **Real-Time Storage** – Immediate data capture via DynamoDB
- **Frontend Hosted on S3** – Easy static web hosting
- **Secure and Scalable**
- **Monitoring via CloudWatch Logs**

---

## 🔧 AWS Services Used and 🧱 Tech Stack


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

1. User opens the HTML feedback form hosted on **Amazon S3**
2. On submission, form sends a **POST** request to **API Gateway**
3. API Gateway triggers a **Lambda function**
4. Lambda processes the feedback and stores it in **DynamoDB**

---

## 🚀 Implementation Steps

### 1. Create DynamoDB Table

- **Table Name**: `Feedback`
- **Primary Key**: `id` (String)

### 2. Lambda Function

- Parses JSON input from API Gateway
- Generates a unique ID and timestamp
- Writes data to DynamoDB

### 3. Configure API Gateway

- **Route**: `POST /submitFeedback`
- Integration: Linked to Lambda
- Enable **CORS** for frontend access

### 4. Upload Frontend to S3

- Upload `index.html`
- Enable **Static Website Hosting**
- Form uses `fetch()` to send data to the API Gateway URL

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for more info.
