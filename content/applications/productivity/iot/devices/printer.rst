=================
Connect a printer
=================

A printer can be attached to the :abbr:`IoT (Internet of Things)` Box in an Odoo database.
Installation is easy and convenient and can be done in a few easy steps. The printer can be used to
print receipts, orders or even reports from the different Odoo apps.

Connection
==========

The :abbr:`IoT (Internet of Things)` Box supports printers connected through :abbr:`USB (Universal
Serial Bus)`, network or Bluetooth. `Supported printers <https://www.odoo.com/page/iot-hardware>`__
will be detected automatically and will appear in the :guilabel:`Devices` list of the
:menuselection:`IoT` app.

.. note::
   The printer can take up to two minutes to appear in the :menuselection:`IoT` app devices list.

.. image:: printer/printer-detected.png
   :align: center
   :alt: The printer as it would appear in the IoT app devices list.

Link the printer
================

Link the printer to work orders
-------------------------------

:guilabel:`Work Orders` can be linked to printers via a :guilabel:`Quality Control Point` to print
labels for manufactured products.

To do so, a :guilabel:`Quality Control Point` needs to be created within the
:menuselection:`Quality` app. Once created, the correct manufacturing operation and work order
operation can be selected. In :guilabel:`Type`, choose :guilabel:`Print Label`. :guilabel:`Save` the
changes.

Now, each time the :guilabel:`Quality Control Point` is reached for the chosen product, a
:guilabel:`Print Labels` button will appear.

.. image:: printer/print-labels-button.png
   :align: center
   :alt: The print label icon that populates once the quality control point is reached.

Link the printer to reports
---------------------------

It's also possible to link a type of report to a certain printer. In the :menuselection:`IoT` app,
go to the :menuselection:`Devices` menu and select the printer that needs to be configured.

Now, go to the :guilabel:`Printer Reports` tab. Click :guilabel:`Edit`, then select :guilabel:`Add a
line`. In the window that appears, check all the types of reports that should be linked to this
printer.

.. image:: printer/printers-listed.png
   :align: center
   :alt: The printer devices listed in the IoT Devices menu.

Now, each time :guilabel:`Print` is selected in the control panel, instead of downloading a PDF,
Odoo will send the report to the selected printer and automatically print it.

.. seealso::
   :doc:`../../../sales/point_of_sale/restaurant/kitchen_printing`
