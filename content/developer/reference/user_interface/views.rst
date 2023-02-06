.. _user_interface/views:

=====
Views
=====

.. _user_interface/views/options:

Generic view options/attributes
===============================

The different view types have a wide variety of attributes allowing customizations of
the generic behaviors. Some main attributes will be explained here. They do not all have
an impact on all view types.

.. todo:: info on create/...

:sample:
  boolean_ (optional)

  (``kanban`` & ``list`` & ``gantt`` & ``graph`` & ``pivot`` & ``cohort`` & ``dashboard``)

  Populate the view with a set of sample records if none are found for the current model.
  This attribute is false by default.

  These fake records will have heuristics for certain field names/models. For example,
  a field 'display_name' on the model 'res.users' will be populated with sample people names
  while an 'email' field will be in the form 'firstname.lastname@sample.demo'.

  The user will not be able to interact with these data and they will be discarded as soon as
  an action is performed (record created, column added, etc.)

:banner_route:
  path_ (optional)

  a route address to be fetched and prepended to the view.

  If this attribute is set, the
  :ref:`controller route url<reference/controllers>` will be fetched and
  displayed above the view. The json response from the controller should
  contain an "html" key.

  If the html contains a stylesheet <link> tag, it will be
  removed and appended to <head>.

  To interact with the backend you can use <a type="action"> tags. Please take
  a look at the documentation of the _onActionClicked method of
  AbstractController (*addons/web/static/src/js/views/abstract_controller.js*)
  for more details.

  Only views extending AbstractView and AbstractController can use this
  attribute, like :ref:`reference/user_interface/views/form`, :ref:`reference/user_interface/views/kanban`,
  :ref:`reference/user_interface/views/list`, ...

  Example:

  .. code-block:: xml

      <tree banner_route="/module_name/hello" />

  .. code-block:: python

      class MyController(odoo.http.Controller):
          @http.route('/module_name/hello', auth='user', type='json')
          def hello(self):
              return {
                  'html': """
                      <div>
                          <link href="/module_name/static/src/css/banner.css"
                              rel="stylesheet">
                          <h1>hello, world</h1>
                      </div> """
              }

.. note:: The current context and user access rights may also impact the view abilities.

.. note::
    In the views architecture, some XML node attributes can use `python expression`_, in
    this case this expression is evaluated with the values of the current view. In case
    of nested view, the magic value `parent` refere to the values from container view.

.. _reference/user_interface/views/form:

.. include:: views/form.rst

.. _reference/user_interface/views/settings:

.. include:: views/settings.rst

.. _reference/user_interface/views/list:

.. include:: views/list.rst

.. _reference/user_interface/views/search:

.. include:: views/search.rst

.. _reference/user_interface/views/kanban:

.. include:: views/kanban.rst

.. _reference/user_interface/views/qweb:

.. include:: views/qweb.rst

.. _reference/user_interface/views/graph:

.. include:: views/graph.rst

.. _reference/user_interface/views/pivot:

.. include:: views/pivot.rst

.. _reference/user_interface/views/calendar:

.. include:: views/calendar.rst

.. _reference/user_interface/views/activity:

.. include:: views/activity.rst

.. _reference/user_interface/views/dashboard:

.. include:: views/dashboard.rst

.. _reference/user_interface/views/cohort:

.. include:: views/cohort.rst

.. _reference/user_interface/views/grid:

.. include:: views/grid.rst

.. _reference/user_interface/views/gantt:

.. include:: views/gantt.rst

.. _reference/user_interface/views/map:

.. include:: views/map.rst
