================
Connect a camera
================

A camera can be connected to the :abbr:`IoT (Internet of Things)` Box with an Odoo database. It can
be added in a few easy steps. Then, it can be used in a manufacturing process and it can be linked
to a control point. Doing so will allow for the taking of pictures when a chosen quality control
point has been reached.

Connection
==========

To connect the camera to the :abbr:`IoT (Internet of Things)` Box, simply connect the two by cable.
This is likely a :abbr:`USB (Universal Serial Bus)` cable.

If the camera is `supported <https://www.odoo.com/page/iot-hardware>`_, there is no need to set up
anything as it will be detected as soon as it is connected.

.. image:: camera/camera-dropdown.png
   :align: center
   :alt: Camera recognized on the IoT box.

Link a camera to a quality control point within a manufacturing process
=======================================================================

In the :menuselection:`Quality` app, a device can be set up on a :guilabel:`Quality Control Point`.
Go to the :menuselection:`Quality Control --> Control Points` and open the :guilabel:`Control Point`
which will be linked with the camera.

Now, edit the :guilabel:`Control Point` and choose the device from the dropdown list. Makes sure the
changes are saved.

.. image:: camera/control-point-device.png
   :align: center
   :alt: Setting up the device on the quality control point.

The camera can be used with the selected :guilabel:`Control Point`. When the :guilabel:`Quality
Control Point` is reached during the manufacturing process, the database will prompt the operator to
take a picture.

.. image:: camera/serial-number-picture.png
   :align: center
   :alt: Graphic user interface of the device on the quality control point.
