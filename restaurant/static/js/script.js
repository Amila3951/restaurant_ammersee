fetch('/static/menu.json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(menu => {
    const dishesContainer = document.getElementById('dishes-container');
    const drinksContainer = document.getElementById('drinks-container');

    // Provjera postoje li spremnici
    if (!dishesContainer || !drinksContainer) {
      throw new Error('Dishes or drinks container not found in the HTML!');
    }

    menu.forEach(category => {
      const categoryElement = document.createElement('div');
      const categoryHeading = document.createElement('h3');
      categoryHeading.textContent = category.category;
      const itemsList = document.createElement('ul');

      category.items.forEach(item => {
        const itemElement = document.createElement('li');
        itemElement.innerHTML = `
          <h4>${item.name}</h4>
          ${item.description ? `<p>${item.description}</p>` : ''}
          <p>${item.price} €</p>
        `;
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
    errorMessage.textContent = `Error loading menu: ${error.message}`;
    errorMessage.style.color = 'red';
    const menuContainer = document.getElementById('menu-container'); 
    if (menuContainer) {
      menuContainer.appendChild(errorMessage);
    } else {
      console.error('Menu container not found for error message!');
    }
  });