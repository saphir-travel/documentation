==========================
Configure reordering rules
==========================

For certain products, it is necessary to ensure that there is always a minimum amount available on
hand at any given time. By adding a reordering rule to a product, it is possible to automate the
reordering process so that a purchase order is automatically created whenever the amount on hand
falls below a set threshold.

.. important::
   The *Inventory* module must be installed to use reordering rules.

Configure products for reordering
=================================

Products must be configured in a specific way before a reordering rule can be added to them.
Starting from the :guilabel:`Inventory`, :guilabel:`Manufacturing`, :guilabel:`Purchase`, or
:guilabel:`Sales` module, navigate to :menuselection:`Products --> Products --> Create`. To allow
for reordering, make sure that the :guilabel:`Can be Purchased` checkbox is activated and the
:guilabel:`Product Type` dropdown is set to `Storable Product`.

.. image:: reordering/product-configured-for-reordering.png
   :align: center
   :alt: Configure a product for reordering in Odoo.

Add a reordering rule to a product
==================================

After properly configuring a product, a reordering rule can be added to it by navigating to the
product page and selecting :menuselection:`Reordering Rules --> Create`.

.. image:: reordering/reordering-rules-tab.png
   :align: center
   :alt: Access reordering rules for a product from the product page in Odoo.

Once created, the reordering rule can be configured to generate purchase orders automatically by
defining the following fields:

- :guilabel:`Location` specifies where the ordered quantities should be stored once they are
  received and entered into stock.
- :guilabel:`Min Quantity` sets the lower threshold for the reordering rule while :guilabel:`Max
  Quantity` sets the upper threshold. If the stock on hand falls below the minimum quantity, a new
  purchase order will be created to replenish it up to the maximum quantity.

   .. example::
      If :guilabel:`Min Quantity` is set to `5` and :guilabel:`Max Quantity` is set to `25` and the
      stock on hand falls to four, a purchase order will be created for 21 units of the product.

- :guilabel:`Multiple Quantity` can be configured so that products are only ordered in batches of a
  certain quantity. Depending on the number entered, this can result in the creation of a purchase
  order that would put the resulting stock on hand above what is specified in the :guilabel:`Max
  Quantity` field.

   .. example::
      If :guilabel:`Max Quantity` is set to `100` but :guilabel:`Multiple Quantity` is set to order
      the product in batches of `200`, a purchase order will be created for 200 units of the
      product.

- :guilabel:`UoM` specifies the unit of measurement by which the quantity will be ordered. For
  discrete products, this should be set to `Units`. However, it can also be set to units of
  measurement like `Volume` or `Weight` for non-discrete products like water or bricks.

.. image:: reordering/reordering-rule-configuration.png
   :align: center
   :alt: Configure the reordering rule in Odoo.

Triggering reordering rules using the scheduler
===============================================

Reordering rules will be automatically triggered by the scheduler, which runs once a day by
default. To trigger reordering rules manually, navigate to
:menuselection:`Inventory --> Operations --> Run Scheduler`.

.. note::
   Manually triggering reordering rules will also trigger any other scheduled actions.

Managing reordering rules
=========================

To manage the reordering rules for a single product, go to the product page and select
:guilabel:`Reordering Rules`. To manage all reordering rules for every product, go to
:menuselection:`Inventory --> Configuration --> Reordering Rules`.
