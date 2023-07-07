$(document).ready(function() {
  $('.increase').click(function() {
    var row = $(this).closest('.item-row');
    var quantityElement = row.find('.quantity');
    var priceElement = row.find('.price');
    var itemTotalsElement = row.find('.item-totals');
    
    var quantity = parseInt(quantityElement.val());
    var price = parseInt(priceElement.text());
    
    quantity++;
    price = price * quantity;
    
    quantityElement.val(quantity);
    priceElement.text(price);
    itemTotalsElement.text(price);
  });
    $('.decrease').click(function() {
      var quantityElement = $(this).closest('.row').find('#quantity');
      var priceElement = $(this).closest('tr').find('#price');
      var itemTotalsElement = $(this).closest('tr').find('.item-totals');
      
      var quantity = parseInt(quantityElement.text());
      var price = parseInt(priceElement.text());
      
      if (quantity > 0) {
        quantity--;
        price = price * quantity;
        
        quantityElement.text(quantity);
        priceElement.text(price);
        itemTotalsElement.text(price);
      }
      
      if (quantity === 0) {
        
        $(this).closest('tr').remove();
      }
    });
    

    $('.remove').click(function() {
      $(this).closest('tr').remove();
    });
  });
  