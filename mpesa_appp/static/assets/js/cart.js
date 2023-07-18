// Get all elements with class"update-cart"
const updateCartButtons = document.getElementsByClassName("update-cart");
//adding and event listener on each button
for (let i = 0; i < updateCartButtons.length; i++) {
  updateCartButtons[i].addEventListener("click", function() {
    //herevwe get eavh item/product id
    var productId = this.getAttribute("data-product");
    var action = this.getAttribute("data-action");
    console.log('ProductId:',productId, 'Action:',action)
    console.log('User', user)
    if (user === null || user === undefined) {
        console.log('User is anonymous');
      } else {
        console.log('User is authenticated');
      }
  });
}
