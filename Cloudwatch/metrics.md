# CloudWatch Custom Metrics

The Amazon CloudWatch Agent publishes operating system metrics from the EC2 instance into the custom namespace **CloudGuard**.

## Metrics Collected

 Metric | Description 

 cpu_usage_user - Percentage of CPU used by user processes 
 cpu_usage_system - Percentage of CPU consumed by kernel processes 
 cpu_usage_idle - Percentage of idle CPU time 

These metrics are collected every 60 seconds and are used to monitor instance health and trigger automated remediation when predefined thresholds are exceeded.
