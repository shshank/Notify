Notify

This is a notification system for IIIT Bhubaneswar's notice board and results page.
*Only webscraping part has been completed now. I am currently working on this project*

Notice Board : http://www.intranet.iiit-bh.ac.in
Results : http://results.bput.ac.in

How::

Both the sites do not provide any public API for data access. Notify will use web scraping to get the notices and results from the respective pages. It will send an alert to the subscribers when a new notice/result is posted.

Notification will be done through email. An android app will also be provided, with cloud messaging notification.

To do::

I.	Web Scraping Module
	http://results.bput.ac.in - Gets the current result links and stores them in the datastore, under 4 courses heading.Does not store when entry already exists. Whenever an entry is made, alert is set to true and the entry is added to result_alert queue.
	
	http://intranet.iiit-bh.ac.in - Gets all the notices and stores them in the datastore. Checks the latest entry on the board with the latest entry in the datastore, if they do not match, scraps again for new entries. stores them to the datastore, whenever a new entry is made notice_alert is set to true and the new entries are added to the notice_alert queue

II.	Email Alert Module:
	Checks for alert variable.
	
	If set to true, gets the new entries from result_alert and notice_alert queues.

	Sends Results to result_subscribers. Sends notices to notice_subscribers

III. Email Subscription Module

	Registers Subscribers

	A front end for users to manage subscribtion to the alerts.
	
	If subscribed to notice, check if user exists in notice_subscriber list, if false, add to notice_subscriber. Else Inform him he is already subscribed.
	
	If subscribed to results check if user exists in results_subscriber. If true add to result_subscriber. Else Inform him user already exists.
	
	If unsubscribed from results, check if user exists, if true delete user, else inform user that he is not subscribed.
	
	If unsubscribed from notice, check if user exists, if true delete user. else inform user that he is unsubscribed.
