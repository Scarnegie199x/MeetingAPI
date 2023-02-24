# MeetingAPI

A project management tool that logs meetings and creates an API endpoint. Each meeting is broken down into topics, time spent per topic and who attended the meeting.


#### Models 

The Meeting model is as follows:

- Title
- Topic(s)
- Created by <user>
- Time started
- Time finished

The Topic model is as follows:
 
 - Title
 - Issue
 - Resolution
 - Time started
 - Time finished
 - Time Updated
 - Attachments
 
 With this data you can search for which topis are being talked about the most, how long was spent on it and if the same problems are coming up.
 
 ### API
 
 The API endpoint has been constructed in the JSON format and has all the information on a single call. 
