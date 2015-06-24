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
        start: function() {
            return new local.PosdemoListarRegistro(this).appendTo(this.$('.oe_homepage_left'));
            
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
                    });
                });

            
         },
    });


}