## SAPtivity

# Running the tool
This funtion is not complete yet but stay tuned. 

SAP Hackathon

## Inspiration
We were inspired by the lack of tool that helps people track productivity and fitness. There are a lot of apps that track productid however you have to manually put your activities. In addition, these apps only track one thing at a time. So, the question for us was: how can we bring physical activities(location) and digital activities (desktop) and track your activity and give you matrix of how much time you spent on each. 

What we did with SAPtivity is that it tracks your activity based on your location, desktop activity and and Outlook calendar and gives you activity log chart.

## What it does
It does three main things.
1.	Tracks your activity and gives chart of how much time you spent on each. 
        With SAPtivity, you don’t have to manually put your activities in the app. It gets your activity data in three main 
        ways and presents productivity chart on daily, weekly and monthly bases. 
•	Based on your location: For a given mapped building, the app tracks your locations and the time you spend in 
        those locations and maps it to different activities. For instance, if you are at the gym for 40 minutes it registers as 
       ‘exercise’, if you spend an hour in a meeting room it registers as meeting. We use longitude, latitude and altitude 
        to get your exact location. 
•	Based on the application you want to track on your desktop: the app also gets data form the apps you want to 
         track on your desktop and gives you chart of how much time you spend doing different tasks. 
•	Outlook calendar: it also uses LP algorisms to track what kind of meeting activities you do. 

2.	Tracks your fitness goal. 
       You set a goal of how many steps you would like to take daily and SAPtivity reports your progress daily, weekly 
        and monthly. 

3.	Make to do-list daily, weekly and monthly and check them off as you get them done.

       The combination of feature 1 and 3 will help you evaluate your progress because you can compare your goal and 
        the amount of time you spent on different activities. 

## How we built it

We chose React Native for the front end so we can have a one code base and deploy it to different platforms. For the back end we used Flask API because it easy to send data back and forth.
We manually hard coded the location (longitude, latitude and altitude) of various rooms on the first floor of SAP building. We store the name, co-ordinate points and radius of these roomss. To find the radius, we took two co-ordinate points (one in the center and one at the end of the room) and used the Pythagorean formula to the radius. 
The algorithm to find a location of a person is as follows
a.	Find which floor the person is using its altitude value.
b.	For each mapped room, find the distance between the persons location and the center of the room
c.	Find the minimum distance. 
d.	Check if the person is within the range of the radius of the room
e.	Return the closest room
f.	If there is a change in the location then update the time stamp. 

## Challenges we ran into
•	The sensor wasn’t very accurate and wasn’t updating as fast as we needed

## Accomplishments that we're proud of
•	We are proud the algorithm we built to accuratly locate a person in the building. 
•	We are proud of the UI we built. 

## What we learned
We learnt how to work in team and make the most of different skills. 

## What's next for SAPtivity 
It need more efficient in grabbing locations
It need improved algorithms to connect all the sources of activities. 



 

