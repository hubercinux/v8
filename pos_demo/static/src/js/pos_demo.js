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
        //'dblclick .oe_pos_demo_listar': 'selected_item',
        'dblclick .oe_pos_demo_editar': 'edit_item_line',
        'click .edit': 'edit_item_detail',
        'click button': 'actualizar_item',
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

        edit_item_line: function(event){
            var self = this;
            var text = $(event.currentTarget).text();
            var text1 = text.trim();
            console.log(this);
            $(event.currentTarget).html('<input type="text" name="name" value="'+text1+'">').find('input').focus();
            $(event.currentTarget).keypress( function(e){
                        if(e.keyCode == 13){
                            var text = $('input', this).val();
                            var demo_id = $(event.currentTarget).data('id');
                            var vals = {'name': text};
                            var model = new instance.web.Model('pos.demo');
                            model.call('write',[demo_id,vals],{context: new instance.web.CompoundContext()});
                            $(this).html( text );
                        }});

            console.log(text1);
            //var model = new instance.web.Model('pos.demo');
            //var demo_id = $(event.currentTarget).data('id')
            //var vals = {'name':'JUAN','descripcion': 'HOLA MUNDO'}
            //model.call('create',[vals],{context: new instance.web.CompoundContext()}).then(function(){
                    //return self.refresh_ui(self.picking.id);
                    //console.log($(event.currentTarget).data('id'))
                //});            
        },

        edit_item_detail: function(event){
            var self = this;         
            var demo_id = $(event.currentTarget).data('id');
            var model = new instance.web.Model('pos.demo');

            /*no funionca
            model.query(['name','descripcion']).filter([['id','=',demo_id]]).all().then(function(result) {
                    //self.$(".oe_pos_demo_editar_detail").text(result.name);
                    console.log(result.name); 
                });

            */
            model.call('search', [[['id','=',demo_id]]], {limit: 15}).then(function (ids) {   
                //console.log(ids[0]);             
                return model.call('read', [ids[0], ['id','name', 'descripcion']]);
            }).then(function (result) {
                //console.log(result.name);
                //self.$(".oe_pos_demo_editar_detail").text(result.name);
                $( 'div' ).remove( '.oe_homepage_left' );
                $( 'div' ).remove( '.oe_homepage_right' );
                self.$el.append(QWeb.render("EditarRegistro",{registro: result})); 
            });                                
        },

        actualizar_item: function (event) { 
            var self = this;
            var text = $('input').val();
            var textarea = $('textarea').val();            
            var demo_id = $(event.currentTarget).data('id');
            var vals = {'name': text, 'descripcion': textarea};
            var model = new instance.web.Model('pos.demo');
            model.call('write',[demo_id,vals],{context: new instance.web.CompoundContext()});
            //.then(function(){
                //return new local.PosdemoListarRegistro(this).appendTo(this.$('.oe_homepage_left'));
            //    console.log(self);  
            //    self.start();
            //});
            var listar = new local.PosdemoListarRegistro(this);
            $( 'div' ).remove( '.oe_pos_demo_listar' );
            return new instance.web.Model("pos.demo").query(['name','descripcion']).order_by('-create_date', '-id').all().then(function(results) {
                    _(results).each(function (item) {
                        self.$el.append(QWeb.render("listarRegistro", {item: item}));
                    });
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