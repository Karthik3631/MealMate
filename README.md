MealMatebuddy
________________
MealMatebuddy is a full-stack food ordering platform that enables customers to browse restaurants, place orders, and make secure payments. Vendors can manage restaurant profiles, orders, and menus through a role-based access system. The platform ensures secure user authentication and authorizes access to specific resources for designated roles.

Features
Customer Features
Registration and Login: Customers can register and log in to place orders. Only active users can access the platform.

Profile Management: Customers may edit personal details such as name and email.

Order Management: Customers can view order history, including restaurant, items, total price, and order status.

Marketplace: Allows browsing a curated list of approved restaurants.

Order Placement: Supports placing orders from multiple vendors and viewing available menus.

Payments: PayPal integration for convenient order payments.

Access Control: Unauthorized access to vendor-specific content is blocked with error messaging.

Vendor Features
Registration and Login: Vendors register/login to manage their restaurants and orders.

Restaurant Management: Vendors add/edit details like categories, menu items, and opening hours.

Order Management: Provides a dashboard for managing orders, customer info, and payment status.

Marketplace Display: Vendors are listed after backend approval.

Access Control: Unauthorized access to customer-specific pages is blocked.

Backend & Admin Features
Approval Process: All new restaurant listings require admin approval before becoming visible.

User Management: Admins activate, deactivate, or manage vendor and customer accounts.

Order Verification: Vendors can verify/update order statuses.

Error Handling & Security
Authentication & Authorization: Strict login and permission checks across all roles.

Unauthorized Access: Users are redirected to an "Unauthorized User" page if they access blocked resources.

Error Handling: Proper feedback and redirection on errors and failed access attempts.

Database Requirements
Users Table: Stores customer and vendor data, tracks roles and active/inactive status.

Restaurants Table: Holds restaurant details, menu, categories, hours, and approval state.

Orders Table: Tracks all orders, items, prices, payment, and statuses.

Menus Table: Stores menu items per restaurant.

Categories Table: Classifies food items for each restaurant.

Technologies and Tools
Frontend: HTML, CSS, JavaScript

Backend: Django (with Django REST Framework) or Flask

Payment Integration: Razorpay API (for payment processing)

Error Handling: Robust error and access control management
