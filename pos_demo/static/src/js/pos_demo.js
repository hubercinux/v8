//Definimos el modulo web de Odoo como una funcion de openerp
//El nombre de la funcion debe ser el mismo que la del modulo(tienda_mascota)
openerp.pos_demo = function(instance, local) {
    //traduccion
    var _t = instance.web._t,
       _lt = instance.web._lt;
    //Qweb
    var QWeb = instance.web.qweb;
 
    //Construimos un widget basico de nombre PaginaPrincipal
    local.PaginaPrincipal = instance.Widget.extend({
        template: 'PosdemoHomePage',
        events: {
        'dblclick .oe_pos_demo_listar': 'selected_item',
        'click .oe_pos_demo_listar': 'selected_item1',
        },
        
        start: function() {


            /*
            Ext.create('Ext.Panel', {
             renderTo     : 'oe_homepage_extjs',
             width        : 200,
             height       : 150,
             bodyPadding  : 5,
             title        : 'Integrando Odoo y Extjs',
             html         : 'Hola <b>Bienvenido a la Inovacion!</b>...'
            });
            */

            /*
            
            Ext.widget({
                renderTo : 'oe_homepage_extjs',
                xtype    : 'grid',
                title    : 'Lista de usuarios',
                width    : 650,
                height   : 300,
                //plugins  : 'rowediting',
                plugins: [
                    new Ext.grid.plugin.CellEditing({
                    clicksToEdit: 1
                    })
                    ],
                store    : {
                    fields : [ 'name', 'age', 'votes', 'credits' ],
                    data   : [
                        [ 'Javier', 35, 10, 427 ],
                        [ 'Huber', 22, 4, 42 ]
                    ]
                },
                columns: {
                    defaults: {
                        editor : 'numberfield',
                        width  : 120
                    },
                    items: [
                        { text: 'Nombre', dataIndex: 'name', flex: 1, editor: 'textfield' },
                        { text: 'Edad', dataIndex: 'age' },
                        { text: 'Votos', dataIndex: 'votes' },
                        { text: 'Creditos', dataIndex: 'credits' }
                    ]
                }
            });
            */

            /* sale errores
            Ext.define('UserDB', {
                extend: 'Ext.data.Model',
                fields: [ 'name', 'email', 'phone' ]
            });
            var userStore = Ext.create('Ext.data.Store', {
                model: 'UserDB',
                data: [
                    { name: 'Lisa', email: 'lisa@simpsons.com', phone: '555-111-1224' },
                    { name: 'Bart', email: 'bart@simpsons.com', phone: '555-222-1234' },
                    { name: 'Homer', email: 'homer@simpsons.com', phone: '555-222-1244' },
                    { name: 'Marge', email: 'marge@simpsons.com', phone: '555-222-1254' }
                ]
            });
            Ext.create('Ext.grid.Panel', {
                renderTo: 'oe_homepage_extjs',
                store: userStore,
                width: 600,
                height: 200,
                selType: 'cellmodel',
                plugins: [
                    new Ext.grid.plugin.CellEditing({
                    clicksToEdit: 1
                    })
                    ],
                title: 'Application Users',
                columns: [
                    {
                        text: 'Name',
                        width: 100,
                        sortable: false,
                        hideable: false,
                        dataIndex: 'name',
                        editor: 'textfield',
                    },
                    {
                        text: 'Email Address',
                        width: 150,
                        dataIndex: 'email',
                        hidden: true,
                        editor: 'textfield',
                    },
                    {
                        text: 'Phone Number',
                        flex: 1,
                        dataIndex: 'phone',
                        editor: 'textfield'
                    }
                ],
            });

            fin sale errores*/
            
            /*Comentado para evitar mostrar el Widget PaginaPrincipal en la pagina de Inicio*/
           return new local.PosdemoListarRegistro(this).appendTo(this.$('.oe_homepage_left'));
            
        },

        
        selected_item: function (event) {
            this.do_action({
                type: 'ir.actions.act_window',
                res_model: 'pos.demo',
                res_id: $(event.currentTarget).data('id'),
                views: [[false, 'form']],
                target: 'current',
            });        
        },

        selected_item1: function (event) {
            var self = this;
            var model =  new instance.web.Model("pos_demo.pos_demo");
            model.call('confirmar', {context: new instance.web.CompoundContext()}).then(function(result) {
            self.$el.append("<div>Hello " + result["hola"] + "</div>");
            // will show "Hello world" to the user
            });      
        },    
        
    });

    //Registra nuestro widget básico como una acción cliente que sera llamado desde la accion creado en  pos_demo/pos_demo_view.xml
    instance.web.client_actions.add('pos_demo.paginainicio', 'instance.pos_demo.PaginaPrincipal');

    local.PosdemoListarRegistro = instance.Widget.extend({
        template: 'PosdemoListarRegistro',
        start: function() {
            var self = this;
            return new instance.web.Model("pos.demo")
                .query(['name','descripcion'])
                .order_by('-create_date', '-id')
                .all()
                .then(function(results) {
                    _(results).each(function (item) {
                        self.$el.append(QWeb.render("listarRegistro", {item: item}));
                        //self.$(".listRegistro").text(item.name);
                        //console.log(item);
                    });
                });

            
         },
    });


}