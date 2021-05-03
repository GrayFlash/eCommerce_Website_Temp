# eCommerce_Website for SoLocl Programming Task

### Environment Setup

* Create a ViretualEnv with, ```python3 -m venv env```.
* ```pip install -r requirements.txt```, for installing the dependencies.
* To export development environment, ```export FLASK_ENV=development```.
* To start the flask server, ```flask run```.

### Stack Used:
* Flask for Backend.
* BeautifulSoup for Scrapping Dummy Data, choice of site (ebay) is awful and hence a large number of images are seen missing.
* HTML, CSS and Bootstrap for Frontend.
* Database is <b>missing</b> currently.

### Description:

* Site has a simple homepage with a choice in two categories, although each category had some subcategories but those were ignored as the data scraped from Ebay had a huge quantity missing and inappropriate.
* Which ever category is picked, we are directed to catalogue page where the items of these categories is displayed.
* You can Add an item and it will be shown in the cart.
* Navbar can be used at any point to move to and fro to various sections.
* An ER models was being planned upon and there were a lot of this that will greatly benifit the flow of data from Database to the page, but are not implemented.