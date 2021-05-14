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