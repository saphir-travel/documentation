==============================
Create a new view from scratch
==============================

Creating a new view is an advanced topic. Here we will only highlight the steps that will probably
need to be done.

#. Create the controller:

    The primary role of a controller is to facilitate the coordination between various components
    of a view, such as the Renderer, Model, and Layout.

   .. code-block:: js

      /** @odoo-module */

      import { Layout } from "@web/search/layout";
      import { useService } from "@web/core/utils/hooks";
      import { Component, onWillStart, useState} from "@odoo/owl";

      export class BeautifulController extends Component {
          setup() {
              this.orm = useService("orm");

              // The controller create the model and make it reactive so whenever this.model is
              // accessed and edited then it'll cause a rerendering
              this.model = useState(
                  new this.props.Model(
                      this.orm,
                      this.props.resModel,
                      this.props.fields,
                      this.props.archInfo,
                      this.props.domain
                  )
              );

              onWillStart(async () => {
                  await this.model.load();
              });
          }
      }

      BeautifulController.template = "my_module.View";
      BeautifulController.components = { Layout };

   The template of the Controller here will display the control panel with Layout and also the
   renderer.

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <templates xml:space="preserve">
          <t t-name="my_module.View" owl="1">
              <Layout display="props.display" className="'h-100 overflow-auto'">
                  <t t-component="props.Renderer" records="model.records" propsYouWant="'Hello world'"/>
              </Layout>
          </t>
      </templates>

#. Create the renderer:

    The primary function of a renderer is to generate a visual representation of data by rendering
    the view that includes records.

   .. code-block:: js

      import { Component } from "@odoo/owl";
      export class BeautifulRenderer extends Component {}

      BeautifulRenderer.template = "my_module.Renderer";

   .. code-block:: xml

      <?xml version="1.0" encoding="UTF-8"?>
      <templates xml:space="preserve">
          <t t-name="my_module.Renderer" owl="1">
              <t t-esc="props.propsYouWant"/>
              <t t-foreach="props.records" t-as="record" t-key="record.id">
                  // Show records
              </t>
          </t>
      </templates>

#. Create the model

   The role of the model is to retrieve and manage all the needed data in the view.

   .. code-block:: js

      /** @odoo-module */

      import { KeepLast } from "@web/core/utils/concurrency";

      export class BeautifulModel {
          constructor(orm, resModel, fields, archInfo, domain) {
              this.orm = orm;
              this.resModel = resModel;
              // We can access arch information parsed by the beautiful arch parser
              const { fieldFromTheArch } = archInfo;
              this.fieldFromTheArch = fieldFromTheArch;
              this.fields = fields;
              this.domain = domain;
              this.keepLast = new KeepLast();
          }

          async load() {
              // The keeplast protect against concurrency call
              const { length, records } = await this.keepLast.add(
                  this.orm.webSearchRead(this.resModel, this.domain, [this.fieldsFromTheArch], {})
              );
              this.records = records;
              this.recordsLength = length;
          }
      }

   .. note::

      For advanced case, instead of creating a model from scratch, it is also possible to use the
      `RelationalModel` which is used by others views.

#. Create the arch parser

   The role of the arch parser is to parse the arch view so the view have access to these
   informations.

   .. code-block:: js

      /** @odoo-module */

      import { XMLParser } from "@web/core/utils/xml";

      export class BeautifulArchParser extends XMLParser {
          parse(arch) {
              const xmlDoc = this.parseXML(arch);
              const fieldFromTheArch = xmlDoc.getAttribute("fieldFromTheArch");
              return {
                  fieldFromTheArch,
              };
          }
      }

#. Create the view

   Now, we have to assemble all of this and register our new view in the views registry.

   .. code-block:: js

      /** @odoo-module */

      import { registry } from "@web/core/registry";
      import { BeautifulController } from "./beautiful_controller";
      import { BeautifulArchParser } from "./beautiful_arch_parser";
      import { BeautifylModel } from "./beautiful_model";
      import { BeautifulRenderer } from "./beautiful_renderer";

      export const beautifulView = {
          type: "beautiful",
          display_name: "Beautiful",
          icon: "fa fa-picture-o", // the icon that will be displayed in the Layout panel
          multiRecord: true,
          Controller: BeautifulController,
          ArchParser: BeautifulArchParser,
          Model: BeautifulModel,
          Renderer: BeautifulRenderer,

          props(genericProps, view) {
              const { ArchParser } = view;
              const { arch } = genericProps;
              const archInfo = new ArchParser().parse(arch);

              return {
                  ...genericProps,
                  Model: view.Model,
                  Renderer: view.Renderer,
                  archInfo,
              };
          },
      };

      registry.category("views").add("beautifulView", beautifulView);

#. Using the new view

   We can now use our new view by using it in an arch.

   .. code-block:: xml

      ...
      <beautiful fieldFromTheArch="res.partner"/>
      ...
