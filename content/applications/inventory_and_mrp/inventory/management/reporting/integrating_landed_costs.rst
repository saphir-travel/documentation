==============================================
Landed Costs: Add additional costs to products
==============================================

When companies perform profit analyses, they need to know that they are as accurate as possible. To
make sure of that, all costs and expenses need to be included; this includes the sum of expenses
associated with shipping a product, also known as :guilabel:`Landed Costs`.

In Odoo, the :guilabel:`Landed Costs` feature allows the user to add and include additional costs
on goods they purchase. This can include the cost of freight, shipping, insurance, taxes, and more.

Configuration
=============

To use :guilabel:`Landed Costs`, go to :menuselection:`Inventory --> Configuration --> Settings`,
scroll down to the :guilabel:`Valuation` section, and click the checkbox to enable
:guilabel:`Landed Costs`. A default accounting journal can also be set, in which entries involving
:guilabel:`Landed Costs` will be recorded. After this has been enabled, click :guilabel:`Save`.

.. image:: integrating_landed_costs/integrating-landed-costs-settings.png
   :align: center
   :alt: Enabled Landed Costs feature in Inventory settings.

.. important::
    :guilabel:`Landed Costs` can only be applied to products using a
    :abbr:`FIFO (First In First Out)` or :abbr:`AVCO (Average Cost)` :guilabel:`Costing Method`,
    and :guilabel:`Automated` :guilabel:`Inventory Valuation`.

Create a Landed Cost product
============================

:guilabel:`Landed Costs` can be manually entered each time a :guilabel:`Vendor Bill` is created.
However, some products might always have the same types of charges applied to them, and thus might
always list :guilabel:`Landed Costs` on :guilabel:`Vendor Bills`. In this case, it could be
beneficial to create a :guilabel:`Landed Cost` product.

To create a :guilabel:`Landed Cost` product, go to :menuselection:`Inventory --> Products -->
Products`, and click :guilabel:`Create`.

Name and fill out the product information, and change the :guilabel:`Product Type` to
:guilabel:`Service`. Then, click the :guilabel:`Purchase` tab, and under the
:guilabel:`Landed Costs` section, select :guilabel:`Is a Landed Cost`. Once selected, a new field
will appear below to select the :guilabel:`Default Split Method`. Select :guilabel:`Equal`, then
:guilabel:`Save`.

.. image:: integrating_landed_costs/integrating-landed-costs-split-method.png
   :align: center
   :alt: Landed costs and split method enabled on product form.

.. note::
    There is no need to set a price (or cost) on a :guilabel:`Landed Cost` product, because the
    price will change with each order, depending on the :guilabel:`Landed Costs` of each shipment.

Create a Request for Quotation
==============================

Before adding :guilabel:`Landed Costs` on goods, create a new :abbr:`RFQ (Request for Quotation)`.
To do that, navigate to the :guilabel:`Purchase` app, and click :guilabel:`Create`.

Add a :guilabel:`Vendor`, add a product to the :guilabel:`Product` lines, and fill out the
remaining information on the new RFQ. Then, click :guilabel:`Confirm Order.` Once the quotation has
been confirmed, it turns into a purchase order. Click :guilabel:`Receive Products`,
:guilabel:`Validate`, and set :guilabel:`Apply` to set the :guilabel:`Done` quantities. Navigate
back to the purchase order (via the breadcrumbs).

Create a Vendor Bill
====================

Now that goods have been received from the purchase order, a :guilabel:`Vendor Bill` can be
created. To do so, click :guilabel:`Create Bill.` The bill will automatically populate with the
information from the purchase order. To add a :guilabel:`Landed Cost` to the bill, click
:guilabel:`Edit`.

While in :guilabel:`Edit` mode, click :guilabel:`Add a line` to add the :guilabel:`Landed Cost`
product created previously. Since this product was created as a :guilabel:`Landed Cost`, the
checkbox under the :guilabel:`Landed Costs` column will be selected by default.

.. image:: integrating_landed_costs/integrating-landed-costs-vendor-bill.png
   :align: center
   :alt: Landed cost added on product lines on vendor bill.

.. important::
    Since no :guilabel:`Price` was set on the product form for the :guilabel:`Landed Cost`, it must
    be set manually on the vendor bill.

Create Landed Costs
===================

Once all the information on the bill has been filled out, click :guilabel:`Create Landed Costs`.
This will navigate to a new accounting entry for the :guilabel:`Landed Cost`. From here, next to
:guilabel:`Transfers`, the warehouse receipt with which this :guilabel:`Landed Cost` is associated
must be specified. Additionally, an expenses :guilabel:`Account` must be selected, as well.

To see how the :guilabel:`Landed Costs` affect the items on the purchase order, click the
:guilabel:`Valuation Adjustments` tab. From here, the :guilabel:`Original Value` and
:guilabel:`New Value` can be seen, as well as the :guilabel:`Additional Landed Cost` that changed
the original purchase order.

.. image:: integrating_landed_costs/integrating-landed-costs-valuation-adjustments.png
   :align: center
   :alt: Valuation adjustments tab for landed costs on vendor bill.

Once everything is set, :guilabel:`Validate` and :guilabel:`Save`. Then, click back to the
:guilabel:`Vendor Bill` (via the breadcrumbs).

.. note::
    When the :guilabel:`Default Split Method` is set to :guilabel:`Equal`, the
    :guilabel:`Landed Cost` will be split equally between all items included on the purchase order.
    Since this :abbr:`PO (Purchase Order)` has just one item, the full amount will be applied to
    this item.

To wrap up the :guilabel:`Vendor Bill`, :guilabel:`Confirm`, :guilabel:`Register Payment`, and
:guilabel:`Create Payment`.

.. tip::
    :guilabel:`Landed Costs` don't always need to be created from the :guilabel:`Vendor Bill`.
    They can also be created by going to :menuselection:`Inventory --> Operations --> Landed Costs`
    and clicking :guilabel:`Create`.
