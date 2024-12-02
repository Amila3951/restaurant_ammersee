fetch('/static/menu.json')
  .then(response => response.json())
  .then(menu => {
    const dishesContainer = document.getElementById('dishes-container');
    const drinksContainer = document.getElementById('drinks-container');

    menu.forEach(category => {
      const categoryHeading = document.createElement('h3');
      categoryHeading.textContent = category.category;

      const itemsList = document.createElement('ul');

      category.items.forEach(item => {
        const itemElement = document.createElement('li');

        const itemName = document.createElement('h4');
        itemName.textContent = item.name;

        const itemDescription = document.createElement('p');
        itemDescription.textContent = item.description || '';

        const itemPrice = document.createElement('p');
        itemPrice.textContent = `${item.price} €`;

        itemElement.appendChild(itemName);
        itemElement.appendChild(itemDescription);
        itemElement.appendChild(itemPrice);

        itemsList.appendChild(itemElement);
      });

      categoryElement.appendChild(categoryHeading);
      categoryElement.appendChild(itemsList);

      if (category.category === "Drinks") {
        drinksContainer.appendChild(categoryElement);
      } else {
        dishesContainer.appendChild(categoryElement);
      }
    });
  })
  .catch(error => {
    console.error('Error loading menu:', error);

    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'An error occurred while loading the menu.';
    errorMessage.style.color = 'red';
    document.getElementById('menu-container').appendChild(errorMessage);
  });