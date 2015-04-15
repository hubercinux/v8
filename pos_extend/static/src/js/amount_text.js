function odoo_amount_text(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    module.Order = module.Order.extend({
        amount_text: function(){
            var model_tex = new instance.web.Model("ir.translation");
            model_tex.call('amount_to_text',{'nbr':250,'lang':'hn','currency':'LEMPIRAS'}).then(function(monto2text){
            self.$el.append("<div>Son: " + monto2text + "</div>");    
            });
        },

    });


}