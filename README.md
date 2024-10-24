# Cruiseship Route Switch GUI
- Simple desktop app that facilitates automatic route switching on a network switch based off a GPS signal

### Features
- Simple config, allowing the creation of an infinent number of 'rules' defining when to switch routes

### Purpose
- Wrote this when I worked on the IT team on a cruise ship, staff used this software to automatically switch the master switch's routes when the ship left port and required a different network destination to be set

### How
- Uses local GPS connection for postion data
- Telnets into switch in order to remove old route and add new route 
