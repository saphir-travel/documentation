=================
Calls for Tenders
=================

*Calls for Tenders* are one of the two main types of :guilabel:`Purchase Agreements` available by
default in Odoo.

Calls for Tenders are used to request offers from multiple vendors at the same time, by inviting
those vendors to submit offers for similar goods (or services) all at once. This helps companies
that use this feature to select the cheapest (and fastest) vendors, depending on their specific
business needs.

While Calls for Tenders are primaily used by organizations in the public sector, who are legally
bound to use them when making a purchase, private companies can also use them to spend money
efficiently, as well.

When multiple offers are sent to a company, the ideal/best option can be chosen, minimizing costs
and increasing profitability in the most efficient manner.

.. note::
    To create and use Calls for Tenders, :guilabel:`Purchase Agreements` must be activated by going
    to :menuselection:`Purchase --> Configuration --> Settings`.

Example flow: Create a Call for Tender
======================================

To create a Call for Tender, first make sure that :guilabel:`Purchase Agreements` are enabled.
Then, navigate to the :guilabel:`Purchase` application.

.. image:: calls_for_tenders/calls-for-tenders-settings-page.png
   :align: center
   :alt: Purchase Agreements enabled in the Purchase app settings.

.. tip::
    To save time on a Call for Tender, custom vendors, prices, and delivery lead times can be set
    in the :guilabel:`Purchase` tab on a product form.

Create an :abbr:`RFQ (Request for Quotation)`
---------------------------------------------

From the main :guilabel:`Purchase` dashboard, click :guilabel:`New` to create a new Request for
Quotation. Then, fill out the information, and add products to the product lines. Once all the
information is entered, click :guilabel:`Send by Email`. This can be useful when creating a Call
for Tender, because vendors can confirm if their past prices still hold today, which can help
companies choose the best offers.

Create alternatives to an :abbr:`RFQ (Request for Quotation)`
-------------------------------------------------------------

Once a purchase order is created (and sent), alternative quotations can be created and sent to
vendors to compare later. To do this, click the :guilabel:`Alternatives` tab,
then click :guilabel:`Create Alternative`. When clicked, a popup appears.

.. image:: calls_for_tenders/calls-for-tenders-alternatives-popup.png
   :align: center
   :alt: Calls for tenders popup to create alternative quotation.

From the popup, click the drop-down menu next to :guilabel:`Vendor`, and select a vendor for the
alternative :abbr:`PO (purchase order)`. Next to this, there is a :guilabel:`Copy Products` checkbox
that is selected by default. When selected, the product quantities of the original
:abbr:`PO (purchase order)` will be copied to the alternative. Once finished, click
:guilabel:`Create Alternative`. This creates (and navigates to) a new purchase order.

Once again, click :guilabel:`Send by Email`. Next, create a second alternative by
clicking the :guilabel:`Alternatives` tab, and click :guilabel:`Create Alternative`. When the popup
appears again, choose a different vendor from the drop-down menu next to :guilabel:`Vendor`, and
this time, *uncheck* the :guilabel:`Copy Products` checkbox. Click :guilabel:`Create Alternative`.

.. tip::
    If one (or two) alternative quotations need to be removed from the :guilabel:`Alternatives` tab,
    they can be individually removed by clicking on the black "X" icon at the end of their row.

This creates a new purchase order, but since the product quantities of the original
:abbr:`PO (purchase order)` were not copied over, new products will need to be added to the product
lines. After the products are added, click :guilabel:`Send by Email`.

From this newest purchase order, click the :guilabel:`Alternatives` tab.

From here, all three purchase orders can be seen, inluding which vendors they were sent to, the
expected arrival of the products (if confirmed), and the status of the order.

Before comparing any product lines, click :guilabel:`New` at the top of the page. This creates
a brand new quotation. Fill out the information on this new quotation, and click
:guilabel:`Send by Email`. Then, click the :guilabel:`Alternatives` tab once more. On this new
:abbr:`PO (purchase order)`, there are no other orders linked. To link this order with the
alternatives, click :guilabel:`Link to Existing RfQ`.

.. image:: calls_for_tenders/calls-for-tenders-link-existing-rfq.png
   :align: center
   :alt: Popup to link new quotation to existing RFQs.

This causes a popup to appear. From the popup, select the three purchase orders created
previously, and click :guilabel:`Select`. All of these orders have now been copied to this
:abbr:`PO (purchase order)` under the :guilabel:`Alternatives` tab.

Compare product lines
---------------------

Now that there are multiple RFQs linked as alternatives, they can be compared in order to determine
which vendors offer the best deal. Under the :guilabel:`Alternatives` tab in the newest purchase
order, click :guilabel:`Compare Product Lines`.

.. image:: calls_for_tenders/calls-for-tenders-compare-product-lines.png
   :align: center
   :alt: Compare Product Lines page for alternative RFQs.

From the :guilabel:`Compare Order Lines` page, each product included in any of the purchase orders
will be shown in a drop-down, with all of the orders they were included in listed below them. In
the different columns, the quantities, unit price, and total price of the products can be compared.

At the end of each row, products can be selected by clicking :guilabel:`Choose`. Once all the
desired products have been chosen, click :guilabel:`Requests for Quotation` (in the breadcrumbs, at
the top of the page) to navigate back to an overview of all RFQs.

.. note::
    To remove one (or two) product lines from the :guilabel:`Compare Order Lines` page, click
    :guilabel:`Clear` at the end of that product line's row.

Cancel (or keep) alternatives
-----------------------------

Now that the desired products have been chosen, based on which vendors provided the best offer, the
other RFQs (from which no products were chosen) can be canceled. Under the :guilabel:`Total`
column, the RFQs from which no products were chosen have automatically had their total cost set to
0.

To confirm the quotations that contain the chosen product quantities, click into them, and select
:guilabel:`Confirm Order`. This causes an *Alternative Warning* popup to appear. From this
popup, either :guilabel:`Cancel Alternatives` or :guilabel:`Keep Alternatives` can be selected.

.. image:: calls_for_tenders/calls-for-tenders-keep-cancel-alternatives.png
   :align: center
   :alt: Keep or cancel popup for alternative RFQs.

:guilabel:`Cancel Alternatives` automatically cancels the alternative purchase orders.
:guilabel:`Keep Alternatives` keeps the alternative purchase orders open, so they can still be
accessed if any additional product quantities need to be ordered. Once all products are ordered,
:guilabel:`Cancel Alternatives` can be selected from whichever :abbr:`PO (purchase order)` is open.

Once all product quantities have been ordered, the purchase process can be followed, and continued
to completion, until the products are received into the warehouse.

.. seealso::
    - :doc:`blanket_orders`
