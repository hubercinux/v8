//Definimos el modulo web de Odoo como una funcion de openerp
//El nombre de la funcion debe ser el mismo que la del modulo(tienda_mascota)
openerp.tienda_mascota = function(instance, local) {
    //traduccion
    var _t = instance.web._t,
       _lt = instance.web._lt;
    //Qweb
    var QWeb = instance.web.qweb;
 
    //Construimos un widget basico de nombre PaginaPrincipal
    local.PaginaPrincipal = instance.Widget.extend({
        start: function() {
            //Agregando el template(HomePageTemplate) definida en tienda_mascota/static/src/xml/tienda_mascota.xml a la PaginaPrincipal
            //QWeb.render() busca la plantilla a mostrar
            this.$el.append(QWeb.render("HomePageTemplate",{name_: "JAVIER HUBER"})); 
            this.$el.append(QWeb.render("HomePageTemplate1")); 

            //Agregando nuevo Widget
            var greeting = new local.GreetingsWidget(this);
            greeting.appendTo(this.$el);

            },            
    });

    //Creando nuevo Widget
    local.GreetingsWidget = instance.Widget.extend({
        start: function() {
        this.$el.append("<div>Hello dear Odoo user GreetingsWidget!</div>");
        console.log(this.getParent().$el );
        // will print "div.oe_petstore_homepage" in the console
        },
    });


    //Usando Qweb dentro Widget
    local.Usowidgets = instance.Widget.extend({
        start: function() {
            var products = new local.ProductsWidget(this, ["cpu", "mouse", "keyboard", "graphic card", "screen"], "#00FF00");
            products.appendTo(this.$el);
        },
    });

    local.ProductsWidget = instance.Widget.extend({
        template: "uso_widgets",
        init: function(parent, products, color) {
            this._super(parent);
            this.products = products;
            this.color = color;
        },
    });


    //Creando nuevo Widget EVENTOS
    local.UsoEventos = instance.Widget.extend({
        start: function() {
            var widget = new local.ConfirmWidget(this);
            widget.on("user_chose", this, this.user_chose);
            widget.appendTo(this.$el);

        },
        user_chose: function(confirm) {
            if (confirm) {
                this.$el.append("<div>Usuario Aceptado</div>");
                
            }
            else {
                this.$el.append("<div>Usuario Anulado</div>");

            }
        },
    });

    local.ConfirmWidget = instance.Widget.extend({
         events: {
            'click button.ok_button': function () {
                this.trigger('user_chose', true);
            },
            'click button.cancel_button': function () {
                this.trigger('user_chose', false);
            }
        },
        start: function() {
        this.$el.append("<div>Are you sure you want to perform this action?</div>" +
            "<button class='ok_button'>Ok</button>" +
            "<button class='cancel_button'>Cancel</button>");
        },
    });

    //EVENTOS Y PROPIEDADES
    local.EventosPropiedades = instance.Widget.extend({
        template: "EventosPropiedades",
        start: function() {
            this.colorInput = new local.ColorInputWidget(this);
            this.colorInput.on("change:color", this, this.color_changed);
            return this.colorInput.appendTo(this.$el);
        },
        color_changed: function() {
            this.$(".oe_color_div").css("background-color", this.colorInput.get("color"));
        },
    });

    local.ColorInputWidget = instance.Widget.extend({
        template: "ColorInputWidget",
        events: {
            'change input': 'input_changed'
        },
        start: function() {
            this.input_changed();
            return this._super();
        },
        input_changed: function() {
            var color = [
                "#",
                this.$(".oe_color_red").val(),
                this.$(".oe_color_green").val(),
                this.$(".oe_color_blue").val()
            ].join('');
            this.set("color", color);
        },
    });



    //Creando nuevo Widget BASE DATOS
    local.BaseDatos = instance.Widget.extend({
        start: function() {
            var self = this;
            var model = new instance.web.Model("tienda.mensaje");
            model.call("mostrar_mensaje", {context: new instance.web.CompoundContext()}).then(function(result) {
            self.$el.append("<div>Hola " + result["mensaje"] + "</div>");
            // will show "Hello world" to the user
                });
            var model_tex = new instance.web.Model("ir.translation");
            model_tex.call('amount_to_text',{'nbr':250,'lang':'hn','currency':'LEMPIRAS'}).then(function(monto2text){
            self.$el.append("<div>SON: " + monto2text + "</div>");    
            });


        },
    });


 
    //Registra nuestro widget básico como una acción cliente que sera llamado desde la accion creado en  tienda_mascota/tienda_mascota.xml
    instance.web.client_actions.add('tienda_mascota.paginainicio', 'instance.tienda_mascota.PaginaPrincipal');
    instance.web.client_actions.add('tienda_mascota.uso_widgets', 'instance.tienda_mascota.Usowidgets');
    instance.web.client_actions.add('tienda_mascota.uso_eventos', 'instance.tienda_mascota.UsoEventos');
    instance.web.client_actions.add('tienda_mascota.uso_eventos_propiedades', 'instance.tienda_mascota.EventosPropiedades');

    instance.web.client_actions.add('tienda_mascota.base_datos', 'instance.tienda_mascota.BaseDatos');


}