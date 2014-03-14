BirthDayScript
==============

This script is helpful in automatically commenting "thank you" messages for your friend's wall-posts on your birth day. 
# Note:
This script is still in the beta stage, so I've not yet added options to dynamically change your response based on the person to which the reply is sent. For example, your teachers and your friends are bound to get similar comments, so watch out!

# Instructions:

1. Install Python 2.7 on your machine
	
  #####$sudo apt-get install python

2. Dowload the .zip or .tar.gz package. Extract it. 
3. Open the *bday.py* file on your editor. 
4. On Line 9, you have to give your access token provided by FB. 
5. Getting an Access Token from Facebook involves these steps:
    * Head to this link [Fb Dev tools](https://developers.facebook.com/tools/explorer)
    * Select __Graph API Explorer__ and then click on __Get Access Token__
    * Select these options: publish_ actions , publish_ stream , read_ stream , status_ update and user_ about_me in the pop-up window
    * And then click on Get Access Token again and voila, you're done
    * Copy the access token and paste it on Line 7 in place of <Your_ Access_ Token>
    * Your access token expires every 1 hour 
6. Save the *bday.py* file and exit from editor.
7. Open up a terminal window and navigate to the directory where bday.py file is present.
8. To run it,
    
  #####$python bday.py
9. And you're done! I've attached screenshots of how it looks when all goes well. Check out!
10. Press Ctrl + Z to stop posting when you'd like the script to stop commenting.

 
#Word of caution!
  *Best time to run the script is at the end of the day, on your birth day when you have a great number of posts.
  
  *Currently there's no end condition for the script, so you have to choose wisely about how to end the script.
  
  *All modifications and updates are welcome.
  
#Resources:
  *[Pradeep Nayak](http://pradeepnayak.in/technology/2012/08/13/programatically-responding-to-your-bday-wishes-on-facebook/) 
  
  *[Quora- Akshit Khurana](http://www.quora.com/Python-programming-language-1/What-are-the-best-Python-scripts-youve-ever-written)
