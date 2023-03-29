===============================
Set up a user default warehouse
===============================

Setting up a **default warehouse** can be useful for field technicians who keep a supply in their
van or those who always resupply in the same warehouse.

With this feature configured, the products in sales orders created during field interventions are
always pulled from the same warehouse, keeping the inventory accurate.

.. seealso::
   :doc:`../../inventory_and_mrp/inventory`

Configuration
=============

Database
--------

In order to be able to set up a user default warehouse, configure the following settings first:

 - Go to :menuselection:`Inventory --> Configuration --> Settings`. Activate :guilabel:`Storage
   locations` and :guilabel:`Multi-step routes`.
 - Have more than one warehouse in your database. To create a warehouse, go to
   :menuselection:`Inventory --> Configuration --> Warehouses`. Then, click :guilabel:`Create`.
   See :doc:`../../inventory_and_mrp/inventory` documentation for more information about warehouse
   management.

User account
------------

After you completed these steps, set up a default warehouse for a specific user.

 - Go to :menuselection:`Settings --> Users --> Manage users`. Then, choose the user
   you wish to configure a default warehouse for from the list.
 - Go to the :guilabel:`Preferences` tab, then scroll down to :guilabel:`Inventory`. Select the
   default warehouse from the drop-down menu.

   .. image:: default_warehouse/default-warehouse-config.png
      :align: left
      :alt: Selection of a default warehouse on a user profile.

Default warehouse in field service tasks
========================================

Once a default warehouse has been configured for a user, the materials used for a sales order
linked to a Field Service task are pulled from that specific warehouse.

To see that the feature was configured correctly, open the sales order created by the user with
default warehouse configured. Go to :guilabel:`Other Info` tab, then scroll down to **Delivery**.
The default warehouse is applied correctly on the creation of the sales order.
