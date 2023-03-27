=================================================
Manage perishable products using expiration dates
=================================================

In Odoo, *Expiration Dates* can be used to manage (and track) the lifecycles of perishable
products, from purchase to sale. Using expiration dates reduces product loss due to unexpected
expiry, and helps to avoid sending expired products to customers. In Odoo, only products that are
tracked using *Lots* and *Serial Numbers* can be assigned expiration information. Once a lot or
serial number has been assigned, an expiration date can be set. This is especially helpful for
companies (such as food manufacturers) that consistently (or exclusively) buy and sell perishable
products.

.. seealso::
  - :doc:`lots`
  - :doc:`serial_numbers`

Configuration
=============

To enable the use of *Expiration Dates*, go to :menuselection:`Inventory --> Configuration -->
Settings`, and scroll down to the :guilabel:`Traceability` section. Then, click the
:guilabel:`checkbox` to enable the :guilabel:`Lots & Serial Numbers` feature. Once that feature is
activated, a new option will appear to enable :guilabel:`Expiration Dates`. Click that
:guilabel:`checkbox` to enable the feature, and be sure to :guilabel:`Save` changes.

.. image:: expiration_dates/expiration-dates-enabled-settings.png
   :align: center
   :alt: Enabled lots and serial numbers and expiration dates settings.

.. tip::
  Once the :guilabel:`Lots & Serial Numbers` feature is activated, additional features appear to
  :guilabel:`Display Lots & Serial Numbers on Delivery Slips`; to
  :guilabel:`Display Lots & Serial Numbers on Invoices`; and to
  :guilabel:`Display Expiration Dates on Delivery Slips`. Activating these features helps with
  end-to-end traceability, making it easier to manage product recalls, identify "bad" batches of
  products, and more.

Configure expiration dates on products
======================================

Once :guilabel:`Lots & Serial Numbers` and :guilabel:`Expiration Dates` have been enabled in the
settings, expiration information can be configured on individual products. To do that, go to
:menuselection:`Inventory --> Products --> Products`, and select a product to edit. Once on the
product form, click :guilabel:`Edit` to make changes.

.. important::
  To be tracked using lots or serial numbers, or to have expiration information configured,
  products *must* have their :guilabel:`Product Type` set as :guilabel:`Storable Product` under the
  :guilabel:`General Information` tab.

Then, click the :guilabel:`Inventory` tab, and scroll down to the :guilabel:`Traceability` section.
From here, make sure that either :guilabel:`By Unique Serial Number` or :guilabel:`By Lots` is
checked. Once it is, a new :guilabel:`Expiration Date` checkbox will appear that will also need to
be clicked. Once both of those are enabled, a new :guilabel:`Dates` field will appear to the right.

.. note::
   If a product has stock on-hand prior to activating tracking by lots or serial numbers, an
   inventory adjustment might need to be performed to assign lot numbers to the existing stock.

.. tip::
  For processing large quantities of products on receipts or deliveries, it is recommended to track
  :guilabel:`By Lots`, so multiple products can be traced back to the same lot if any issues arise.

.. image:: expiration_dates/expiration-dates-product-configuration.png
   :align: center
   :alt: Expiration dates configuration on the product form.

Under the :guilabel:`Dates` field, there are four categories of expiration information to
configure for the product:

- :guilabel:`Expiration Time`: is the number of days after receiving products (either from a
  vendor or in stock after production) in which goods may become dangerous and should not be
  used or consumed.
- :guilabel:`Best Before Time`: is the number of days before the expiration date in which the
  goods start deteriorating, *without* necessarily being dangerous yet.
- :guilabel:`Removal Time`: is the number of days before the expiration date in which the goods
  should be removed from stock.
- :guilabel:`Alert Time`: is the number of days before the expiration date in which an alert
  should be raised on goods in a particular lot or containing a particular serial number.

.. note::
  The values entered into these fields will automatically compute the expiration date for goods
  entered into stock, whether purchased from a vendor or manufactured in-house.

Once all the expiration information has been configured, :guilabel:`Save` changes.

.. tip::
  If the :guilabel:`Dates` field is not populated with any values for expiration information, dates
  (and lots) can be manually assigned upon receipts and deliveries in and out of the warehouse.
  Even when assigned, they can still be overwritten and changed manually if needed, as well.

Use lots & serial numbers to set expiration dates on receipts
=============================================================

Generating expiration dates for *incoming* goods can be done directly from the purchase order. To
create a purchase order, go to the :guilabel:`Purchase` app and click :guilabel:`Create` to create
a new Request for Quotation (RFQ). Then, fill out the information by adding a :guilabel:`Vendor`,
and by adding products to the :guilabel:`Product` lines by clickng :guilabel:`Add a product`.
Choose the desired quantity to order by changing the number in the :guilabel:`Quantity` column, and
click :guilabel:`Confirm Order`. This will convert the :abbr:`RFQ (Request for Quotation)` into a
purchase order.

Click the :guilabel:`Receipt` smart button at the top of the purchase order to be taken to the
:guilabel:`Warehouse Receipt Form`.

.. note::
  Clicking :guilabel:`Validate` before assigning a serial number to the ordered product quantities
  will cause a :guilabel:`User Error` popup to appear. The popup requires entry of a lot or serial
  number for the ordered products. The :abbr:`RFQ (Request for Quotation)` cannot be validated
  without a lot or serial number being assigned.

.. image:: expiration_dates/expiration-dates-user-error-popup.png
   :align: center
   :alt: User error popup when validating an order with no lot number.

From here, click the :guilabel:`Additional Options` menu (hamburger) icon, and a
:guilabel:`Detailed Operations` popup will appear. Click :guilabel:`Add a line`, and assign a lot
or serial number under the :guilabel:`Lot/Serial Number Name` field. An expiration
date will automatically populate based on the configuration on the product form (if previously
configured). If the :guilabel:`Dates` field on the product form has not been configured, this date
can be manually entered. Mark the :guilabel:`Done` quantities, and click :guilabel:`Confirm` to
close the popup. Finally, click :guilabel:`Validate`.

.. image:: expiration_dates/expiration-dates-detailed-operations-popup.png
   :align: center
   :alt: Detailed operations popup showing expiration dates for ordered products.

A :guilabel:`Traceability` smart button will appear upon validating the receipt. Click the
:guilabel:`Traceability` smart button to see the updated :guilabel:`Traceability Report`, which
includes: a :guilabel:`Reference` document; the :guilabel:`Product` being traced; the
:guilabel:`Lot/Serial #`; and more.

Set expiration dates on manufactured products
=============================================

Expiration dates can also be generated for products manufactured in-house. To assign expiration
dates to manufactured products, a manufacturing order (MO) needs to be completed.

To create a :abbr:`MO (Manufacturing Order)`, go to :menuselection:`Manufacturing --> Operations
--> Manufacturing Orders`, and click :guilabel:`Create`. Choose a product to manufacture from the
:guilabel:`Product` :guilabel:`drop-down` menu, and choose a :guilabel:`Quantity` to produce.

.. image:: expiration_dates/expiration-dates-manufacturing-order.png
   :align: center
   :alt: Manufacturing order for product with expiration date.

.. note::
  To manufacture a product, there need to be materials :guilabel:`To Consume` in the
  :guilabel:`Product` lines. This can be achieved either by creating a :guilabel:`Bill of Material`
  for the :guilabel:`Product`, or manually adding materials to consume by clicking
  :guilabel:`Add a line`.

Click :guilabel:`Confirm`. Then, next to :guilabel:`Lot/Serial Number`, either select an existing
lot number from the :guilabel:`drop-down` menu, or click the green :guilabel:`+` sign to
automatically assign a new lot number. Then, mark the done :guilabel:`Quantity`, and
:guilabel:`Mark as Done`.

Click on the assigned :guilabel:`Lot/Serial Number` to be taken to a form for that number. Under
the :guilabel:`Dates` tab, all expiration information previously configured for the product will be
available. The same information is also available directly from the product form, or by going to
:menuselection:`Inventory --> Products --> Lots/Serial Numbers`.

.. image:: expiration_dates/expiration-dates-dates-tab-lot-number.png
   :align: center
   :alt: Dates tab with expiration information for specific lot number.

Sell products with expiration dates
===================================

.. note::
  To sell perishable products with expiration dates, the :guilabel:`Removal Strategy` for the
  :guilabel:`Location` the products are stored in must be set to
  :abbr:`FEFO (First Expiry, First Out)`. If there is not enough stock of perishable products in
  one lot, Odoo will automatically take the remaining quantity required from a second lot with the
  next-soonest expiration date. Removal strategies can also be set on
  :guilabel:`Product Categories`.

.. seealso::
    - :doc:`../../routes/strategies/removal`

Selling perishable products with expiration dates is done the same as any other type of product.
The first step in selling perishable products is to create a sales order. To do that, go to
:menuselection:`Sales --> Create` to create a new quotation, and fill out the information. Add a
:guilabel:`Customer`, click :guilabel:`Add a product` to add products to the :guilabel:`Product`
lines, then set a :guilabel:`Quantity`.

Then, click the :guilabel:`Other Info` tab. Under the :guilabel:`Delivery` section, change the
:guilabel:`Delivery Date` to a date after the expected date, and click the
:guilabel:`green checkmark` to confirm the date. Finally, :guilabel:`Confirm` the sales order.

Click the :guilabel:`Delivery` smart button at the top of the sales order to be taken to the
:guilabel:`Warehouse Receipt Form`. Click :guilabel:`Validate` and :guilabel:`Apply` to process all
:guilabel:`Done` quantities and deliver the products. If the products are delivered before
the :guilabel:`Alert Date` set on the product form, then no alerts will be created.

View expiration dates for lots & serial numbers
===============================================

To view and group all products with expiration dates by lot number, go to :menuselection:`Inventory
--> Products --> Lots/Serial Numbers`. Remove any :guilabel:`Filters` in the
:guilabel:`Search bar`, then click :guilabel:`Group By`, :guilabel:`Add Custom Group`, and click
the :guilabel:`drop-down` to select :guilabel:`Expiration Date.` :guilabel:`Apply` the filter. This
will break down all perishable products, their :guilabel:`Expiration Dates`, and the assigned lot
number.

.. image:: expiration_dates/expiration-dates-group-by-dates.png
   :align: center
   :alt: Group by expiration dates on lots and serial numbers page.

To see any expiration alerts for products that are either expired (or will expire soon), remove all
:guilabel:`Filters` from the :guilabel:`Search bar`. Then, click :guilabel:`Filters`, then
:guilabel:`Expiration Alerts`.

Expiration alerts
-----------------

To see expiration alerts, go to :menuselection:`Inventory --> Products --> Lots/Serial Numbers`.
Then, click into a :guilabel:`Lot/Serial Number` containing perishable products. Once on the serial
number form, click the :guilabel:`Dates` tab to see all expiration information about the products.

Click :guilabel:`Edit` to edit the form, then change the :guilabel:`Expiration Date` to today's
date (or earlier), and :guilabel:`Save` changes. The lot number now displays a red
:guilabel:`Expiration Alert` below it at the top of the lot form to indicate that the products in
this lot are either expired or expiring soon. Click back to the :guilabel:`Lots/Serial Numbers`
page (via the breadcrumbs) and click :guilabel:`Filters`, then click :guilabel:`Expiration Alerts`
to see the new alert.

.. image:: expiration_dates/expiration-dates-expiration-alert.png
   :align: center
   :alt: Expiration alert for product past the expiration date.
