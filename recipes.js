const recipes = {
    Rice: {
      Egg: [
      {
        description: "Egg Fried Rice",
        image: "images/eggfried.jpeg",
        steps: [
          "Cook rice and let it cool.",
          "Scramble eggs in a pan with some oil.",
          "Add vegetables like carrots, peas, and onions to the eggs.",
          "Mix in the rice and season with soy sauce.",
          "Stir fry everything together for a few minutes before serving."
           
        ],
        
      },
      {
        description: "Rice and Egg Bowl",
        image:'images/Easy-Egg-Rice-Bowl-Recipe-500x500.jpg',
        steps: [
          "Cook rice according to the package instructions.",
          "Fry an egg sunny-side-up in a small pan.",
          "Serve the fried egg over the cooked rice, drizzle with soy sauce, and garnish with green onions."
        ]
      }
    ],
    Potato: [
      {
        description: "Potato Rice Bowl",
        image:'images/Potato-Rice.jpg',
        steps: [
          "Cook rice as per the instructions.",
          "Boil and mash potatoes with butter and salt.",
          "Serve the mashed potatoes over the rice and top with a savory gravy."
        ]
      },
      {
        description: "Spanish Rice with Potatoes",
        image:'images/spanishRiceandPotatoes.jpeg',
        steps: [
          "Heat oil in a pan and sauté diced onions and tomatoes.",
          "Add diced potatoes and spices like cumin, paprika, and chili powder.",
          "Mix in the rice and cook until everything is well combined and the potatoes are tender."
        ]
      }
    ],
      "Arhar Dal": {
        description: "Rice with Arhar Dal: Cook rice and dal separately, mix with spices like cumin and coriander, and serve with a dollop of ghee.",
        image:"images/soft-mashed-rice-and-moong-dal-recipe_726334837-768x525.jpg",
        steps: [
          "Rinse the rice under cold water until the water runs clear.",
          "In a pot, boil water and add the rice. Cook until fluffy, about 15-20 minutes.",
          "In a pressure cooker, add washed Arhar dal with water, turmeric, and salt. Cook for about 3 whistles or until soft.",
          "In a separate pan, heat ghee and add cumin seeds. Once they splutter, add coriander powder and mix.",
          "Combine the cooked dal with the spice mixture, adjust salt, and serve it over rice."
        ],
      },
      Chickpea: {
        description: "Chickpea Rice: Cook rice, add boiled chickpeas, spices, and garnish with cilantro.",
        image:"images/1370452352191.jpeg",
        steps: [
          "Rinse the rice under cold water, then boil it in salted water until tender.",
          "If using dried chickpeas, soak overnight and boil until soft. If using canned, rinse and drain.",
          "In a pan, heat oil and add cumin seeds. Once they splutter, add cooked chickpeas and spices.",
          "Stir to combine and heat through, then mix with the cooked rice.",
          "Garnish with chopped cilantro and serve."
        ],
      },
      "Kidney Beans": {
        description: "Rice with Kidney Beans: Cook rice and kidney beans with spices, serve with onion and lemon.",
        image:"images/riceandKidneybeans.jpeg",
        steps: [
          "Rinse and boil the rice in salted water until done.",
          "If using dried kidney beans, soak overnight and boil until soft. If using canned, rinse and drain.",
          "In a pan, heat oil and sauté chopped onions until golden brown.",
          "Add boiled kidney beans, salt, and spices of your choice (like cumin and chili powder).",
          "Serve the kidney beans over rice, garnished with fresh lemon juice."
        ],
      },
      None: {
        description: "Simple Rice: Boil rice and serve with salt or a side of your choice.",
        image:"images/Simplerice.jpg",
        steps: [
          "Rinse the rice under cold water.",
          "Boil in water with a pinch of salt until soft, about 15-20 minutes.",
          "Drain and serve plain or with your choice of side."
        ],
      },
      Chicken: [
        {
          description: "Chicken Fried Rice: Stir-fried rice with chicken, vegetables, and soy sauce.",
          image:"images/Chicken-Fried-Rice-min.jpg",
          steps: [
            "Cook the rice and let it cool.",
            "In a pan, heat oil and stir-fry diced chicken until cooked through.",
            "Add diced vegetables and stir-fry for a few minutes.",
            "Add the cooled rice, soy sauce, and mix well.",
            "Cook for a few more minutes until heated through and serve."
          ],
        },
        {
          description: "Chicken and Rice Casserole: A baked dish with chicken, rice, cream of mushroom soup, and herbs.",
          image:"images/Baked-Chicken-Rice-IMAGE-1.jpg",
          steps: [
            "Preheat the oven to 375°F (190°C).",
            "Layer cooked rice and chicken pieces in a baking dish.",
            "Mix cream of mushroom soup with some herbs and pour over the rice and chicken.",
            "Cover with foil and bake for 25-30 minutes.",
            "Remove the foil and bake for another 10 minutes to brown slightly."
          ],
        },
      ],
    },
    Chicken: {
      Egg: [
      {
        description: "Chicken and Egg Curry",
        image:"IMAGES/chickenAndEgg.jpeg",
        steps: [
          "Sauté onions, garlic, and spices in a pan.",
          "Add chicken pieces and cook until browned.",
          "Add water or broth and simmer until chicken is tender.",
          "In a separate pot, boil eggs and peel them.",
          "Add boiled eggs to the chicken curry and simmer for another 5-10 minutes.",
          "Serve with rice or bread."
        ]
      },
      {
        description: "Egg and Chicken Stir-Fry",
        image:"images/egg-stir-fry-peppers-15.jpg",
        steps: [
          "Scramble eggs in a pan and set aside.",
          "In the same pan, stir-fry vegetables and chicken pieces.",
          "Add the scrambled eggs back in and toss everything together.",
          "Serve hot with rice or noodles."
        ]
      }
    ],
      Tofu: {
        description: "Chicken and Tofu Stir-Fry: Sauté chicken and tofu with garlic, soy sauce, and vegetables of choice.",
        image:"images/chickenandTofu.jpeg",
        steps: [
          "Cut chicken and tofu into bite-sized pieces.",
          "Heat oil in a pan and sauté chicken until golden brown.",
          "Add tofu and continue to stir-fry until crispy.",
          "Add garlic, soy sauce, and vegetables of choice (e.g., bell peppers, carrots).",
          "Stir-fry for a few more minutes, then serve hot."
        ],
      },
      Mushroom: {
        description: "Chicken Mushroom Curry: Cook chicken with mushrooms, tomatoes, and spices until tender.",
        image:"images/ChickenAndMushroom.jpeg",
        steps: [
          "Heat oil in a pan and sauté onions until golden brown.",
          "Add diced chicken and cook until browned.",
          "Add mushrooms, tomatoes, and spices (e.g., turmeric, cumin, coriander).",
          "Cook until the chicken is tender and the sauce thickens.",
          "Serve hot with rice or bread."
        ],
      },
      None: {
        description: "Grilled Chicken: Season chicken with spices and grill until cooked through.",
        image:"images/Simply-Recipes-Grilled-BBQ-Chicken-LEAD-10-03fd9892eaae4ce1a8a3f4c949657cfd.jpg",
        steps: [
          "Season chicken with salt, pepper, and your choice of spices (e.g., paprika, garlic powder).",
          "Preheat the grill to medium-high heat.",
          "Grill chicken on each side for 5-7 minutes or until fully cooked.",
          "Let rest for a few minutes before serving."
        ],
      },
    },
    Egg: {
      Potato: {
        description: "Egg and Potato Scramble: Scramble eggs with sautéed potatoes and onions.",
        image:"images/EggAndPotato.jpeg",
        steps: [
          "Peel and dice potatoes into small cubes.",
          "Heat oil in a pan and sauté potatoes until golden and crispy.",
          "In a separate bowl, whisk eggs with salt and pepper.",
          "Pour the eggs into the pan with the potatoes and scramble until cooked through.",
          "Serve hot."
        ],
      },
      Mushroom: {
        description: "Egg and Mushroom Omelette: Whisk eggs, add sautéed mushrooms, and cook until set.",
        image:"images/EggAndMushroom.jpeg",
        steps: [
          "Heat oil in a pan and sauté mushrooms until golden brown.",
          "In a bowl, whisk eggs with salt and pepper.",
          "Pour the eggs into the pan with mushrooms and cook until the edges set.",
          "Flip the omelette or fold in half, then serve."
        ],
      },
    },
    Potato: {
      Mushroom: {
        description: "Potato Mushroom Stir-Fry: Sauté potatoes and mushrooms with spices and serve hot.",
        image:"images/PotatoAndMushroom.jpeg",
        steps: [
          "Peel and dice potatoes into small cubes.",
          "In a pan, heat oil and sauté potatoes until golden brown and crispy.",
          "Add sliced mushrooms and continue to cook until they release moisture and turn golden.",
          "Season with salt, pepper, and your favorite spices (e.g., garlic powder, paprika).",
          "Serve hot."
        ],
      },
      None: {
        description: "Mashed Potato: Boil and mash potatoes with butter and salt.",
        image:"images/MashedPotatoes.jpeg",
        steps: [
          "Peel and cut potatoes into cubes.",
          "Boil the potatoes in salted water until tender.",
          "Drain the potatoes and mash them with butter and salt.",
          "Serve as a side dish."
        ],
      },
    },
    Mushroom: {
      None: {
        description: "Sautéed Mushrooms: Sauté mushrooms in butter and garlic until golden brown.",
        image:"images/SauttedMushroom.jpeg",
        steps: [
          "Heat butter in a pan over medium heat.",
          "Add sliced mushrooms and sauté until they release moisture and turn golden brown.",
          "Add minced garlic and cook for another minute.",
          "Season with salt and pepper, then serve."
        ],
      },
    },
    Carrot: {
      None: {
        description: "Carrot Salad: Grate carrots, add lemon juice and salt for a refreshing salad.",
        image:"images/Carrot_Salad",
        steps: [
          "Peel and grate fresh carrots into a bowl.",
          "Add freshly squeezed lemon juice and a pinch of salt.",
          "Toss to combine and serve as a refreshing salad."
        ],
      },
    },
    Tofu: {
      None: {
        description: "Tofu Stir-Fry: Sauté tofu with vegetables and sauce of your choice.",
        image:"images/TofuStirFry.jpeg",
        steps: [
          "Cut tofu into cubes and pat dry with a paper towel.",
          "Heat oil in a pan and sauté tofu until crispy on all sides.",
          "Add vegetables of your choice (e.g., broccoli, bell peppers) and stir-fry until tender.",
          "Add soy sauce or your preferred sauce and mix well.",
          "Serve hot."
        ],
      },
    },
    Milk: {
      None: {
        description: "Milkshake: Blend milk with your choice of fruits like bananas or strawberries for a delicious milkshake.",
        image:"images/Milkshake.jpg",
        steps: [
          "In a blender, add cold milk and your choice of fruit (e.g., bananas or strawberries).",
          "Add sugar or honey if desired.",
          "Blend until smooth and creamy.",
          "Pour into a glass and enjoy."
        ],
      },
    },
    "Kidney Beans": {
      Rice: {
        description: "Rice with Kidney Beans: Cook rice and kidney beans with spices, serve with onion and lemon.",
        image:"images/KidneyBeansAndRice.jpg",
        steps: [
          "Rinse and cook the rice until tender.",
          "Boil kidney beans until soft.",
          "In a pan, sauté onions with spices and mix in the cooked kidney beans.",
          "Serve kidney beans over rice with a squeeze of lemon juice."
        ],
      },
      None: {
        description: "Kidney Bean Salad: Mix boiled kidney beans with chopped veggies, lemon juice, and spices.",
        image:"images/kidneyBeansSlad.png",
        steps: [
          "Boil kidney beans until tender.",
          "Mix the cooked beans with chopped veggies like onions, tomatoes, and cucumbers.",
          "Add lemon juice and spices, toss well, and serve."
        ],
      },
    },
    Chickpea: {
      Rice: {
        description: "Chickpea Rice: Cook rice, add boiled chickpeas, spices, and garnish with cilantro.",
        image:"images/channachawal.jpg",
        steps: [
          "Rinse and cook rice until tender.",
          "Boil chickpeas until soft.",
          "In a pan, sauté chickpeas with spices and mix with the cooked rice.",
          "Garnish with cilantro and serve."
        ],
      },
      None: {
        description: "Chickpea Salad: Mix boiled chickpeas with chopped vegetables and a lemon dressing.",
        image:"images/chickpeaSalad.jpeg",
        steps: [
          "Boil chickpeas until soft.",
          "Mix with diced cucumbers, tomatoes, onions, and cilantro.",
          "Dress with lemon juice, olive oil, salt, and pepper.",
          "Toss to combine and serve."
        ],
      },
    },
  };
  
 
  document
  .getElementById("recipeForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Get the selected ingredients or set them to "None" by default
    const ingredient1 = document.getElementById("ingredient1").value || "None";
    const ingredient2 = document.getElementById("ingredient2").value || "None";
    let recipeOutput = "";

    // Function to generate the recipe steps HTML
    function generateRecipeOutput(recipe) {
      let output = `<h3>${recipe.description}</h3><ol>`;
      if (recipe.image) {
        output += `<img src="${recipe.image}" alt="${recipe.description}" style="width: 300px; height: auto;">`;
      }
      output += `<ol>`;
      recipe.steps.forEach((step, index) => {
        output += `<li>${step}</li>`;
      });
      output += "</ol>";
      return output;
    }

    // Function to check and return the recipe regardless of ingredient order
    function getRecipe(ingredient1, ingredient2) {
      if (recipes[ingredient1] && recipes[ingredient1][ingredient2]) {
        return recipes[ingredient1][ingredient2];
      } else if (recipes[ingredient2] && recipes[ingredient2][ingredient1]) {
        return recipes[ingredient2][ingredient1];
      }
      return null;
    }

    // Check for combination recipes (in both ingredient orders)
    if (ingredient1 && ingredient2) {
      const recipeList = getRecipe(ingredient1, ingredient2);

      if (recipeList) {
        const recipeArray = Array.isArray(recipeList) ? recipeList : [recipeList];
        recipeOutput += `<h2>Recipes for ${ingredient1} and ${ingredient2}:</h2>`;
        recipeArray.forEach((recipe) => {
          recipeOutput += generateRecipeOutput(recipe);
        });
      } else {
        recipeOutput += `<h2>No recipe found for ${ingredient1} and ${ingredient2} combination.</h2>`;
      }
    }


    

    // Check for individual recipes if one or both ingredients are "None"
    if (ingredient1 === "None" && recipes[ingredient2] && recipes[ingredient2]["None"]) {
      recipeOutput += `<h2>Recipe for ${ingredient2}:</h2>`;
      recipeOutput += generateRecipeOutput(recipes[ingredient2]["None"]);
    } else if (ingredient2 === "None" && recipes[ingredient1] && recipes[ingredient1]["None"]) {
      recipeOutput += `<h2>Recipe for ${ingredient1}:</h2>`;
      recipeOutput += generateRecipeOutput(recipes[ingredient1]["None"]);
    }

    document.getElementById("recipeResults").innerHTML = recipeOutput;
  });
