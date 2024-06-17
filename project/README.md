# Book's Brightness
### Video Demo:  [Books Brightness](https://www.youtube.com/watch?v=42CYYqUiFeI)
### Description
The **Book's Brightness** web app is designed thoughtfully, with various features grouped into clear categories. This README file provides a detailed overview of the project's structure, explains each file's purpose, and sheds light on the reasons behind specific design choices I made during the development.
Project Structure
## App.py:
The main backend application, app.py, is divided into several key categories of routes:
# User Authentication:

The user authentication routes contain functionalities for registration, login, logout, account removal, and checkout. These features are backed by tests that handle form validation, ensuring a secure and user-friendly experience. I included the CS50 cat meme within the apology messages. To add a playful touch to the user experience.
# Link Management:

The link management routes handle the following links: About Us, Coming Soon, Delivery Information, Privacy Policy, Terms and Conditions, and Payment. The primary objective of these routes is to redirect users to other templates. I also used samples from other websites to create the structure of those templates (about us, delivery information, privacy policy, and terms and conditions).
# Data Display:

The data display routes are responsible for presenting server-side data (e.g., products and user information). Routes included are grade, novel, curriculum, product, profile, cart, and catalog. In those routes, the code selects specific data from the database file using SQL, and then it display it on the front-end side for the user.
# Product Details and Cart Functionality:

These are product details and add-to-cart routes. The first is responsible for displaying the product details to the user. It fetches a specific product according to its ID and then displays it. The second, which is within the same template, adds the product to a user's cart. The user can only add a product to the cart when he logs in. I chose this method so I could manage the relationship between each table in the database easily. I searched a lot to understand the link between those parts of the project and to be able to implement it correctly. The structure of the SQL code for those two is simple because the user has to be logged in to add anything to the cart and purchase something. As I continue to learn more, this will be updated in future versions so that anyone can add to the cart and purchase items.
# Additional Features:

The subscribe route is added so the user receives updates and/or newspapers related to the business. This is a standard function on all e-commerce websites. It has a table in the database for storing customers' emails. I added it after realizing, it is better than adding mails according to each user account.
## Help.py
The help.py from the finance problem set is a file that contains helpful functions such as (usd, login_required, apology). I kept it in my project because it was easier that way.

### Templates:

*The templates folder contains multiple templates, categorized into dynamic templates (e.g., profile, cart) and static templates (e.g., company information templates).*

To enhance the user's sense of engagement and personalization, the user profile contains user information and his order history. The design is simple, and the colors are a black-to-white transition.
The index template serves as the catalog for the shop's products. It provides the user with the content of the website. I used a sample of products from online pages (I mentioned that in the acknowledgment file) to illustrate the outcome of the final product.

The apology template contains the apology cat meme from the CS50 finance set.

The books template displays all products that are books from the database. The data gets retrieved using SQL at the back end.

Grade, novel, and curriculum templates display all products, categorized by their category of books in the database. The data gets retrieved using SQL at the back end.

The products template displays all non-book products from the database. The data gets retrieved using SQL at the back end.

Register, remove, check out, and login are responsible for displaying forms. Their purposes are the following: to create an account, to delete an account, to enter their personal information, and to log in. I wanted to maintain a sense of harmony between each template, so I used the same CSS design for those templates.

The cart contains all the items the user may add. All are organized in a table that shares the same CSS file as the profile template to maintain a minimal, modern design.

Payment contains two links for the payment methods that lead the user to the checkout. For now, the only option for the user is to pay for delivery. Online payments will be included in future versions of this website. If the user chooses online payment, he will be redirected to the coming soon template.

The layout is the main template of the project. It contains the nav bar, the footer, the newsletter section, the main content section, and the features sections. In the design of this template, I tried to maintain a minimalistic and modern design. I searched for multiple inspirations online to choose a specific structure for my website. I noticed that library shops tend to be bland and classic design-wise, so I wanted to break free from that. I added a unique design features section. The navbar is fixed while scrolling, so the user can easily navigate through different pages without having to scroll up. There are multiple ways to do that, but I thought this way looked best. The main section displays the index template. It contains a catalog of the available products, which leads the user to a more specific page for each product. It is the section that the other templates get extended to. The newspaper section is where the user can submit to receive journals or news about the shop. The footer section is inspired by various examples (look in the acknowledgments file). It contains the logo of the project, which I created using Canva. I followed a modern design for it as well. In addition to the social media links, company information, the option to log in from there, apps, and payment links, which would be added in a future version of the web app as I continue to enhance my knowledge in this field,

## Statistics:

The statistics folder consists of the images and CSS files, with distinct CSS files created for each template group. This organization ensures a cohesive and visually appealing design throughout the application. The design of this web app was created with modern aesthetics, employing a simple yet elegant color palette and clean design principles to ensure a visually pleasing and user-friendly interface.

**The CSS files are separated into distinct categories:**

form.css = This is the styling file for the forms template. It follows a clean transition of colors from brown to grey in the edges.
productdetails.css = This is the styling file for the templates of the products details. It is a simple standard design.
products.css = This is the styling file for templates that display products( index, books...). It is simple and modern. I chose gold as a color for the price to break the color pattern and to highlight it.
profile.css = This is the styling file for the profile and cart. Both tempaltes display the data in a table form.
styles.css = This is the styling file for the layout template.
 *You can notice that almost all the templates in one way or another have the a very close deign pattern.*

## Database:

The library file is the database; it is responsible for storing product information and user information. The tables are users, orders, carts, and mail. Currently, it contains samples of data (not the actual products or users). Of course, when this website launches officially, it will contain real data about the shop.

## Rest of the files:
Requirements is a file that contains the needed packages for my project.

The acknowledgment file contains a list of resources (such as Overflow, GitHub, etc.) that I used to understand certain aspects of creating an e-commerce website that I failed to learn or create on my own. Furthermore, I included code comments on top of certain parts to explicitly distinguish parts of code that I used help for. I also left comments in the CSS files that mention credit for where I was inspired for my design choices, such as the design of the log-in file.

Check.sql and output.txt are files used to test the functionality of my project and the database. I tested each part at a time to fix errors and make the needed changes smoothly.

The readme file is an explanation of each file in this project. It contains the video link to my project and a detailed explanation of the functionality of each file in my project.

Furthermore, I included comments in almost all of my code to explain the specific job of certain sections and to mention credits. I don't have any partners in my project, so I used online help from the resources mentioned in the acknowledgment file.

> [!NOTE]
> I am going to work on major parts of my project after my submission. Things like responsiveness, online payment, future apps, etc.


