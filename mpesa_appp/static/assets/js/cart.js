// Get all elements with class"update-cart"
const updateCartButtons = document.getElementsByClassName("update-cart");
//adding and event listener on each button
for (let i = 0; i < updateCartButtons.length; i++) {
    updateCartButtons[i].addEventListener("click", function() {
      var productId = this.getAttribute("data-product");
      var action = this.getAttribute("data-action");
      console.log('ProductId:', productId, 'Action:', action);
      console.log('User', user);
      if (user === null || user === undefined) {
        console.log('User is anonymous');
      } else {
        updateUserOrder(productId, action);
      }
    });
  }

  function updateUserOrder(productId, action) {
    console.log('sending data...', 'Product ID:', productId, 'Action:', action);
    var url = '/app/update/';
  
    // Create the data object
    var data = {
      productId: productId,
      action: action
    };
  
    // Send the POST request
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(data)
    })
      .then(response => {return response.json()})
      .then(data => {
        console.log('Response:', data);
        location.reload()
        // Handle the response data as needed
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle any errors that occur during the request
      });
  }

