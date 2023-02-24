==========================
Connect a measurement tool
==========================

With Odoo's :abbr:`IoT (Internet of Things)` Box, it is possible to connect measurement tools to the
Odoo database. Find the list of supported devices here: `Supported devices
<https://www.odoo.com/page/iot-hardware>`_.

Connect with Universal Serial Bus (USB)
=======================================

To add a device connected by :abbr:`USB (Universal Serial Bus)`, just plug the :abbr:`USB (Universal
Serial Bus)` cable in the :abbr:`IoT (Internet of Things)` Box, and the device should appear in the
Odoo database.

.. image:: measurement_tool/device-dropdown.png
   :align: center
   :alt: Measurement tool recognized on the IoT box.

Connect with Bluetooth
======================

Activate the Bluetooth on the device (see the device manual for further explanation) and the
:abbr:`IoT (Internet of Things)` Box will automatically try to connect to the device.

Here is an example of what it should look like:

.. image:: measurement_tool/measurement-tool.jpeg
   :align: center
   :alt: Bluetooth indicator on measurement tool.

Link a measurement tool to a quality control point within a manufacturing process
=================================================================================

In the :menuselection:`Quality` app, a device can be set up on a :guilabel:`Quality Control Point`.
Go to the :menuselection:`Quality Control --> Control Points` and open the :guilabel:`Control Point`
which will be linked with the measurement tool.

Now, edit the :guilabel:`Control Point` and choose the device from the dropdown list.
:guilabel:`Save` the changes.

Now, the measurement tool is linked to the chosen :guilabel:`Control Point`. The value, which
usually needs to be changed manually, will be automatically updated while the tool is being used.

.. image:: measurement_tool/measurement-control-point.png
   :align: center
   :alt: Measurement tool input in the Odoo database.
