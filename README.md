**Ntbook** is a small and simple desktop database designed as a web-based CRUD application running under python/django and using sqlite3.  

Typical use: type in a code snippet or note (or just paste it in) then optionally
include meta data about your snippet. Often the meta may be more actual lines/text
than your code, as you may want to include how you use the code, where you found it, or other background info that you may want to reference in the future. You could also use it for, say, poetry- put your poems in the snippet field and discussion in the meta field...the snippet field will retain your formatting.  

#### Features:  
* The splitter bar that splits the two main panels can be dragged to alter their relative sizes (courtesy of  https://github.com/RickStrahl/jquery-resizable ).  
* Code snippets are syntax highlighted (courtesy of https://highlightjs.org/ using the *xcode* style ).  
* Date added will appear under the meta section, if meta exists.  
* Click on any snippet or meta to display or update.  
* Search for a string/phrase using the search box. This will search both the snippet and meta fields.  Do not use Boolean logic or quotes.
* After any search, just click the 'search' button when the search bar is empty to
return to the full display.  
* Responsive Design: Flexbox used for scaling the main panels, media queries will alter heading and bottom panel layout, and switch the two main panels between row and column formats depending on device size.

#### Requirements:
* Proper installation of python3 (or use virtual environment) with django 1.11 or higher (might work with older versions but not tested)  
* Working Internet connection: this is used only for the CDN access to **jquery** and a graphic for the splitter bar from Rick Strahl.  
* Designed for desktop or other devices with a minimum dimension of 800x600, but will work well on smaller devices (but probably not as small as a phone!).  
* Access by pointing your browser to localhost:8000 after running the server. For django admin access: localhost:8000/admin/ login is 'admin' password is 'codelouisville'.  

#### Screenshot
![Screenshot](ntbook.png "Screenshot")
