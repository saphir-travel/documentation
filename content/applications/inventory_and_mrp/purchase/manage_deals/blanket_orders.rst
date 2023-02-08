==============
Blanket Orders
==============

*Blanket Orders* are one of the two main types of :guilabel:`Purchase Agreements` available by
default in Odoo.

Blanket Orders are long-term purchase agreements between a company and a vendor to deliver
products on a recurring basis with predetermined pricing. Using Blanket Orders are useful when
products are always purchased from the same vendor, but in different quantities at different times.

By simplifying the ordering process, Blanket Orders not only save time, they also save money, since
they can be advantageous when negotiating bulk pricing with vendors.

.. note::
   To create (and use) Blanket Orders, the :guilabel:`Purchase Agreements` feature must be
   activated. To do that, navigate to :menuselection:`Purchase --> Configuration --> Settings`.

Example flow: Create a Blanket Order
====================================

To create a Blanket Order, first make sure that :guilabel:`Purchase Agreements` are enabled. Then,
navigate to the :guilabel:`Purchase` application.

.. image:: blanket_orders/blanket-orders-settings-page.png
   :align: center
   :alt: Purchase Agreements enabled in the Purshase app settings.

From the main :guilabel:`Purchase` dashboard, click :menuselection:`Orders --> Blanket Orders -->
New` to create a new blanket order. Then, fill out the information, and add products to the product
lines.

.. note::
   When creating a Blanket Order, the prices of products will not be set automatically. Prices must
   be set on the product lines manually before confirming the order.

Make sure that the :guilabel:`Agreement Type` is set to *Blanket Order*. Once the
:guilabel:`Agreement Type` is set, click the :guilabel:`Internal link arrow` to see the
:guilabel:`Agreement Type` information set for Blanket Orders.

From here, the settings for Blanket Orders can be edited. The name of the
:guilabel:`Agreement Type` can be changed, and the :guilabel:`Agreement Selection Type` can be
changed, as well. There are two :guilabel:`Agreement Selection Types`:
:guilabel:`Select only one RFQ (exclusive)`, and :guilabel:`Select multiple RFQ (non-exclusive)`.

.. image:: blanket_orders/blanket-orders-edit-agreement-type.png
   :align: center
   :alt: Purchase Agreement type edit screen for Blanket Orders.

- :guilabel:`Select only one RFQ (exclusive)`: When a purchase order is confirmed, the remaining
  purchase orders will be canceled.
- :guilabel:`Select multiple RFQ (non-exclusive)`: On confirmation of a purchase order, remaining
  purchase orders will not be canceled. Instead, multiple purchase orders are allowed.

Additionally, the options for :guilabel:`Data For New Quotations` can be customized from here, too.
:guilabel:`Lines` can be set to either :guilabel:`Use lines of agreement`, or
:guilabel:`Do not create RfQ lines automatically`. :guilabel:`Quantities` can be set to either
:guilabel:`Use quantities of agreement`, or :guilabel:`Set quantities manually`.

Once the desired changes have been made (if any), click :guilabel:`New` (via the breadcrumbs) to
navigate back to the new Blanket Order, and :guilabel:`Confirm`. Once confirmed, the blanket order
changes from *Draft* to *Ongoing*.

Create an :abbr:`RFQ (Request for Quotation)` from the blanket order
--------------------------------------------------------------------

After confirming a Blanket Order, new quotations can be created that will be linked to the Blanket
Order. To create a new :abbr:`RFQ (Request for Quotation)`, click :guilabel:`New Quotation`. Then,
set the :guilabel:`Quantity` and :guilabel:`Unit Price` on the product lines. Once finished, click
:guilabel:`Confirm Order` to create a purchase order.

.. tip::
   Click back to the Blanket Order (via the breadcrumbs), and repeat the process to create as many
   new quotations as needed.

From the Blanket Order, click on the :guilabel:`RFQs/Orders` smart button to view all existing
quotations made under the Blanket Order.

.. image:: blanket_orders/blanket-orders-rfq-smart-button.png
   :align: center
   :alt: RFQs and Orders smart button from Blanket Order form.

.. tip::
   An :abbr:`RFQ (Request for Quotation)` can also be created separate from a Blanket Order, and
   then linked to an existing Blanket Order.

Blanket Orders and replenishment
================================

Once a Blanket Order is confirmed, a new vendor line is added under the :guilabel:`Purchase` tab of
of the products included in the :abbr:`BO (blanket order)`. This makes Blanket Orders useful with
:doc:`automated replenishment <../../purchase/products/reordering>`, because information about the
:guilabel:`Vendor`, :guilabel:`Price`, and the :guilabel:`Agreement` are referenced on the vendor
line. This information is used to determine where, when, and for what price this product could be
replenished.

.. image:: blanket_orders/blanket-orders-automated-replenishment.png
   :align: center
   :alt: Product form with replenishment agreement linked to Blanket Order.

.. seealso::
    - :doc:`calls_for_tenders`
