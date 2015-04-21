openerp.pos_extend = function(instance){

    var module = instance.point_of_sale;

    multicurrency_payment(instance,module);
    odoo_amount_text(instance,module);
    

};
