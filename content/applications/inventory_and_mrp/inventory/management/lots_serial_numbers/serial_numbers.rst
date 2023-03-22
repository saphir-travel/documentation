====================================
Use serial numbers to track products
====================================

*Serial Numbers* are one of the two ways to identify and track products in Odoo. A serial number
is a unique identifier assigned incrementally (or sequentially) to an item or product, used to
distinguish it from other items and products.

Serial numbers can consist of many different types of characters: they can be strictly numerical;
they can contain letters and other typographical symbols; and they can be a mix of all of the
above. The goal of assigning serial numbers to individual products is to make sure that every
item's history is identifiable when it travels through the supply chain. This can be especially
useful for manufacturers that provide after-sales services to products that they sell and deliver.

.. seealso::
    - :doc:`lots`

Configuration
=============

To track products using *serial numbers*, the :guilabel:`Lots & Serial Numbers` feature must be
enabled. To enable this, go to :menuselection:`Inventory --> Configuration --> Settings`, scroll
down to the :guilabel:`Traceability` section, and click the box next to
:guilabel:`Lots & Serial Numbers`. :guilabel:`Save` changes.

.. image:: serial_numbers/serial-numbers-enabled-setting.png
   :align: center
   :alt: Enabled lots and serial numbers setting.

Track products by serial number
===============================

Once the :guilabel:`Lots & Serial Numbers` setting has been activated, individual products can now
be configured to be tracked using serial numbers. To do this, go to :menuselection:`Inventory -->
Products --> Products`, and choose a product. Once on the product form, click the
:guilabel:`Inventory` tab.

To track this product using serial numbers, click :guilabel:`Edit`, and under the
:guilabel:`Traceability` section, click :guilabel:`By Unique Serial Number`. :guilabel:`Save`
changes. Existing or new serial numbers can now be selected and assigned to newly-received or
manufactured batches of this product.

.. image:: serial_numbers/serial-numbers-product-tracking.png
   :align: center
   :alt: Enabled serial number tracking on product form.

Create new serial numbers for products already in stock
-------------------------------------------------------

New serial numbers can be created for products already in stock with no assigned serial number. To
do this, go to :menuselection:`Inventory --> Products --> Lots/Serial Numbers`, and click
:guilabel:`Create`. A new :guilabel:`Lot/Serial Number` will be generated automatically.

.. tip::
    Although Odoo automatically generates a new :guilabel:`Lot/Serial Number` to follow the most
    recent number, it can be edited and changed to be whatever number is desired by clicking the
    line under the :guilabel:`Lot/Serial Number` field and changing the generated number.

Once the :guilabel:`Lot/Serial Number` is generated, click the :guilabel:`drop-down` next to
:guilabel:`Product`, and select the product that this new number will be assigned to.
:guilabel:`Save` changes.

.. image:: serial_numbers/serial-numbers-new-serial-number.png
   :align: center
   :alt: New serial number created for existing product stock.

After the new serial number has been created and assigned to the desired product, navigate back to
the product form by going to :menuselection:`Products --> Products`, and selecting the product the
new serial number was just assigned to. Click the :guilabel:`Lot/Serial Numbers` smart button to
see the new serial number.

Manage serial numbers for shipping and receiving
================================================

Manage serial numbers on receipts
---------------------------------

Assigning serial numbers to *incoming* goods can be done directly from the purchase order. To
create a purchase order, go to the :menuselection:`Purchase app --> Create` to create a new Request
for Quotation (RFQ). Then, fill out the information by adding a :guilabel:`Vendor`, and by adding
products to the :guilabel:`Product` lines by clicking :guilabel:`Add a product`. Choose the desired
quantity to order by changing the number in the :guilabel:`Quantity` column.

Click :guilabel:`Confirm Order`. This will convert the :abbr:`RFQ (Request for Quotation)` to a
:guilabel:`Purchase Order`. Click the :guilabel:`Receipt` smart button to be taken to the
:guilabel:`Warehouse Receipt Form`.

.. note::
    Clicking :guilabel:`Validate` before assigning a serial number to the ordered product
    quantities will cause a :guilabel:`User Error` popup to appear. The popup requires entry of a
    lot or serial number for the ordered products. The :abbr:`RFQ (Request for Quotation)` cannot
    be validated without a serial number being assigned.

.. image:: serial_numbers/serial-numbers-user-error-popup.png
   :align: center
   :alt: User error popup prompting serial number entry.

From here, click the :guilabel:`Additional Options` menu (hamburger) icon, and a
:guilabel:`Detailed Operations` popup will appear. The next step is to assign a serial number (or
serial numbers) under the :guilabel:`Lot/Serial Number Name` field. There are three ways to do
this:

- **Manually assign serial numbers**: Click :guilabel:`Add a line` and choose the location the
  product will be stored in under the :guilabel:`To` column. Then, type a new
  :guilabel:`Serial Number Name` and set the :guilabel:`Done` quantity. Repeat for the quantity of
  products shown in the :guilabel:`Demand` field, and until the :guilabel:`Quantity Done` field
  displays the correct (matching) number of products processed.

- **Automatically assign serial numbers**: If a large quantity of products need individual serial
  numbers assigned to them, Odoo can automatically generate and assign serial numbers to each of
  the individual products. In the :guilabel:`First SN` field, type the first serial number in the
  desired order to be assigned. Then, in the :guilabel:`Number of SN` field, type the total number
  of items that need newly-generated unique serial numbers assigned to them. Finally, click
  :guilabel:`Assign Serial Numbers`. A list will populate with new serial numbers matching the
  ordered quantity of products.

.. image:: serial_numbers/serial-numbers-auto-assign-sn.png
   :align: center
   :alt: Automatic serial number assignment in detailed operations popup.

- **Copy/paste serial numbers from an Excel file**: Populate an Excel spreadsheet with all of the
  serial numbers received from the supplier (or manually chosen to assign upon receipt). Then, copy
  and paste them in the :guilabel:`Lot/Serial Number Name` column. Odoo will automatically create
  the necessary number of lines based on the amount of numbers pasted in the column. From here, the
  :guilabel:`To` locations and :guilabel:`Done` quantities can be manually entered in each of the
  serial number lines.

.. image:: serial_numbers/serial-numbers-excel-spreadsheet.png
   :align: center
   :alt: List of serial numbers copied in Excel spreadsheet.

.. tip::
    For purchase orders that include large quantities of products to receive, the best method of
    serial number assignment is to automatically assign serial numbers using the
    :guilabel:`Assign Serial Numbers` button. This will prevent any serial numbers from being
    reused or duplicated, and improves traceability reporting.

Once all product quantities have been assigned a serial number, click :guilabel:`Confirm` to close
the popup, and click :guilabel:`Validate`. A :guilabel:`Traceability` smart button will appear upon
validating the receipt. Click the :guilabel:`Traceability` smart button to see the updated
:guilabel:`Traceability Report`, which includes: a :guilabel:`Reference` document; the
:guilabel:`Product` being traced; the :guilabel:`Lot/Serial #`; and more.

Manage serial numbers on delivery orders
----------------------------------------

Assigning serial numbers to *outgoing* goods can be done directly from the sales order. To create a
sales order, go to the :guilabel:`Sales` app, and click :guilabel:`Create` to create a new
quotation. Then, fill out the information by adding a :guilabel:`Customer`, and by adding products
to the :guilabel:`Product` lines by clicking :guilabel:`Add a product`. Choose the desired quantity
to sell by changing the number in the :guilabel:`Quantity` column.

Once the quotation has been filled out, click :guilabel:`Confirm`. When the quotation is confirmed,
it will become a :guilabel:`Sales Order`, and a :guilabel:`Delivery` smart button will appear.
Click the :guilabel:`Delivery` smart button to be taken to the warehouse delivery form.

From here, click the :guilabel:`Additional Options` menu (hamburger) icon, and a
:guilabel:`Detailed Operations` popup will appear. A :guilabel:`Lot/Serial Number` will be chosen
by default, with each product of the total :guilabel:`Reserved` quantity listed with their unique
serial numbers (most likely listed in sequential order). To manually change a product's serial
number, click the :guilabel:`drop-down` under :guilabel:`Lot/Serial Number`, and choose (or type)
the desired serial number. Then, mark the :guilabel:`Done` quantities, and click
:guilabel:`Confirm` to close the popup. Finally, click :guilabel:`Validate` to deliver the products.

.. image:: serial_numbers/serial-numbers-detailed-operations-popup.png
   :align: center
   :alt: Serial numbers listed in detailed operations popup.

A :guilabel:`Traceability` smart button will appear upon validating the delivery order. Click the
:guilabel:`Traceability` smart button to see the updated :guilabel:`Traceability Report`, which
includes: a :guilabel:`Reference` document; the :guilabel:`Product` being traced; the
:guilabel:`Lot/Serial #` assigned; and the :guilabel:`Reference` receipt from the previous purchase
order (if any of the product quantities shared a serial number assigned during receipt of that
:abbr:`PO (Purchase Order)`).

Manage serial numbers for different operations types
====================================================

By default in Odoo, the creation of new serial numbers is only allowed upon *receiving* products
from a purchase order. *Existing* serial numbers cannot be used. For sales orders, the opposite is
true: new serial numbers cannot be created on the delivery order, only existing serial numbers can
be used.

To change the ability to use new or existing serial numbers on any operation type, go to
:menuselection:`Inventory --> Configuration --> Operations Types`, and select the desired
:guilabel:`Operation Type`. For :guilabel:`Receipts`, the
:guilabel:`Use Existing Lots/Serial Numbers` option can be enabled by clicking :guilabel:`Edit` and
then clicking the :guilabel:`checkbox`. For :guilabel:`Delivery Orders`, the
:guilabel:`Create New Lots/Serial Numbers` option can be enabled by clicking :guilabel:`Edit` and
clicking the :guilabel:`checkbox`. For any changes made, be sure to :guilabel:`Save`.

.. image:: serial_numbers/serial-numbers-operations-types.png
   :align: center
   :alt: Enabled traceability setting in operations type form.

Serial number traceability
==========================

Manufacturers and companies can refer to the traceability reports to see the entire lifecycle of a
product: where (and when) it came from; where it was stored; and who (and when) it went to.

To see the full traceability of a product or group by serial numbers, go to
:menuselection:`Inventory --> Products --> Lots/Serial Numbers.` From here, products with serial
numbers assigned to them will be listed by default, and can be expanded to show the serial numbers
those products have assigned to them.

To group by serial numbers (or lots), first remove any :guilabel:`Filters` in the
:guilabel:`Search bar`. Then, click :guilabel:`Group By`, click :guilabel:`Add Custom Group`, and
click the :guilabel:`drop-down` menu to select :guilabel:`Lot/Serial Number`. Click
:guilabel:`Apply`. All existing serial numbers and lots are now displayed and can be expanded to
show all quantities of products with that assigned number. For unique serial numbers that are not
reused, there should be just one product per serial number.

.. image:: serial_numbers/serial-numbers-reporting-page.png
   :align: center
   :alt: Serial numbers reporting page with drop-down lists.

.. note::
    For additional information regarding an individual serial number (or lot number), click the
    line item for the serial number. From the :guilabel:`Serial Number` form, click the
    :guilabel:`Location` and :guilabel:`Traceability` smart buttons to see all stock on-hand using
    that serial number, and any operations made using that serial number.

.. seealso::
    - :doc:`differences`
