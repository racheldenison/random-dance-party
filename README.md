# random-dance-party
Randomly generated dance party

We're using the MacOS scheduler launchctl to automatically (each day) run a python script that will launch a web browser and play a youtube video at a randomly generated time within the hours you select. Enjoy your dance party!

How to set up launchctl:
1. Add the plist file containing the launchd script to ~/Library/LaunchAgents
2. <load> the launchctl (see below)
3. <start> the launchctl to test it
If you make changes to the plist file, you have to unload and reload.

A few more notes:
Apple provides launchctl to manage your agents. The main commands you need are
launchctl load ~/Library/LaunchAgents/org.dance-party.plist
launchctl unload ~/Library/LaunchAgents/org.dance-party.plist
launchctl start org.dance-party
launchctl stop org.dance-party
launchctl list

Notice that load and unload require the filename, while start and stop require the label. The start command will manually run the job, even if it isn’t the right time. This can be useful for testing. The stop command just kills the process, but is convenient because you don’t need to know the pid. The list command shows all loaded agents, with the pid if they are currently running and the exit code returned the last time they ran.

Adapted from: http://nathangrigg.net/2012/07/schedule-jobs-using-launchd/
