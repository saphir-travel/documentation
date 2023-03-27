=======================
Putaway Rules
=======================

A good warehouse implementation ensures that products automatically move to their appropriate
destination location. This process is seamless using Odoo's *Putaway rules*. Putaway is the process
of receiving shipments and putting products in appropriate locations.

If, for example, a warehouse contains volatile substances, it is crucial that certain products are
not stored in close proximity in the risk of a chemical reaction. That is where putaway rules
intervene-- to avoid storing products wrongly.

Configuration
=============

In the :guilabel:`Inventory` app, go to :menuselection:`Configuration --> Settings` and activate
:guilabel:`Multi-Step Routes`. By doing so, :guilabel:`Storage Locations` is also automatically
enabled. Lastly, :guilabel:`Save`.

.. image:: putaway/putaw1.png
   :align: center

Create a Putaway Rule
=====================

In some cases, like when a grocery store sells fruits and vegetables, products should be stored in
different locations depending on several factors like frequency, size, product category, and
specific environment needs.

Suppose the warehouse location :guilabel:`WH/Stock` contains two sub-locations
`WH/Stock/Vegetables` and `WH/Stock/Fruits`.

To manage what products are stored in those locations, from the :guilabel:`Inventory` application,
navigate to :menuselection:`Configuration --> Putaway Rules`. Then, click on :guilabel:`Create` to
instruct :guilabel:`When product arrives in` a certain warehouse location, :guilabel:`Store to` one
of the existing sub-locations instead.

.. image:: putaway/putaw2.png
   :align: center

.. note::
   The putaway rules can also be defined per product/product category, location, and package
   type (enable :guilabel:`Packages` in :menuselection:`Configuration --> Settings`). Define them
   through the :guilabel:`Smart Button` on each form.

.. note::
   If the location does not appear in the drop-down menu, add a new location in
   :menuselection:`Configuration --> Locations`. :guilabel:`Store to` locations can only be child
   locations of the location of origin.

With these rules, when apples and carrots are purchased from the supplier, they will be grouped in
the same :abbr:`PO (Purchase Order)` and :guilabel:`Receipt`, but redirected to separate locations 
automatically, thanks to putaway rules. View the summary of incoming product movements in
:menuselection:`Reporting --> Inventory Report`.

.. image:: putaway/putaw3.png
   :align: center

.. image:: putaway/putaw4.png
   :align: center

.. image:: putaway/putaw5.png
   :align: center

.. note::
   :guilabel:`Inventory Report` displays only :guilabel:`Product Types` with :guilabel:`Storable
   Product` as the value. To see how :guilabel:`Consumable Products` are moved using putaway rules,
   track them with :menuselection:`Reporting --> Product Moves`.