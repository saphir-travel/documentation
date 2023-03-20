=====================================
Use lots to manage groups of products
=====================================

*Lots* are one of the two ways to identify and track products in Odoo. A lot usually indicates a
specific batch of an item that was received, is currently stored, or was shipped from a warehouse,
but can also pertain to a batch of products manufactured in-house, as well.

Manufacturers assign lot numbers to groups of products that have common properties; this can lead
to multiple goods sharing the same lot number. This helps to identify a number of products in a
single group, and allows for end-to-end traceability of these products through each step in their
lifecycles. Lots are useful for products that are manufactured or received in large quantities
(such as clothes or food) and can be used to trace a product back to a group. This is especially
useful when managing product recalls or expiration dates.

.. seealso::
    - :doc:`serial_numbers`

Configuration
=============

To track products using *Lots*, the :guilabel:`Lots & Serial Numbers` feature must be enabled. Go
to :menuselection:`Inventory --> Configuration --> Settings`, scroll down to the
:guilabel:`Traceability` section, and click the box next to :guilabel:`Lots & Serial Numbers`.
:guilabel:`Save` changes.

.. image:: lots/lots-enabled-lots-setting.png
   :align: center
   :alt: Enabled lots and serial numbers feature in inventory settings.

Track products by lots
======================

Once the :guilabel:`Lots & Serial Numbers` setting has been activated, individual products can now
be configured to be tracked using lots. To do this, go to :menuselection:`Inventory --> Products
--> Products`, and choose a product. Once on the product form, click the :guilabel:`Inventory` tab.

To track this product using lots, click :guilabel:`Edit`, and under the :guilabel:`Traceability`
section, click :guilabel:`By Lots`. :guilabel:`Save` changes. Existing or new Lot numbers can now
be assigned to newly-received or manufactured batches of this product.

.. note::
   If a product has stock on-hand prior to activating tracking by lots or serial numbers, an
   inventory adjustment might need to be performed to assign lot numbers to the existing stock.

.. image:: lots/lots-tracking-product-form.png
   :align: center
   :alt: Enabled tracking by lots feature on product form.

Create new lots for products already in stock
---------------------------------------------

New lots can be created for products already in stock with no assigned lot number. To do this, go
to :menuselection:`Inventory --> Products --> Lots/Serial Numbers`, and click :guilabel:`Create`. A
new :guilabel:`Lot/Serial Number` will be generated automatically.

.. tip::
    Although Odoo automatically generates a new :guilabel:`Lot/Serial Number` to follow the most
    recent number, it can be edited and changed to be whatever number is desired by clicking the
    line under the :guilabel:`Lot/Serial Number` field and changing the generated number.

Once the :guilabel:`Lot/Serial Number` is generated, click the :guilabel:`drop-down` next to
:guilabel:`Product`, and select the product that this new number will be assigned to.
:guilabel:`Save changes`.

.. image:: lots/lots-new-lot-number.png
   :align: center
   :alt: New lot number creation form with assigned product.

After the new lot number has been created and assigned to the desired product, navigate back to the
product form by going to :menuselection:`Products --> Products`, and selecting the product the new
lot number was just assigned to. Click the :guilabel:`Lots/Serial Numbers` smart button to see the
new lot number. When additional quantity of this product is received or manufactured, this new lot
number can be selected and assigned to it.

Manage lots for shipping and receiving
======================================

Manage lots on receipts
-----------------------

Assigning lot numbers to *incoming* goods can be done directly from the purchase order. To create a
purchase order, go to the :menuselection:`Purchase app --> Create` to create a new Request for
Quotation (RFQ). Then, fill out the information by adding a :guilabel:`Vendor`, and by adding
products to the :guilabel:`Product` lines by clicking :guilabel:`Add a product`. Choose the desired
quantity to order by changing the number in the :guilabel:`Quantity` column.

Once the :abbr:`RFQ (Request for Quotation)` has been filled out, click :guilabel:`Confirm Order`.
When the :abbr:`RFQ (Request for Quotation)` is confirmed, it will become a
:guilabel:`Purchase Order`, and a :guilabel:`Receipt` smart button will appear. Click the
:guilabel:`Receipt` smart button to be taken to the warehouse receipt form.

.. note::
    Clicking :guilabel:`Validate` before assigning a lot number to the ordered product quantities
    will cause a :guilabel:`User Error` popup to appear. The popup prompts entry of a
    lot or serial number for the ordered products. The :abbr:`RFQ (Request for Quotation)` cannot
    be validated without a lot number being assigned.

.. image:: lots/lots-user-error-popup.png
   :align: center
   :alt: Add lot/serial number user error popup.

From here, click the :guilabel:`Additional Options` menu (hamburger) icon, and a
:guilabel:`Detailed Operations` popup will appear. The next step is to assign a lot number under
the :guilabel:`Lot/Serial Number Name` field. There are two ways to do this:

- **Manually assign Lot numbers**: Click :guilabel:`Add a line` and choose the location the
  products will be stored in under the :guilabel:`To` column. Then, type a new
  :guilabel:`Lot Number Name` and set the :guilabel:`Done` quantity.

.. image:: lots/lots-assign-lot-number-popup.png
   :align: center
   :alt: Assign lot number detailed operations popup.

.. note::
    If quantities should be processed in multiple locations and lots, click :guilabel:`Add a line`
    and type a new :guilabel:`Lot Number Name` for additional quantities. Repeat until the
    :guilabel:`Quantity Done` matches the :guilabel:`Demand`.

- **Copy/paste Lot numbers from an Excel file**: Populate an Excel spreadsheet with all of the lot
  numbers received from the supplier (or manually chosen to assign upon receipt). Then, copy and
  paste them in the :guilabel:`Lot/Serial Number Name` column. Odoo will automatically create the
  necessary number of lines based on the amount of numbers pasted in the column. From here, the
  :guilabel:`To` locations and :guilabel:`Done` quantities can be manually entered in each of the
  lot number lines.

.. image:: lots/lots-excel-spreadsheet.png
   :align: center
   :alt: List of lot numbers copied on excel spreadsheet.

Once all product quantities have been assigned a lot number, click :guilabel:`Confirm` to close the
popup, and click :guilabel:`Validate`. A :guilabel:`Traceability` smart button will appear upon
validating the receipt. Click the :guilabel:`Traceability` smart button to see the updated
:guilabel:`Traceability Report`, which includes: a :guilabel:`Reference` document; the
:guilabel:`Product` being traced; the :guilabel:`Lot/Serial #` assigned; and more.

Manage lots on delivery orders
------------------------------

Assigning lot numbers to *outgoing* goods can be done directly from the sales order. To create a
sales order, go to the :guilabel:`Sales` app, and click :guilabel:`Create` to create a new
quotation. Then, fill out the information by adding a :guilabel:`Customer`, and by adding products
to the :guilabel:`Product` lines by clicking :guilabel:`Add a product`. Choose the desired quantity
to sell by changing the number in the :guilabel:`Quantity` column.

Once the quotation has been filled out, click :guilabel:`Confirm`. When the quotation is confirmed,
it will become a :guilabel:`Sales Order`, and a :guilabel:`Delivery` smart button will appear.
Click the :guilabel:`Delivery` smart button to be taken to the :guilabel:`Warehouse Delivery Form`.

From here, click the :guilabel:`Additional Options` menu (hamburger) icon, and a
:guilabel:`Detailed Operations` popup will appear. A :guilabel:`Lot/Serial Number` will be chosen
by default, with the full :guilabel:`Reserved` quantity taken from that specific lot (if there is
enough stock in that particular lot). If there is insufficient stock in that lot, or if partial
quantities of the :guilabel:`Demand` should be taken from multiple lots, change the quantity in the
:guilabel:`Done` column to only include part of the total quantity.

.. note::
    The lot automatically chosen for delivery orders will vary depending on the selected removal
    strategy (:abbr:`FIFO (First In, First Out)`, :abbr:`LIFO (Last In, First Out)`, or
    :abbr:`FEFO (First Expiry, First Out)`). It will also depend on the quantity ordered, and if
    there is enough quantity in one lot to fulfill the order.

.. seealso::
    - :doc:`../../routes/strategies/removal`

Then, click :guilabel:`Add a line`, select an additional (different) :guilabel:`Lot/Serial Number`,
apply the rest of the :guilabel:`Done` quantities, and click :guilabel:`Confirm` to close the
popup. Click :guilabel:`Validate` to deliver the products.

.. image:: lots/lots-detailed-operations-popup.png
   :align: center
   :alt: Detailed operations popup for source lot number on sales order.

A :guilabel:`Traceability` smart button will appear upon validating the delivery order. Click the
:guilabel:`Traceability` smart button to see the updated :guilabel:`Traceability Report`, which
includes: a :guilabel:`Reference` document; the :guilabel:`Product` being traced; the
:guilabel:`Lot/Serial #` assigned; and the :guilabel:`Reference` receipt from the previous purchase
order (if the product quantities shared the same lot number).

Manage lots for different operations types
==========================================

By default in Odoo, the creation of new lots is only allowed upon *receiving* products from a
purchase order. *Existing* lot numbers cannot be used. For sales orders, the opposite is true: new
lot numbers cannot be created on the delivery order, only existing lot numbers can be used.

To change the ability to use new or existing lot numbers on any operation type, go to
:menuselection:`Inventory --> Configuration --> Operations Types`, and select the desired
:guilabel:`Operation Type`. For :guilabel:`Receipts`, the
:guilabel:`Use Existing Lots/Serial Numbers` option can be enabled by clicking :guilabel:`Edit` and
then clicking the :guilabel:`checkbox`. For :guilabel:`Delivery Orders`, the
:guilabel:`Create New Lots/Serial Numbers` option can be enabled by clicking :guilabel:`Edit` and
clicking the checkbox. For any changes made, be sure to :guilabel:`Save`.

.. image:: lots/lots-operations-type-form.png
   :align: center
   :alt: Enabled traceability setting on operations type form.

.. tip::
    For inter-warehouse trasnfers involving products tracked by lots, it can be useful to enable
    the :guilabel:`Use Existing Lots/Serial Numbers` option for :guilabel:`Receipts`.

Lots traceability
=================

Manufacturers and companies can refer to traceability reports to see the entire lifecycle of a
product: where (and when) it came from; where it was stored; and who (and when) it went to.

To see the full traceability of a product or group by lots, go to :menuselection:`Inventory -->
Products --> Lots/Serial Numbers`. From here, products with lot numbers assigned to them will be
listed by default, and can be expanded to show the lot number(s) those products have assigned to
them.

To group by lots (or serial numbers), first remove any filters in the search bar. Then, click
:guilabel:`Group By`, click :guilabel:`Add Custom Group`, and click the drop-down menu to select
:guilabel:`Lot/Serial Number`. Click :guilabel:`Apply`. All existing lots and serial numbers are
now displayed and can be expanded to show all quantities of products with that assigned number.

.. image:: lots/lots-traceability-report.png
   :align: center
   :alt: Lots and serial numbers traceability report.

.. seealso::
    - :doc:`differences`
