# PROJECT 03 - NUTRICO2

## Description:

This was my third of four projects for the Software Engineering Immersive course run by General Assembly. The project was created over the course of a week and was a team effort created with one other; Einar Skreslett (https://github.com/eskres)

## Deployment link:

Our project can be viewed by clicking this link. [https://bit.ly/Nutrico2](https://bit.ly/Nutrico2)

(link doesnt work as trying to host project elsewhere now as Heroku are starting to charge)
#

## Technologies Used:

I spent the previous two weeks prior to the course focusing on the below and used them to create our project:

- Python
- Django
- SQL
#

## Brief:

The brief for the project stipulated the below:

- Create the application using at least 2 related models, one of which should be a user

- Include all major CRUD functions for at least one of your models

- Add authentication AND authorisation (page protection) to restrict access to appropriate users:

        - User must be able to sign up or login

        - Signed in user must be able to change password and logout

        - change password and logout must only be available to logged in users

- Give feedback to the user after each action, and after form submissions with success/failure

- Clear forms after submission failure

- Manage team contributions and collaboration using a standard Git flow on Github

- Layout and style your front-end with clean & well-formatted CSS, with or without a framework. Put effort into your design!

- Deploy your application online so it's publicly accessible; we will walk through the setup

A number of bonus options were also suggested:

- Allow user to change website theme, Dark mode etc

- Include Pagination

- Utilise 3rd party API's

- Sent verification email upon registration

- Allow users to upload image files

- Password reset using an email
#

## Planning:

As the General Assembly course was entirely remote we communicated exclusively through Zoom and Slack. We spent all working day on Zoom together and then (due to different schedules outside of the course) we communicated during the evenings and weekends via slack.

We discussed the Technical Requirements and from the off decided we wanted to push ourselves and strive for a number of the bonus options; these being:

- Utilise 3rd party API's

- Allow users to upload image files

- Send verification email upon registration

- Password reset using an email

We had a couple of ideas:

- **Green Social Network:**

Users could sign up and create a profile. They could share hints and tips for leading a green and more sustainable lifestyle. They could review and link to green products or companies.

- **Food Receipt App:**

Users could sign up and upload receipts of their weekly supermarket shops.

We would then provide a C02 figure of their shop and highlight products with high carbon footprints so users could appreciate the impact of their weekly shop or their choice of a certain product.

Although we liked the Food Receipt App idea there just wasn't sufficient enough data online to support the idea. Whilst we could find emissions data for food we struggled to locate anything useful for cleaning products, toiletries etc. Any API we were able to locate focused primarily on emissions created from supply chains and logistics and weren't suitable for our requirements.

However during our research for the above idea I found an image to text API which we were keen to use and Einar found data (both for nutrition and carbon emissions) for raw food ingredients.

Then we came up with the idea of a recipe app that provides users with nutritional information and the C02 emissions of raw ingredients. Users could upload a photo of ingredients from a recipe book; we would convert this to text and provide them with a list of nutritional information and the C02 emissions of the ingredients.

I set about testing the [API](https://apilayer.com/marketplace/image_to_text-api) to confirm if it was viable for our intended use. I located stock ingredients photos online and ran them through the API live demo:

![](./readme-images/Screenshot%202022-11-20%20at%2010.46.44.png)

The results of which appeared as below:

![](./readme-images/Screenshot%202022-11-20%20at%2011.37.24.png)

The full output from the API test can be found [here](./api-output.py).

We decided that although it was viable we would need to give the User the ability to edit the results of running an image through the image to text API to make the text more usable.
#

### Wireframe:

I completed the Wireframe as below and Einar worked on the ERD.

We had both previously expressed that we liked the Pinterest homepage so I incorporated this into my Wireframe. My full Wireframe can be viewed here (LINK)
#

### User Stories:

We created User Stories together which we used to 'tick off' features once complete:

- As a new user I want to be able to sign up to the site.
- As an existing user I want to be able to change my password.
- As an existing user I want to be able to request a password reset by email.
- As an existing user I want to be able to delete my profile
- As a user I want to be able to upload and view a recipe.
- As a user I want to be able to add custom ingredients.
- As a user I want to be able to add my custom ingredients to my recipes.
- As a user I want to be able to view other's recipes.
- As a user I want to be able to edit or delete my recipes.
- As a user I want to be able to see the nutritional value of my recipes.
- As a user I want to be able to see the C02e emissions of my recipes.

## Trello Board:

I then created a Trello Board and we both populated it with "To Do" tasks:

![](./readme-images/Screenshot%202022-11-20%20at%2010.50.18.png)

However, as time went on we didn't feel a need to use it. We were both clear on what we were doing as well as what each other were doing and were responsible for. Our communication throughout was also excellent; we were constantly updating each other with progress of what we were working on and effectively rendered our Trello board redundant.
#

## Delegation of work:

After a short discussion I volunteered to be Team Leader; my partner expressed they were a little uncomfortable presenting; something I was a little more confident with.

I was also keen to have first hand experience of managing merges and conflicts over GitHub as well as deploying via Heroku; the main other responsibilities as team lead.

We finalised our idea late on Friday and Einar advised he couldn't work on the project over the weekend so we agreed it best that I be responsible for creating the basic files/folders, functionality and user authorisation/authentication.

Einar would focus on collating the necessary nutrition and emissions data as well as the headline features of connecting the image to text API and image upload etc.
#

## Build/Code Process

### Step 1:

I created our base.html file and then extended the file to every other html page I had created; as well as the block content. I then populated each block content field to act as a placeholder on each file; for example the homepage and recipe detail files:

![](./readme-images/Screenshot%202022-11-20%20at%2010.51.18.png)

I then started to populate some of the python files with the basics; for example the urls.py file:

![](./readme-images/Screenshot%202022-11-20%20at%2010.51.27.png)

And the view.py to tie the website together:

![](./readme-images/Screenshot%202022-11-20%20at%2010.51.50.png)

Before then creating some basic models:

![](./readme-images/Screenshot%202022-11-20%20at%2010.52.00.png)

I then ran migrations (python3 manage.py makemigrations/python3 manage.py migrate) to connect and push the tables to pgAdmin. However despite there being no error messages or problems the tables folder failed to populate in the Database.

I was keen to make progress on the project and believing I could resolve the migration issue at a later stage I moved on.

### Step 2:

Einar had previously located [fullPage.js](https://alvarotrigo.com/fullPage/) used on the Pinterest homepage. I set about implementing fullPage.js on our own project homepage.

I ran "npm install fullpage.js" to install fullPage.js. Then I linked the base.html file to the relevant stylesheets:

![](./readme-images/Screenshot%202022-11-20%20at%2010.55.07.png)

And then linked the home.html file to the relevant JS scripts as below:

![](./readme-images/Screenshot%202022-11-20%20at%2010.55.22.png)

I then created the necessary divs with the relevant class names and IDs:

![](./readme-images/Screenshot%202022-11-20%20at%2010.55.30.png)

This resulted in our homepage appearing as below:

![](./readme-images/Screenshot%202022-11-20%20at%2010.55.43.png)

Each section (Food info/C02 info and Sign up) should have taken up the full height and width of the browser window. It should then have been possible to scroll up/down to move between each section.

I realised I should have linked to the external scripts before running the local jQuery so moved the external scripts above. However I still couldn't get fullPage.js to work so I replaced the jQuery with Vanilla JS:

![](./readme-images/Screenshot%202022-11-20%20at%2010.55.53.png)

This resulted in fullPage.js then working; the result of which can be seen on our deployed website.

### Step 3:

I further populated the urls.py file with urls for the CRUD operations of the recipes and ingredients:

![](./readme-images/Screenshot%202022-11-20%20at%2010.57.25.png)

Then started working on the CRUD operations themselves:

![](./readme-images/Screenshot%202022-11-20%20at%2010.57.35.png)

Using our ERD as a guide I then started to populate our models:

![](./readme-images/Screenshot%202022-11-20%20at%2010.57.46.png)

### Step 4:

Having now created the CRUD operations and Models I thought it best I turn my attention back to connecting to pgAdmin. Coming back with fresh eyes I soon realised I hadn't imported the Recipe and Ingredient models into Views.py.

Desipite having now done so the migrations still didn't populate pgAdmin so to be safe; I deleted all the existing numbered migration files in the migrations folder, renamed the database in Settings.py, created a new database in pgAdmin to match and then ran migrations again. This time the Tables folder in pgAdmin successfully populated.

### Step 5:

I then started work on User Authentication and Authorisation as one of the major points of the brief was the below:

- Add authentication AND authorisation (page protection) to restrict access to appropriate users

I started to create a basic user model in models.py: 

![](./readme-images/Screenshot%202022-11-20%20at%2011.01.18.png)

As well as a user/detail.html file in templates.I then started to replace some of the pseudo code I had previously written with authentication to secure a number of our pages from the options in the nav bar:

![](./readme-images/Screenshot%202022-11-20%20at%2011.01.32.png)

Before then adding a number of paths to urls.py:

![](./readme-images/Screenshot%202022-11-20%20at%2011.01.58.png)

### Step 6:

Our brief stipulated that we "give feedback to the user after each action, and after form submissions with success/failure" so I implemented success and error messages for things like adding a recipe; logging in/out and registration:

![](./readme-images/Screenshot%202022-11-20%20at%2011.04.49.png)

However; I then realised I would have to create classes and CSS styling for each type of message; success, error, warning etc. I thought there must be a better way to implement messages and their different types. I researched what was available in Django and settled on the inbuilt messages framework.

to do so via Django's inbuilt messages framework; meaning I could take advantage of each messages styling:

![](./readme-images/Screenshot%202022-11-20%20at%2011.04.59.png)

So each message appeared in exactly the same place (regardless of what page you were on) I created a messages.html file:

![](./readme-images/Screenshot%202022-11-20%20at%2011.05.10.png)

Which I then included on our nav.html file below the nav bar itself so all messages would appear directly below the nav:

![](./readme-images/Screenshot%202022-11-20%20at%2011.05.22.png)

### Step 7:

I wasn't happy that I hadn't as of yet achieved the bonus goals I had set myself of:

- Send verification email upon registration.

- Password reset using an email.

So much so that on the last full day of the project I made a conscious decision to focus on doing so rather than focusing on the appearance and CSS styling of our website.

I researched the best way of achieving the verification and password reset by email and realised it wasn't possible with our existing User model and that to be able to do so I would need to use Django's built in (and automatically installed) Auth app; django.contrib.auth.

I learnt that Auth provides several authentication views and URLs for handling login, logout, and password management:

![](./readme-images/Screenshot%202022-11-20%20at%2011.07.45.png)

And each URL has an associated auth view to which I only needed to create a template to use. For example; to create a login page I just needed to create a login.html file within a folder called registration which itself was in a folder called templates. Then make reference to the registration folder within templates in settings.py.

Then in views.py I created my own SignupView, PasswordChange and PasswordReset classes:

![](./readme-images/Screenshot%202022-11-20%20at%2011.07.53.png)

I discovered I had to use reverse\_lazy for the success\_urls because for all generic class-based views the urls are not loaded when the file is imported, so I had to use the lazy form of reverse to load them later when they were available.

I then created my own password\_change and password\_change/done html pages to replace the existing Django administration templates:

![](./readme-images/Screenshot%202022-11-20%20at%2011.08.13.png)

![](./readme-images/Screenshot%202022-11-20%20at%2011.08.56.png)

As well as my own password\_reset and password\_reset/done pages:

![](./readme-images/Screenshot%202022-11-20%20at%2011.09.17.png)
![](./readme-images/Screenshot%202022-11-20%20at%2011.09.31.png)

Although I never achieved sending a verification email upon registration I did however achieve the stretch goal of Password reset by email. Albeit there was no back end email client (such as MailGun or SendGrid) so the emails weren't sent to registered users but instead stored in a sent\_emails folder which I achieved by adding the below to settings.py:

![](./readme-images/Screenshot%202022-11-20%20at%2011.09.53.png)

The cryptographically secure emails appeared as below with a one-time link to a password reset page:

![](./readme-images/Screenshot%202022-11-20%20at%2011.10.03.png) 

By this point I had run out of time and didn't have a chance to either; update the emails with my own text or create our own 'set-password'/'reset/done' HTML pages to which I could extend our base.html file or bootstrap styling. Hence both pages currently use the Django administration templates:

![](./readme-images/Screenshot%202022-11-20%20at%2011.10.34.png)
#

## Challenges:

- In hindsight basing our project around two of the bonus options (Utilise 3rd party API's/Allow users to upload image files) wasn't the best idea. All other teams in our cohort had been placed in teams of 3 and we were the only pair so we were a little disadvantaged from the off. It was silly to have made the decision we did and forced ourselves into such a corner from day 1. We should have set our sights slightly lower; on a project that was easier to achieve in the given time frame to which we could then have connected a 3rd party API/user image upload if time allowed.
#

## Wins:

- I was very happy to have successfully integrated the password reset by email. Although the resulting email only appears in VS Code and isn't sent to a user's email address I was the only individual in our cohort to achieve this; despite larger teams having people focused solely on authentication.
- Our communication and teamwork were exemplary. We held catch ups at the start and end of each day, fixed multiple issues together whilst screen sharing and pair coding (via Live Share in VS Code) and when we weren't on zoom together we were in constant communication via slack.
#

## Key Learnings & Takeaways:

- To always focus on the functionality first. There's no need to collect circa 400 data points; we could have created and tested our website with 20 data points and then added to our data at a later date. In hindsight as Team Leader this is something I should have voiced at the time.
- As previously mentioned in Challenges we set our sights too high from the off; we should have set them slightly lower on a project more achievable in the timeframe. Had time allowed we could then have expanded our project and connected to an API.

## Bugs:

- When a new User clicks on Sign Up and then Register an alert appears in the browser (as below) before a User has even entered any information. It's also no possible to clear this message by pressing the 'X' to the right:

![](./readme-images/Screenshot%202022-11-20%20at%2011.21.56.png)

- The image location appears in both the Recipe index and the Recipe itself if you view the individual Recipe page:

![](./readme-images/Screenshot%202022-11-20%20at%2011.22.23.png)
![](./readme-images/Screenshot%202022-11-20%20at%2011.22.47.png)

- The function to add customer ingredients to recipes doesn't work; if you attempt to do so you receive an " **IntegrityError"** message screen.
- The View My Recipes page isn't linked to the specific user viewing the page. Any user that clicks this option receives the full list of recipes on the website as opposed to those uploaded to them and directly linked to their details.
- The same goes for the View My Ingredients page; this lists all ingredients added by all users as opposed to those added by the specific user viewing the page.
#

## Future Improvements:

- To resolve all of the above bugs.
- To link email functionality to a server host (sendgrid or mailgun) so emails are sent to user's as opposed to just being created and stored in VS code.
- To improve upon the email functionality and user experience by sending an email to the user to confirm registration.
- To populate the about page with information about ourselves and an explanation as to where we got our data from. It is currently just a placeholder and needs to be populated; we were using it to experiment with a carousel effect.
- To include pagination (another bonus objective mentioned in the brief) when the number of recipes added reaches a point where it is no longer logical to conitnue scrolling down a page. 
- To update the set-password and reset/done HTML pages from the Django templates to our own HTML pages with base.html etc.
- Allow users to upload a profile picture which will appear on the right of the nav bar.
- Update the edit page to allow users to change their profile picture as well as their email address etc.
- To remove any legacy code from the previous use of 'User' before implementing Auth.
- To reinstate some of the user feedback messages I lost from doing the above.
- To include CSS styling; we felt the functionality of our website was of higher priority than the styling. We were happy styling is something we could quickly add further down the line once we had hit the stretch goals we were aiming for.