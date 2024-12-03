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

    if (!dishesContainer || !drinksContainer) {
      throw new Error('Dishes or drinks container not found in the HTML!');
    }

    menu.forEach(category => {
      const categoryElement = document.createElement('div');
      categoryElement.classList.add('category-item');

      const categoryHeading = document.createElement('h3');
      categoryHeading.textContent = category.category;
      categoryElement.appendChild(categoryHeading);

      const itemsPerColumn = Math.ceil(category.items.length / 2); 
      let currentColumn = document.createElement('div');  
      currentColumn.classList.add('menu-column');
      categoryElement.appendChild(currentColumn);

      category.items.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.className = 'menu-item';
        itemElement.innerHTML = `
          <h4>${item.name}</h4>
          ${item.description ? `<p>${item.description}</p>` : ''}
          <p>${item.price} €</p>
        `;

        currentColumn.appendChild(itemElement);

       
        if ((index + 1) % itemsPerColumn === 0 && index < category.items.length - 1) {
          currentColumn = document.createElement('div');
          currentColumn.classList.add('menu-column');
          categoryElement.appendChild(currentColumn);
        }
      });

      if (category.category === "Appetizers" || category.category === "Main Courses" || category.category === "Desserts") {
        dishesContainer.appendChild(categoryElement);
      } else if (category.category === "Drinks") {
        drinksContainer.appendChild(categoryElement);
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