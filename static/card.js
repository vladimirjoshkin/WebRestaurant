function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function removeFromCard(productId) {
    $('#card-' + productId).css("display", "none");
    var added_products_str = getCookie("added_products")
    console.log(added_products_str)
    var added_products = added_products_str.split(",");
    console.log(added_products)
    console.log(productId)
    added_products = added_products.filter(function(e) { return e !== productId.toString() })
    console.log(added_products)
    document.cookie = "added_products=" + added_products;
}

