# csc322
Project done for Software Design Class
Ego


NoNo Web File
Software Requirements Specification
For NoNo Web File

Version 1.2

  Group Members:   Rongjun Wu
Xiaoyan Zhang
Julia Helena Aguiar

Project Git Repository
https://github.com/jhrbva/csc322



Revision History

Date
Version
Description
Author
10/22/18
1.0
Project requirements including use case diagram and high level database 
Group Members
11/10/2018

1.1
Detailed design specifications added to SRS, including several additional diagrams and descriptions of system.
Group Members




11/17/18
 1.2  
Application System Functions - Pre and Post requisites of every function in the system
Group Members
 			                                      

Table of Contents
1. Introduction	1
1.1 Purpose	1
1.2 Scope	2
1.3 Definitions, Acronyms, and Abbreviations	2
1.3.1 Definition of document sharing	3
1.4 References	3
1.5 Overview	3
2. Overall Description	3
2.1 Use-Case Model Survey	3
2.2 Assumptions and Dependencies	5
2.3 ER Diagram of System	6
3. Specific Requirements	6
3.1 Use-Case Report	6
3.1.1 Document Visibility	7
3.1.2 Document Locking	7
3.1.3 Data Modeling	7
3.2 Supplementary Requirements	8
3.2.1 Version History	8
4. Supporting Information	8
4.1 Index	8
4.2 Apendices	9
4.2.1 Appendix A - Use Case Scenarios For Each User Case	9
4.2.2 Appendix B - System Prototypes	14
4.2.3 Appendix C - Application system functions	14


Software Requirements Specification
1. Introduction
1.1 Purpose
	The purpose of this software requirement specification document is to give the most up-to-date detailed description of the NoNo Web File system, the behaviour of the application, and the different user types involved. Any functional and non-functional requirements, design constraints, and any other information regarding this product can be found in this document. Hence, this SRS is to be the primary reference for developing any further improvements on the project, or addressing any new specifications as required by the client.
1.2 Scope
The NoNo Web File is a document sharing system in which individuals working in teams can collaborate on the same documents without causing inconsistencies. The files can be viewed, edited, and saved by users depending on their type of permissions. The system also allows users to not only read current versions of documents, but also previous versions with details about which user made the changes. A security featured required by the NoNo Web File is the ability for the superuser to maintain a list of taboo words, which are to be avoided during the creation of documents. Warnings will be displayed to users who try to use the words on this list so that they can be aware of what words to avoid in order to maintain a healthy collaborative environment. 
The NoNo Web File software will be built using the programming language Python, and will be accessible by three different types of users, who will be granted different levels of permissions:
Superuser (SU) 
Ordinary User (OU)
Guest User(GU).  
The different permission levels allowed to each of these users is highlighted in section 2.1. 
1.3 Definitions, Acronyms, and Abbreviations

SRS : Software Requirement Specification
This document is denominated a Software Requirement Specification, or SRS
GU : Guest User*
A user who is not logged in and can read open files in the application but has no permission to write. The guest user can only suggest content for files.
OU : Ordinary User*
A user who is logged in and can open and close files they create. They have permission to read and write to their files and choose who they would like to share their files with.
SU: Superuser*
A System administrator who is given the highest level of permissions allowed by the system.

*Further explanation about user permissions can be found in section 2.1. 

1.3.1 Definition of document sharing

Document sharing is given when two or more people access the same document at the same time via the internet, or a piece of software. The most famous example of document sharing is Google Docs.  According to the G Suite Learning Center, “With Google Docs, you can create and edit text documents right in your web browser—no special software is required. Even better, multiple people can work at the same time, you can see people’s changes as they make them, and every change is saved automatically.” 
Our software, which will allow team members to edit documents asynchronously, will operate differently then Google Docs, in ways which are explained in greater detail throughout this document.                
1.4 References
Draw.io, online diagram builder used to develop the diagrams in this document
Google Sheets, used to build the table outline of the database which will be used in this software.
G Suite Learning Center, used for defining specifications to a rival product, Google Sheets.
1.5 Overview
	This SRS is organized by Introduction in the section 1, which gives a high level description of this SRS and software requirements, alongside some important definitions on general document sharing software and their expected functionality.
Section 2 contains the users overview, which consists of deeper descriptions of user permissions and use case diagrams.  Additionally, this section also explains the types of dependencies and assumptions made for the system to work correctly.
Section 3 contains a brief analysis of users permissions as given by section 2, followed by a deeper level explanation of user actions, and specific requirement of the different software functionalities which are required by the project. This section also contains detailed descriptions of the data modeling done by the system, including a data flow diagram for quick visual reference.
2. Overall Description
2.1 Use-Case Model Survey
	The NoNo Web File system can be accessed by three different types of users, Guest Users, Ordinary Users, and Superusers. Each of these users is granted different levels of permissions, described below in detail:

GU - Lower level permissions. The GU can
Read open documents
Retrieve old version of open documents
Complains about document they can read
Send suggestions of taboo words to SU
Fill out an application to become an OU, including their name and technical interests

OU - Middle level permissions. The OU has all privileges granted to GUs, and can additionally:
Create new documents. The OU becomes the owner of the documents they create.
Invite other OUs to update their documents 
Set their document’s visibility settings to open, restricted, shared, or private *
Accept or deny requests placed by other OUs to view their documents 
Lock a shared document for updating *
Update a locked document *
Unlock a shared document locked by themselves
File complaints directly to the owner of a document about updates
File complaints about other OUs
Remove OUs from shared documents that has been previously invented
Search their files based on keywords
Search  information about other OUs based on name or interests

SU - High level permissions. The SU has all privileges granted to OUs, and can additionally:
Update user’s membership, such as inviting new people to edit or expel members
Maintain a list of taboo words, to prevent members to write these sensitive words in their documents
Unlock locked documents
Access private documents directly 
Process any complaints about OUs
        
*Functional descriptions about each of these permissions can be found in section 3.1

A visual representation of the different use cases for this software system is given by the following Use Case Diagram:


2.2 Assumptions and Dependencies
	One important factor which will allow the NoNo Web File system to function correctly, is that the software should be able to tell the difference between user types, in order to make sure that the appropriate permissions are given to each user. For this function to work properly, users should be logged in. If a user is not logged in, they should assumed to be GUs and only be given the permissions appropriated to this type of user.
	The appropriate use of the list of taboo words is dependent on the SU maintaining and updating this list appropriately. The software will be delivered with a basic list containing some pre-set values, however, this list should be updated by the SU to reflect the values of the team who will be collaborating using this software. If that list is not updated and users are dissatisfied with this software functionality, the team responsible for the developing of this software is not liable, as this is a responsibility of the SU alone.
	Additionally, the system assumes that the correct permissions are given by the SU to GUs and OUs accordingly. If a GU is given OU permissions accidentally, this is solely an issue of the SU erroneously assigning permissions, as the system cannot make decisions about user types. Similarly, if a user is dissatisfied with their permission level, this is also an issue that depends on the SU maintenance of users and their allocated permissions, rather than an issue of software functionality.

2.3 ER Diagram of System

3. Specific Requirements
3.1 Use-Case Report
          Based on the Use-Case Diagram and user privileges descriptions given in section 2.1, we can infer that GUs has very limited privileges. GUs can only read open documents, including older versions, but have no writing permission. They make complaints about the documents they can read and suggest taboo words that should be excluded from documents. They can also and apply to become an OU.
OUs have all privileges granted to GUs in addition to many others. OUs can create new documents and invite other OUs to update them. They have read and write permissions to all documents they create or are invited to. They can restrict the public’s access to these documents and have locking and unlocking access to the documents they create. They can also file complains about updates made to documents they do not own, and search not only their documents but also information about other OUs. 
The SU has the most privileges. In addition to all privileges granted to GUs and OUs, the SU can also update the membership of OUs, maintain lists of taboo words, unlock any locked documents, and process complaints about OUs and taboo words.  
Some additional descriptions, required by user permissions are given below:
3.1.1 Document Visibility
Once a document is created by an OU, they can set its visibility to:
Public - Anyone can read the document, including GUs
Restricted - Only the owner of the document and the OUs he shared the document with can read and write to the document
Private - Can only be viewed and edited by the document’s owner
3.1.2 Document Locking
When an OU wishes to update a document, they must first lock it. Once the document is successfully locked, the changes can be made. At the time changes are being made, the system indicated that the document is locked, and displays the name of the user who is making changes.
Once changes are made and saved, the document can be set to unlocked. Upon saving, a unique version sequence number is attached to the document to let the version history knows which user made the changes highlighted, and the date updates were made.
Only one OU can lock a document at the time. While a document is locked, another OU cannot unlock it to make changed themselves. However, the SU can unlock locked documents any any time, and is the only user who has this type of permission.

3.1.3 Data Modeling


3.2 Supplementary Requirements
There should be only ONE word for each line in all documents 
Any word(s) belonging to the taboo list are replaced by the system using a word suggested by the SU. If the word is on the taboo list but does not have a suggested replacement (e.g cuss words), they will be replaced by UNK. Team members who use these words are warned automatically. This team member should update the document next time they log in as the first job (all other activities are blocked).
Users should have their own page populated by their picture and their 3 most recent documents. For a brand-new user, the 3 most popular (most read and/or updated) files in the system are shown.
The supplementary requirements associated to version history can be found in section 3.2.1.
3.2.1 Version History
	The NoNo Web File software requires that the user be able to view what is the version of the document they are currently reading. Each version should have a specific code assigned to it. User should also be able to view what are the changes associated with the version they are currently viewing. Additionally, users can view previous versions of documents and the users associated with that particular versions’ changes.
	Generally, the NoNo Web File software should follow the requirements below:
There should be only ONE current version for any document
Older versions can be edited in three possible ways: add, delete, and update.
The retrieval of older versions of documents will be done based on the current version and/or a sequence of history files.
4. Supporting Information
4.1 Index

A


N
B


O
OU - Ordinary User                                       p. 2, 4
C


P
Permissions                                              p. 3, 5, 6
Profile, user                                                       p. 7
D
Data, Database                                                 p. 7
Document Sharing                                            p. 2
Q
E


R
F
S
Sharing p.
SRC - Software Requirement Specification p.
Superuser p.
G
GU - Guest User                                         p. 2,3,6
T
Taboo, words                                         p. 2, 5, 6, 7
H


U
Use Case Scenarios                                         p. 9
I


V
Version, SRS                                                     p. 0
Version, document history                             p. 6, 7
Visibility, document                                           p. 6
J


W
K


X
L
Log In, user                                                       p. 5
Y
M


Z

4.2 Apendices
4.2.1 Appendix A - Use Case Scenarios For Each User Case

Normal Scenarios

GU reads a public document, views a previous version of the document and complains about the document’s current version 
GU enters the system 
From the home page they can views a list of public documents
GU clicks on a document they wish to read
Document loads on the screen and has the following action buttons: “Make a Complaint” and “Previous Versions”
GU clicks on “Previous Versions”
A list of previous versions is displayed to the GU
GU clicks on the version they wish to see
The document’s version chosen by the GU is displayed on the screen and has the following action button: “Current Version”
The GU clicks on “Current Version” and the current version of the document is displayed on the screen again with the action buttons “Make a Complaint” and “Previous Versions”
The GU clicks on “Make a Complaint” and a form appears on the screen
The form has two fields, “Document Name” and “Complaint”
The GU types the document name first then the complaint to the form and clicks “Send”
The GU complaint is sent to the SU for review

GU applied to become a OU
GU enters the system
From the home page they can click on “Become Ordinary User”
GU clicks on that button and a form appears on the screen
The form contains two fields: “Name” and “Your Technical Interests”
The GU fills out the form and clicks on “Send”
The form is sent to SU for review

GU suggests a taboo word
GU enters the system and clicks on “Suggest a Taboo Word”
A form appears on the screen with a field for the SU to type the word(s) they wish to suggest
After typing, the GU presses “Send”
The word(s) is sent to the SU for review

OU creates a new document, sets the document visibility to shared, locks the document for editing, unlocks the document so that others can edit it next
OU enters the system
From their profile page they can choose the option “Create New”
OU clicks on that option and a new blank document appears
OU clicks on “Set Document’s Visibility” to which 3 options appear “Private”, “Public”, or “Restricted”
The OU clicks on “Restricted” and a field for the name(s) of the other OUs they wish to share the document with appears
OU types the name in the field. If they wish to share it with more than one other OU, the names should be entered separated by commas
The OU finishes typing and clicks “Send”
An invitation(s) is sent to the OU who’s name was typed
The OU who created the document then clicks on “Lock” and starts making changes to the document
Once they are done with changes, the OU clicks on “Unlock” so that others can lock the document to continue editing the document next

OU searches for a document, reads it, retrieves an older version of it, complains about the current version of the document to the owner
OU enters the system and locates the “Search” field
The OU types the name of a document they are looking for
The document comes up on the search result and the OU clicks on it to open it
This document was created by another OU, but this current OU has permission to view and edit it
The OU retrieves an older version of the document
The version appears on the screen for the OU to read it
The OU clicks on “Current Version” which displays the current version of the document on the screen
The OU clicks on “Make a Complaint” and a form appears with the options “Document Complaint” and “User Complaint”
The OU choose the “Document Complaint” option and  a form appears with two fields: “Document Name” and “Complaint”
The OU fills out the form and clicks on “Send”
The complaint is sent to the OU who is the owner of the document

OU reads a document and complains about another OU to the SU
OU enters the system and clicks on a document they have access to read and write to
OU reads the document and clicks on “Make a Complaint”
A form with the options “Document Complaint” and “User Complaint” appears on the screen
The OU chooses “User Complaint” and a form with two fields appears on the screen: “User Name” and “Complaint”
The OU fills out the form and clicks on “Send”
The OU’s complaint is sent to the SU for review

OU searches for another OUs information, reads it, then makes a complaint to the SU
OU enters the system and locates the search field
OU enters the name of another OU in the search field
In the search results they can see the profile page for the OU they were looking for
The OU can see the name, documents, and technical interests in this OUs profile page
The OU clicks on “Make a Complaint” and options appear for “Document Complaint” or “User Complaint”
The OU choose “User Complaint” and a form with two fields appear: “User Name” and “Complaint”
The OU fills out the form and clicks on “Send”
The complaint is sent to the SU for review

OU requests access to a document
The OU enters the system and views a list of recent documents
On the list they find a document they do not have access to
The OU clicks on “Request Access” and a message with their request is sent to the OU who owns that document

OU receives a request from another OU to access on of their documents
OU enters the system and goes to their profile page
On their profile page they can see a new message
When they click on the message, they can view that another OU has requested to view one of their documents
The OU decides with they which to share the document or not with this other user. They can choose from “Accept” or “Decline”
If the OU clicks on “Accept” the document will be added to the other user’s list of documents that they have access to
If the OU clicks on “Decline” the request is denied and the document does not appear in the other user’s list of documents they have access to

SU receives a complaint about a document and reviews it
SU enters the system and goes to their profile
In their profile page they can see a new complaint about a document
The SU reads the complaint
If they decide the complaint is valid they can: contact the owner of the document about the complaint, access the document and make the changes to it themselves, delete the document
If they decide that the complaint is not valid they can just ignore the request

SU receives a complaint about a user
SU enters the system and goes to their profile
In their profile page they can see a new complaint about a user
The SU reads the complaint
If they decide the complaint is valid they can: warn the user who’s complaint is about and ask them to modify their behaviour, ban the user from the system
If they decide that the complaint is not valid they can just ignore the request

SU receives a suggestion for a taboo word
SU enters the system and goes to their profile
In their profile page they can see a new suggestion for a taboo word
The SU reads the suggestion
The SU decides the suggestion is good and clicks on “Taboo Words” 
A document displaying the taboo words will appear on the screen
They type in the new word to be banned from all documents, and a replacement word for it. They then click on “Save”
The system scans all documents to find the new taboo word and replaces all instances with the word suggested by the SU 
If the SU decides that the complaint is not valid, they can just ignore the request

SU receives a request from a GU to become a OU
SU enters the system and goes to their profile
In their profile page they can see a new request to become OU
The SU reads the request
The SU decides the request is good and clicks on “Authorize”
The GU profile changes to a OU profile, now they can have all privileges granted to OUs
If the SU decides that the request is not valid, they can just ignore it

SU invites a new user to become a Ordinary User, who accepts the request
SU enters the system and goes to their profile
In their profile page they can click on “Invite a New User”
The SU clicks on the button and a form appears with two fields: “Invitee Email”, “Message”, and “User Type”
Under “User Type” the SU can choose “Ordinary User” or “Guest User”
The SU choose “Ordinary User”, fills out the form and clicks on “Send”
A email with the message the SU typed is sent to the invitee, with two options “Accept” or “Reject”
The invitee reads the email and clicks on “Accept”
The invitee is taken to the NoNo System where they are asked to fill out information in their ordinary user account
The invitee enters their email, name, and technical interests
They now have a profile where they have all OU privileges

SU invites a new user to become a Guest User, who accepts the request
SU enters the system and goes to their profile
In their profile page they can click on “Invite a New User”
The SU clicks on the button and a form appears with two fields: “Invitee Email”, “Message”, and “User Type”
Under “User Type” the SU can choose “Ordinary User” or “Guest User”
The SU choose “Guest User”, fills out the form and clicks on “Send”
A email with the message the SU typed is sent to the invitee, with two options “Accept” or “Reject”
The invitee reads the email and clicks on “Accept”
The invitee is taken to the NoNo System where they are asked to fill out information in their guest user account
The invitee enters their email, name, and technical interests
They now have a profile where they have all GU privileges

Exceptional Scenarios

OU reads a document and complains about the document but choose the wrong option in the complaint form
OU enters the system and clicks on a document they have access to read and write to
OU reads the document and clicks on “Make a Complaint”
A form with the options “Document Complaint” and “User Complaint” appears on the screen
The OU chooses “User Complaint” and a form with two fields appears on the screen: “User Name” and “Complaint”
The OU fills out with complaints about a document, not another user, and clicks on “Send”
The OU’s complaint is sent to the SU for review

SU receives a complaint about a document that was supposed to go to the OU who owns the document
SU enters the system and see they have a new complaint about a user
While reading the complaint the SU sees that is a complaint about a document that should have been sent to the document’s owner, not them
SU notify the user who made a complain that they must make the complaint again and choose “Document Complaint” in the complaint form, not “User Complaint”

4.2.2 Appendix B - System Prototypes
4.2.3 Appendix C - Application system functions

Application main function
	This is the main access point for the whole program, where takes the total control and the flow of the application between user and data, by defining user roles and given control to user. Since different user has different roles. System will be develop total sets of function by given different showing.
	Variables:
User information
Authority level, guest/ OU/SU
CurrentPage: base on the authority level, different gui page will be formed.
 Popular files/ HIstory files
currentfile

Database
User class
News, type :invitation/lock message, messages from other user
FIle visited history: files self created or visited history
Authority level

File
ID
Title
Author
Date 
Description
Authority
Friend list
Invited List
History( text with version number)

Main function
Authorization
Load popular files/ history files
Direct user to their corresponding pages

Authorization function
Pre: User name and password
Post: return a user json
Access the username and password that’s in the local file.
If the username existed and correct password, update the user class.
Ir the username existed with incorrect password, return incorrect password and  resend the password.

Initialization User
Pre: User id
Post: update file history
Connect to the files database
If the user has editing file or file history then it will update the list
Else will return the top 10 popular file.

Note: FIle will be return in the form of title, id, and description

Search file
	Pre: A keyword
	Post: will be show the name of the file and the access id
Search Level( Title > Author > Description)
Load all the file name and search for the given title,
Then author, then Description
*Advance development: User can define the level of the search
There will be a small file class in the current application to keep track of the history

Open file
Pre: file id
Post: display the text to the user
Connect to the databases of the file
Check the statue of the file, 
if the file is current locked, can’t open the file
Update the current file variable
Display the most Update version of the file. 

Revisit older version of the file:
	Pre: select file history
	Post: display the Corresponding version
Base on the user input, update the current file’s display text.

Complaint on file
	Pre: user, complaint
	Post; push the complaint in the the database
Push the complaint  into the database

Suggest tacto words
	Pre: user, tacto word list
	Post: Push the tacto word into the databases

Apply to user
	Pre: Username, email, password, reason 
	Post: Update to the databases
Connect to the databases, check for existing username and email
If existed, let guest user modify inputs
Else push them into the databases with the application list

Ordinary user
Create file
	Pre: Name, description
	Post: Generate the file
Load tacto words, 
if name and description existed a tacto word, rejected and let user modify inputs
Generate name and description for the current file
Call function set up authority

Set up Authority
	Pre: file 
	Post: update current file in the application
Four level
Privated
Public
Restricted
Shared	, If it is shared, then call the invited  OU function

Load OU,
	Pre: call
	Post: List of the current OU
Load the lost of the current OU

Invited OU function
	Pre: username
	Post: Add the user name to the current file, invited list
Load OU
Get user input and update the current file in the application and push back to the database system, update a invitation to the OU

Accept/ Denied invitation
	Pre: user input with true or false
	Post: update file
Load invitation for the current user
If true, push the user name into the corresponding file’s friend list

Remove OU function
	Pre: username
	Post: Remove the user name in the friend list
Load OU
Get user input and update the current file in the application and push back to the database system

Save file
	Pre: user input
	Post: update the file in the database
Save the current file to a String
Load the tacto list
Compare the tacto list and the File string
If the file is safe, update the current file of the application and push the string into the databases by calling databases function(id,User, file string)
Else display the tacto word to the user.

Complaint on other OU
	Pre: user, complaint
	Post; push the complaint in the the database
Load OU list
Save the user and complaint to the database(Complaint OU List)

Super User
Lock file
	Pre: user id and file
	Post: lock the file and update to the databases
Lock the current file/ unlock with given reason send to the file creator and the friend list
Update the file statue, and Update all the user’s new list
Set Document Visibility
	Pre: file id and permission
	Post: update the file authority
Update the current file status in the application and file system

Review tacto list request
	Pre: load tacto list
	Post: update tacto list
Load tacto list
Load suggest tacto list

Maintain tacto List
	Pre: modify the tacto list
	Post: upata tacto list
Get user input and push back to the databases

Review complaints
	Pre: load Complaint
	Post: update the statues of the complaint
If the SU required all complaint and search for the complaint base on tile, id, username
Else return the the open complaints

Delete / Completed complaint
	Pre: complaint id
	Post: update the display and update the complaint from the databases

Reply complaint
	Pre: complaint id
	Post: generate complaint message to user.
Send message to the user about the complaint with the opening of the 
Complaint id.

Review Guest User Application
	Pre: load guest user application
	Post: update user database
If SU agree, then add the use to the user databases, else delete the application

Update User’ membership
	Pre: load OU list
	Post: update user databases
Invite new users or expel user

Invited new user
	Pre: email address
	Post: Send an email to the given email address
Gather Email address
Send invitation

Expel User
	Pre: OU id
	Post: update user database
Change the authority level to the corresponding user.

