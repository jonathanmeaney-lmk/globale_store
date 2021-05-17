# **TESTING** 

- The website was tested on Google Chrome, Microsoft Edge, Firefox and Safari browsers.
- The website was viewed on a variety of devices such as Desktop, Laptop, Tablet, iPhone 6s, iPhone SE, Huawei Y6, Huawei P9 and Samsung Phones. The website was found to be responsive across all of these devices. 
- A large amount of testing was done to ensure that all pages were linking correctly, and buttons and forms sections were working as intended (more details below).
- Friends, family members and fellow Code Institute students were asked to review the site and documentation to point out any bugs and/or user experience issues.

<hr>

## **USER STORIES TESTING**

*Note that the actual functionality testing of the features outlined in the User Stories section will be covered in the Functionality Testing section.*

### **<u>Visitor Goals</u>**

### **General searching and browsing**

**1. I want to generally browse all of the products on the GlobALE store**

- On landing on the homepage, users can click on the 'All Products' navbar link or 'BUY BEER' call-to-action button to see a list of all products available on the store.

**2. I want to search products available on the GlobaALE store by category**

- Users can click on the 'Category' or 'Country' navbar links to browse the products by beer type (ales, lagers, stouts, etc.) or by country.

**3. I want to find a particular product I am interested in by name or description**

- Users can search for a particular product by typing keywords in the Searchbar located in the navbar, which will display a list of results of products containing the keywords entered.

**4. I want to view more detailed information on a particular product I am interested in purchasing**

- Users can click on the product, which will direct them to the product detail page, which contains more detailed information on the product, including description, brewer, size, ABV, and a list of product reviews. 

### **Log In, Registration and User Profiles**

**1. I want to sign up as a registered user of the GlobALE store**

- Users can click on the Profile dropdown menu in the navbar and choose 'Register'.
- On the Register page, they can fill out the simple registration form which will prompt a verification link to be sent to their email once they submit the form. They will be instructed to go their email to verify their email address through the link.
- After clicking on the verification link in the email, they will be redirected to the site's Confirm Email page. Upon pressing 'Confirm', the new registered user will be directed to the Sign In page, where they can log in with their new details. A message will appear to say thay their email has been confirmed successfully.

**2. As a registered user, I want to sign in to the GlobALE store**

- Users can click on the Profile dropdown menu in the navbar in the navbar to choose 'Sign In'
- Having entered their credentials correctly in the Sign In form, users can click 'Sign In', which will display a message to inform them that they have signed in correctly.

**3. As a signed in in user, I want to view my personalized user profile and add/edit my delivery details for storage**

- Users can click on the Profile dropdown menu in the navbar and choose 'My Profile'.
- Here they can add or update their delivery details by filling out/updating the form and click 'Update Information'. A message will appear to say that they have updated their information successfully.

**4. As a signed in user, I want to view past orders**

- Users can click on the Profile dropdown menu in the navbar and choose 'My Profile'.
- Here they can view a list of all past orders. For each order they can click to 'See Details' or 'File Issue'. 

**5. As a signed in user, I want to log out of the GlobALE store**

- Users can click on the Profile dropdown menu in the navbar and choose 'Log Out'.
- Having clicked the 'Log Out' button on the Log Out page, a message will appear to say that they have successfully logged out of the system. 

**6. As a registered user, I have forgotten my password and would like to reset it in order to sign in.**

- On the Sign In page, users can click the 'Forgot Password' link, which takes them to the Password Reset page. 
- Having entered their email address and clicking 'Reset My Password', they are informed that they have received an email. Clicking on the link in this email will take them to the Change Password page.
- On the Change Password Page, they can enter their new Password. Once they submit, a message will appear to say their password has been successfully updated. 
- At this point, they can now successfully sign in with their new password. 

### **Storing items for purchase and making purchases**

**1. Having chosen a project I want to purchase, I want to select the quantity of the product and add it to a shopping cart to make it available for purchase at a later point.**

- Users can click on the chosen product to open the product detail page (as described above in the General searching and browsing section). Here they can use the input bar to select a quantity from 1-99. 
- Clicking 'Add to Cart' will add the desired quantity of the product to their shopping cart. A message will appear to say that the desired quantity of the selected product has been added to their cart. 

**2. I want to easily view my shopping cart at any point, and delete or update products or items currently in my shopping cart.**

- Users can access their shopping cart by clicking on the Shopping Cart icon in the navbar. 
- Here they can see all of the items in their shopping cart, as well as all relevant cash totals (line item subtotal, final order total, delivery charge and grand total).
- Users can easily update the quantity of products by using changing the quantity in the input bar and clicking update. A message will appear to say that the product quantity has been updated successfully.
- Users can easily delete a product by clicking the delete button (represented by a trashcan icon). A message will appear to say that the product has been deleted successfully.

**3. I want to proceed to purchase the items in my shopping cart.**

- On their Shopping Cart page, once users are happy with the content of their cart, they can proceed to the checkout page by clicking the 'Go to Checkout' button. 

**4. I want to easily add my delivery details and make a secure payment with my credit card.**

- On the Checkout Page, users can fill out the form broken into three fields: Name & Email, Delivery Details, and Payment.
- The Email and Delivery Details fields will be autofilled for registered users who have added their delivery information to their profile page.
- Once the three form fields have been completed correctly, the user can click 'Complete Order' to confirm the order and payment. They will then be directed to the Order Confirmation Page, which includes their order number and a review of their order.   

### **Post-purchase**

**1. I want to view an order/payment confirmation.**

- Users will be directed to their Order Confirmation page once they Complete an order (as described directly above).
- Registered users can view order confirmations by clicking on the Orders section of the Profile dropdown menu in the navbar (as outlined in the Log In, Registration and User Profiles section above).
- Both registered and unregistered users will recieve a confirmation email once an order is completed.

**2. I want to contact GlobALE to file an issue or query about a particular order.**

- Registered users can file an issue about a particular order by clicking on the Orders section of Profile dropdown menu. Here they can click the 'File Issue' button on the order in question, which will direct them to the Submit an Order Issue page.
- On the Submit an Order Issue page, they can fill out the simple Issue form. Clicking 'Submit' will file their issue with admin. A message will appear to say that the issue has been logged successfully.
- Unregistered users can file an issue or query by responding to the Order Confirmation email they received when they completed their order. 

**3. I want to leave feedback/review of a product for fellow site users.**

- Registered and logged in users can access the Leave a Review form on the Product Detail page. 
- Having filled out the form and clicked 'Submit', their review will be immediately added to and appear on the Reviews section of the Product Detail page. They will receive a message to say that their review has been submitted successfully.  

### **<u>Site Owner/Admin Goals</u>**

### **Product management**

**1. I want to add a new product to the GlobALE store.**

- Admin users can click on the Profile dropdown menu in the navbar and choose 'Product Mangagement' which will take them to the 'Add a Product' page.
- Having filled in the form correctly and clicked 'Submit', the new product will be added to the database.
- Users are then directed to the Product Detail page for the new product. A message will appear to say that the new product has been added successfully. 

**2. I want to update/edit an exisiting product on the store.**

- Admin users can click on the 'Edit' link on the Products page or Product Detail page. This will direct them to the 'Edit a Product' page. This link only appears for admin users.
- On the Edit a Product page, users can make any neccesary changes to the prefilled form. The form is prefilled with the product's existing details. 
- Having updated the form correctly and clicked 'Submit', the the changes will be applied to the product on the database.
- Users are then re-directed to the product detail page where they can see the changes applied. A message will appear to say that the product has been updated successfully. 

**3. I want to delete an existing product on the store.**

- Admin users can click on the 'Delete' link on the Products page or Product Detail page. This link only appears for Admin users.
- Clicking this link will remove the product from the database. A message will appear to say that the product has been deleted successfully. 


### **Customer queries, issues**

**1. I want to view customer order issues or queries.**

- Admin users can log into the Django admin to view a list of order issues arranged in date order. Clicking on the order issue will open the Order Issue page containing all the order issue details submitted by the user. 

**2. I want to deal with and manage customer issues and queries.**

- Admin users can contact the User that has filed the order issue by using the email provided when the user submitted the order issue. Once an issue has been resolved, in the Order Issue page in the Django Admin, admin users can select 'Yes' in the 'Query Resolved' field to close the Order Issue. 

<hr>

## **FUNCTIONALITY TESTING**

*The following functionality and interactive features of the entire website were checked to ensure they are working correctly:*

### **Navbar and Homepage**

- GlobALE Logo: When clicked, returns user to the homepage.
- All Beers link: Changes color when hovered over, when clicked, directs users to the All Beers page.
- Categories Link: Changes color when hovered over. Opens dropdown menu when clicked. Each category link directs the user to the correct chosen category page.
- Countries Link:  Changes color when hovered over. Opens dropdown menu when clicked. Each country link directs the user to the correct chosen country page. 
- Profile link: Changes color when hovered. Opens dropdown menu when clicked. Each link in the drop down menu directs user to correct page.
   - When a user is not signed in: the dropdown menu only displays the 'Register' and 'Sign In' links.
   - When a regular user is signed in: the dropdown menu displays the 'My Profile', 'Orders' and 'Sign Out' links.
   - When a admin user (superuser) is signed in: the dropdown menu displays the 'Product Management', 'My Profile', 'Orders' and 'Sign Out' links.
- Shopping Cart link: Changes color when hovered. When clicked, directs user to the Shopping Cart page.
- Buy Beer button: Changes color when hovered over. When clicked, directs users to the All Beers page.
- Search bar: 
  - When user clicks the search button after entering a keyword, user is shown a correct list of products containing those keywords. 
  - A feedback message title is displayed informing them of the number of results for the keyword entered **PICTURE 1**.
  - If a user clicks the search button without inputting a word in the search bar, a message is displayed to warn them that they have not entered any search criteria, and they are redirected to the All Beers page. **PICTURE 2**
- Responsive design:
    - 'Hamburger' toggle button: For smaller screens, the hamburger toggle button appears and, when clicked, shows/hides navbar links. 
    - The homepage image is repositioned, and slogan becomes smaller and is repositioned. Buy beer button is also repositioned. **PICTURE 3**

### **Products Page**
- When a user is on the 'All Beers' / general Products page, they are shown all of the products on the store, which are displayed in alphabetic order.
- Each product card contains the correct image, name, category, country and price. 
- When a user hovers over a product, the border changes color. When they click on the product image, they are taken to the Product Detail page.
- When a user clicks on the 'country' link in the product card, they are directed to the correct category page.
- When a user clicks on the 'category' link in the product card, they are directed to the correct country page.
- When a user lands on the Products page after having chosen a particularly category or country, they are shown a correct list of products for that particular chosen country or category only. The correct page heading displays for each chosen category or country.  **PICTURE 4 / PICTURE 5**
- Responsive design:
  - Four product cards displayed per row for laptop / monitor screens
  - Two product cards displayed per row for tablet screens.
  - Images and texts resized to allow two products to be correctly displayed per row correctly for mobile screens. **PICTURE 6**

### **Product Detail Page**

- Clicking on a product from the Product page, directs users to the correct Product Detail page, which renders the product image, all relevant product information (name, brewer, description, price, size, ABV), a quantity input and 'Add to Cart' button, as well as a reviews form (if user is logged in) and product reviews (if any).

- Above the product image, three 'back' links appear allowing users to return to the All Beers section, or the relevant category or country. When clicked, each link returns user to the correct All Beers, category or country page. **PICTURE 7**

- For users that are not logged in, the reviews form is not displayed, instead a message is displayed prompting them to sign in or register to leave a review. **PICTURE 8**

- For a product that does not have reviews, a message appears to inform the user that no reviews have been added for the product yet. **PICTURE 9**

- Adding product to shopping cart:
  - Quantity Inputs:
    - 'Plus' button increases the quantity by one with each click. 
    - 'Plus' button is disabled when user reaches 99
    - 'Minus' button decreases the quantity by one with each click. 
    - 'Minus' button is disabled when quantity is at 1. As such, 'Minus' button is initially disabled as the default quantity is 1. Once user clicks the 'Plus' button once to reach 2, the 'Minus' button is enabled.

  - 'Add to Cart' button:
    
    - Changes color when hovered over.
    - Once user clicks the 'Add to Cart' button, the selected quantity is added to their shopping cart.
    - A message appears to inform them that the selected quantity of the product has been added to the shopping cart. 

    - Shopping cart icon turns from white to orange to indicate there is something in the Cart, and next to it a number is displayed representing the number of items in the cart. **PICTURE 10**

    - Should a user accidentally delete the quantity from the input bar and then click 'Add to Cart', the quantity will be set to 1 as default and 1 item of the product will be added to the cart. A message appears to inform them that 1 item has been added to their cart.

- Review Form:

    - Review form displays for logged in users only.
    - When user completes form and clicks submit (submit button correctly changes color when hovered over), their review is immediately added to top of the reviews section (reviews are displayed in date order, most recent first), along with their username and the date of the review.
    - A message appears to tell them that there review for the product was added successfully added.
    **PICTURE 11**
    - If user  does not choose a rating, a default rating of 3 will be submitted.
    - If user leaves review content text input empty, the review will be submitted with just a rating.



      
