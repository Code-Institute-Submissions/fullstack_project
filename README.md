
#Webshop Application 


It's an ecommerce website where a user can buy ingame items for their nintendo switch. The users only have three critical goal paths:

View the store's inventory of amiibo villagers.

Keep track of the villagers they want to purchase using favorites or using a shopping cart. Note: They don't need to create 
an account or anything to purchase an item.

Check out and pay for their items.


#UX

The central target audience for the website are people who want to buy in-game items for their Switch. These are people of all ages. 


#User Stories 

1) Authentication: User can signup/login/logout 

2) Filtering: User can view lists of items per category and search by name, filter by species or personalities.

3) Shopping Cart: User can add items to shopping cart. User can edit or remove items from the shopping cart.  

4) Checkout: User can fill in a form and submit shipping info. After submitting this info, order is processed and a success page is 
displayed.

5) Order processed: user gets confirmation email with order nr

6) Customer can create a profile (only for logged in users), where the user can save their favorite villagers, view order history 
or leave reviews on items.

7) If the user is logged in, he can view profile page. If not, user gets redirected to the login page.

8) User can edit and update profile details them if needed

9) Customer is able to read reviews of other customers

10) Pagination added to reviews so it's not too crowded on a single page

11) Customer can use text search function to find something specific

12) User gets notification when an item is added/edited/removed to/from the cart.

13) Shows the total price of all items (on every page)

14) Allows them to purchase items, purchasing takes the user to payment form 

15) Create a form that allows the user to enter billing info

16) On submit, the order status changes to purchased

17) A link to the shopping cart must be present on every page. This should display order total. 

18) Users, even anonymous ones that haven’t registered or logged in, should be able to
add items to their cart.

19) A user can edit the billing information on their profile.

20) A user can sign up for a newsletter

21) User can also leave a review.

#Tested on

ipad ipad pro (landscape and portrait) laptop with hpdi aptop with mpdi, iphone 5, iphone 6/7/8/, iphone 6/7/8 plus, iphone x
(phones tested in portrait mode)

#Nice to haves

Responsive design 

#Technologies Used

#Main Tools/Frameworks

Django, Stripe, Django Crispy Forms, Allauth, Pillow, Heroku, SQlite3, Bootstrap


#Languages
This project uses HTML, CSS, JavaScript and Python programming languages.

#Testing
Testing is done using the Django testing framework. Everything else was tested manually.

#Validation Services:

The following validation services and linter were used to check the validity of the website code.

W3C Markup Validation was used to validate HTML.

W3C CSS validation was used to validate CSS.


#Deployment to Heroku

Steps to take:

Firstly, create a Heroku app by clicking the "New" button in the Heroku dashboard.

Secondly, we need to link our local Git repository to Heroku, which is what we're going to do in this video.

Thirdly, create a requirements.txt file (pip freeze > requirements.txt), which contains a list of our dependencies.

And finally, create a Procfile (echo web: python run.py > Procfile), which is a special kind of file that tells Heroku how to run the project.

In heroku dashboard select the master branch then click "Deploy Branch".

Link Heroku app to a GitHub repo. You can selectively deploy from branches or configure auto-deploys.

#MEDIA

Image sources: https://www.nintendo.com/, www.starface.com 