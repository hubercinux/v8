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
          
          $('#moneda_base').html(this.pos.currency.name);

          return (this.get('paymentLines')).reduce((function(sum, paymentLine) {                        
              if(paymentLine.cashregister.currency[1]==='USD' &&  $('#moneda_base').text() !== 'USD' ){                
                //console.log("ERROR11",$('#typo_cambio_valor').text());
                sum = sum + round_di(parseFloat(parseFloat(paymentLine.get_amount()) / $('#typo_cambio_valor').text() ) || 0, 2);
                return sum;
              }
              else if(paymentLine.cashregister.currency[1]!=='USD' &&  $('#moneda_base').text() === 'USD' ){
                sum = sum + paymentLine.get_amount()*$('#typo_cambio_valor').text();
                //console.log("ERROR222",$('#typo_cambio_valor').text());
                return sum;
              }
              else{                
                //console.log("ERROR3333",round_di(parseFloat(parseFloat($('#typo_cambio_valor').text()) ) || 0, 4));
                sum = sum + paymentLine.get_amount();
                return sum;
              }
          }), 0);
      },

    });
}