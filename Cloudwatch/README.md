# Amazon CloudWatch Monitoring

This directory contains the CloudWatch Agent configuration and alarm settings used to monitor EC2 performance.

## Components

- CloudWatch Agent
- Custom Metrics (CloudGuard Namespace)
- CloudWatch Alarm
- Lambda Trigger

## Monitoring Flow

EC2 Instance
|
V
CloudWatch Agent
|
V
Custom Metrics (CloudGuard)
|
V
CloudWatch Alarm
|
V
AWS Lambda
|
V
EC2 Auto Remediation

## Objective

Continuously monitor CPU utilization and automatically remediate high CPU incidents by invoking an AWS Lambda function.
