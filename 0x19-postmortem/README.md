# 0x19-postmortem

Earlier this week we experienced an outage in our web server. Today we’re providing an incident report that details the nature of the outage and our response.

## issue summary:
From 3:31 to 6:02 pm EET requests to the server resulted in 500 error response messages. At its peak, the issue affected 100% of traffic to the server. The outage was caused by a typo error of one of the configuration file on our server.

## Timeline:
- 3:31 pm: The server started to respond with 500 error messages.
- 4:35 pm: The team was alerted to the issue and began investigating.
- 5:40 pm: The team identified the issue as a typo error in the configuration file.
- 6:02 pm: The typo error was corrected and the server was restored to full functionality.

## Root cause:
At 3:31 pm, a configuration change was inadvertently released to our production environment without first being released to the testing enviroment. The change contained a typo error that caused the server to respond with 500 error messages. The typo error was in the configuration file that was responsible for specifiying a key configuration file for word-press configuration.

## Resolution:
The typo error was corrected and the configuration file was updated. The server was restored to full functionality at 6:02 pm. The team is currently working on implementing a new process to ensure that configuration changes are first released to the testing environment before being released to the production environment.

## Corrective and preventative measures:
- Implement a new process to ensure that configuration changes are first released to the testing environment before being released to the production environment.
- Implement a monitoring system to alert the team to server issues as soon as they occur.
- Implement a backup system to ensure that the server can be restored to full functionality in the event of an outage.
