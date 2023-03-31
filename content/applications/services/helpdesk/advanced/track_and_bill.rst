=================
Track & Bill Time
=================

*Odoo Helpdesk* provides teams the opportunity to track the amount of hours spent working on a
ticket, and to bill a customer for that time. Through integrations with the *Sales*, *Timesheets*
and *Accounting* applications, customers can be charged once the work is completed, or before it
has even begun.

.. warning::
   Since the :guilabel:`Track & Bill Time` features require integration with other applications,
   enabling them may result in the installation of additional modules (or applications).

   Installing a new application on a *One-App-Free* database will trigger a 15-day trial. At the
   end of the trial, if a paid subscription has not been added to the database, it will no longer
   be active or accessible.

Configure track & bill time
===========================

Enable track & bill time on a helpdesk team
-------------------------------------------

To enable the :guilabel:`Track & Bill Time` features on a *Helpdesk* team, first navigate to
:menuselection:`Helpdesk --> Configuration --> Teams`. Select a team from the list or :doc:`create
a new one </applications/services/helpdesk/overview/getting_started>`.

On the team's settings page, scroll to the :guilabel:`Track & Bill Time` heading. Check the boxes
next to :guilabel:`Timesheets` and :guilabel:`Time Billing`.

Checking the box for :guilabel:`Timesheets` causes a new field to appear, labeled
:guilabel:`Project`. This is the project where all the *timesheets* for this team's tickets will be
recorded.  Click into the drop-down to select a :guilabel:`Project`. To create a new one, click
into the drop-down and type a name, then click :guilabel:`Create`.

.. image:: track_and_bill/track-bill-enable-settings.png
   :align: center
   :alt: View of a helpdesk team settings page emphasizing the track and bill time settings.

Configure service products
--------------------------

When the :guilabel:`Time Billing` feature is enabled, a new product is created in the
:guilabel:`Sales` app called :guilabel:`Service on Timesheets`. This product can be found under
:menuselection:`Sales app --> Products --> Products`. Search for `Service on Timesheets`.

This product is configured with the :guilabel:`Product Type` set to :guilabel:`Service` and the
:guilabel:`Invoicing Policy` set to :guilabel:`Based on Timesheets`. This is the product that will
be used when invoicing for services after they have been completed (*post-paid support services*).

.. image:: track_and_bill/track-bill-product-based-on-timesheets.png
   :align: center
   :alt: View of a service product with the invoicing policy set to 'Based on timesheets'.

In order to invoice for support services before the work has been completed (*prepaid support
services*), a separate product with a different invoicing policy will need to be created.

To create a new service product, go to :menuselection:`Sales app --> Products --> Products` and
click :guilabel:`New`. Add a :guilabel:`Product Name`, and set the :guilabel:`Product Type` to
:guilabel:`Service`. Set the :guilabel:`Invoicing Policy` to :guilabel:`Prepaid/Fixed Price`. This
means that an invoice can be generated (and payment can be received) for this product *before*
any timesheets entries have been recorded for these services.

.. image:: track_and_bill/track-bill-product-prepaid-fixed.png
   :align: center
   :alt: View of a service product with the invoicing policy set to 'prepaid/fixed'.

Set the :guilabel:`Sales Price`, and confirm the :guilabel:`Unit of Measure` is set to
:guilabel:`Hours`.

Invoice prepaid support services
================================

When support services are billed on a fixed price, an invoice can be created before any work is
completed on the issue. In this case, a service product with the invoicing policy set to
:guilabel:`Prepaid/Fixed Price` (like the one created above) would be used.

Create a sales order with prepaid product
-----------------------------------------

To invoice a customer for prepaid support services, first create a sales order (SO) with the
support services product. To do this, go to :guilabel:`Odoo Dashboard --> Sales --> Orders -->
Quotations --> New`.

Fill out the :guilabel:`Quotation` with the :guilabel:`Customer` information.

On the :guilabel:`Order Lines` tab, click :guilabel:`Add a Product`. Select the prepaid services
product configured in the steps above. Update the :guilabel:`Quantity` field with the number of
hours. After updating any other necessary information, :guilabel:`Confirm` the quotation. Then
click :guilabel:`Create Invoice`.

Create and send an invoice for prepaid services
-----------------------------------------------

This will open a :guilabel:`Create Invoices` pop-up window. If a :guilabel:`Down Payment` needs
to be collected, change the :guilabel:`Create Invoice` type. Then click :guilabel:`Create Invoice`.
The invoice can now be sent to the customer for payment.

Create helpdesk ticket for prepaid services
-------------------------------------------

Next, navigate to the :menuselection:`Helpdesk` app and select a :guilabel:`Team`. On the
:guilabel:`Pipeline`, click :guilabel:`New` to create a new ticket.

Fill out the ticket information, and enter the :guilabel:`Customer` information. When the customer
name is added, the :guilabel:`Sales Order Item` field will automatically populate with the most
recent prepaid sales order item that has time remaining.

Track hours on helpdesk ticket
------------------------------

Click on the :guilabel:`Timesheets` tab on the :guilabel:`Ticket`. To track the time spent on this
ticket against the hours sold on the :abbr:`SO (sales order)`, click :guilabel:`Add a line`. Choose
an :guilabel:`Employee`, and enter the number of :guilabel:`Hours Spent`. As new lines are added to
tab, the :guilabel:`Remaining Hours on SO` is updated.

.. image:: track_and_bill/track-bill-remaining-hours-total.png
   :align: center
   :alt: View of the timesheets tab on a ticket with an emphasis on the remaining hours on an SO.

.. note::
   If the number of hours on the :guilabel:`Timesheets` tab goes over the number of hours sold, the
   :guilabel:`Remaining Hours of SO` will turn red.

As hours are added to the :guilabel:`Timesheets` tab, they are updated in the :guilabel:`Delivered`
field on the :guilabel:`Sales Order`.

Invoice post-paid support services
==================================

When support services are billed based on the amount of time spent on an issue, an invoice cannot
the total number of hours required to solve the problem have been entered on a timesheet. In this
case, a service product with the invoicing policy set to :guilabel:`Based on Timesheets` (like the
one created above) would be used.

Create a sales order with a time tracked product
------------------------------------------------

To invoice a customer for post-paid support services, first create a sales order (SO) with the
support services product. To do this, go to :guilabel:`Odoo Dashboard --> Sales --> Orders -->
Quotations --> New`.

Fill out the :guilabel:`Quotation` with the :guilabel:`Customer` information.

On the :guilabel:`Order Lines` tab, click :guilabel:`Add a Product`. Select the post-paid services
product configured in the steps above. After updating any other necessary information,
:guilabel:`Confirm` the quotation.

.. note::
   Unlike with the prepaid services quotation, Odoo will not allow an invoice to be created at
   this time. (Since no services have been performed, nothing has been *delivered*, therefore there
   there is nothing to invoice).

Create a helpdesk ticket for time-tracked services
--------------------------------------------------

To record a :guilabel:`Timesheet` entry, go to the :menuselection:`Helpdesk` app and select the
appropriate :guilabel:`Team`.

If there is already an existing ticket for this issue, select it from the kanban view to go to the
details form. If there is no existing ticket for this customer issue, click :guilabel:`New` to
create a new ticket and enter the necessary customer information.

In the :guilabel:`Sales Order Line` drop-down, select the :abbr:`SO (sales order)` created in the
previous step.

Track support hours on a ticket
-------------------------------

In order to create an invoice for a product based on timesheets, hours need to be tracked and
recorded. At this point, the service is considered *delivered*. To record hours for this support
service, click on the :guilabel:`Timesheets` tab of the :guilabel:`Helpdesk ticket`.

Click :guilabel:`Add a Line` to record a new entry. Select an :guilabel:`Employee` from the
drop-down, and record the :guilabel:`Hours Spent`.

Repeat these steps as needed until all time spent on the issues has been recorded.

.. image:: track_and_bill/track-bill-record-timesheet-hours.png
   :align: center
   :alt: View of the timesheets tab on a helpdesk ticket.

Create an invoice for hours tracked on a ticket
-----------------------------------------------

After the customer's issue has been solved, and it is determined no additional timesheet entries
will be made, an invoice can be created and the customer can be billed.

To do this, return to the :abbr:`SO (sales order)` by clicking on the :guilabel:`Sales Order` smart
button at the top of the :guilabel:`Helpdesk Ticket`.

Before creating the invoice, confirm that the number in the :guilabel:`Delivered` column matches
the total number of :guilabel:`Hours Spent` listed in the :guilabel:`Timesheets` tab on the ticket.

.. image:: track_and_bill/track-bill-delivered-timesheet-hours.png
   :align: center
   :alt: View of a sales order with emphasis on the delivered column.

Then click :guilabel:`Create Invoice`. This will open a :guilabel:`Create Invoices` pop-up window.
If a :guilabel:`Down Payment` needs to be collected, change the :guilabel:`Create Invoice` type.

.. important::
   Use the :guilabel:`Timesheets Period` field if this invoice should only include timesheets from
   a certain time period. If this field is left blank, *all* applicable timesheets that have not
   yet been invoiced will be included.

.. image:: track_and_bill/track-bill-create-invoice-timesheets-period.png
   :align: center
   :alt: View of create invoices pop up showing timesheets period fields.

Click :guilabel:`Create Invoice`. The invoice can now be sent to the customer for payment.

.. seealso::
   - :doc:`/applications/inventory_and_mrp/inventory/management/products/uom`
