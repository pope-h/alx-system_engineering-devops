# Postmortem Report

![They never stop coming](non_stop.gif)

## Issue Summary:

Duration: The issue occurred on May 20, 2023, at around 10 AM UTC and was resolved by May 23, 2023, at approximately 12 PM UTC.
Impact: The SSH permission denied (publickey) error affected my ability to log in to web server 02. As a result, I was unable to perform checks for my ALX project "0x14-sql." The server downtime only affected me, as the website was still under development and not accessed by users.
Root Cause: The root cause of the issue was an incomplete uninstallation of MySQL version 8 on web server 02, leading to conflicts during the installation of the correct version.

## Timeline:

The issue was detected on May 20, 2023, around 10 AM UTC when I encountered the SSH permission denied (publickey) error while attempting to log in to web server 02.
I initially attempted to resolve the issue through basic methods such as restarting my Linux environment and checking other servers, but these did not succeed.
Seeking help online, including from search engines and chat platforms, provided misleading information and pointed me to contact the administrators.
I escalated the issue to mentors who confirmed the server's irreparability, resulting in the need to request a new server.
During the server restoration process from May 23-28, 2023, I encountered challenges while installing the correct version of MySQL, causing extended downtime.
The issue was ultimately resolved on May 28, 2023, when I completely removed MySQL version 8 and successfully installed the appropriate version on web server 02.

![No idea what i'm doing](no_idea.gif)

## Root Cause and Resolution:

Root Cause: The incomplete uninstallation of MySQL version 8 on web server 02 caused conflicts during the installation of the correct version.
Resolution: I resolved the issue by completely removing the remnants of MySQL version 8 and installing the correct version on web server 02.

## Corrective and Preventative Measures:

To prevent similar incidents in the future, the following measures have been implemented:
       	+ Establishing inter-server connectivity to enable login from any server, not just the working environment.
       	+ Thoroughly documenting installation steps and procedures for web servers and other installations to avoid following erroneous instructions
       	+ Ensuring comprehensive and accurate removal of software components to prevent conflicts during future installations.
       	+ Implementing proper monitoring and alerting mechanisms to detect and address issues promptly.
       	+ Conducting regular system audits and reviewing best practices for system administration and troubleshooting.

![No idea what i'm doing](no_idea.gif)
