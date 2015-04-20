function odoo_amount_text(instance,module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    //Reemplazamos y agregamos la propiedad 'name' al model original para ver el nombre de la moneda ejmp: PEN
    module.PosModel.prototype.models.splice(12,1,{
        model: 'res.currency',
        fields: ['symbol','position','rounding','accuracy','name','rate_silent'],
        ids:    function(self){ return [self.pricelist.currency_id[0]]; },
        loaded: function(self, currencies){
            self.currency = currencies[0];
            if (self.currency.rounding > 0) {
                self.currency.decimals = Math.ceil(Math.log(1.0 / self.currency.rounding) / Math.log(10));
            } else {
                self.currency.decimals = 0;
            }
        },
    });

    //Extendemos el model Order para agregarle una nueva funcion amount_tex()
    module.Order = module.Order.extend({
        amount_text: function(){
            var model_tex = new instance.web.Model("ir.translation");
            //console.log("ERROR1", this.pos.currency.name.toLowerCase().substring(0, 2) );
            model_tex.call('amount_to_text_pos',{'nbr':this.getTotalTaxIncluded(),'lang':this.pos.currency.name.toLowerCase().substring(0, 2),'currency':''}).then(function(monto2text){
                //console.log("ERROR1", monto2text );
                $('#montotext').html('SON: '+ monto2text);                          
            });        
        },

    });
}
