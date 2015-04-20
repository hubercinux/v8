openerp.pos_extend = function(instance){

    var module = instance.point_of_sale;

    odoo_amount_text(instance,module);
    multicurrency_payment(instance,module);

};
