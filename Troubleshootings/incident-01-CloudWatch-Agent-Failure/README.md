
# Incident 01 – CloudWatch Agent Failure (Monitoring Data Loss)

## Overview

A CloudWatch monitoring failure was simulated by intentionally stopping the Amazon CloudWatch Agent on an EC2 instance. Although the EC2 instance remained healthy and accessible, it stopped publishing custom CPU utilization metrics to Amazon CloudWatch.

This incident demonstrates how a Cloud Support Engineer investigates missing monitoring data, identifies the root cause, restores the monitoring service, and validates successful recovery.

---

## 1. Monitoring Healthy (Baseline)

Before introducing the incident, the CloudWatch Agent was successfully publishing custom CPU metrics from the EC2 instance to the **CloudGuard** namespace.

![Monitoring Healthy](01-cloudwatch-metrics-working.png)

**Observation:** CPU utilization metrics were continuously being published, confirming that monitoring was functioning normally.

---

## 2. CloudWatch Agent Stopped

The Amazon CloudWatch Agent service was intentionally stopped to simulate a monitoring outage.

![Agent Stopped](02-cloudwatch-agent-stopped.png)

The service status was verified immediately after stopping the service.

![Service Status](03-cloudwatch-agent-status-inactive.png)

System logs confirmed that the CloudWatch Agent had stopped successfully.

![Agent Stop Logs](04-cloudwatch-agent-stop-logs.png)

**Observation:** The CloudWatch Agent entered an **inactive (dead)** state, preventing the EC2 instance from publishing custom metrics.

---

## 3. Monitoring Failure Observed

Initially, CloudWatch continued displaying historical metric data. After several minutes, no new CPU datapoints appeared on the graph, resulting in a visible gap.

![Metric Gap](05-cloudwatch-metric-gap.png)

As older datapoints aged out of the selected time window, CloudWatch displayed **No data available**, confirming complete loss of monitoring visibility.

![No Metrics Available](06-cloudwatch-no-data.png)

**Observation:** The EC2 instance remained operational, but CloudWatch stopped receiving new custom CPU metrics.

---

## 4. Investigation & Resolution

The CloudWatch Agent service was restarted to restore monitoring.

![Agent Restart](07-cloudwatch-agent-started.png)

The service logs were reviewed after startup to verify successful initialization.

![Recovery Logs](08-cloudwatch-agent-recovery-logs.png)

**Root Cause:** The Amazon CloudWatch Agent service had been stopped, preventing the collection and publication of custom CloudWatch metrics.

**Resolution:** The CloudWatch Agent service was restarted successfully, restoring metric collection.

---

## 5. Validation

After restarting the CloudWatch Agent, new CPU utilization datapoints began appearing in CloudWatch.

![Metrics Restored](09-cloudwatch-metrics-restored.png)

The associated CloudWatch alarm automatically returned to the **OK** state after receiving fresh metrics.

![Alarm Restored](10-cloudwatch-alarm-ok.png)

---

## Skills Demonstrated

- Amazon EC2
- Amazon CloudWatch
- Amazon CloudWatch Agent
- Linux Service Management (`systemctl`)
- Linux Log Analysis (`journalctl`)
- CloudWatch Monitoring
- Incident Troubleshooting
- Root Cause Analysis
- Monitoring Recovery
- Cloud Infrastructure Support
