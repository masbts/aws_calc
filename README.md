**AWS Lambda Functions and REST API Setup Guide**

This README.md file provides step-by-step instructions for setting up AWS Lambda functions and a REST API to perform mathematical calculations and hosting a static website to interact with these functions.

**AWS Task 3: Setting Up Lambda Functions and REST API**

1. Sign into your AWS account and access the AWS Management Console.
2. Search for "Lambda" using the research bar and navigate to the Lambda service.

**Creating Lambda Functions:**

1. Create four Lambda functions:
   - "calc_average" using Python 3.10
   - "calc_middle" using Python 3.10
   - "calc_power" using Python 3.10
   - "calc_sqr" using Python 3.10
   Confirm the creation for each.

2. Modify each function:
   - Open each function's code and replace it with the corresponding code from the provided files.
   - Create test events for each function, copying the code from "testerevent.json" file.
   - Save changes and test each function to ensure expected outputs.

**Setting Up REST API:**

1. From the research bar, navigate to the API Gateway service.

2. Create a new API named "Mycalc".

3. Create four resources for each function:
   - Use the same approach for resource naming as used for function names.

4. Customize each resource's method:
   - Configure each resource's method to be "GET".
   - Set the Lambda function to the respective function's name for each resource.

5. Customize integration request:
   - For each method, navigate to "Integration Request".
   - Click on "Mapping template" and add a mapping template of type "application/json".
   - Add the mapping filter from "application/json.json" file.
   - Save changes for each method.

**Enabling CORS:**

1. Enable CORS for each resource:
   - Access the "Actions" menu and select "Enable CORS".
   - Repeat this step for each resource.

**Deploying REST API:**

1. Deploy the API to a stage named "prod":
   - From the "Actions" menu, select "Deploy API" and choose the "prod" stage.

2. Retrieve the Invoke URL for testing:
   - The Invoke URL will be in the format: https://[API-ID].execute-api.[region].amazonaws.com/prod

3. Test the API for each function:
   - Access the URLs for each function with appropriate query parameters:
     - "calc_average": /calc_average?a=[Value]&b=[Value]&c=[Value]
     - "calc_middle": /calc_middle?a=[Value]&b=[Value]&c=[Value]
     - "calc_power": /calc_power?a=[Value]&b=[Value]&c=[Value]
     - "calc_sqr": /calc_sqr?a=[Value]&b=[Value]&c=[Value]

**Hosting Static Website on S3:**

1. Create an S3 bucket for hosting the website:
   - Choose a unique bucket name and disable "block public access" setting.
   - Create the bucket.

2. Configure bucket permissions:
   - Modify the bucket's ARN to ensure proper access.

3. Enable website hosting for the bucket:
   - In bucket properties, enable static website hosting.
   - Set the index document to your HTML file's name.

4. Upload HTML file and link API:
   - Open the HTML file and replace the API URLs with the correct Invoke URL.
   - Upload the updated HTML file to the bucket's objects.

5. Access the hosted website:
   - Visit the website using the provided S3 bucket URL to interact with the functions.

Congratulations! You have successfully set up Lambda functions, a REST API, and hosted a static website to perform mathematical calculations using AWS services.
