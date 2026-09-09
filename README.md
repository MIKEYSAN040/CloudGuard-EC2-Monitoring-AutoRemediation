# Project Setup & Implementation

## Overview

To build a cloud-native monitoring and automated remediation solution, two Amazon EC2 instances were provisioned to represent separate environments:

- Development Environment
- Production Environment

Amazon CloudWatch Agent was configured on both servers to publish operating system metrics into a custom CloudWatch namespace. A CloudWatch Alarm was then configured to monitor CPU utilization and automatically invoke an AWS Lambda function capable of rebooting an affected EC2 instance when predefined thresholds were exceeded.

This implementation demonstrates how AWS native services can be integrated to create a self-healing infrastructure capable of reducing manual operational effort.

---

## 1. EC2 Infrastructure Provisioned

Two Linux EC2 instances were launched to simulate Development and Production workloads.

![EC2 Instances](Implementation/01-ec2-instances-created.png)

The environments provide isolated workloads that can be monitored independently.

---

## 2. Development Server Verification

The Development EC2 instance was accessed using SSH to verify connectivity and confirm the operating system before configuration began.

![Development Server](Implementation/02-dev-instance-verification.png)

This ensured the instance was reachable and ready for monitoring agent installation.

---

## 3. Production Server Verification

The Production EC2 instance was verified using the same process to ensure both environments were operational.

![Production Server](Implementation/03-prod-instance-verification.png)

Having identical environments helps simulate real enterprise deployments.

---

## 4. CloudWatch Agent Installation

Amazon CloudWatch Agent was installed and configured on both EC2 instances.

![CloudWatch Agent Installation](Implementation/04-cloudwatch-agent-installation.png)

The agent enables operating system metrics such as CPU utilization, memory usage, and disk statistics to be published into Amazon CloudWatch.

---

## 5. CloudWatch Agent Running Successfully

After installation, the CloudWatch Agent service was started and verified.

![Agent Running](Implementation/05-cloudwatch-agent-running.png)

Successful service execution confirmed that the monitoring agent was actively collecting metrics.

---

## 6. Custom Metrics Published

After the agent started successfully, custom EC2 metrics appeared under the CloudGuard namespace inside Amazon CloudWatch.

![Custom Metrics](Implementation/06-custom-metrics-visible.png)

This verified that metric collection from the operating system was functioning correctly.

---

## 7. CloudWatch Metrics Dashboard

The custom metrics were visualized through the CloudWatch Metrics dashboard.

![Dashboard](Implementation/07-cloudwatch-dashboard.png)

The dashboard provided real-time visibility into CPU utilization for both Development and Production servers.

---

## 8. CloudWatch Alarm Created

A CloudWatch Alarm was configured to continuously monitor CPU User Utilization.

![Alarm Created](Implementation/08-cloudwatch-alarm-created.png)

Whenever CPU utilization exceeds the configured threshold, CloudWatch transitions the alarm into the **ALARM** state.

---

## 9. SNS Notification Configuration

Amazon SNS was configured as the notification service for CloudWatch alarms.

![SNS Topic](Implementation/09-sns-topic-created.png)

This enables operations teams to receive immediate alerts whenever monitored resources experience abnormal behavior.

---

## 10. Email Subscription Confirmed

The email subscription associated with the SNS topic was confirmed successfully.

![SNS Subscription](Implementation/10-email-subscription-confirmed.png)

This completed the notification pipeline from CloudWatch to administrators.

---

## 11. AWS Lambda Function Created

An AWS Lambda function was created to perform automatic remediation.

![Lambda Created](Implementation/11-lambda-created.png)

Instead of requiring manual intervention, Lambda can automatically execute corrective actions whenever CloudWatch detects an incident.

---

## 12. Lambda Auto-Remediation Logic

The Lambda function was implemented using Python and AWS Boto3.

![Lambda Code](Implementation/12-lambda-code.png)

The function performs the following tasks:

- Receives an EC2 Instance ID
- Connects to Amazon EC2 using Boto3
- Initiates an EC2 reboot operation
- Logs the execution outcome

This allows infrastructure recovery to occur automatically without requiring administrator intervention.

---

## 13. CloudWatch Alarm Action Configuration

The CloudWatch Alarm was configured to invoke the Lambda function whenever the alarm entered the **ALARM** state.

![Alarm Actions](Implementation/14-cloudwatch-alarm-actions.png)

This established the event-driven integration between CloudWatch and Lambda.

---

## 14. Automated Self-Healing Workflow

The complete monitoring workflow was successfully integrated.

![Workflow](Implementation/15-auto-remediation-workflow.png)


## 15. Completed Project Architecture

The final implementation demonstrates a complete AWS monitoring and automated remediation solution.

![Final Architecture](Implementation/16-final-project-overview.png)

The solution combines multiple AWS services into an event-driven architecture capable of:

- Continuous infrastructure monitoring
- Real-time metric collection
- Automated alert generation
- Serverless remediation
- Reduced operational response time
- Improved infrastructure availability

---

## AWS Services Used

- Amazon EC2
- Amazon CloudWatch
- Amazon CloudWatch Agent
- Amazon SNS
- AWS Lambda
- AWS IAM
- Amazon VPC

---

## Skills Demonstrated

- Amazon EC2 Administration
- Linux Server Management
- CloudWatch Monitoring
- CloudWatch Agent Configuration
- CloudWatch Alarm Configuration
- AWS Lambda Development
- Amazon SNS Notifications
- IAM Role Management
- Infrastructure Monitoring
- Event-Driven Architecture
- Automated Remediation
- Root Cause Analysis
- Cloud Operations
