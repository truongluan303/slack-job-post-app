JOB = "https://www.linkedin.com/jobs/view/3092250691/?alternateChannel=search&refId=PvqH9SOvs6v2PFBTB98eIg%3D%3D&trackingId=%2B2QJwFVKSfhjk18pSV2lrA%3D%3D"
from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    USER_TOKEN,
    USER_SECRET,
    RETURN_URL,
    linkedin.PERMISSIONS.enums.values(),
)

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

application.get_profile()
