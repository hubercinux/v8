function multicurrency_payment(instance,module){
    var QWeb = instance.web.qweb;
  	var _t = instance.web._t;

    round_di = openerp.web.round_decimals;
    //Permite pagar en dolares
    module.Order = module.Order.extend({        
        getPaidTotal: function() {
          var currency = new instance.web.Model('res.currency');
          currency.query(['rate_silent']).filter([['name', '=', 'USD']]).first().then(function (cur) {
                    $('#typo_cambio_valor').html(cur.rate_silent);
                    //console.log("ERROR1",cur.rate_silent);
          });

          return (this.get('paymentLines')).reduce((function(sum, paymentLine) {                        
              if(paymentLine.cashregister.currency[1]==='USD'){                
                //console.log("ERROR222",$('#typo_cambio').text());
                sum = sum + round_di(parseFloat(parseFloat(paymentLine.get_amount()) / $('#typo_cambio_valor').text() ) || 0, 2);
                return sum;
              }
              else{
                sum = sum + paymentLine.get_amount();
                return sum;
              }
          }), 0);
      },

    });
}