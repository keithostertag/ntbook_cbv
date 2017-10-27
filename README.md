**Ntbook** is a small and simple desktop database designed as a web-based CRUD application running under python/django and using sqlite3.  

Typical use: type in a code snippet or note (or just paste it in) then optionally
include meta data about your snippet. Often the meta may be more actual lines/text
than your code, as you may want to include how you use the code, where you found it, or other background info that you may want to reference in the future.  

#### Features:  
* The vertical bar that splits the two panels can be dragged to alter their relative sizes (courtesy of https://github.com/RickStrahl/jquery-resizable ).  
* Code snippets are syntax highlighted  
* Date added will appear under the meta section, if meta exists.  
* Click on any snippet or meta to display or update.  
* Search for a string/phrase using the search box. This will search both the snippet and meta fields.  Do not use Boolean logic or quotes.
* After any search, just click the 'search' button when the search bar is empty to
return to the full display.  
* Responsive Design down to 800x600: Flexbox used for scaling the main panels, media queries will alter heading and bottom panel layout.

#### Requirements
* Proper installation of python3 (or use virtual environment) with django 1.11 or higher (might work with older versions but not tested)  
* Working Internet connection: this is used only for the CDN access to [**highlightjs**](https://highlightjs.org/) and a graphic for the vertical splitter bar from Rick Strahl.  
* Designed for desktop or other devices with a minimum dimension of 800x600.
