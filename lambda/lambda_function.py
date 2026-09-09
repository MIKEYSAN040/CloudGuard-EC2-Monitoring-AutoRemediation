import json
import boto3

ec2 = boto3.client("ec2")


def lambda_handler(event, context):
    """
    Auto-remediation Lambda Function

    Triggered by Amazon CloudWatch Alarm.
    Reboots the specified EC2 instance when CPU utilization exceeds
    the configured threshold.
    """

    INSTANCE_ID = "i-09f993bd5be3d655d"   # cloudguard-dev

    print(f"Auto-remediation triggered for {INSTANCE_ID}")

    try:
        ec2.reboot_instances(
            InstanceIds=[INSTANCE_ID]
        )

        print("EC2 reboot initiated successfully")

        return {
            "statusCode": 200,
            "message": f"Reboot initiated for {INSTANCE_ID}"
        }

    except Exception as e:

        print(f"Error: {str(e)}")

        return {
            "statusCode": 500,
            "message": str(e)
        }
