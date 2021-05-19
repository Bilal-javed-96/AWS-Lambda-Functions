# AWS-Lambda-Functions

## 1) Lambda_Function_To_Automatically_Delete_AWS_EC2_Instances

### Steps to configure this Lambda Function

This Lambda Function is use to delete all running and stopped EC2 instances in AWS. Following steps can be performed to configure lambda function.

1. Create a Lambda function (Python)
2. Copy the code
3. Set timeout setting of lambda function to 15 seconds
4. create a cloud watch Event trigger so it can be triggered periodically (i have configure it to be executed after every 3 hours with cron expression  
5. cron expression for this will be (* 0/3 * * ? *)))
6. you are good to go.
