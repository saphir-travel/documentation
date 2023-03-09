==========================================
Deliver and invoice to different addresses
==========================================

With :guilabel:`Odoo Sales`, customers can use different addresses for delivery and invoicing.

Activate the feature
====================

Activate the :guilabel:`Customer Addresses` feature in the settings.

If the :guilabel:`Accounting` app is installed, the :guilabel:`Customer Addresses` feature is
located in :menuselection:`Accounting --> Configuration --> Settings`.

If the :guilabel:`Accounting` app is *not* installed, the :guilabel:`Customer Addresses` feature is
located in :menuselection:`Invoicing --> Configuration --> Settings`.

.. image:: different_addresses/customer-addresses-setting.png
   :align: center
   :class: img-thumbnail
   :alt: Activate the Customer Addresses setting

Configure the contact form
==========================

Navigate to the :guilabel:`Contacts` app (or to :menuselection:`Sales --> Orders --> Customers`),
and click on a customer to open their contact form.

Under the :guilabel:`Contacts & Addresses` tab, click :guilabel:`Add`.

.. image:: different_addresses/contact-form-add-address.png
   :align: center
   :class: img-thumbnail
   :alt: Add a contact/address to the contact form

Then, select which type of address to add to the contact form (i.e. :guilabel:`Invoice Address` or
:guilabel:`Delivery Address`).

.. image:: different_addresses/create-contact-window.png
   :align: center
   :class: img-thumbnail
   :alt: Create a new contact/address on a contact form

Enter the address information. Then, click :guilabel:`Save & Close` to save the address and close
the :guilabel:`Create Contact` window. Or, click :guilabel:`Save & New` to save this address and
immediately input another one.

Add addresses to the quotation
==============================

When a customer is added to a quotation, the :guilabel:`Invoice Address` and :guilabel:`Delivery
Address` will autopopulate according to the customer’s contact form.

.. image:: different_addresses/quotation-address-autopopulate.png
   :align: center
   :class: img-thumbnail
   :alt: Invoice and Delivery Addresses autopopulate on a quotation

The :guilabel:`Invoice Address` and :guilabel:`Delivery Address` can also be edited directly from
the quotation, by clicking on the :guilabel:`Internal link` button next to the address line.
