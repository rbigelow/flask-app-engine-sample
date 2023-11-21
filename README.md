# Sample GCP app engine flask application

This is a sample flask application using GCP app engine. 
To deploy this application complete the following steps..

1. Sign into GCP console and if you haven't already create a project. 

2. You will need to create a billing profile for the project (May require credit card)

3. Install the gcloud command line tool. (https://cloud.google.com/sdk/docs/install)

4. Once installed run the following to initalize the command line tool 
       >. gcloud init

5. Upload and deploy the application to app engine 
       >. gcloud app deploy

6. To view logs for troubleshooting. 
       >. gcloud app logs tail -s default   

