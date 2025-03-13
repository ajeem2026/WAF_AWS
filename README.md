# Deploying AWS WAF for Web Security

## Introduction

AWS WAF (Web Application Firewall) is a managed service that provides fine-grained control over HTTP/HTTPS requests reaching AWS resources. It allows users to define security rules to protect web applications without the need for additional software.

### **Why AWS WAF?**
AWS WAF integrates with key AWS services to enhance security:
- **Application Load Balancers (ALBs)**
- **Amazon CloudFront (Content Delivery Network)**
- **Amazon API Gateway (API Management Service)**
- **AWS AppSync (GraphQL Service)**
- **Amazon Cognito (Identity and Access Management Service)**
- **Amazon ECS (Elastic Container Service)**

### **AWS WAF Components**
AWS WAF operates on three primary components:
1. **Web Access Control Lists (ACLs):** Collections of rules that define security behavior.
2. **Rules:** Statements that inspect requests and specify actions.
3. **Rule Groups:** Reusable rule sets, both managed by AWS and custom.

---

## **Step 1: Creating a Web ACL**

1. Navigate to AWS WAF service and click **Create Web ACL**.
2. Name the ACL **first_rules** and configure the **CloudWatch metric name**.
3. Attach the ACL to your **CloudFront distribution**.

![Web ACL Creation](images/screenshot1.png)

---

## **Step 2: Creating Rules**

1. Click **Add Rules** → **Add Managed Rule Groups**.
2. Browse **AWS Managed Rule Groups** to find pre-configured security policies.
3. Select **Amazon Reputation IP List** and click **Add to Web ACL**.
4. The rule now appears in the managed rule list, consuming **25/5000 WEBACL units**.

![Adding Rules](images/screenshot2.png)

---

## **Step 3: Configuring Rules**

1. Set **Default Web ACL Action** to **Allow requests that don’t match any rules**.
2. (Optional) Add custom headers prefixed with `x-amzn-waf-`.
3. Enable **CAPTCHA verification** for suspected bot traffic.
4. Configure a **Token Domain List** to prevent re-verification when users navigate across applications.

![Rule Configuration](images/screenshot3.png)

---

## **Step 4: Setting Rule Priorities**

1. Ensure that critical rules have higher priority.
2. Rules are evaluated top-down, so incorrect priority may lead to security misconfigurations.

![Setting Rule Priorities](images/screenshot4.png)

---

## **Step 5: Configuring CloudWatch Metrics**

### **What is CloudWatch?**
AWS CloudWatch is a monitoring and observability service for AWS resources.
- Default settings suffice for basic monitoring.
- Enables logging for security analysis.

![CloudWatch Configuration](images/screenshot5.png)

---

## **Step 6: Review & Deploy**

1. Review configurations and click **Create Web ACL**.
2. AWS WAF now begins filtering requests based on defined rules.

![Final Web ACL](images/screenshot6.png)

---

## **Monitoring Web ACLs**

1. Navigate to **AWS WAF > Web ACLs > first_rules**.
2. Under the **Rules tab**, select **Amazon Reputation IP List**.
3. AWS WAF documentation provides additional rule explanations. ([AWS IP Reputation Rule Group](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-ip-rep.html))

### **Understanding "Count" in AWS WAF**
- "Count" mode logs requests without blocking them.
- Useful for analyzing traffic before enabling full blocking.
- Rule priority affects how requests are counted or blocked.

![Monitoring Web ACL](images/screenshot7.png)

---

## **Additional Features of AWS WAF**
- **BOT Control:** Detects and mitigates bot traffic.
- **Application Integration SDKs:** Provides additional user telemetry.
- **IP Sets & Regex Pattern Sets:** Enables custom filtering.
- **OWASP Top 10 Add-On Protections:** Addresses common security vulnerabilities.

---

## **Conclusion**
By implementing AWS WAF, we have:
- Secured our CloudFront distribution.
- Applied managed rule groups to mitigate threats.
- Configured logging and monitoring via CloudWatch.

This project demonstrates my expertise in AWS security configurations, application protection, and cloud-based threat mitigation.
