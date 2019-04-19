## Custom S3 Prefixes and Kinesis Data Firehose Blog

Sample code for blog - Custom S3 Prefixes and Kinesis Data Firehose

Prerequisites

    Amazon Web Services account
    [AWS Command Line Interface (CLI)]
    Python
    boto3

Overview of Example

This blog post is intended to illustrate how streaming data can be written into S3 using Kinesis Data Firehose using a Hive compatible folder structure. We show how AWS Glue crawlers can infer the schema and extract the proper partition names we designate in Kinesis Data Firehose and catalog them in AWS Glue Data Catalog.  We finish up by executing sample queries to show that partitions are indeed being honored.  To demonstrate this we use a Lambda function to generate sample data.  We also use a Lambda transform on Kinesis Data Firehose to forcibly create failures demonstrating how data can be saved to the Error Output location. Remember to substitute the "account-id" in the json files for your own.

## License Summary

This sample code is made available under a modified MIT license. See the LICENSE file.
