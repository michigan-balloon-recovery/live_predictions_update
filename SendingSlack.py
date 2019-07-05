import os

directmessage = 1
channel = 0
recipientName = "Robby"
slackURL = <INSERTSLACKURLHERE>
icon = "ghost"
botUsername = "Python Bot"
messageText = "Hell yeah"

#curl -X POST --data-urlencode "payload={\"message\": \"Robby\", \"username\": \"PythonBot\", \"text\": \"Hello\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/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

if directmessage == 1:
    messageType = "message"
    
if channel == 1:
    messageType = "channel"

curlcommand = "curl -X POST --data-urlencode "
payloadcommand = '"payload={\\"'+messageType+'\\": \\"'+recipientName+'\\", \\"username\\": \\"' + botUsername + '\\", \\"text\\": \\"' + messageText + '\\", \\"icon_emoji\\": \\":' + icon + ':\\"}" ' + slackURL
command = curlcommand+payloadcommand
os.system(command)
