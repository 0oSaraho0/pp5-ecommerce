# Laneys Loft

Laneys loft is a charity ecommerse site.  It takes donations of clothes books and kids toys and sells the items online.  It then donates proceeds to charities and charitable events. 

You can reach the live site [here](https://pp5-laneys-loft.herokuapp.com/)

![Responsive Screens](/media/responsive-screens.png)

# Table of contents   

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# User-Experience-Design

## Site Goals

The site is aimed at anyone that wants to donate their unwanted items to charity, and anyone who wants to buy preloved items  Without signing in the user can browse the online store and donate their items.  They can also look at the site blog to see where they money is being spent.  They can log in to see a log of the items they have bought and leave a review of the site.  They can also save their details for future purchases.

## Agile Planning

This project was developed using agile methodologies, delivering small features over 6 sprints spaced out over 6 weeks.  Each issue was labelled must have, should have and could have.  The must have features were completed first, then the should have's, then the could have's.  It was done this way to ensure a complete website is made with the nice to have features added if there is capacity.

My kanban board was made using github projects which can be viewed [here]().  Each view can be clicked in to obtain further information.

![kanban](/media/pp5-kanban.png)

The user stories were grouped into different Epics

Epic 1 - Set up

The base setup of the Django app was done first as nothing else can be completed before this is done. I completed the base html, and the header. 

Epic 1 user stories

- As a developer, I need to set up the project so that it is ready for implementing core features
- As a developer, I want to create a base HTML page so that all pages can use the same format.
- As a user, I want to be able to navigate around the site easily from any device


Epic 2 - Products and shopping bag

Setting up database model and admin functions and template pages to be able to view the products available to buy and have messages confirming when items have been added to the bag.

Epic 2 User Stories

- As a shopper, I want to view a list of products so that I can select something to buy
- As a shopper, I want to be able to click into a product to view its details so I can see what size it is etc
- As a user I want to be able to view what I have added to my shopping bag and the total price
- As a user I want to be able to delete items from my bag when I decide I no longer want something.
- As a user I want to receive a confirmation when I have made changes ie, adding and removing items to my bag so that I know when a change has been completed.

Epic 3 - payment and purchase confirmation emails.

Epic 3 User Stories

- As a shopper I want to be able to easily enter my payment details so that I can purchase my chosen items.
- As a shopper I want to see confirmation that my payment has gone through successfully and that my purchase is being sent to the correct address so that I know it has been done correctly
- As a shopper I want laneys loft to send me an email so that I can keep confirmation of purchase for my own records.

Epic 4 Allauth
User Stories
- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.
- As a developer, I want to ensure the forms are all the same style and look good on all devices

Epic 5 - Profile Page
 - As a user I want to be able to access a profile page so that I can update my orders
 - As a usder I want to see what donations I have made in the past
 - As a user I want to be able to update my details if I move house.

Epic 6 - Blog

- As a site user I want to be able to see where the money from the site is being sent so I can feel good about my purchases
- As a site owner I want to easily be able to add blog entries onto the Site
- As a site owner I want to be able to edit my blog posts so that I can make corrections easily
- As a site owner I want to be able to delete blog posts as necessary.
- As a site owner I want to be the only one who can create edit and delete blog posts


Epic 7 - Reviews

Epic 7 User Stories

- As a user I would like to be able to read reviews about so I can decide if I want to use it
- As a site user who is logged in I would like to be able to leave my own review so that I can tell others about my experience
- As a user it would be nice to give my review a rating out of five for ease of reference
- As a site owner it would be nice to be able to reply to reviews to show a personal touch


Epic 8 Donations

- As a user I want to be able to arrange for my donated items to be picked up easily.

Epic 9 Footer

Epic 9 User Stories

- As site owner, I want to share social media links and contact details
- As site owner I want a nav bar for the site extras such as the blog, reviews and subsribe pages

Epic 10 - Documentation and styling

Epic 10 Tasks

- Complete Styling on all pages and all screen sizes
- Complete Readme documentation
- Complete testing and writeup

## Scope
- Responsive Design
- Home page with information about Laneys Loft
- Ability to perform CRUD functionality on the Blog
- Restricted features for not logged in as users and superusers

## Structure

### Laneys Loft Features

Navbar

user story - As a user I want to be able to navigate easily around the site from any devise

Navigation Menu

from the main top navigation bar the user can log in or sign in.  Once logged in they can access their profile page.

They can browse all the site products and check their shopping bag.  They can also search the site using the search bar.

![Navbar full size nav bar](/media/full-size-nav-bar.png)

on mobile devices they shopping navigation collapses into a dropdown square and the search bar drops down to a magnifie glass search icon

![mobile nav bar](/media/mobile-nav-bar.png)

### Home Page

- User Story - As a user I want the front page to be clear and self-explanatory so I know I am in the right place

The front page contains an image of a charity shop.  This gives the initial impression of pre loved goods.
![Hero Image](/media/homepage_background_cropped.webp)
The front page also containes a tag line advising the user they can shop or donate with a button to take them to either place on the website.  This gives an imediate idea of what the website is for.

![tag line](/media/front-page-tag-line.png)


Under this is information about the site and how to shop or donate.

![Welcome Text](/media/about-laneys-loft.png)

### Footer

- User Story: As site owner, I want to share social media links and contact details
- User Story : As site owner I want a nav bar for the site extras such as the blog, reviews and subsribe pages

The Footer has been added to the bottom of the site and contains links the sites blog, reviews and donations form.  Users can also subscribe the sites news letter from here.

underneath the footer navigation bar users can see the contact email for the site and links to the social media pages.

![Footer](/media/laneysloft-footer.png)

### Browse Items

- User Story: As a shopper, I want to view a list of products so that I can select something to buy

Users can easily brows items to buy, products come up in rows of 4 on the larges screen and they reduce down to 3,2 then 1 depending on screen size. 

Users can also search by womens, mens and kids items. They can also pick from a dropdown list of different clothing types to refine their search further.

Users can also search by price.  They can also search for specific words in the search bar at the top of the page

![Brows Items Page](/static/images/browse-ideas.png)

### Item Detail 

- As a shopper, I want to be able to click into a product to view its details so I can see what size it is etc

Users can select see more detail about an item by clicking on the picture.  This takes them to a detail page where they can then add it to their basked if they wish


![Detail Page](/static/images/detail-page.png)


### Sign in, log in, log out

- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.
- As a developer, I want to ensure the forms are all the same style and look good on all devices

![log in](/media/sign-in-form.png) ![log in](/media/sign-out-form.png) ![log in](/media/register-form.png)

The sign in, log in, log out pages were made using allauth.
They all have a white background with round corner buttons and input boxes.
They all have greay writing.  This crates continuity within the authorisation section of the site.  I have made them on a white background rather than gray so that they are slightly different from the other ones on the site but they still keep the font style for the title to connect them with the test of the site.

The user will receive a toast message saying they have successfully signed in and out.

![log in toast](/media/sign-in-success.png) ![log out toast](/media/sign-out-success.png)

### Shopping Bag

User Stories
- As a user I want to be able to view what I have added to my shopping bag and the total price
- As a user I want to be able to delete items from my bag when I decide I no longer want something.
- As a user I want to receive a confirmation when I have made changes ie, adding and removing items to my bag so that I know when a change has been completed.

![shopping Bag](/media/shopping-bag.png)

The shopping bag shows a picture of the itme(s) in the bag along with the item name, price, quantity (although it is only ever one because there is only one of each item) and the price.  There is also a delete button so items can be deleted easily.

When items are added or deleted from the basked a success message appears that contains the bag content and a link to the checkout page.

![shopping Bag](/media/add-item-to-basket.png) ![shopping Bag](/media/remove-item-from-basket.png)

### Checkout Page

User Stories
- As a shopper I want to be able to easily enter my payment details so that I can purchase my chosen items easily.

![checkout 1](/media/checkout-1.png)
![checkout 2](/media/checkout-2.png)

The checkout page has an easy to complete form that takes the users name, address and card details. It also has a summary of the purchase to confirm what is being bought.

It also has a tickbox to save the details to the profile page so it will be prefilled the next time they buy something.

Dispite the rest of the boxes on the site having rounded edges, I decided to keep the checkout boxes with sharp edges.  This is because it feels like a more important/trustworthy shape for an important transaction.

### Order Confirmation 

- As a shopper I want to see confirmation that my payment has gone through successfully and that my purchase is being sent to the correct address so that I know it has been done correctly
- As a shopper I want laneys loft to send me an email so that I can keep confirmation of purchase for my own records.

Once the order has been processed a confirmation page tells the user the order details.  It also advises an email has been sent to the email address provided.

### Profile Page

 - As a user I want to be able to access a profile page so that I can update my orders
 - As a user I want to be able to update my details if I move house.

![checkout 2](/media/profile-page.png)

The profile page has the users address details available to edit if necessary.  It also has a record of all of past shopping orders.

### Blog
User stories:
- As a site user I want to be able to see where the money from the site is being sent so I can feel good about my purchases

The blog page shows a list of blog posts that have been entered by the site owner. 
![blog](media/blog.jpg)

The create edit and delete a blog post buttons is only visible to the superuser
![blog](media/blog-not-superuser.png)

- As a site owner I want to be the only one who can create edit and delete blog posts

The blog forms are all simple to use with clear instructions.
![blog](media/add-blog-post.png)
- As a site owner I want to easily be able to add blog entries onto the Site
![blog](media/edit-blog.png)
- As a site owner I want to be able to edit my blog posts so that I can make corrections easily
![blog](media/delete-blog.png)
- As a site owner I want to be able to delete blog posts as necessary.

### Reviews
- As a user I would like to be able to read reviews about so I can decide if I want to use it

The reviews page lists the customer reviews in order of most recent first.  They are clear and easy to read.
![reviews](media/reviews.png)

- As a site user who is logged in I would like to be able to leave my own review so that I can tell others about my experience

Everyone can see the write a review button so that users are encouraged to write a review.  However if you not registered it directs you to the registration page.

### Donations

- As a user I want to be able to arrange for my donated items to be picked up easily.

The donations form is simple to complete.  The user doesn't need to be logged in to arrange a collection.  They can just complete the form with the address details of collection, a date and what and how many bags are to be collected.

The user is then directed to a confirmation screen.

### Subscribe

Users can subscribe to the sites mailing list.  Mailchimp has been used to set up the mailing list and all the user needs to do is fill out their name and email address.

## Facebook Page

I set up my company facebook page and added the link to the facebook icon in the footer.

Here is a screen shot of my page
![reviews](media/facebook-page.png)

# Keywords

The keywords I thought of for this site were:
- Charity
- Charity Shop
- Donating
- Second had clothes
- Second hand
- Where can I donate my old clothes
- Buy preloved clothes

I tied to use as many of these as I could arround the site.  I added the about Laneys Loft section on the front page and added as many as I could fit into it. I also used a few in the blog section.
If I had more time I would like to create a FAQ page so that I could add plenty of key works there.

## Features left to impliment

There were a few items that would have been really nice to include, that I included in my user stories but unfortunately I ran out of time.
- I wanted to add the donation details to the profile page as well as the orders so that user could have a record of this as well. 
- I wanted to add a star rating system to the reviews page. This would have been a nice extra visual to see what people though of the site. 
  - As a user it would be nice to give my review a rating out of five for ease of reference
- I wanted to add replies to the reviews page so that the site owner could reply to customers and solve problems they have, this would add extra user experience value and would deffinately be in the next update if there was one.
  - As a site owner it would be nice to be able to reply to reviews to show a personal touch
- I would like to add a FAQ page as mentioned above to add more keywords into the site
- I wanted to add more search options on the producs page so the user could search by colour and size etc on the list view.
- I wanted to add email confirmation to the donations page but ran out of time so have added a confirmation page instead at the moment.
# Wireframes

Home Page

![Home page wireframe](/media/wireframe-home.png)

Sign Up

![Sign up wireframe](/media/wireframe-sign-in.png)

Log In

![Log in wireframe](/media/wireframe-login.png)

Log out

![log out wireframe](/media/wireframe-log-out.png)

Products

![Browse Ideas wireframe](/media/wireframe-products-page.png)

Product Detail

![Idea Detail wireframe](/media/wireframe-product-detail.png)

bag

![Create/Edit Idea wireframe](/media/wireframe-bag.png)

Checkout

![Delete Idea wireframe](/media/wireframe-checkout.png)

Order Confirmation

![Delete Idea wireframe](/media/wireframe-order-confirmation.png)

Blog Post
![Delete Idea wireframe](/media/wireframe-blog-posts.png)

Donation Form
![Delete Idea wireframe](/media/wireframe-order-confirmation.png)

Reviews
![Delete Idea wireframe](/media/wireframe-reviews.png)


# Database

The database was designed for the items to be tracked all the way through to sale and then recorded onto the user profile once sold.  
I originaly made lots of models for the different items in the items app. They were all joined to the main items database by primary key.  The aim of this was to make it easier to put search options on the producs pages for different colours, sizes, age ranges of products etc.  Unfortuanately I did not have time to implement all the search options I wanted to but I have left the different models in, in case of future developement.

The items are connected to the user and shopping bag by primary key and are then stored on the users profile as past orders.

# Security

If statemets were used to ensure that buttons that were only for the superuser were hidden from everyone else. The userpasses test mixin was used to make sure the superuser is signed in to complete the blog.

I have also used a UserPassesTest Mixin to ensure that the page can't be reached via the url.

Environment variables were stored in an env.py file for security purposes to ensure no secret keys, api keys or sensitive information were added to the repository.  These variables were added to heroku config vars within the project

# Design

## Colour Scheme

I opted for a simple black white and gray colour scheme.  I wanted the site to look clean and simple in its design

## Typogropny

I used Alfa slab One for the logo font and Rubi for the body of the site

I downloaded these from google fonts and imported them into the style sheet

## Imagery  

The front page image was taken from vogue magazine on a guide to the best charity shops

# Technologies

- HTML
  - The structure of the site was made using HTML
- CSS
  - The website was styled using CSS in an external stylesheet 
- Python 
  - Python was the main programming language used within the django app
- Github
  - Source code was hosted in Github
- Git
  - Git was used to write, commit and push code during development 
- Font Awesome
  - Various Font Awesome icons were used throughout the site
- Balsamiq
  - Balsamiq wireframes were used to plan 
- javascript
  - Used throughout the site
- [GitHub Wiki TOC generator](http://ecotrust-canada.github.io/markdown-toc/)
  - I used this to enter my table of contents.
-AWS Amazon
  - Used to store pictures

## External Python Modules
- asgiref==3.5.2
- backports.zoneinfo==0.2.1
- boto3==1.24.89
- botocore==1.27.89
- dj-database-url==0.5.0
- Django==3.2
- django-allauth==0.41.0
- django-countries==7.2.1
- django-crispy-forms==1.14.0
- django-storages==1.13.1
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- jmespath==1.0.1
- oauthlib==3.2.1
- Pillow==9.2.0
- psycopg2-binary==2.9.4
- python3-openid==3.2.0
- pytz==2022.2.1
- requests-oauthlib==1.3.1
- s3transfer==0.6.0
- sqlparse==0.4.2
- stripe==4.2.0

# Testing

## Functional Testing

### Navigation Links

Testing was performed on on all navigation links throughout the site.  I achieved this by clicking on each link to ensure it went to the correct place.

Laneys Loft Logo => index.html

All Products
- By Price => Arranges products by price
- By Category => Arranges products by A-Z Category
- All Products => Shows all products

Womens

Skits, Jeans, Dresses, Tshirts and All clothing
- All these filter womens cloths by the desired clothing type

Mens 

clothes all filter by the correct clothing types

Kids clothes and toys all filter by the correct types

My Account

My Profile => Profile page

Log out (if logged in) => to log out page

(if not logged in) Sign in => to sign in page

(if not logged in) Register => to Registration page

### Products page
Picture => Product detail page

Sort Box => All items in the sort box were tested and sort items accordingly

### Product Details page
Keep Shopping => goes back to the products page

Add to bag => correctly adds the item to the users bag this shows a success toast with the bag contents and the bag total cost shows up in under shopping bag icon.  

The user can either click the cross on the toast to get rit of it or they can go to the checkout by clicking the go to secure checkout button.  This works correctly

I tested adding the same item twice to the shoppig bag and an error message correctly appears advising the user they cant do that.

### Bag Icon
The shopping bag icon takes the user to the shopping bag.

### Shopping Bag
The red remove button correctly deletes the item from the shopping bag and the correct toast appears confirm this has been successful.

The Keep Shopping button correctly takes the user back to the products page

The Secure checkout button correctly takes the user to the checkout form.

### Checkout

I checked the checkout form for positive and negative tests

I left each box blank and the form flagged an error when these were not filled in correctly.
The email box flagged an error when an incorrect email address was input.  I tried it with just letters and with only an @, and with only a .com.  These all showed errors as expected.

I tested The save delivery information button to profile button both ticked an unticked and it correcly saved the forms information when the box was ticked.  I then logged in again to check that the information was in the form the next time and it was.

The adjust bag button correctly takes the user back to the bag.

### Card Details
I used stripes give card number to use on the site.  It shoed an error when the card number was input incorrectly

### Order Confirmation

The order confirmation button takes the user to a thank you page confirming their email address, address and order deatils.
A success message also correctly appears supplying the order number and confirming the confirmation email is sent to the email address given.

I checked the latest deals button takes the user back to the products page.

Once the item has been bought, it correctly no longer appears on the procucts page to be bought again.  As this is a second had site there is only one of each item.

### Stripe
I checked the stripe website to make sure that the payment had gone through correctly there and the webhooks had worked correctly and all was working well.

### Profile Page
I checked that the order had corretly been added to the profile page

I also updated the customer details which then changed on the checkout form the next time I bought something.

### Footer
### Blog
The blog button correctly takes the user to the blog list page, each  blog post photo and title correctly take the user to the blog detail page for that post.

On the blog post only the superuser can see the create blog post button.  I tested this both logged out completely and logged in as a regular user.
The same applies to the delete and edit buttons located in the blog detail.

I also used the url to try and get to the create, edit and delete pages without the buttons and you could get there as the superuser but could not as either not logged in or logged in as a different user.

The charity website link takes you to the correct website and it opens in a new window as it should.

The create and edit forms both upload the information and pictures as expected.  The edit form also contained all the previous infomation ready to edit as expected.

Unfortunately an error occured in the blog form. If a picture is not correctly uploaded it caused an error on the blog list page.  
I have written about this in the bug section and it has now been fixed so workes correctly.

### Reviews
The reviews button correctly takes the user to the reviews page, the reviews are correctly ordered with newest first.
The write a review button takes you to the form to write your review.  once completed the submit button correctly takes you back to the review page where the new review is visable.

If you are not logged in the reviews button correctly takes the user to the sign in page

### Donate your preloved items
This button correctly takes you to the form to be completed to get your items collected.
I tested this form and all of the stared fields did need to be entered in order for the form to be sent.  Errors were correctly shown on each line that was incorrect.

I tried putting text in the number of bags box and it did nothing until a number was put in.  This is a slight error as it should really show an error message.  I will fix this bug if I have time and write about it in the bug section

The email field correctly showed an error if the email address was not completed correctly

The submit button correctly takes the user to a confirmation page confirming the details of the collection and that an email has been sent to the user with the details for their records.

Subscribe
The subscribe button correctly takes the user to the mailchimp subscription page.  I tested this with an email that I had already used before and it would not accept it and told me to enter an different email address as it had already been use.

A new email address was successfully added.  

It also correctly flagged an error when an incompolete email address was added.

All of the social media icons correctly take to you their respective social media pages which open in a new page as expected.

The facebook icon correcly went to the Laneys Loft facebook page.

Emails

I was correctly able to set up a new user, receive an email to confirm the email address of the user, click the link to the site and confirm the email address.
I then logged in with an incorrect name and email for the user and both flagged errors correctly by the system. 

A confirmation email was correctly sent once an order was completed.

## Accessibility

I used the [Wave Accessibility](https://wave.webaim.org/)tool to check for aid accessibility testing.

The page showed a couple of errors and they were for labels on the search box in the nav bar.  I added aria labels for this but the errors stayed in the box dispite dissapearing on the page.

On other pages it showed Alerts that show redundant links, on the blog picture and name.  

I have chosen to leave these links as they are because I think they make navigation around the site better.

## Validator Testing

All pages were run through the [w3 HTML validator](https://validator.w3.org/).  Initially, there were some errors, for example there were some missing closing tags and a <p> tag that was used incorrectly inside a <span>.  

All issues were fixed and all pages ran through the checker with no errors.

![w3 HTML Validator](media/html-check.png)

## PP8 Validator

The pep8 validator was not working at the time of checking this project.  I checked in the terminal using linter and corrected all the items shown until it said no problems detected in workspace.  There were some long lines in the settings tab in Laneys Loft that I left because they were there already.  I could not find a way of screenshotting a picture of this.

## Javascript
I didn't use any Javascript in this project over the js used in boutique ado so I have not tested for that.

## Lighthouse Report

The lighthouse report initially showed a low score on performance.  I compressed my hero image which fixed the problem.  

![Lighthouse](/media/lighthouse-test.png)

# Responsiveness

I checked the website for responsiveness on all devices from 320px and up.  I checked on Chrome, Edge, Firefox and Opera browers.

I did this by using developer tools and resising the website to down to 320px.

As expected there were no responsiveness issues.

# Bugs

Error when migration change in checkout model.
File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/dummy/base.py", line 20, in complain
    raise ImproperlyConfigured("settings.DATABASES is improperly configured. "
django.core.exceptions.ImproperlyConfigured: settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.

- I looked at the error and went to the database section in settings.  I found a typo in Databases and updated this to fix the problem

--------
Error on donations form.  number of bags field does not show a proper error when the incorrect informatin is put in.  This is bad ux as the user could become confused as to what to put in the box.  I have unfortunately not had time to fix this error and as it is only a small bug I felt I could leave it until the next update.

---------

Error on donation form. If a picture is not input correctly it causes an error on the blog list page. The only way to get back in is to go into the admin panel and delete the blog post.
- I after some investigation I found that my placeholder image was not working because I had negleted to put the placeholder name in the model. Once I did this the bug was fixed.

-----------
Error the bag information shows when the blog is being updated.  I have decided to leave this bug.  I have run out of time and realisticaly the site owner probably wont have anything in her bag anyway.

-----
An error occured when I added the user passes test mixin to the blog create edit and delete views.  This caused an error page when I logged into them.
I fixed this by looking at the documentation and adding a def text_func function that checked the user had the correct email address.

# Deployment

To deploy my site to Heroku I followed the following steps

- Navigate to heroku and create/log into account
- Click the new button in the top right corner
- Select create new app
- Enter app name (kids-bored)
- Select region and click create app (europe)
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click Deploy

The app should now be deployed

# References
- I used the django documentation 
- I used the bootstrap documentation
- I used slack overflow
- I used CI slack community

# Acknowledgements

I want to thank:
- My mentor Daisy McGirr for all her guidance
- The wonderful slack community
- My husband for putting up with my stress


